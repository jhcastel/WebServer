from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pymes/', include('pymes.urls', namespace="pymes")),
    #url(r'^simu/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^hirefire/7f53079738f19d64899f5c648a5c9db8e260cee5/info', TemplateView.as_view(template_name='info', content_type='application/json')), #{'template': settings.MEDIA_ROOT, 'mimetype': 'text/plain'})
    #url(r'^hirefire/','serve', {'document_root': settings.MEDIA_ROOT}),
)
=======
    url(r'^hirefire/7f53079738f19d64899f5c648a5c9db8e260cee5/info','serve', {'document_root': settings.MEDIA_ROOT}),
)
	#url(r'^hirefire/', include('views.hirefire', namespace="hirefire")),

>>>>>>> 4c0e9915e27c632e6007c1cce797c92e1fb039b1
