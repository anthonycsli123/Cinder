# Generated by Django 2.1.2 on 2018-10-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matchmaking', '0002_auto_20181020_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='match',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='hasMatched',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
