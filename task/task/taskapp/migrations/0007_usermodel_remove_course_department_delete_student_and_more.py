# Generated by Django 4.2.7 on 2023-11-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
