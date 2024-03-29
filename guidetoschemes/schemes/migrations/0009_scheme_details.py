# Generated by Django 2.1.2 on 2018-11-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0008_delete_sc'),
    ]

    operations = [
        migrations.CreateModel(
            name='scheme_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('eligibility_criteria', models.TextField()),
                ('check_link', models.TextField()),
                ('apply_link', models.TextField()),
                ('website_link', models.TextField()),
            ],
        ),
    ]
