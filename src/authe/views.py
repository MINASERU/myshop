from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import AuthorForm, LoginForm
from .models import Author, ConfirmCode
from .utils import send_code

# Create your views here.
def register(request):
    form=AuthorForm()
    if request.method=='POST':
        save_form=AuthorForm(request.POST)
        if save_form.is_valid():
            author=Author(username=request.POST['username'],email=request.POST['email'])
            author.set_password(request.POST['password'])
            author.save()
            code= ConfirmCode.objects.create(author=author)
            send_code(f"Ваш код подтверждения - http://127.0.0.1:8000/authe/confirm/{code.code}", request.POST['email'])
            message = "Мы отправили на вашу почту код верификации"
            return render(request,'reply.html',{"message":message}) 
        elif Author.objects.filter(username = request.POST['username'], verified = False) or Author.objects.filter(email = request.POST['email'], verified = False):
            author = None
            if Author.objects.filter(username = request.POST['username']):
                author = Author.objects.get(username = request.POST['username'])
            elif Author.objects.filter(email = request.POST['email']):
                author = Author.objects.get(email = request.POST['email'])
            code= ConfirmCode.objects.create(author=author)
            send_code(f"Ваш код подтверждения - http://127.0.0.1:8000/authe/confirm/{code.code}", request.POST['email'])
            message = "Мы отправили на вашу почту код верификации"
            return render(request,'reply.html',{"message":message}) 
        message=save_form.errors
        return render(request,'reply.html',{"message":message})    
                
    return render(request,'signin.html',{'form':form})

def confirm(request, code):
    code = ConfirmCode.objects.filter(code = code)
    message = 'Ваш код не действителен'
    if code:
        if not code.last().confirm:
            code = code.last()
            code.confirm = True
            code.save()
            author = code.author
            author.verified = True
            author.save()
            message = 'Ваша почта подтверждена'
    return render(request, 'reply.html', {'message': message}) 

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            auth_login(request, user)
            return render(request, 'reply.html', {'message': 'Вы зашли', 'success': True})
        return render(request, 'reply.html', {'message': 'Такой пользователь не найден', 'succes':False})
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('my_app:product_list')
