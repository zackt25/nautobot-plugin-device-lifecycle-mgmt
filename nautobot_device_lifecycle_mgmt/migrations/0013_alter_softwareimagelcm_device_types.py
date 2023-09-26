# Generated by Django 3.2.16 on 2023-07-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0016_device_components__timestamp_data_migration"),
        ("nautobot_device_lifecycle_mgmt", "0012_add_related_name_to_results_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="softwareimagelcm",
            name="device_types",
            field=models.ManyToManyField(blank=True, related_name="software_images", to="dcim.DeviceType"),
        ),
    ]