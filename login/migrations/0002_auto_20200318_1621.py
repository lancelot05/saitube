# Generated by Django 3.0.4 on 2020-03-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='abc123@gmail.com', max_length=225, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='abc123@gmail.com', max_length=225),
            preserve_default=False,
        ),
    ]
