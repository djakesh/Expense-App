from django.urls import path
from .views import (
    # expense_create_view,
    # expenses_list_api_view,
    # expense_retrieve_api_view,
    # expense_put_update_api_view, expense_delete_api_view
    # ExpenseCreateAPIView,
    # ExpenseListAPIView,
    # ExpenseRetrieveAPIView,
    # ExpenseUpdateAPIView,
    # ExpenseDeleteAPIView,
    ExpenseListCreateAPIView, ExpenseRetrieveUpdateDestroyAPIView

)
urlpatterns = [
    path('',ExpenseListCreateAPIView.as_view()),
    path('<int:pk>/',ExpenseRetrieveUpdateDestroyAPIView.as_view()),


    # path('create/', ExpenseCreateAPIView.as_view()),
    # path('list/', ExpenseListAPIView.as_view()),
    # path('expense/<int:pk>/', ExpenseRetrieveAPIView.as_view()),
    # path('expense-update/<int:pk>/', ExpenseUpdateAPIView.as_view()),
    # path('expense-delete/<int:pk>/', ExpenseDeleteAPIView.as_view()),
]





# urlpatterns = [
#     path('create/', expense_create_view, name='expense_create'),
#     path('list/', expenses_list_api_view, name='expense_list'),
#     path('expense/<int:pk>/', expense_retrieve_api_view, name='expense_list'),
#     path('expense-update/<int:pk>/', expense_put_update_api_view, name='expense_update'),
#     path('expense-delete/<int:pk>/', expense_delete_api_view, name='expense_delete'),
# ]
