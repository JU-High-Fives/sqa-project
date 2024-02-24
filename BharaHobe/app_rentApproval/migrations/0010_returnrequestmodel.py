# Generated by Django 4.1.1 on 2024-02-22 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_rentApproval', '0009_renteemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_approved_at', models.DateTimeField(blank=True, null=True)),
                ('m_is_approved', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=20)),
                ('reason', models.CharField(choices=[('defective', 'Defective'), ('damaged', 'Damaged'), ('incorrect', 'Incorrect'), ('changed_mind', 'Changed Mind')], max_length=20)),
                ('m_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rentApproval.productmodel')),
                ('m_rentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rentApproval.renteemodel')),
            ],
        ),
    ]