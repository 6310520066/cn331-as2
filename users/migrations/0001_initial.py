# Generated by Django 4.1.1 on 2022-09-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_num', models.CharField(max_length=5)),
                ('course_name', models.CharField(max_length=64)),
                ('seat', models.IntegerField(null=True)),
                ('maxSeat', models.IntegerField(null=True)),
                ('semester', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('state', models.BooleanField(default=None)),
            ],
        ),
    ]