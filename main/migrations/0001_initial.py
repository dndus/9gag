# Generated by Django 3.2.7 on 2021-09-15 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gag.helpers
import gag.minix


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50, verbose_name='Nomi (uz)')),
                ('name_ru', models.CharField(max_length=50, verbose_name='Nomi (ru)')),
                ('image', models.ImageField(upload_to=gag.helpers.UploadTo('category'))),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
            bases=(gag.minix.TranslateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Izoh')),
                ('file', models.FileField(upload_to=gag.helpers.UploadTo('post'), verbose_name='Rasm/Video')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.category')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(gag.minix.TranslateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Izoh')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=gag.helpers.UploadTo('comment'))),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='PostComment', to='main.postcomment')),
                ('post', models.ForeignKey(default='username', on_delete=django.db.models.deletion.RESTRICT, to='main.post')),
                ('user', models.ForeignKey(default='username', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(gag.minix.TranslateMixin, models.Model),
        ),
    ]
