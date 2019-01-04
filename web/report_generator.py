import random
from flask import render_template
import collections
from flask import current_app

def get_templates():
 return [
    ("template_diet.html", fill_template_variables(["value"])),
    ("template_suggestion_2.html",fill_template_variables(["value_other"]))
]

Face = collections.namedtuple("Face",["image","suggestions"])
Suggestion = collections.namedtuple("Suggestion",["template","context"])

def fill_template_variables(variable_names):
    def _fill_template_variables(rnd,template):
        context = {}
        for name in variable_names:
            value = rnd.uniform(0,100.0)
            context[name]= value
        return template,context
    return _fill_template_variables

def pick_random_templates(rnd):
    templates = get_templates()
    num_templates = rnd.randint(1,len(templates))
    templates_copy = templates[:]
    rnd.shuffle(templates_copy)
    return templates_copy[:num_templates]

def generate_report(url, image_id):
    rnd = random.Random(image_id)
    picked_templates = pick_random_templates(rnd)
    suggestions = []
    for template, fill_function in picked_templates:
        template, context = fill_function(rnd,template)
        suggestions.append(Suggestion(template,context))
    return Face(url,suggestions)

def render_suggestion(suggestion):
    rendered = render_template(suggestion.template, **suggestion.context)
    return rendered