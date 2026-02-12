from django.urls import path
from django.conf.urls.static import static, settings
from . import views


urlpatterns = [
    
    
    
    #path('delete/<int:pk>/', views.delete_item_api, name='delete_item_api'),
    #path('update/<int:pk>/', views.putItem, name='putItem')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)