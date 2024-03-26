
from .models import Skill , Profile
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage


def paginationProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator=Paginator(profiles,results)
    try:
        profiles=paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles=paginator.page(page) 
    except EmptyPage:
        page=paginator.num_pages 
        profiles=paginator.page(page)   


    leftIndex=(int(page)-1)

    if leftIndex <1:
        leftIndex=1 

    rightIndex=(int(page)+1)

    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages

    custom_range=range(leftIndex,rightIndex)
    



    return custom_range , profiles ,paginator



def searchProfiles(request):

    search_query= ''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    skills=Skill.objects.filter(name__iexact=search_query)
    ##profiles=Profile.objects.filter(name__icontains=search_query) ###agr serach query khali bashad kole object hara bar migardanad va mishavad mesele khat paiini   
    ##profiles=Profile.objects.filter(name__icontains=search_query , short_intro__icontains=search_query) ##dar inja miad va and mikone engar va msln agr chizio serach mikoni msln charecter 'n' ro byd ham too short_intro bashe ham toie title ta on profileo namayesh bede
    profiles=Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills))
    ##profiles = Profile.objects.all()

    return profiles , search_query