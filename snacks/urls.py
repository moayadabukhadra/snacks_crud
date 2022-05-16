from django.urls import path
from .views import (SnackListView,
                    SnackDetailView,
                    SnackUpdateView,
                    SnackDeleteView,
                    SnackCreateView
                    )

urlpatterns = [
    path('', SnackListView.as_view(), name = "snack_list"),
    path('create/', SnackCreateView.as_view(), name = "create_snack"),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = "update_snack"),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name = "delete_snack"),
    path('<int:pk>/' , SnackDetailView.as_view() , name='snack_detail')
]