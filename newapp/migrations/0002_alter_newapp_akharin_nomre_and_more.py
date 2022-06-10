# Generated by Django 4.0.2 on 2022-04-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newapp',
            name='akharin_nomre',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='آخرين نمره'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='code_pish_niaz',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='کد پيش نيازها'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='code_standard',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='کد استاندارد'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='dars',
            field=models.CharField(blank=True, max_length=255, verbose_name='درس'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='noe_dars',
            field=models.CharField(blank=True, max_length=255, verbose_name='نوع درس'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='pish_niaz',
            field=models.CharField(blank=True, max_length=255, verbose_name='پيش نيازها'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='saat_amali',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ساعت عملي'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='saat_teori',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ساعت تئوري'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='vahed_amali',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='واحد عملي'),
        ),
        migrations.AlterField(
            model_name='newapp',
            name='vahed_teori',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='واحد تئوري'),
        ),
    ]
