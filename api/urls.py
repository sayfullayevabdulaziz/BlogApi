from django.urls import path
from .views import ListViewSets #ListPost, RetrievePost
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('v1', ListViewSets, basename='v1')
urlpatterns = router.urls




# urlpatterns = [
#     path('v1/', ListPost.as_view()),
#     path('v1/<int:pk>/', RetrievePost.as_view()),
# ]
