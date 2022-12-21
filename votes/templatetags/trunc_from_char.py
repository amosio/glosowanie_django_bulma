from django import template

register = template.Library()


@register.filter(name='trunc_from_char')
def trunc_from_char(s, ch):
    """base translate to Polish"""
    where_finded = s.find('@')
    if s=='': return ''
    if where_finded == -1: return s
    return s[:where_finded]
