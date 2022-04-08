from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.vary import vary_on_cookie
import logging
from django.urls import reverse


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
  posts = Post.objects.filter(
    published_at__lte=timezone.now()
  ).select_related('author').defer("created_at", "modified_at")
  
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html", {'posts': posts})


def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
  )

  
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)
      
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)
        
    else:
      comment_form = CommentForm()
  else:
    comment_form = None
  
  return render(request, "blog/post-detail.html", 
                { 
                  "post" : post,
                  'comment_form': comment_form
                }
               )
  


def post_table(request):
    return render(
        request, "blog/post-table.html", {"post_list_url": reverse("post-list")}
    )


def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])
