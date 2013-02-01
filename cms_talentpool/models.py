from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors.resize import Resize, ResizeToCover
from imagekit.processors.crop import Crop
from imagekit.processors.base import Anchor
from PIL import ImageOps
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.conf import settings
from ckeditor.fields import RichTextField


class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class CustomResize(object):
    
    def __init__(self, width, height):
        self.width, self.height = width, height

    def process(self, img):
        original_width, original_height = img.size
        ratio = max(float(self.width) / original_width,
                float(self.height) / original_height)
        new_width, new_height = (int(original_width * ratio),
                int(original_height * ratio))
        new_img =  Resize(new_width, new_height).process(img)
        return Crop(self.width, self.height, anchor=Anchor.TOP).process(new_img)

class BlackAndWhite(object):
    def process(self, img):
        return ImageOps.grayscale(img)

def company_logo_upload_path(instance, filename):
    return "upload/original-logo-%s" % slugify(instance.name)

def people_photo_upload_path(instance, filename):
    return "upload/original-photo-%s" % slugify(instance.full_name_slug)

class Company(models.Model):
    name = models.CharField(_('label'), max_length=200)
    original_logo = models.ImageField(upload_to=company_logo_upload_path)
    logo = ImageSpecField([ResizeToCover(*settings.CIE_LOGO_THUMB_SIZE)], 
                          image_field='original_logo',
                          format='png')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")
        app_label = string_with_title('cms_talentpool', _("talent pool"))

    
class SkillCategory(models.Model):
    label = models.CharField(_('label'), max_length=200)
    order = models.PositiveSmallIntegerField(_('order'))
    
    class Meta:
        verbose_name = _("skill category")
        verbose_name_plural = _("skill categories")
        ordering = ["order"]
        app_label = string_with_title('cms_talentpool', _("talent pool"))
        
    def __unicode__(self):
        return self.label

class TalentPeople(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    full_name_slug = AutoSlugField(unique=True,
                                   always_update=True,
                                   populate_from='get_full_name')
    email = models.EmailField(_('e-mail address'), blank=True)
    
    original_photo = models.ImageField(upload_to=people_photo_upload_path)
    photo = ImageSpecField([CustomResize(*settings.TALENT_PHOTO_THUMB_SIZE)], 
                            image_field='original_photo',
                            format='png')
    
    skills = models.ManyToManyField(SkillCategory, verbose_name=_("skills"))
    
    company = models.ForeignKey(Company, verbose_name=_("compagny"))
    post = models.CharField(_('post'), max_length=200)

    quote = models.TextField(_("quote"))
    description = models.TextField(_("description"), blank=True)
    
    cv_domain = RichTextField(blank=True, config_name='talentpool_ckeditor')
    cv_experiences = RichTextField(blank=True, config_name='talentpool_ckeditor')
    cv_studies = RichTextField(blank=True, config_name='talentpool_ckeditor')
    cv_references = RichTextField(blank=True, config_name='talentpool_ckeditor')
    
    def __unicode__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse("show_talent", args=[self.full_name_slug])
    
    class Meta:
        verbose_name = _("talent people")
        verbose_name_plural = verbose_name
        ordering = ["first_name", "last_name"]
        app_label = string_with_title('cms_talentpool', _("talent pool"))
        
class NetworkConnection(models.Model):
    subject = models.ForeignKey(TalentPeople, related_name='connections')
    people = models.ForeignKey(TalentPeople, related_name='+')
