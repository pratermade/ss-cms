# Generated by Django 2.0.3 on 2018-04-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20180329_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
