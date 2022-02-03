from django import forms
from .models import resume,Experience, PersonalInfo, Education, PersonalInfo, Experience, Skills, Projects, About, Awards


class PersonalInfoForm(forms.ModelForm):

    class Meta:

        model = PersonalInfo
        fields = ('first_name', 'last_name',
                  'address', 'email', 'github', 'linkedin', 'website',)

        widgets = {
            'first_name': forms.TextInput(attrs={'title': 'First Name'}),
            'last_name': forms.TextInput(attrs={'title': 'Last Name'}),
            'address': forms.Textarea(attrs={'title': 'Address'}),
            'email': forms.EmailInput(attrs={'title': 'Email'}),
            'github': forms.URLInput(attrs={'title': 'Github'}),
            'linkedin': forms.URLInput(attrs={'title': 'LinkedIn'}),
            'website': forms.URLInput(attrs={'title': 'Website'}),
        }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('degree', 'stream', 'passing_year', 'result',)
        widgets = {
            'degree': forms.Select(attrs={'title': 'Degree'}),
            'stream': forms.TextInput(attrs={'title': 'Stream'}),
            'passing_year': forms.DateInput(attrs={'title': 'Passing Date'}),
            'result': forms.TextInput(attrs={'title': 'Result'})
        }


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('title', 'start_date', 'end_date', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'title': 'Title'}),
            'start_date': forms.DateInput(attrs={'title': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'title': 'End Date'}),
            'description': forms.Textarea(attrs={'title': 'Description'})
        }


class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('skill_detail',)
        widgets = {

            'skill_detail': forms.Textarea(attrs={'title': 'Skill_detail'})
        }


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('project_detail',)
        widgets = {

            'project_detail': forms.Textarea(attrs={'title': 'Project_detail'})
        }


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('about_detail',)
        widgets = {

            'about_detail': forms.Textarea(attrs={'title': 'About_detail'})
        }

class AwardsForm(forms.ModelForm):

    class Meta:
        model = Awards
        fields = ('award_detail',)
        widgets = {

            'award_detail': forms.Textarea(attrs={'title': 'Award_detail'})
        }

class resumeForm(forms.ModelForm):

    class Meta:
        model = resume
        fields = ('first_name', 'last_name',
                  'address', 'email', 'github', 'linkedin', 'website',)
        