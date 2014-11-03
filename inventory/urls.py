from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^transfer/', 'order.views.transfer_stock', name='transfer-stock'),
    url(r'^check_stock/(?P<store_id>\d+)/(?P<iv_id>\d+)/$', 'store.views.check_stock', name='check_stock-stock'),
    url(r'^add/', 'store.views.add_stock', name='add-stock'),
    url(r'^admin/', include(admin.site.urls)),
)
