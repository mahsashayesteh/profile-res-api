from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            return ValueError('کاربر باید یک آدرس ایمیل داشته باشد.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=70)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retireve full name of user"""
        return self.name

    def get_short_name(self):
        """Retireve short name of user"""
        return self.name

    def __str__(self):
        return self.email
