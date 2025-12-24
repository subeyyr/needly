from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Service

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    return render(
        request,
        'services/service_detail.html',
        {'service': service}
    )

@login_required
def home(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'home.html', {'categories': categories})
@login_required
def category_services(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    services = Service.objects.filter(category=category, is_active=True)

    return render(
        request,
        'services/category_services.html',
        {
            'category': category,
            'services': services
        }
    )

from django.db.models import Q
from .models import Service

def service_search(request):
    query = request.GET.get('q')

    services = Service.objects.none()

    if query:
        services = Service.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )

    return render(request, 'services/search_results.html', {
        'services': services,
        'query': query
    })
