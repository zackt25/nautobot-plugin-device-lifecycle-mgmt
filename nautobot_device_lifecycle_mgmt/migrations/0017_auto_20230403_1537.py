# Generated by Django 3.2.16 on 2023-04-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_device_lifecycle_mgmt', '0016_inventoryitemsoftwarevalidationresult_valid_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicesoftwarevalidationresult',
            name='valid_software',
        ),
        migrations.AddField(
            model_name='devicesoftwarevalidationresult',
            name='valid_software',
            field=models.ManyToManyField(blank=True, null=True, to='nautobot_device_lifecycle_mgmt.ValidatedSoftwareLCM'),
        ),
    ]