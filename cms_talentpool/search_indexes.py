from django.conf import settings
from .models import TalentPeople


if 'haystack' in settings.INSTALLED_APPS:
    import haystack
    from haystack import site
    from haystack.fields import CharField
    from haystack.indexes import SearchIndex
    
    class TalentPeopleIndex(SearchIndex):
        text = CharField(document=True, use_template=True)
    
        def index_queryset(self):
            return TalentPeople.objects.all()
    
    site.register(TalentPeople, TalentPeopleIndex)