# Generated by Django 4.2 on 2023-04-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://pluspack.com/wp-content/uploads/2018/09/placeholder-picture.jpg', max_length=500),
        ),
    ]