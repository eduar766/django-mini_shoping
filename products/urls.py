from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
