import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    
operations = [
    migrations.CreateModel(
        name='Proyect',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('nombre', models.CharField(max_length=200)),
        ],
    ),
    migrations.CreateModel(
        name='Task',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=200)),
            ('description', models.TextField()),
            ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.proyect')),  # Asegúrate de que la FK apunte a Proyect
        ],
    ),
    migrations.DeleteModel(
        name='Project',
    ),
]
