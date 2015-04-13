import os
from django.conf import settings
from calaccess_raw import get_model_list
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Generate documentation for raw CAL-ACCESS database models'

    def handle(self, *args, **kwargs):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs'
        )
        self.target_path = os.path.join(self.docs_dir, 'models.rst')
        context = {
            'model_list': get_model_list(),
        }
        rendered = render_to_string('toolbox/models.rst', context)
        with open(self.target_path, 'wb') as target_file:
            target_file.write(rendered)