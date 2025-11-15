from django.urls import path
from .views import (
    home,
    DiaryListView, DiaryCreateView, DiaryDetailView,
    ProjectListView, ProjectCreateView, ProjectDetailView,
    SketchListView, SketchCreateView,
    SuggestView  # new view for general suggestions
)

urlpatterns = [
    path('', home, name='home'),

    # Diary URLs
    path('diary/', DiaryListView.as_view(), name='diary-list'),
    path('diary/new/', DiaryCreateView.as_view(), name='diary-create'),
    path('diary/<int:pk>/', DiaryDetailView.as_view(), name='diary-detail'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    # Sketch URLs
    path('sketches/', SketchListView.as_view(), name='sketch-list'),
    path('sketches/new/', SketchCreateView.as_view(), name='sketch-create'),

    # Suggestion page
    path('suggest/', SuggestView.as_view(), name='suggest'),
]