# Generated by Django 5.0.3 on 2024-04-17 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialplatform', '0005_remove_group_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupJoinedMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialplatform.group')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialplatform.groupadmin')),
            ],
        ),
    ]
