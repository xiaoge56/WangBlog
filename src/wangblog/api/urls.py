from django.conf.urls import url, include
from rest_framework import routers
from wangblog.api.endpoints.user import UserViewSet, UserDetailsView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', UserDetailsView.as_view(), name='user-details' ),
]