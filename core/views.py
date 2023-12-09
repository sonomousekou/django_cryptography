# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Config

def view_configs(request):
    # Read - Retrieve all Config objects
    configs = Config.objects.all()

    return render(request, 'config_list.html', {'configs': configs})

def create_config(request):
    # Create - Add a new Config object
    if request.method == 'POST':
        cle = request.POST.get('cle')
        valuer = request.POST.get('valuer')
        config_ob = Config.objects.create(cle=cle)
        if config_ob:
            config_ob.set_value(valuer)
            config_ob.save()

    return render(request, 'create_config.html')
