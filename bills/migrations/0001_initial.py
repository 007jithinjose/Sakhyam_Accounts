# Generated by Django 4.2.3 on 2023-08-02 06:14

import bills.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bills',
            fields=[
                ('bill_Date', models.DateField(default=datetime.date(2023, 4, 1), help_text='Please use the following format: <em>DD-MM-YYYY</em>.', validators=[bills.models.Validate_DateRange], verbose_name='Bill Issue Date')),
                ('bill_Id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_No', models.CharField(help_text='Bill or Invoice Number', max_length=20, verbose_name='Bill Number')),
                ('bill_Name', models.CharField(help_text='Bill Description', max_length=100, verbose_name='Bill Name')),
                ('bill_Amount', models.PositiveIntegerField(help_text='Bill Amount in Rs Ps > 0', verbose_name='Bill Amount')),
            ],
            options={
                'ordering': ['bill_Date'],
            },
        ),
    ]
