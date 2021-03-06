# Generated by Django 4.0.5 on 2022-06-13 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaur_app', '0003_mesozoic_end_mesozoic_start_alter_dinosaur_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dinosaur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dinosaur_app.dinosaur')),
            ],
        ),
    ]
