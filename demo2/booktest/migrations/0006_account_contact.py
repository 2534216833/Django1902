# Generated by Django 2.2.1 on 2019-05-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20190515_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=40, null=True, verbose_name='密码')),
                ('register_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20, null=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booktest.Account')),
            ],
        ),
    ]