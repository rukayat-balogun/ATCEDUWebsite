from django.shortcuts import render





def home(request):
    context = {}
    template_name = 'index.html'
    return render(request, template_name, context=context)

