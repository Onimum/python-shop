from django.urls import path
from myapp.views import (
    add_item,
    update_item,
    delete_item,
    ProductListView,
    ProductDetailView,
    PaymentSuccessView,
    PaymentFailedView,
)

app_name = 'myapp'

urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    # path("", index, name='index'),
    path("", ProductListView.as_view(), name='index'),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("failed/", PaymentFailedView.as_view(), name="failed"),
    path("api/checkout-session/<int:id>/", update_item, name="api_checkout_session"),

]
