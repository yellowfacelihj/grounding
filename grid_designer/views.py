from django.shortcuts import render
from django.views.generic import CreateView
from .models import GroundingMeshProject
from .forms import ProjectGrid
from .createGrid import evaluate_case

# Create your views here.

def index(request):
    return render(request, 'grid_designer/index.html')

def about(request):
    return render(request, 'grid_designer/about.html')

def contact(request):
    return render(request, 'grid_designer/contact.html')

def project_grid(request):
    if request.method == 'POST':
        form = ProjectGrid(request.POST)
        from pprint import pprint
        if form.is_valid():
            success, *data = evaluate_case(form.__dict__['cleaned_data'])
            context = {
                'img_path': data[0],
                'conductor_diameter': '{0:.2f}'.format(data[1]*1000),
                'final_spacement': data[3]
            }
            if success:
                return render(request, 'grid_designer/success.html', context)
            return render(request, 'grid_designer/fail.html', context)
        
    else:
        form = ProjectGrid()

    context = {
        'form': form
    }
    return render(request, 'grid_designer/design.html', context)
