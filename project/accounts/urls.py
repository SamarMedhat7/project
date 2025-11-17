from django.urls import path
from .views import RegisterView, LoginView, StudentDashboardView, AdminDashboardView, TeacherDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('student-dashboard/', StudentDashboardView.as_view(), name='student_dashboard'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('teacher-dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard'),]