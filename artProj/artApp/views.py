from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'artApp/index.html')

def project_detail(request):
    return render(request, 'artApp/project-detail.html')

# 좋아요 url
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.update_counter()
    return JsonResponse({'message': 'Like successful'})

# exhibition1
def hong0(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/enter.html', {'posts': posts})

def hong1(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/1page.html', {'posts': posts})

def hong2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/2page.html', {'posts': posts})

def hong3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/3page.html', {'posts': posts})

def hong4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/4page.html', {'posts': posts})

def hong5(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition1/5page.html', {'posts': posts})

# exhibition2
def exhibition2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition2/enter.html', {'posts': posts})

def exhibition2_1(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition2/1page.html', {'posts': posts})

def exhibition2_2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition2/2page.html', {'posts': posts})

def exhibition2_3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition2/3page.html', {'posts': posts})

def exhibition2_4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition2/4page.html', {'posts': posts})


# exhibition3
def exhibition3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/enter.html', {'posts': posts})

def exhibition3_1(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/1page.html', {'posts': posts})

def exhibition3_2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/2page.html', {'posts': posts})

def exhibition3_3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/3page.html', {'posts': posts})

def exhibition3_4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/4page.html', {'posts': posts})

def exhibition3_5(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/exhibition3/5page.html', {'posts': posts})


#홍세연 작가 페이지
def hong_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/artist/artist-page-hong.html', {'posts': posts})

# 홍원표 작가 페이지
def pyo_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/artist/artist-page-pyo.html', {'posts': posts})

# 유근택 작가 페이지
def yoo_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/artist/artist-page-yoo.html', {'posts': posts})




