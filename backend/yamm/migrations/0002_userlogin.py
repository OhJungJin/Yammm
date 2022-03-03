# Generated by Django 4.0.2 on 2022-03-01 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yamm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_key', models.CharField(db_column='providerKey', max_length=255)),
                ('user', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, related_name='user_logins', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserLogins',
            },
        ),
    ]
