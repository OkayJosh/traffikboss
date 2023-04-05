from django.db import models


class DeviceManager(models.Manager):

    def log_in_device(self, user, device_name, device_id):
        device_count = user.logged_devices.count()
        #TODO max_devices should be based on plans
        max_devices = 2
        if device_count >= max_devices:
            return "This user has reached the device login limit"
        else:
            device = self.create(user=user, device_name=device_name, device_id=device_id)
            return device
