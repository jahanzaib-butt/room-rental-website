from django.db import migrations
from django.utils import timezone

def set_default_created(apps, schema_editor):
    Room = apps.get_model('your_app_name', 'Room')
    Room.objects.filter(created__isnull=True).update(created=timezone.now())

class Migration(migrations.Migration):
    dependencies = [
        ('base', '0015_alter_room_beds'),
    ]

    operations = [
        migrations.RunPython(set_default_created),
    ]