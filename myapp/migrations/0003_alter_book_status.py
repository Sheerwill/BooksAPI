# Generated by Django 4.2.6 on 2023-11-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('First Approval', 'First Approval'), ('Verified', 'Verified')], default='Pending', max_length=20),
        ),
    ]
