from django.urls import path
from . import views
from .views import AboutPageView
urlpatterns = [
    path('', views.index),
    path('bookings/', views.index, name='all-bookings'),
    path('bookings/<slug:course_slug>/sucess', views.confirm_registration, name='confirm-registration'),
    path('bookings/<slug:course_slug>', views.courses_details, name='course-detail'),
    path("about/", AboutPageView.as_view(), name="about")
]

# urlpatterns = [
#     path('', views.index, name='all-bookings'),
#     path('<slug:course_slug>/sucess', views.confirm_registration, name='confirm-registration'),
#     path('<slug:course_slug>', views.courses_details, name='course-detail')
# ]