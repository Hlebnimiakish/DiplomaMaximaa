from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea
from tropic_starter.models import Post, Comment, TSUser


class RegisterForm(ModelForm):
    class Meta:
        model = TSUser
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]
        widgets = {
            'username': TextInput(attrs={'class': 'txtinlil', 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': 'txtinlil', 'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'class': 'txtinlil', 'placeholder': 'Password'}),
            'first_name': TextInput(attrs={'class': 'txtinlil', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'txtinlil', 'placeholder': 'Last Name'})
        }

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'txtinlil', 'placeholder': 'Title'}),
            'content': Textarea(attrs={'placeholder': 'Post content'})
        }

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': Textarea(attrs={'placeholder': 'Type your comment here'}),
        }

class LoginForm(ModelForm):
    class Meta:
        model = TSUser
        fields = [
            'email',
            'password',
        ]
        widgets = {
            'email': EmailInput(attrs={'class': 'txtinlil', 'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'class': 'txtinlil', 'placeholder': 'Password'})
        }