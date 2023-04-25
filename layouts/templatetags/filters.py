from django import template

register = template.Library()

@register.filter(name='test')
def testFilter(value):
    return "<h1> test filter </h1>"