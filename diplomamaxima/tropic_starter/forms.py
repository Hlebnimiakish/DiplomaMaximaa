from django.forms import ModelForm
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

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]

class LoginForm(ModelForm):
    class Meta:
        model = TSUser
        fields = [
            'email',
            'password',
        ]