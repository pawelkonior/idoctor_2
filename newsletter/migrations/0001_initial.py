# Generated by Django 3.2 on 2021-08-13 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('required', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='users_categories', through='newsletter.Agreement', to='newsletter.NewsletterCategory')),
            ],
        ),
        migrations.CreateModel(
            name='AgreementLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='log', to='newsletter.agreement')),
            ],
        ),
        migrations.AddField(
            model_name='agreement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agreement_category', to='newsletter.newslettercategory'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agreement_email', to='newsletter.newsletteruser'),
        ),
    ]
