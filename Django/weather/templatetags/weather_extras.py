from django import template

register = template.Library()


@register.filter(name="showHour")
def showHour(value):
    answer = value.split()[-1]
    return answer
