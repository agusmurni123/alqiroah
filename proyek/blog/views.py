from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import IndexWeb
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm (request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User dibuat'
            return redirect('index')
        else:
            msg = 'form tidak valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form,'msg':msg})

def login_view(request):
    form = LoginForm (request.POST or None)
    msg =None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.admin:
                login(request,user)
                return redirect('redaksi:adminpage')
            elif user is not None and user.staff:
                login(request,user)
                return redirect('redaksi:staff')
            else:
                msg ='invalid credentials'
        else:
            msg='error validating form'
    return render(request, 'login.html', {'form':form,'msg':msg})

def admin(request):
    return render(request, 'admin.html')
def staff(request):
    data_webs = IndexWeb.objects.all()
    return render(request, 'staff.html',{'object_list':data_webs})

class TampilWeb(ListView):
    queryset = IndexWeb.objects.all()
class TambahWeb(CreateView):
    model = IndexWeb
    fields = '__all__'
    success_url = reverse_lazy('redaksi:beranda')
class DetailWeb(DetailView):
    model = IndexWeb
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
class UpdateWeb(UpdateView):
    model = IndexWeb
    fields = '__all__'
    success_url = reverse_lazy('redaksi:beranda')
class DeleteWeb(DeleteView):
    model =IndexWeb
    fields='__all__'
    success_url = reverse_lazy('redaksi:beranda')

def like_post(request):
    post_id = request.GET.get('post_id')
    try:
        post_id = int(post_id)
        post= IndexWeb.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'success':True,'likes':post.likes})
    except IndexWeb.DoesNotExist:
        return JsonResponse({'success':False,'error':'Post not found'})
    
def view_blogs(request):
    view_id = request.GET.get('view_id')
    try:
        view_id = int(view_id)
        blogs = IndexWeb.objects.get(pk=view_id)
        blogs.views += 1
        blogs.save()
        return JsonResponse({'success':True,'views':blogs.views})
    except IndexWeb.DoesNotExist:
        return JsonResponse({'success':False,'error':'Blog not found'})