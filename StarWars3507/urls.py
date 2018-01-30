from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from starwars.views import IndexMovie

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('starwars.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
