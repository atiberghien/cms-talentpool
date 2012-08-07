from django.contrib import admin
from .models import Company, SkillCategory, TalentPeople, NetworkConnection

class CompanyAdmin(admin.ModelAdmin):
    pass


class SkillCategoryAdmin(admin.ModelAdmin):
    pass


class NetworkConnectionInline(admin.TabularInline):
    model = NetworkConnection
    fk_name = "subject"
    max_num = 3


class TalentPeopleAdmin(admin.ModelAdmin):
    inlines = [
        NetworkConnectionInline,
    ]
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name', 'original_photo'),
                       ('quote', 'description'),
                       ('company', 'post'),
                       'skills',)
        }),
        ('CV', {
            'classes': ('wide',),
            'fields': (('cv_domain', 'cv_experiences'),
                       ('cv_studies', 'cv_references'))
        }),
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(TalentPeople, TalentPeopleAdmin)