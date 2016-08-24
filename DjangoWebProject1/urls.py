from django.conf.urls import include, url

import blog.views
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # редирект на /blog/
    url(r'^$', RedirectView.as_view(url='blog/')),
    # приложение blog/
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]
