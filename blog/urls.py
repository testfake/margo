from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
   	# ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    # ex: /blog/tag/8/
    url(r'^tag/(?P<tag>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # ex: /blog/5/comment/
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
]