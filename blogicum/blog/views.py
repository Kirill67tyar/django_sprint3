from django.shortcuts import (
    render,
    get_object_or_404,
)

from blog.models import (
    Post,
    Category,
)


def index(request):
    posts_qs = Post.valid_posts.all()[:5]
    context = {
        'post_list': posts_qs,
    }
    return render(request,
                  'blog/index.html',
                  context,
                  )


def post_detail(request, pk):
    posts_qs = Post.valid_posts.all()
    post = get_object_or_404(
        klass=posts_qs,
        pk=pk,
    )
    context = {
        'post': post,
    }
    return render(request,
                  'blog/detail.html',
                  context
                  )


def category_posts(request, category_slug):
    category_qs = Category.objects.filter(
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.valid_posts.filter(
        category__slug=category_slug,
    )
    category = get_object_or_404(
        klass=category_qs,
        slug=category_slug,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request,
                  'blog/category.html',
                  context
                  )
