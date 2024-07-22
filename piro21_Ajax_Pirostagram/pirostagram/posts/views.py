from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

@csrf_exempt
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'likes_count': post.likes.count(), 'liked': liked})

@csrf_exempt
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content')
    comment = Comment.objects.create(post=post, content=content)
    return JsonResponse({'comment_id': comment.id, 'content': comment.content})

@csrf_exempt
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'success': True})