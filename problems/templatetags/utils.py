from django import template

register = template.Library()

@register.filter(name="is_equal")
def is_equal(x, y):
    return x == y

@register.filter(name="is_success")
def is_success(i, solved):
    return i in solved
