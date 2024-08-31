
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
# from django.utils.translation import gettext as _
from django.utils.translation import gettext as _ 

# from .managers import CustomUserManager 

class User(AbstractBaseUser):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"),unique=True, blank=True)
    created_at = models.DateTimeField(auto_created=True,  auto_now=False)
    updated_at = models.DateTimeField(auto_created=False,  auto_now=True)
    is_deleted = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
    


class UserAdddressess(models.Model):
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    address = models.TextField(blank=False , null=False)
    