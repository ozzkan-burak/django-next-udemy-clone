# Generated by Django 3.2.5 on 2022-02-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_section',
            field=models.ManyToManyField(blank=True, to='courses.CourseSection'),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='episodes',
            field=models.ManyToManyField(blank=True, to='courses.Episode'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='related_curse',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
    ]
