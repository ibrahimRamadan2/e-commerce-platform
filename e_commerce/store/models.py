from django.db import models
from django.utils.translation import gettext as _ 
from users.models import User

# Create your models here.
class Prodcut(models.Model):
    title = models.CharField(max_length=200)    
    demo = models.TextField(default="")
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    # category_id 
    rate = models.FloatField(default=0.0) 
    available_count = models.IntegerField(default=0)
    price = models.FloatField(null=False, blank=False)
    images_urls = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    # brand_id 
    
    
class Category(models.Model):
    '''Model definition for Category.'''
    name = models.CharField(_("category"), max_length=150)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    
class Brand(models.Model):
    title = models.CharField(_(""), max_length=100)
    logo = models.TextField(_(""))
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    product = models.ForeignKey(Prodcut, verbose_name=_(""), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_(""),  auto_now_add=True)
    updated_at = models.DateTimeField(_(""), auto_now=True)
    is_deleted = models.BooleanField(_(""))
    status = models.CharField(_(""), max_length=50)
    count  = models.IntegerField(_(""))
    
    
    # validation 
    # count > 0 
    # produtct is a available 
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name




class Review(models.Model):
    title = models.CharField(_(""), max_length=200)    
    text = models.TextField(_(""))
    rate = models.FloatField(_(""))
    product = models.ForeignKey(Prodcut, verbose_name=_(""), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return self.name

