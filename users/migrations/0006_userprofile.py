# Generated by Django 4.0.3 on 2022-04-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('flat_no', models.CharField(max_length=200)),
                ('tower_no', models.CharField(max_length=200)),
            ],
        ),
    ]
