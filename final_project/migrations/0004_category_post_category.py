# Generated by Django 4.1.3 on 2022-12-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_project', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=250),
        ),
    ]