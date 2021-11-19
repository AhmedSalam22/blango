from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html


user_model = get_user_model()

from django import template

register = template.Library()


@register.filter
def author_details(user, current_user=None):
  if not isinstance(user, user_model):
    return ''
  
  if user == current_user:
    return format_html('<strong>Me</strong>')
  
  if user.first_name and user.last_name:
    name =  escape(f'{user.first_name} {user.last_name}')
  else:
    name =  escape(f'{user.username}')
  
  if user.email:
    email = escape(user.email)
#     prefix = f'<a href="mailto:{email}">'
    prefix = format_html('<a href="mailto:{}">', user.email)
    suffix = '</a>'
  else:
    prefix, suffix = '', ''
    
  return mark_safe(f'{prefix}{name}{suffix}')
    