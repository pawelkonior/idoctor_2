from django import template

register = template.Library()


@register.simple_tag
def make_color(val=None):
    colors = {
        1: 'success',
        2: 'info',
        3: 'warning'
    }

    return colors.get(val, 'success')
