# Generated by Django 2.2.5 on 2019-09-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20190820_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
