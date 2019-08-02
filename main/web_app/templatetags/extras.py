from django import template

register = template.Library()
# remember to {% load my_templates %} on top of html
# replace my_templates with whatever you decide to call .py file containing extra template tags
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut',cut)
