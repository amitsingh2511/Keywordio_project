from book_api.viewset import BookViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book',BookViewset)