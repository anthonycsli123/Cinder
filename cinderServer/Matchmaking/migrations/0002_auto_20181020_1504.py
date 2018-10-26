# Generated by Django 2.1.2 on 2018-10-20 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('Matchmaking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reciever', to='userprofile.Profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to='userprofile.Profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='match',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user1', to='userprofile.Profile'),
        ),
        migrations.AddField(
            model_name='match',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user2', to='userprofile.Profile'),
        ),
    ]