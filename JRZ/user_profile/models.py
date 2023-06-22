from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image
from hr_system.models import Employee, Manager, Department


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='profile',
        null=True, blank=True,
    )
    picture = models.ImageField(_("picture"), upload_to='user_profile/pictures')
    employee = models.OneToOneField(
        Employee,
        verbose_name=_("employee profile"), 
        on_delete=models.CASCADE,
        related_name='employee_profile',
        editable=False,
        null=True, blank=True,
    )
    @property
    def manager(self):
        if self.employee:
            return self.employee.department.manager
        return None

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.picture:
            pic = Image.open(self.picture.path)
            if pic.width > 300 or pic.height > 300:
                new_size = (300, 300)
                pic.thumbnail(new_size)
                pic.save(self.picture.path)
    
class ManagerProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='manager_user_profile',
        null=True, blank=True,
    )
    picture = models.ImageField(_("picture"), upload_to='user_profile/pictures')
    manager = models.OneToOneField(
        Manager,
        verbose_name=_("manager profile"), 
        on_delete=models.CASCADE,
        related_name='manager_profile',
        null=True, blank=True,
    )
    @property
    def get_department(self):
        if self.manager:
            return Department.objects.filter(manager=self.manager).get()



    @property
    def employees(self):
        if self.manager:
            obj=Employee.objects.filter(department=self.get_department)
            return obj
        return None

    class Meta:
        verbose_name = _("manager profile")
        verbose_name_plural = _("manager profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.picture:
            pic = Image.open(self.picture.path)
            if pic.width > 300 or pic.height > 300:
                new_size = (300, 300)
                pic.thumbnail(new_size)
                pic.save(self.picture.path)
