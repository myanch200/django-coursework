"""
Тъй като django template engine не приема параметри при извикване то на функции
 ни се налага да си създададем собствени тагове, които да го правят за нас
"""

from django import template

register = template.Library()

@register.filter(name='dict_key')
def dict_key(d, key):    
   return d.get(key)