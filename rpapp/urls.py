from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^allcontracts/$', views.contract_list, name='contract_list'),
    url(r'^free/$', views.post_free_list, name='post_free_list'),
    url(r'^leased/$', views.post_leased_list, name='post_leased_list'),
    url(r'^allarendators/$', views.arendator_list, name='arendator_list'),
    #-----------------------------------------------------------------------------
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^contract/(?P<pk>\d+)/$', views.contract_detail, name='contract_detail'),
    url(r'^arendator/(?P<pk>\d+)/$', views.arendator_detail, name='arendator_detail'),
    #-----------------------------------------------------------------------------
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^contract/new/$', views.contract_new, name='contract_new'),
    url(r'^arendator/new/$', views.arendator_new, name='arendator_new'),
    #-----------------------------------------------------------------------------
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^contract/(?P<pk>\d+)/edit/$', views.contract_edit, name='contract_edit'),
    url(r'^arendator/(?P<pk>\d+)/edit/$', views.arendator_edit, name='arendator_edit'),
    #-----------------------------------------------------------------------------
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #-----------------------------------------------------------------------------
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^contract/(?P<pk>\d+)/remove/$', views.contract_remove, name='contract_remove'),
    url(r'^arendator/(?P<pk>\d+)/remove/$', views.arendator_remove, name='arendator_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
