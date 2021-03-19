# Generated by Django 3.1.7 on 2021-03-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogIn', '0002_auto_20210316_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Accepted'), ('d', 'Decline'), ('c', 'Cancel'), ('r', 'Remove'), ('p', 'Pending')], default='p', max_length=1),
        ),
    ]
