from django import template

register = template.Library()

@register.filter(name='list_index')
def list_index(my_list, iter):
    return my_list[iter]