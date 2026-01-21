from django.urls import path
from .views import UniversityListAPIView, UniversityDetailAPIView, ApplicationFieldsAPIView, SubmitApplicationAPIView

urlpatterns = [
    path('universities/', UniversityListAPIView.as_view(), name='university-list'),
    path('universities/<int:university_id>/', UniversityDetailAPIView.as_view(), name=""),
    path('universities/<int:university_id>/fields/', ApplicationFieldsAPIView.as_view(), name='application-fields'), 
    path('application/submit/', SubmitApplicationAPIView.as_view(), name='submit-application'),
]
