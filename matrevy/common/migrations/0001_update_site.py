from django.conf import settings
from django.db import migrations


def update_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    db_alias = schema_editor.connection.alias
    Site.objects.using(db_alias).update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': 'matrevy.dk',
            'name': 'matrevy.dk',
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site, migrations.RunPython.noop),
    ]
