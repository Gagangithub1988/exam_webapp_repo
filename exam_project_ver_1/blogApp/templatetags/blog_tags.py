from blogApp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blogApp/latest_posts123.html')
def show_latest_posts(count=3):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


from django.db.models import Count
@register.inclusion_tag('blogApp/latest_posts123.html')
def get_most_commented_posts(count=5):
    most_updated_post=Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'most_updated_post':most_updated_post}