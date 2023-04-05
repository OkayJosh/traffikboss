import random
import secrets
import string

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from users.models import User, ResetToken


class UserService:
    """
    Responsible for all user related database action.
    """

    def create_user(
            self, *, email: str, password: str, account_type: str, channel: str, username: str, fcmb_token: str
    ) -> User:
        """
        Create a new `User` instance using the provided information
        :param username:
        :param email:
        :param password:
        :param account_type: basic, premium or affiliate
        :param channel:
        :return: User
        """
        user = User()
        setattr(user, "email", email)
        setattr(user, "account_type", account_type)
        setattr(user, "channel", channel)
        setattr(user, "fcmb_token", fcmb_token)
        setattr(user, "username", self.unique_username(username=username, email=email))

        user.set_password(password)
        user.save()
        return user

    @classmethod
    def __generate_unique_username(cls, email: str) -> str:
        parts = email.split("@")
        first_part = parts[0]
        return first_part + secrets.token_hex(5)

    @classmethod
    def unique_username(cls, username: str, email: str) -> str:
        if cls.username_exists(username=username):
            _username = cls.__generate_unique_username(email=email)
            if cls.username_exists(username=_username):
                return cls.unique_username(username=username, email=email)
        else:
            _username = username

        return _username

    @classmethod
    def update_user_password(cls, *, password: str, user: User) -> User:
        """
        update user password
        :param password: new user password
        :param user:
        :return: user (User): the updated user
        """
        user.set_password(password)
        user.save()

        return user

    @classmethod
    def username_exists(cls, username: str):
        return User.objects.filter(username=username).exists()

    @classmethod
    def update_user_fcmb_token(cls, *, fcmb_token: str, user: User) -> User:
        """
        Update user Firebase Cloud Messaging token
        :param fcmb_token: Firebase Cloud Messaging token
        :param user:
        :return: user (User): the updated user
        """
        user.fcmb_token = fcmb_token
        user.save()

        return user


class AuthenticationService:
    @staticmethod
    def change_password(user, old_password, new_password, device_name, device_id):
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            device = user.logged_devices.get(device_name=device_name, device_id=device_id)
            token = Token.objects.create(user=user)
            device.token = token
            return token
        else:
            raise ValueError('Invalid Password')

    @staticmethod
    def setup_reset_password(email):
        # check if a user with the email exist
        user = User.objects.filter(email=email).first()
        if user:
            # send email to user for password reset
            reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            user.reset_token = reset_token
            user.save()
            # construct the password reset link
            reset_link = f"{settings.SITE_URL}{reverse('password_reset')}?token={reset_token}"
            # send email to user with password reset link
            email_template = render_to_string('password_reset_email.html', {'reset_link': reset_link})
            # send email to user with password reset link
            send_mail(
                'Password Reset Request',
                email_template,
                'noreply@traffik.com',
                [email],
                html_message=email_template,
                fail_silently=False,
            )
        else:
            pass

    @staticmethod
    def check_reset_token(token):
        # check if token is valid and find the associated user
        user = ResetToken.objects.filter(token=token).latest('created').user
        if user:
            return True
        else:
            return False

    @staticmethod
    def reset_password(token, new_password):
        user = ResetToken.objects.filter(token=token).latest('created').user
        if user:
            user.set_password(new_password)
            user.reset_token = None
            user.save()
            return True
        else:
            return False