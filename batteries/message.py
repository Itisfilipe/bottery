import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from batteries.conf import settings


class Message:
    def __init__(self, plataform, user, text, timestamp, raw):
        self.plataform = plataform
        self.user = user
        self.text = text
        self.timestamp = timestamp
        self.raw = raw

    @property
    def datetime(self):
        return datetime.fromtimestamp(self.timestamp)


def render(message, template_name, context={}):
    base_dir = os.path.join(os.getcwd(), 'templates')
    paths = [base_dir]
    if settings.TEMPLATE_DIRS:
        paths.extends(settings.TEMPLATE_DIRS)

    env = Environment(
        loader=FileSystemLoader(paths),
        autoescape=select_autoescape(['html']))

    template = env.get_template(template_name)

    default_context = {
        'user': message.user
    }
    default_context.update(context)
    return template.render(**default_context)
