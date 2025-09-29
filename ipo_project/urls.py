# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
# # from ipo.views import upcoming_ipos 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('ipo.urls')), 
#     # path('', include('ipo.urls')),
#     # path('', upcoming_ipos, name='home'),
# ]

# # Serve media files
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from ipo import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/ipo/', include('ipo.api_urls')),  # API endpoints
#     path('', views.dashboard, name='home'),   # dashboard page with HTML
#     path('ipo/export/csv/', views.export_ipos_csv, name='export_csv'),
#     path('ipo/export/excel/', views.export_ipos_excel, name='export_excel'),
# ]



from django.contrib import admin
from django.urls import path, include
from ipo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ipo/', include('ipo.urls')),  # API & export
    path('', views.dashboard, name='home'),  # dashboard page
]
