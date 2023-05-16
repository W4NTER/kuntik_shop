from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView
# Create your views here.


class Shop(ListView):
    model = Post
    template_name = "shop/shop.html"
    context_object_name = 'posts'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магазин'
        return context


def post(request, post_id):
    posts = Post.objects.get(id=post_id)
    return render(request, 'shop/post.html', {'posts': posts})