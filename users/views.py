from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib import messages
##from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm ,ProfileForm ,SkillForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles ,paginationProfiles


from .models import Profile , Message

# Create your views here.


def profiles(request):
    profiles , search_query=searchProfiles(request)

    custom_range , profiles , paginator =paginationProfiles(request,profiles,1)

    context = {'profiles': profiles ,'search_query':search_query ,'custom_range':custom_range, 'paginator':paginator}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    page='register'

    if request.user.is_authenticated:
        return redirect('profiles')



    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,"user does not exist")  
        
        user= authenticate(request , username=username, password=password)  

        if user is not None:
            login(request , user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request,'username or password is incorect') 
          
  


    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.info(request,"user was succesfully logout") 
    return redirect('login')    


def registerUser(request):
    page='register'
    ##form=UserCreationForm()
    form=CustomUserCreationForm()


    if request.method=='POST':
        ##form=UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request ,'user account was created!')
            login(request, user)
            return redirect('edit-account')
        else:

            messages.error(request , 'an error has occurred')

    context={'page':page , 'form':form}
    return render(request,'users/login_register.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    skills = profile.skill_set.all()
    products=profile.product_set.all()
    ##topSkills = profile.skill_set.exclude(description__exact="")
    ##otherSkills = profile.skill_set.filter(description="")
    
    context={'profile':profile,'skills':skills,'products':products}

    return render(request,'users/account.html',context)    


@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)

    if request.method =="POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile) ##befahmim k kodom profile mikha dupdate she
        if form.is_valid():
            form.save()
            return redirect('account')


    context={'form':form}
    return render(request,'users/profile_form.html',context)

@login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form=SkillForm()

    if request.method=="POST":
        form=SkillForm(request.POST)
        if form.is_valid():
          skill=form.save(commit=False)
          skill.owner=profile
          skill.save()     
          return redirect('account') 



    context={'form':form}
    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def updateSkill(request ,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)

    if request.method=="POST":
        form=SkillForm(request.POST ,instance=skill)
        if form.is_valid():
          skill.save()     
          return redirect('account') 



    context={'form':form}
    return render(request,'users/skill_form.html',context)

def deleteSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)

    if request.method=='POST':
        skill.delete()
        messages.success(request,'Skill was successfully deleted')
        return redirect('account')
    context={'object':skill}
    return render(request , 'delete_template.html',context) 



@login_required(login_url='login')
def inbox(request):
    profile=request.user.profile
    messageRequests=profile.messages.all()
    unreadCount=messageRequests.filter(is_read=False).count()
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount}
    return render(request, 'users/inbox.html' , context)