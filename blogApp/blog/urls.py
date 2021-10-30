from django.conf.urls import url
from .views import index, new_entry, view_entry, delete_entry, delete_comment, update_entry, login

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new_entry$', new_entry, name='new-entry'),
    url(r'view_entry/(?P<blog_id>\d+)$', view_entry, name='view-entry'),
    url(r'delete_entry/(?P<blog_id>\d+)$', delete_entry, name='delete-entry'),
    url(r'delete_comment/(?P<blog_id>\d+)/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
    url(r'update_entry/(?P<blog_id>\d+)$', update_entry, name='update-entry'),
    url(r'^login$', login, name='login'),
]
