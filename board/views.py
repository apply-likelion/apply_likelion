from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Article
from .forms import NewArticle
# Create your views here.
def welcome(request):
    return render(request, 'board/index.html')

def read(request):
    articles = Article.objects.all()
    return render(request, 'board/funccrud.html',{'boards':articles})

def create(request):
    # 새로운 데이터 저장역할 == post
    if request.method == 'POST':
        form = NewArticle(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 글쓰기 페이지 띄우는 역할== get
    else:
        # 단순히 입력받을 수 있는 form을 띄워줘라
        form = NewArticle()
        return render(request, 'board/new.html', {'form':form})

    return
def update(request, pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고 오기
    article=get_object_or_404(Article, pk=pk)

    # 해당하는 블로그 객체번호 pk에 맞는 입력공간 new.html이 해당하겟지
    form = NewArticle(request.POST, instance = article)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'board/new.html', {'form':form})
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('home')