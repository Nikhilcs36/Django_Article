from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogComment, Contact
from .forms import ContactForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

#--------function based view------------
# def blog_home(request):
#     all_blogs = Blog.objects.all()
#     context = {
#         'blogs': all_blogs
#     }
#     return render(request, 'blog_home.html', context)

#---------class based view------------
class BlogHome(generic.ListView):
    model=Blog
    template_name = "blog_home.html"
    

# def blog_detail(request, slug_url):
#     blog = Blog.objects.get(slug=slug_url)
#     all_blogs = Blog.objects.all().order_by('post_date')[:5] # for indexing 5 items only
#     context ={
#         'blog':blog,
#         'all_blogs': all_blogs,
#     }
#     return render(request, 'blog_detail.html', context)
    
class BlogDetail(generic.DetailView):
    model=Blog
    template_name = "blog_detail.html"

# def contact_us(request):
    #----- fetching data from html form-----------
    
    # if request.method == "POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     message = request.POST['message']
        
    #     if len(name)<2 or len(email)<5 or len(phone_number)<9 or len(message)<2 :
    #         return redirect('home')
    #     else:
    #         save_data = Contact(name=name,email=email,phone_number=phone_number,message=message)
    #         save_data.save()
    #         return redirect('contact_us')
    
    
    # form = ContactForm()
    # if request.method == "POST":
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "submit successfully")
    #     else:
    #         # form = ContactForm()
    #         messages.error(request, "filll the details properly")
    # return render(request, "contact_us.html", {"form": form})
    
class ContactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "contact_us.html"
    success_url = "/"
    success_message = "your query has been submited successfully, we will contact you soon."
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "please submit the form carefully")
        return redirect('home')

    
