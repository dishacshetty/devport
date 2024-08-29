from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):
    search_query = '' #will be passed into the filter that we send on every request,
                      #but if we have no data we want to make sure its an empty string 
                      #so that it doesnt ruin our filter
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    #have to search the profile and skills together to see if the profile has these skills
    #to check if the profile has the skill 
    skills = Skill.objects.filter(name__icontains = search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                       Q(short_intro__icontains=search_query) |
                                       Q(skill__in=skills)
    )
    return profiles, search_query