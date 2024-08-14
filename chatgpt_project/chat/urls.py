from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # 홈 페이지
    path('chat/', views.ChatView.as_view(), name='chat'),  # ChatGPT 서비스 페이지
    path('history/', views.SearchHistoryView.as_view(), name='search_history'),
    # 로그인/로그아웃 URL 등 추가
    # path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),  # 로그인 페이지
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # 로그아웃 후 홈으로 리디렉션
]
