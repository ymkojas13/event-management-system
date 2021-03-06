# Generated by Django 3.2.5 on 2021-08-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Confirm_password', models.CharField(max_length=50)),
                ('Software_courses', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('.Net', '.Net'), ('Aws', 'Aws'), ('Datascince', 'Datascince'), ('UI', 'UI'), ('Mysql', 'Mysql'), ('selenium', 'selenium')], max_length=50)),
            ],
        ),
    ]
