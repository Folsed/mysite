from django.shortcuts import render, redirect
from .models import Conference
from .forms import ConferenceForm
from django.views.generic import DetailView, UpdateView, DeleteView


def conferences_home(request):
    conferences = Conference.objects.all()
    return render(request, 'conferences/conferences_home.html', {'conferences': conferences})


# Класс динамической страницы
class ConfDetailView(DetailView):
    model = Conference
    template_name = 'conferences/details_view.html'  # Шаблон обработки страницы
    context_object_name = 'objectkey'    # Ключ по которому передается объект
    

# Класс динамической страницы для редактирования
class ConfEditView(UpdateView):
    model = Conference
    template_name = 'conferences/create.html'
    form_class = ConferenceForm
    
    
# Класс динамической страницы для удаления
class ConfDeleteView(DeleteView):
    model = Conference
    success_url = '/conferences/'
    template_name = 'conferences/conf_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conferences_home')
        else:
            error = 'Not correct format'
    # Новый объект 
    form = ConferenceForm()
    # Словарь для передачи в шаблон 
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'conferences/create.html', data)