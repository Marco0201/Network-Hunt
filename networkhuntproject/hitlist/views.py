from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import *
from django.db.models import Q


class HitlistHomeView(ListView):
    model = HitlistPerson
    template_name = 'hitlist.html'
    ordering = ['name']
    paginate_by = 10


def HitlistSearchView(request):    

    hit_list = HitlistPerson.objects.all()
    query = request.GET.get('q')

    if query:
        hit_list = HitlistPerson.objects.filter(
                Q(name__icontains=query) | Q(company__icontains=query) | Q(position__icontains=query)
        )
            
    paginator = Paginator(hit_list.order_by('name'), 10)
    page = request.GET.get('page')

    try:
        hitlist = paginator.page(page)
    except PageNotAnInteger:
            hitlist = paginator.page(1)
    except EmptyPage:
        hitlist = paginator.page(paginator.num_pages)

    context = {
        'hitlist': hitlist
    }
    return render(request, "hitlist_search_results.html", context)

class HitlistDetailView(DetailView):
    model = HitlistPerson
    template_name = 'hitlist_detail.html'

class AddHitlistView(CreateView):
    model = HitlistPerson
    template_name = 'add_hitlist.html'
    form_class = HitlistForm


class UpdateHitlistView(UpdateView):
    model = HitlistPerson
    template_name = 'update_hitlist.html'
    form_class = EditHitlist


class DeleteHitlistView(DeleteView):
    model = HitlistPerson
    template_name = 'delete_hitlist.html'
    success_url = reverse_lazy("hitlist")