from django.template import Library

register = Library()

@register.inclusion_tag('core/pagination.html')
def pagination(request, paginator, current_page, query, redirect):
  context = {
   'paginator': paginator,
   'request': request,
   'page_obj': current_page,
   'query': query,
   'redirect': redirect
  }
  return context
