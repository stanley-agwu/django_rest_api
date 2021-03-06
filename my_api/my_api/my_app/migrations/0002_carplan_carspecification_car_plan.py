# Generated by Django 4.0.3 on 2022-04-02 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=20)),
                ('years_of_warranty', models.PositiveIntegerField(default=1)),
                ('finance_plan', models.CharField(default='unavailable', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='carspecification',
            name='car_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.carplan'),
        ),
    ]
