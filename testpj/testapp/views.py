from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'testapp/index.html')

def test(request):
    return render(request, 'testapp/project-detail.html')