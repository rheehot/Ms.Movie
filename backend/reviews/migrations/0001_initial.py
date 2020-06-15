# Generated by Django 3.0.2 on 2020-06-15 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disliked_users', models.ManyToManyField(blank=True, related_name='disliked_reviews', to=settings.AUTH_USER_MODEL)),
                ('liked_users', models.ManyToManyField(blank=True, related_name='liked_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('1', '부적절한 홍보 게시글'), ('2', '음란성 또는 청소년에게 부적합한 내용'), ('3', '명예훼손 / 사생활 침해 및 저작권침해 등'), ('4', '기타')], max_length=200)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
