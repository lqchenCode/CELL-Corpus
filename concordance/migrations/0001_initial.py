# Generated by Django 2.1 on 2018-08-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concordance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_word', models.CharField(max_length=50)),
                ('concord', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpus_name', models.CharField(max_length=250)),
                ('corpus_type', models.CharField(max_length=250)),
                ('corpus_file', models.FileField(upload_to='')),
            ],
        ),
    ]