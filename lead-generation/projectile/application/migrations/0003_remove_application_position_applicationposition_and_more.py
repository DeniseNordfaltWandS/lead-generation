# Generated by Django 4.1.5 on 2023-01-10 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application_bio_application_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='position',
        ),
        migrations.CreateModel(
            name='ApplicationPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.application')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.position')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='positions',
            field=models.ManyToManyField(through='application.ApplicationPosition', to='application.position'),
        ),
    ]
