from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    # Aquí van la las variables para la plantilla
    context = {}
    return render(request,'test.html', context)