# Generated by Django 2.1.3 on 2018-11-25 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Matchmaking', '0005_auto_20181122_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='userprofile.Profile'),
        ),
    ]