# Generated by Django 4.2.3 on 2023-07-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contacts_delete_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
