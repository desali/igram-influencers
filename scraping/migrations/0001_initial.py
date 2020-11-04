# Generated by Django 3.1.3 on 2020-11-04 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('followers', models.IntegerField()),
                ('quality_followers', models.IntegerField()),
                ('engagement_rate', models.FloatField()),
                ('account_quality_score', models.FloatField()),
                ('account_type', models.IntegerField(choices=[(0, 'Не выбрано'), (1, 'Персональный'), (2, 'Бренд')], default=0)),
                ('contact_info', models.IntegerField(choices=[(0, 'Не выбрано'), (1, 'Есть почта или номер')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AgeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_start_id', models.IntegerField(null=True)),
                ('hype_end_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'age_intervals',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'gender_types',
            },
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hype_id', models.CharField(max_length=255, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.country')),
            ],
        ),
        migrations.CreateModel(
            name='AudienceGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('gender_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.gendertype')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.interval')),
            ],
            options={
                'db_table': 'audience_gender',
            },
        ),
        migrations.CreateModel(
            name='AudienceCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.country')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.interval')),
            ],
            options={
                'db_table': 'audience_country',
            },
        ),
        migrations.CreateModel(
            name='AudienceCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.city')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.interval')),
            ],
            options={
                'db_table': 'audience_city',
            },
        ),
        migrations.CreateModel(
            name='AudienceAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('age_interval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.ageinterval')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.interval')),
            ],
            options={
                'db_table': 'audience_age',
            },
        ),
        migrations.CreateModel(
            name='AccountLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.language')),
            ],
            options={
                'db_table': 'account_languages',
            },
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.category')),
            ],
            options={
                'db_table': 'account_categories',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.ageinterval'),
        ),
        migrations.AddField(
            model_name='account',
            name='categories',
            field=models.ManyToManyField(through='scraping.AccountCategory', to='scraping.Category'),
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.city'),
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.country'),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scraping.gendertype'),
        ),
        migrations.AddField(
            model_name='account',
            name='languages',
            field=models.ManyToManyField(through='scraping.AccountLanguage', to='scraping.Language'),
        ),
    ]
