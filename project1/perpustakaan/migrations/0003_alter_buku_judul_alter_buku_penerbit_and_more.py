# Generated by Django 5.0.4 on 2024-05-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0002_alter_kelompok_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='judul',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penerbit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penulis',
            field=models.CharField(max_length=244),
        ),
    ]