from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from analytics.mixins import ObjectViewedMixin
from .models import Blog
from blog_category.models import Categories

class BlogListView(ListView):
    # print(request.session.get('first_name', 'unknown')) #get
    queryset = Blog.objects.all()
    template_name = "blogs/blog.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        return context

    # def get_popular_posts(self, *args, **kwargs):
    #     popular = Blog.objects.filter(active=True, popular=True)
    #     return popular

class BlogDetailSlugView(ObjectViewedMixin, DetailView):
    # print(request.session.get('first_name', 'unknown')) #get
    # return render(request, "blogs/blog_detail.html",)
    queryset = Blog.objects.all()
    template_name = "blogs/blog_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Blog.objects.get(slug=slug, active=True)
        except Blog.DoesNotExist:
            raise Http404("Not Found")
        except Blog.MultipleObjectsReturned:
            qs = Blog.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmm")
        return instance
# def BlogListView(request):
#     return render(request, "blogs/blog.html",)
#
# def BlogDetailSlugView(request):
#     return render(request, "blogs/blog_detail.html",)
