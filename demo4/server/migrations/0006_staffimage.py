# Generated by Django 2.2.1 on 2019-05-29 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20190529_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staimg', models.ImageField(upload_to='ads', verbose_name='员工头像')),
                ('staimg_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Staff')),
            ],
            options={
                'verbose_name': '员工头像',
                'verbose_name_plural': '员工头像',
            },
        ),
    ]
