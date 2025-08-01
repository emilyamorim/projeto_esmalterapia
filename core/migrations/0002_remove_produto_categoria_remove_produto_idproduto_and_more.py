# Generated by Django 5.2.4 on 2025-07-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='idProduto',
        ),
        migrations.AddField(
            model_name='produto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
