# Generated by Django 2.2.10 on 2021-02-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addDonors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donorinfo',
            old_name='District',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='donorinfo',
            old_name='Last_Donate_Date',
            new_name='last_Donate_Date',
        ),
        migrations.RenameField(
            model_name='donorinfo',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='donorinfo',
            old_name='Phone_Number',
            new_name='phone_Number',
        ),
        migrations.RenameField(
            model_name='donorinfo',
            old_name='Select_Blood_Group',
            new_name='select_Blood_Group',
        ),
    ]
