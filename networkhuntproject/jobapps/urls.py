from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Landing_PageView.as_view(), name="landing_page"),
    path('job_home', login_required(JobHomeView.as_view()), name="home"),
    path('job/<int:pk>', login_required(JobDetailView.as_view()), name='job-detail'),
    path('add_job/', login_required(AddJobView.as_view()), name='add_job'),
    path('job/edit/<int:pk>', login_required(UpdateJobView.as_view()), name='update_job'),
    path('job/<int:pk>/remove', login_required(DeleteJobView.as_view()), name='delete_job'),
    path('jobsearch/', login_required(JobSearchView), name='job_search_results'),
    path('faqs', login_required(FAQS_PageView.as_view()), name='faqs_page'),
]
