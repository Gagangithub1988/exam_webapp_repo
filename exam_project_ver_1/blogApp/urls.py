from django.urls import path
from blogApp import views
urlpatterns=[
    path('blog_job_view/',views.blog_job_view),
    path('post_list_view/',views.post_list_view),
    path('tag/(?P<tag_slug>[-\w]+)/',views.post_list_view,name='post_list_by_tag_name'),
    path('share/<int:id>', views.mail_send_view),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/',views.post_detail_view,name='post_detail'),
    
]
