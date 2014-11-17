from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pymes/', include('pymes.urls', namespace="pymes")),
    #url(r'^simu/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^hirefire/7f53079738f19d64899f5c648a5c9db8e260cee5/info','serve', {'document_root': settings.MEDIA_ROOT}),
)
=======
	#url(r'^hirefire/', include('views.hirefire', namespace="hirefire")),
)
>>>>>>> ad29b7b71b5eff2b2d43b4a8c40b5ca31e884fd3
