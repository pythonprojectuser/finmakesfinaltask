# Generated by Django 4.2.7 on 2023-11-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_orderitem_remove_new_course_remove_new_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('cpassword', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
