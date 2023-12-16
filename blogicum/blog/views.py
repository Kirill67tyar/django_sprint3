from django.shortcuts import render
from django.http import Http404



# def index(request):
#     context = {
#         'posts': posts,
#     }
#     return render(request,
#                   'blog/index.html',
#                   context
#                   )


# def post_detail(request, id):
#     posts_by_id = {post['id']: post for post in posts}
#     if id not in posts_by_id:
#         raise Http404('Page not found.')
#     context = {
#         'post': posts_by_id[id],
#     }
#     return render(request,
#                   'blog/detail.html',
#                   context
#                   )


# def category_posts(request, category_slug):
#     context = {
#         'category_slug': category_slug,
#     }
#     return render(request,
#                   'blog/category.html',
#                   context
#                   )
