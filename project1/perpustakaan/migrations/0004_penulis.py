# Generated by Django 5.0.4 on 2024-05-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_alter_buku_judul_alter_buku_penerbit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]