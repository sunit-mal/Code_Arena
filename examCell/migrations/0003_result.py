# Generated by Django 4.1.2 on 2023-09-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examCell', '0002_alter_examquestions_examid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('time', models.DateField()),
                ('totalQuestion', models.CharField(max_length=500)),
                ('rightAnswer', models.CharField(max_length=500)),
            ],
        ),
    ]