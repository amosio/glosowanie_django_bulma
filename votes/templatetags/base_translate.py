from django import template

register = template.Library()


@register.filter(name='base_translate')
def base_translate(s):
    """base translate to Polish"""
    string_to_translate = s.lower()
    if (string_to_translate == 'none'):
        return 'brak danych'
    if (string_to_translate == 'true'):
        return 'tak'
    if (string_to_translate == 'false'):
        return 'nie'
    return s
