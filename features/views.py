from operator import contains
from django import shortcuts
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render


#homepage views
def home(request):
    
    project = Project.objects.all()
    if project:
        paginator = Paginator(project, 3)
        page = request.GET.get('page')
        project = paginator.get_page(page)

    testimonial = Testimonial.objects.all()

    team=Team.objects.all()
    if team:
        paginator = Paginator(team, 4)
        page = request.GET.get('page')
        team = paginator.get_page(page)
    
    blog=Blog.objects.all()
    if blog:
        paginator = Paginator(blog, 3)
        page = request.GET.get('page')
        blog = paginator.get_page(page)
    return render(request,'home.html', {'project': project, 'testimonial':testimonial, 'team':team,'blog':blog})


#About page views
def about(request):
    team = Team.objects.all()
    if team:
        paginator = Paginator(team, 4)
        page = request.GET.get('page')
        team = paginator.get_page(page)

        
    testimonial = Testimonial.objects.all()
    if testimonial:
        paginator = Paginator(testimonial, 2)
        page = request.GET.get('page')
        testimonial = paginator.get_page(page)

    partner = BusinessPartner.objects.all()

    
    message = Message.objects.all().order_by('-created')
    count=message.count()
    if(count == 1):  
        message1 = message[0]
        print('count1')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner, 'message1':message1})
       
    elif(count >= 2):
        message1 = message[0]
        message2 = message[1]
        print('count2')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner, 'message1':message1, 'message2':message2})
    else:
        print('count3')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner})
        
    


def blogs (request):
    blog=Blog.objects.all()
    return render(request,'blogs.html',{'blog':blog})


def blog_single (request, id):
    blog=Blog.objects.get(id= id)
    comment=Comment.objects.filter(blog_id=id)
    return render(request,'blog_single.html',{'blog':blog, 'comment':comment})


def comment(request,id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        comment = request.POST['comment']
        
        Comment.objects.create(full_name=full_name, email=email,comment=comment,blog=Blog.objects.get(id=id))
        
        return redirect ('blog_single',id)
    return redirect('blog_single')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(full_name=full_name, email=email, message=message,contact=contact)
        return redirect ('home')
    return render (request,'contact.html')


def events (request):
    event= Event.objects.all()
    return render(request, 'events.html', {'event':event})


def event_single (request, id):
    event=Event.objects.get(event_id= id)
    return render(request,'event_single.html',{'event':event})


def projects (request):
    completed = Project.objects.filter(status = "completed")
    ongoing = Project.objects.filter(status = "ongoing")
    upcoming = Project.objects.filter(status = "upcoming")
    return render(request, 'projects.html', {'completed': completed,'ongoing': ongoing,'upcoming': upcoming})


def project_single (request, id):
    project=Project.objects.get(project_id= id)
    return render(request,'project_single.html',{'project':project})


def error(request,exception):
    return render (request, '404.html')
