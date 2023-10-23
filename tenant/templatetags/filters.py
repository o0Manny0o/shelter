from django import template

register = template.Library()


@register.filter(name='removeFirst')
def cut(value):
    return value[1:]
