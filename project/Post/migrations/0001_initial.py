# Generated by Django 4.0.5 on 2022-08-11 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pics', models.ImageField(null=True, upload_to='post image')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_video')),
                ('content', models.TextField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channelPost', to='Artist_app.artist_chanel')),
            ],
        ),
        migrations.CreateModel(
            name='post_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10)),
                ('likepost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='Post.post')),
            ],
        ),
        migrations.CreateModel(
            name='post_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment_image', models.ImageField(blank=True, null=True, upload_to='comment image')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postComment', to='Post.post')),
            ],
        ),
        migrations.CreateModel(
            name='Event_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10)),
                ('likeEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Event_like', to='Artist_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_comment_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10)),
                ('likecommentEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='Artist_app.event_comment')),
            ],
        ),
        migrations.CreateModel(
            name='comment_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10)),
                ('likecomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to='Post.post_comments')),
            ],
        ),
    ]