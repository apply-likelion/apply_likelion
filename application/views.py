from django.shortcuts import get_object_or_404,render,redirect
from django.utils import timezone
from .models import Application
from .forms import ApplicationForm

def application(request):#작성 페이지 가져오는 함수
    return render(request, 'application.html')

def applicationform(request):#작성 내용 POST방식으로 불러오기
    if request.method=='POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application=form.save(commit=False)
            application.pub_date=timezone.now()
            return redirect('main')
    else: 
        form=ApplicationForm()
        return render(request,'application.html',{'form':form})

#def update(request,pk):#지원서 수정
#   application=get_object_or_404(Application, pk=pk)



