from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Obter o modelo de usuário customizado
User = get_user_model()

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Este e-mail já está cadastrado.')
        else:
            messages.error(request, 'As senhas não coincidem.')

    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autentica usando o email como username
        user = authenticate(request, username=email, password=password)
        print("0")
        if user is not None:
            print("1")
            login(request, user)
            return redirect('conteudo')  # Redireciona para 'conteudo'
        else:
            print("2")
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login.html')


@login_required
def conteudo_view(request):
    return render(request, "conteudo.html")

from django.shortcuts import render

def pagamento_view(request):
    if request.method == "POST":
        # Aqui você pode processar os dados do pagamento
        # Por exemplo, salvar informações no banco ou integrar com um gateway de pagamento
        return render(request, 'pagamento_concluido.html')  # Exemplo de página de confirmação
    return render(request, 'pagamento.html')

def pagamento2_view(request):
    if request.method == "POST":
        # Aqui você pode processar os dados do pagamento
        # Por exemplo, salvar informações no banco ou integrar com um gateway de pagamento
        return render(request, 'pagamento_concluido.html')  # Exemplo de página de confirmação
    return render(request, 'pagamento2.html')

def pagamento3_view(request):
    if request.method == "POST":
        # Aqui você pode processar os dados do pagamento
        # Por exemplo, salvar informações no banco ou integrar com um gateway de pagamento
        return render(request, 'pagamento_concluido.html')  # Exemplo de página de confirmação
    return render(request, 'pagamento3.html')