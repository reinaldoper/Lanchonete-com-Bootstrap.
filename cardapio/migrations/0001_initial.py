# Generated by Django 2.2.6 on 2020-02-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.FileField(blank=True, max_length=20, null=True, upload_to='')),
            ],
        ),
    ]
