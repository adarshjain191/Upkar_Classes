# Generated by Django 3.2.7 on 2022-02-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('Class', models.TextField(max_length=10)),
                ('Feedback', models.TextField(max_length=500)),
            ],
        ),
    ]