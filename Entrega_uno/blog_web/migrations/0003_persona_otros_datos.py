# Generated by Django 4.0.4 on 2022-06-02 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_web', '0002_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='otros_datos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog_web.usuario'),
        ),
    ]
