import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from ecommerce_project.utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3900200021)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "category/{new_filename}/{final_filename}".format(
                new_filename=new_filename,
                final_filename=final_filename
            )

class Categories(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(default="blog", blank=True, unique=True)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active      = models.BooleanField(default=True)

    # objects = CategoryManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title

def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver, sender=Categories)
