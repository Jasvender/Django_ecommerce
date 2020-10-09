import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from blog_category.models import Categories
from ecommerce_project.utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3900200021)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "blogs/{new_filename}/{final_filename}".format(
                new_filename=new_filename,
                final_filename=final_filename
            )

class BlogQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    def popular(self):
        return self.filter(popular=True)

class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()
    def populars(self):
        return self.get_queryset().popular()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

class Blog(models.Model):
    categories  = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(default="abc", blank=True, unique=True)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    description = models.TextField()
    active      = models.BooleanField(default=True)
    popular     = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = BlogManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("blogs:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title

def blog_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(blog_pre_save_receiver, sender=Blog)
