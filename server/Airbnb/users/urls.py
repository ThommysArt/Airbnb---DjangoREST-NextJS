from django.urls import path, include # This needs to be added

urlpatterns = [
    (r'^auth/', include('rest_framework_social_oauth2.urls')),
]
