from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Idea, IdeaStar
from .forms import IdeaForm

def idea_list(request):
    order = request.GET.get('order', '-created_at')
    if order == 'stars':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif order == 'name':
        ideas = Idea.objects.order_by('title')
    elif order == 'created':
        ideas = Idea.objects.order_by('created_at')
    else:
        ideas = Idea.objects.order_by('-created_at')
    return render(request, 'ideas/idea_list.html', {'ideas': ideas, 'current_order': order})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form': form})

@login_required
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_form.html', {'form': form})

@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('idea_list')

@login_required
def idea_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    star, created = IdeaStar.objects.get_or_create(idea=idea, user=request.user)
    if not created:
        star.delete()
    return redirect('idea_detail', pk=pk)