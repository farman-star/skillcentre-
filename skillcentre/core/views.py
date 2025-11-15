from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import DiaryEntry, Project, Sketch, Comment
from django.views import View
# Homepage view
def home(request):
    context = {
        'username': 'Rihan',
        'avatar_url': '/media/avatars/rihan.jpg',
        'bio': 'Self-taught developer and creative thinker.',
        'skills': ['Python', 'Django', 'Sketching'],
        'interests': ['Machine Learning', 'Cartoons', 'Emotional Design'],
        'resume_url': '/media/rihan_resume.pdf',
        'email': 'rihan@example.com',
        'latest_diaries': DiaryEntry.objects.filter(is_private=False).order_by('-created_at')[:3],
        'latest_projects': Project.objects.all().order_by('-created_at')[:3],
        'now': timezone.now(),
    }
    return render(request, 'home.html', context)

# Diary view
class DiaryListView(ListView):
    model = DiaryEntry
    template_name = 'diary_list.html'
    context_object_name = 'diary_entries'

    def get_queryset(self):
        return DiaryEntry.objects.filter(is_private=False).order_by('-created_at')

class DiaryCreateView(CreateView):
    model = DiaryEntry
    fields = ['title', 'content', 'emotion_tag', 'is_private']
    template_name = 'diary_form.html'
    success_url = '/diary/'

    def form_valid(self, form):
        return super().form_valid(form)

class DiaryDetailView(DetailView):
    model = DiaryEntry
    template_name = 'diary_detail.html'
    context_object_name = 'diary'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        entry = self.get_object()
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(content=content, diary=entry)
        return redirect('diary-detail', pk=entry.pk)

# Project views
class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().order_by('-created_at')

class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'description', 'tech_stack', 'upload']
    template_name = 'project_form.html'
    success_url = '/projects/'

    def form_valid(self, form):
        return super().form_valid(form)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(content=content, project=project)
        return redirect('project-detail', pk=project.pk)

# Sketch views
class SketchListView(ListView):
    model = Sketch
    template_name = 'sketch_list.html'
    context_object_name = 'sketches'

    def get_queryset(self):
        return Sketch.objects.all().order_by('-created_at')

class SketchCreateView(CreateView):
    model = Sketch
    fields = ['title', 'image', 'description']
    template_name = 'sketch_form.html'
    success_url = '/sketches/'

    def form_valid(self, form):
        return super().form_valid(form)

class SuggestView(View):
    template_name = 'suggest.html'

    def get(self, request):
        suggestions = Comment.objects.filter(diary=None, project=None).order_by('-created_at')
        return render(request, self.template_name, {'suggestions': suggestions})

    def post(self, request):
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(content=content)
        return redirect('suggest')