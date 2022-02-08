from django.urls import path

from billing.api.views.billing import InvoiceCreate
from .views import Index
from .api.views.billing import ClientList

app_name = "billing"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("api/clients/", ClientList.as_view(), name="client-list"),
    path("api/invoices/", InvoiceCreate.as_view(), name="invoice-create"),
]
