from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pymes/', include('pymes.urls', namespace="pymes")),
    #url(r'^simu/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hirefire/','TemplateView', {'template': settings.MEDIA_ROOT, 'mimetype': 'text/plain'})
    #url(r'^hirefire/','serve', {'document_root': settings.MEDIA_ROOT}),
)
