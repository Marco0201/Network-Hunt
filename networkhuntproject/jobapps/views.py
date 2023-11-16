from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import *
from django.db.models import Q

# Create your views here.

class Landing_PageView(TemplateView):
    template_name = 'landing_page.html'

class JobHomeView(ListView):
    model = Job_application
    template_name = 'home.html'
    ordering = ['-date_applied']
    paginate_by = 11

    
def JobSearchView(request):

    job_list = Job_application.objects.all()
    query = request.GET.get('q')

    if query:
        job_list = Job_application.objects.filter(
             Q(position__icontains=query) | Q(company__icontains=query))
        
    paginator = Paginator(job_list.order_by('date_applied'), 10)
    page = request.GET.get('page')

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        'jobs': jobs
    }
    return render(request, "job_search_results.html", context)


class JobDetailView(DetailView):
    model = Job_application
    template_name = 'job_detail.html'


class AddJobView(CreateView):
    model = Job_application
    template_name = 'add_job.html'
    form_class = PostJobForm


class UpdateJobView(UpdateView):
    model = Job_application
    template_name = 'update_job.html'
    form_class = EditJobForm


class DeleteJobView(DeleteView):
    model = Job_application
    template_name = 'delete_job.html'
    success_url = reverse_lazy("home")

class AboutView(TemplateView):
    template_name = 'about.html'

class FAQS_PageView(TemplateView):
    template_name = 'faqs.html'