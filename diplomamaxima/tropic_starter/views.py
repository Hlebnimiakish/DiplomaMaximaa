from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from tropic_starter.forms import RegisterForm, AddPostForm, LoginForm, AddCommentForm
from tropic_starter.models import Post, Comment, TSUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages


class HomepageView(View):
    def get(self, request):
        posts = Post.objects.order_by('-datetime')
        postspage = Paginator(posts, 10)
        pgnum = request.GET.get('pgnum')
        if pgnum is None:
            postspage = postspage.get_page(1)
            return render(request, 'homepage.html', {'postspage': postspage})
        else:
            postspage = postspage.get_page(pgnum)
            return render(request, 'homepage.html', {'postspage': postspage})


class LoginView(View):
    def get(self, request):
        if request.user.id is None:
            loginform = LoginForm()
            return render(request, 'login.html', {'form': loginform})
        else:
            messages.error(request, "Already logged in!")
            return redirect('homepage')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = TSUser.objects.get(email=email, password=password)
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect(request.GET.get('next') or f'/userpage/{user.id}')
        except ObjectDoesNotExist:
            messages.error(request, 'No such user. Please check the data given')
            return redirect('loginpage')



class RegistrationView(View):
    def get(self, request):
        regform = RegisterForm()
        return render(request, 'registration.html', {'form': regform})

    def post(self, request):
        try:
            TSUser.objects.get(email=request.POST['email'])
            messages.error(request, 'Error: This email is already registred')
            return redirect('registrationpage')
        except ObjectDoesNotExist:
            regform = RegisterForm(request.POST)
            if regform.is_valid():
                regform.save()
                user = TSUser.objects.get(email=request.POST['email'], password=request.POST['password'])
                login(request, user)
                messages.success(request, "U've been registred successfully")
                return redirect('homepage')
            else:
                messages.error(request, 'Registration form data is invalid. Please check the data.')
                return redirect('registrationpage')



class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "U've been logged out")
            return redirect('homepage')
        else:
            messages.error(request, "Something went wrong")
            return redirect('loginpage')


class AddPostView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        postform = AddPostForm()
        return render(request, 'addpost.html', {'form': postform})
    def post(self, request):
        postform = AddPostForm(request.POST)
        if postform.is_valid():
            postcr = Post.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                author=TSUser.objects.get(id=request.user.id)
                )
            messages.success(request, "Post have been added")
            return redirect(f'/post/{postcr.id}')
        else:
            messages.error(request, "Something went wrong")
            return redirect('addpostpage')


class ThePostPage_WithCommView(View):
    def get(self, request, id):
        thepost = Post.objects.get(id=id)
        postcomments = Comment.objects.filter(post_id=id).order_by('-id')
        if request.user.is_authenticated:
            commentform = AddCommentForm()
        else:
            commentform = None
        return render(request, 'thepost.html', {'thepost': thepost, 'postcomments': postcomments, 'commentform': commentform})
    def post(self, request, id):
        if request.user.is_authenticated:
            commentform = AddCommentForm(request.POST)
            if commentform.is_valid():
                Comment.objects.create(
                    post=Post.objects.get(id=id),
                    author=TSUser.objects.get(id=request.user.id),
                    content=request.POST['content']
                )
                return redirect(f'/post/{id}')
            else:
                messages.error(request, "Something went wrong")
                return redirect(f'/post/{id}')
        else:
            messages.error(request, "U have to be logged in!")
            return redirect('loginpage')


# class AddCommentView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     def get(self, request):
#         commentform = AddCommentForm()
#         return render(request, 'thepost.html', {'commentform': commentform})
#     def post(self, request):
#         commentform = AddCommentForm(request.POST)
#         if commentform.is_valid():
#             Comment.objects.create(
#                 post = Post.objects.get(id=request.POST[Post.pk]),
#                 author = TSUser.objects.get(id=request.user.id),
#                 content = request.POST['content']
#             )
#             return redirect(f'/post/{request.POST[Post.pk]}')
#         else:
#             messages.error(request, "Something went wrong")
#             return redirect(f'/post/{request.POST[Post.pk]}')



class UserPageView(View):
    def get(self, request, id):
        user = TSUser.objects.get(id=id)
        userposts = Post.objects.filter(author_id=id).order_by('-datetime')
        userpostspag = Paginator(userposts, 10)
        pgnum = request.GET.get('pgnum')
        if pgnum is None:
            userpostspage = userpostspag.get_page(1)
            return render(request, 'userpageposts.html', {'userpostspage': userpostspage, 'user': user})
        else:
            userpostspage = userpostspag.get_page(pgnum)
            return render(request, 'userpageposts.html', {'userpostspage': userpostspage, 'user': user})



