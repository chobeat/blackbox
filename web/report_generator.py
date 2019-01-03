import random
from jinja2 import Template
import collections
from flask import current_app
templates = [ ]

Face = collections.namedtuple("Face",["image","suggestions"])
Suggestion = collections.namedtuple("Suggestion",["template","context"])
def generate_report(url, image_id):
    rnd = random.Random(hash)
    num_templates = rnd.randint(0,len(templates))
    return Face(url,[Suggestion(
        current_app.jinja_env.get_or_select_template("template_diet.html"),{"value":1})
    ]
                )


def render_suggestion(suggestion):
    return suggestion.template.render(suggestion.context)