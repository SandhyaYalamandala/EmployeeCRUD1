

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_describe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
            name='name',
            name='email',
            name='address',
            name='designation',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
