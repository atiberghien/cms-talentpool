from .models import TalentPeople, SkillCategory
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from haystack.forms import ModelSearchForm

def show_talent_pool(request):
    categories = SkillCategory.objects.all()
    selected_skills = []
    people = TalentPeople.objects.all()
    
    template_name = "talentpool/main.html"
    if request.is_ajax():
        template_name = "talentpool/talent-main-mosaic.html"
    
    if request.method == "POST" and request.POST.getlist("skills"):
        selected_skills = [int(x) for x in request.POST.getlist("skills")]
        people = people.filter(skills__in=selected_skills)
        
    elif request.GET.get('q'):
        form = ModelSearchForm(request.GET, searchqueryset=None, load_all=True)
        searchqueryset = form.search()
        results = [ r.object.id for r in searchqueryset if issubclass(type(r.object), TalentPeople)]
        people = TalentPeople.objects.filter(id__in=results)
        selected_skills = []
    
    return render_to_response(template_name,
                              {'people' : people,
                               'categories' : categories,
                               'selected_skills' : selected_skills},
                              context_instance=RequestContext(request))
    
def show_talent(request, talent_slug):
    talent = get_object_or_404(TalentPeople, full_name_slug=talent_slug)
    connections = [TalentPeople.objects.get(id=id) for id in talent.connections.values_list('people', flat=True)]
    
    return render_to_response("talentpool/talentpeople.html",
                              {'talent' : talent,
                               'connections' : connections},
                              context_instance=RequestContext(request))
