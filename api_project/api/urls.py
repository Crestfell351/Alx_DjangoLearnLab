from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
