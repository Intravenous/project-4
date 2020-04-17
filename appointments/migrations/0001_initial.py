# Generated by Django 3.0.5 on 2020-04-17 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150)),
                ('delivery_time', models.CharField(choices=[('B1', '1 Business Day'), ('B2', '2 Business Days'), ('BS', '2 - 3 Business Days'), ('B3', '3 Business Days'), ('B4', '4 Business Days'), ('B5', '5 Business Days'), ('B6', '6 Business Days'), ('B7', '7 Business Days')], default='B1', max_length=2)),
                ('private_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('business_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='appointments.Category')),
            ],
            options={
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('services', models.ManyToManyField(related_name='appointments', to='appointments.Service')),
            ],
        ),
    ]
