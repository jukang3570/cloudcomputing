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

# 장고운 개인전 url
def project_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/project-detail.html', {'posts': posts})

def project_detail2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/project-detail-2.html', {'posts': posts})

def project_detail3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/project-detail-3.html', {'posts': posts})

def project_detail4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/project-detail-4.html', {'posts': posts})

def project_detail5(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/project-detail-5.html', {'posts': posts})

# 아트랩범어 전시회 url
def reMixing_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/reMixing/reMixing-detail.html', {'posts': posts})

def reMixing_detail2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/reMixing/reMixing-detail-2.html', {'posts': posts})

def reMixing_detail3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/reMixing/reMixing-detail-3.html', {'posts': posts})

def reMixing_detail4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/reMixing/reMixing-detail-4.html', {'posts': posts})

def reMixing_detail5(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/reMixing/reMixing-detail-5.html', {'posts': posts})

# 김성미 개인전 url
def kim_detail(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/kimsungmi/kim-detail.html', {'posts': posts})

def kim_detail2(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/kimsungmi/kim-detail-2.html', {'posts': posts})

def kim_detail3(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/kimsungmi/kim-detail-3.html', {'posts': posts})

def kim_detail4(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/kimsungmi/kim-detail-4.html', {'posts': posts})

def kim_detail5(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'artApp/kimsungmi/kim-detail-5.html', {'posts': posts})

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




