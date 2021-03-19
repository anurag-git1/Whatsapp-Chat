# Generated by Django 3.1.7 on 2021-03-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogIn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Accepted'), ('d', 'Decline'), ('c', 'Cancel'), ('r', 'Remove')], default='c', max_length=1),
        ),
    ]
