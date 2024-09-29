# Generated by Django 4.2.11 on 2024-09-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0004_alter_newspaper_options_alter_redactor_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
