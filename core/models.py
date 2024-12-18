from django.db.models import EmailField, CharField, UUIDField, BooleanField, Model
from django.contrib.auth.models import PermissionsMixin, UserManager, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.fields import BooleanField
from django.forms import IntegerField
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            return ValueError(_("Email field is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True. "))
        elif extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True. "))
        elif extra_fields.get('is_admin') is not True:
            raise ValueError(_("Superuser must have is_admin=True. "))
        
        return self.create_user(email, password, **extra_fields)
    
def file_generate_upload_path(instance, filename):
	# Both filename and instance.file_name should have the same values
    return f"profile_image/{instance.uuid}"

class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(unique=True, blank=True)
    full_name = CharField(max_length=255, blank=True)
    phone_number = CharField(max_length=10, blank=True)
    password = CharField(max_length=255, blank=True)
    age = models.IntegerField()
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    
    is_active = BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "phone_number", "age"]

    
    def has_perm(self, perm: str, obj=True) -> bool:
        return self.is_admin
    
    def has_module_perms(self, app_label: str) -> bool:
        return True

    def __str__(self):
        return self.full_name
