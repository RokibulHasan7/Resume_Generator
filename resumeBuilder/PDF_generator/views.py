from venv import create
from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4


from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.contrib.auth import get_user_model
from .models import PersonalInfo, Education, Experience, Skills, About, Awards, Projects, resume
from .forms import PersonalInfoForm, EducationForm, ExperienceForm, SkillsForm, AwardsForm, AboutForm, ProjectsForm
User = get_user_model()
"""
def resumeFill(request):
    if request.method == 'POST':
        personalInfoform = PersonalInfoForm(request.POST)
        aboutform = AboutForm(request.POST)
        educationform = EducationForm(request.POST)
        experienceform = ExperienceForm(request.POST)
        skillsform = SkillsForm(request.POST)
        projectsform = ProjectsForm(request.POST)
        awardsform = AwardsForm(request.POST)

        if personalInfoform.is_valid():
            personalInfoform.save()

        if aboutform.is_valid():
            aboutform.save()

        if educationform.is_valid():
            educationform.save()

        if experienceform.is_valid():
            experienceform.save()

        if skillsform.is_valid():
            skillsform.save()

        if projectsform.is_valid():
            projectsform.save()

        if awardsform.is_valid():
            awardsform.save()

    return render(request, 'input_file.html', {

        'personform': PersonalInfoForm(),
        'educationform': EducationForm(),
        'experienceform': ExperienceForm(),
        'Skillsform': SkillsForm(),
        'aboutform': AboutForm(),
        'awardsform': AwardsForm(),
        'projectsform': ProjectsForm(),
    })


def resumeView(request):
    #site_name = RequestSite(request).domain
    person = PersonalInfo.objects.all()[:1]
    education = Education.objects.all()
    experience = Experience.objects.all()[:5]
    skills = Skills.objects.all()[:5]
    about = About.objects.all()[:5]
    awards = Awards.objects.all()
    projects = Projects.objects.all()

    context = {
        #'site_name': site_name,
        'person': person,
        'education': education,
        'experience': experience,
        'skills': skills,
        'about': about,
        'awards': awards,
        'projects': projects,
    }
    if request.method == 'GET':
        return render(request,'output.html', context)  # , context_instance=RequestContext(request))
    
    return render(request, 'output.html')

"""
def resumeFill(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        github = request.POST['github']
        linkedin = request.POST['linkedin']
        website = request.POST['website']
        mobile = request.POST['mobile']
        
        degree = request.POST['degree']
        varsity_name = request.POST['varsity_name']
        passing_year = request.POST['passing_year']
        result = request.POST['result']

        title = request.POST['title']
        place = request.POST['place']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        description = request.POST['description']

        skill_detail = request.POST['skill_detail']
        project_detail = request.POST['project_detail']
        about_detail = request.POST['about_detail']
        award_detail = request.POST['award_detail']

        my_resume = resume.objects.create(first_name = first_name, last_name = last_name,
                        address = address, email = email, github = github, linkedin = linkedin,
                        website = website, mobile = mobile, degree = degree, varsity_name = varsity_name,
                        passing_year = passing_year, result = result, title = title, place = place, 
                        start_date = start_date, end_date = end_date, description = description,
                        skill_detail = skill_detail, project_detail = project_detail,
                        about_detail = about_detail, award_detail = award_detail)
        
        
    
        my_resume.save()
        return redirect('home')
    return render(request, 'input_file.html')


def resumeView(request):
    last_entry = resume.objects.all().last()
    first_name = last_entry.first_name
    last_name = last_entry.last_name
    address = last_entry.address
    email = last_entry.email
    github = last_entry.github
    linkedin = last_entry.linkedin
    website = last_entry.website
    mobile = last_entry.mobile
        
    degree = last_entry.degree
    varsity_name = last_entry.varsity_name
    passing_year = last_entry.passing_year
    result = last_entry.result

    title = last_entry.title
    place = last_entry.place
    start_date = last_entry.start_date
    end_date = last_entry.end_date
    description = last_entry.description

    skill_detail = last_entry.skill_detail
    project_detail = last_entry.project_detail
    about_detail = last_entry.about_detail
    award_detail = last_entry.award_detail

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'email': email,
        'github': github,
        'linkedin': linkedin,
        'website': website,
        'mobile': mobile,

        'degree': degree,
        'varsity_name': varsity_name,
        'passing_year': passing_year,
        'result': result,

        'title': title,
        'place': place,
        'start_date': start_date,
        'end_date': end_date,
        'description': description,

        'skill_detail': skill_detail,
        'project_detail': project_detail,
        'about_detail': about_detail,
        'award_detail': award_detail,
    }
    if request.method == 'GET':
        return render(request,'resume2.html', context)  # , context_instance=RequestContext(request))
    
    return render(request, 'resume2.html')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('resume2.html')
        last_entry = resume.objects.all().last()
        first_name = last_entry.first_name
        last_name = last_entry.last_name
        address = last_entry.address
        email = last_entry.email
        github = last_entry.github
        linkedin = last_entry.linkedin
        website = last_entry.website
        mobile = last_entry.mobile
        
        degree = last_entry.degree
        varsity_name = last_entry.varsity_name
        passing_year = last_entry.passing_year
        result = last_entry.result

        title = last_entry.title
        place = last_entry.place
        start_date = last_entry.start_date
        end_date = last_entry.end_date
        description = last_entry.description

        skill_detail = last_entry.skill_detail
        project_detail = last_entry.project_detail
        about_detail = last_entry.about_detail
        award_detail = last_entry.award_detail

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'email': email,
            'github': github,
            'linkedin': linkedin,
            'website': website,
            'mobile': mobile,

            'degree': degree,
            'varsity_name': varsity_name,
            'passing_year': passing_year,
            'result': result,

            'title': title,
            'place': place,
            'start_date': start_date,
            'end_date': end_date,
            'description': description,

            'skill_detail': skill_detail,
            'project_detail': project_detail,
            'about_detail': about_detail,
            'award_detail': award_detail,
        }
        html = template.render(context)
        pdf = render_to_pdf('resume2.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='/pdf')
            filename = "Resume_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
