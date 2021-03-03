# Generated by Django 3.1.6 on 2021-02-26 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('dob', models.DateField()),
                ('Language', models.CharField(max_length=100)),
                ('userscontact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoingMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomsg', models.CharField(max_length=500)),
                ('recivedfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.contact')),
                ('sentby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommingMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frommesg', models.CharField(max_length=500)),
                ('recivedfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.contact')),
                ('sentby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
