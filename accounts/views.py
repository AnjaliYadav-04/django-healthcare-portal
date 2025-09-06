from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, BlogPostForm
from .models import BlogPost, Category, CustomUser

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")

@login_required
def dashboard_view(request):
    if request.user.user_type == 'doctor':
        return render(request, "doctor_dashboard.html", {"user": request.user})
    else:
        return render(request, "patient_dashboard.html", {"user": request.user})

# Blog Views
@login_required
def create_blog_post(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('my_blogs')
    else:
        form = BlogPostForm()
    
    return render(request, 'create_blog.html', {'form': form})

@login_required
def my_blogs(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')
    
    blogs = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'my_blogs.html', {'blogs': blogs})

@login_required
def blog_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        blogs = BlogPost.objects.filter(category_id=category_id, is_draft=False)
    else:
        blogs = BlogPost.objects.filter(is_draft=False)
    
    blogs = blogs.order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs, 'categories': categories})

@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})