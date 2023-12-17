from django.shortcuts import (
    render,
    get_object_or_404,
)

from blog.models import (
    Post,
    Category,
)


QUANTITY_POSTS = slice(5)


def index(request):
    posts_qs = Post.valid_posts.all()[QUANTITY_POSTS]
    context = {
        'post_list': posts_qs,
    }
    return render(
        request,
        'blog/index.html',
        context,
    )


def post_detail(request, post_id):
    posts_qs = Post.valid_posts.all()
    post = get_object_or_404(
        posts_qs,
        pk=post_id,
    )
    context = {
        'post': post,
    }
    return render(
        request,
        'blog/detail.html',
        context,
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.valid_posts.filter(
        category=category,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(
        request,
        'blog/category.html',
        context,
    )
