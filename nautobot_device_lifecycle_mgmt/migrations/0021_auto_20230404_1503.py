# Generated by Django 3.2.16 on 2023-04-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_device_lifecycle_mgmt', '0020_alter_devicesoftwarevalidationresult_valid_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitemsoftwarevalidationresult',
            name='valid_software',
        ),
        migrations.AddField(
            model_name='inventoryitemsoftwarevalidationresult',
            name='valid_software',
            field=models.ManyToManyField(related_name='_nautobot_device_lifecycle_mgmt_inventoryitemsoftwarevalidationresult_valid_software_+', to='nautobot_device_lifecycle_mgmt.ValidatedSoftwareLCM'),
        ),
    ]