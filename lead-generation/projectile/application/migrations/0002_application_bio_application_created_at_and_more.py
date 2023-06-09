# Generated by Django 4.1.5 on 2023-01-09 10:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='is_highlighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.position'),
        ),
        migrations.AddField(
            model_name='application',
            name='skills',
            field=models.ManyToManyField(through='application.ApplicationSkill', to='application.skill'),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Unread', 'Unread'), ('Read', 'Read'), ('Interview 1', 'Interview 1'), ('Interview 2', 'Interview 2'), ('Interview 3', 'Interview 3'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Archived', 'Archived')], default='Unread', max_length=50),
        ),
        migrations.CreateModel(
            name='PositionSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.position')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.skill')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='skills',
            field=models.ManyToManyField(through='application.PositionSkill', to='application.skill'),
        ),
    ]
