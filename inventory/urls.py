from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^transfer/', 'warehouse.views.transfer', name='transfer'),
    url(r'^admin/', include(admin.site.urls)),
)
