import os

from django.db import migrations


def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    from users.models import Nationality
    User = get_user_model()

    nationality = Nationality.objects.create(iso='ENG', full_name="England")

    DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

    superuser = User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD,
        birthday='2021-10-10',
        gender=1,
        personal_identity_number='',
        address=1,
        nationality=nationality,
        queue_priority=1
    )

    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser)
    ]
