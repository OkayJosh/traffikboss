# Generated by Django 4.1.5 on 2023-06-08 15:18

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('tone', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('ability', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to=users.models.user_directory_path)),
                ('backstory', models.CharField(blank=True, max_length=255, null=True)),
                ('personality_traits', models.CharField(blank=True, max_length=255, null=True)),
                ('relationships', models.CharField(blank=True, max_length=255, null=True)),
                ('arc', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('original_url', models.URLField(blank=True, null=True)),
                ('shortened_url', models.URLField(blank=True, null=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_url', to='business.business')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
