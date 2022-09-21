# Generated by Django 4.0.7 on 2022-09-21 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_id', models.CharField(default=None, max_length=255, null=True)),
                ('fetched', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=100)),
                ('by', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=500, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(null=True)),
                ('score', models.BigIntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'All Story',
                'verbose_name_plural': 'All Stories',
                'ordering': ['-time', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('technewsApp.allstories',),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
            ],
            options={
                'ordering': ['-time', 'title'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('technewsApp.allstories',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
                'ordering': ['-time', 'title'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('technewsApp.allstories',),
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('allstories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='technewsApp.allstories')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_polloptions', to='technewsApp.poll')),
            ],
            bases=('technewsApp.allstories',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('allstories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='technewsApp.allstories')),
                ('kids', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_comments', to='technewsApp.comment')),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poll_comments', to='technewsApp.poll')),
                ('story', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='story_comments', to='technewsApp.story')),
            ],
            bases=('technewsApp.allstories',),
        ),
    ]