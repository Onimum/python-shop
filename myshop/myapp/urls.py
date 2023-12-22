from django.urls import path
from myapp.views import index, indexItem, add_item, update_item

app_name = 'myapp'

urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    path("", index),
    path("<int:my_id>/", indexItem, name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    # http://127.0.0.1:8000/myapp/hello
    # http://127.0.0.1:8000/myapp/
    # path("contacts/", contacts)
    # http://127.0.0.1:8000/myapp/contacts
]
