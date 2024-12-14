from django.contrib import admin
from django.urls import path
from EdUnity import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login_view, name='login'),
    path('conteudo/', views.conteudo_view, name='conteudo'),  # Página de conteúdo após login
    path('pagamento/', views.pagamento_view, name='pagamento'),
    path('pagamento2/', views.pagamento2_view, name='pagamento2'),
    path('pagamento3/', views.pagamento3_view, name='pagamento3'),
]

