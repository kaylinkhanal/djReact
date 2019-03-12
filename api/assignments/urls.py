from rest_framework.routers import DefaultRouter
from api.views import AssignmentViewset

router= DefaultRouter()
router.register(r'',AssignmentViewset,base_name='assignments')
urlpatterns=router.urls
