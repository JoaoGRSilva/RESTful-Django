from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class BlogPost(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.CharField(max_length=512)


    class CatergoryPost(models.TextChoices):
        TECHNOLOGY = "Tech", _("Technology")
        COOKING = "Cook", _("Cooking")
        MUSIC = "Music", _("Music")

    post_category = models.CharField(
        max_length=5,
        choices=CatergoryPost,
        default=CatergoryPost.TECHNOLOGY,
    )

    class TagPost(models.TextChoices):
        TECH = "Tech", _("Tech")
        PROGRAMMING = "Programming", _("Programming")

    post_tag = models.CharField(
        max_length=11,
        choices=TagPost,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)