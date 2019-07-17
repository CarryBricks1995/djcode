# Generated by Django 2.2.3 on 2019-07-14 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=32)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_time', models.DateTimeField(auto_now=True)),
                ('datastatus', models.SmallIntegerField(default=0)),
            ],
        ),
    ]