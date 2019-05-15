# Generated by Django 2.2.1 on 2019-05-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190515_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='出版时间'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='title',
            field=models.CharField(max_length=30, verbose_name='书名'),
        ),
    ]
