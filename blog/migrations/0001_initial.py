# Generated by Django 2.2.6 on 2019-10-08 00:51

from django.db import migrations, models
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_published', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published Date')),
                ('created_by', models.CharField(max_length=255, verbose_name='Author')),
                ('body', markdownx.models.MarkdownxField(help_text='You can write in Markdown', verbose_name='body')),
            ],
        ),
    ]
