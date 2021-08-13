import os

from django.db import migrations


def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    from users.models import Nationality
    User = get_user_model()

    nationality = Nationality.objects.create(iso='EN', full_name='England')
    from users.models import Address
    address = Address.objects.create(street='baker', building_number='1', flat_number='1', zip_code='1234',
                                     city='Pekin', country='China')

    from users.models import QueuePriority
    queue_priority = QueuePriority.objects.create(name='basic', level=0)
    # DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    # DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    # DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

    superuser = User.objects.create_superuser(
        username='a',
        email='p@p.pl',
        password='testpass123',
        birthday='2021-10-10',
        gender=1,
        personal_identity_number='',
        nationality=nationality,
        queue_priority=queue_priority
    )

    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser)
    ]
