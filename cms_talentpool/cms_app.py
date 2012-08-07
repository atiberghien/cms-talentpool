from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class TalentPoolApp(CMSApp):
    name = _("talent pool")
    urls = ["cms_talentpool.urls"]
    
apphook_pool.register(TalentPoolApp)