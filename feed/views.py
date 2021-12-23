from django.views.generic import ListView
from django.views.generic.edit import FormView

from feed.forms import PostForm
from feed.models import Post


class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]


class AddPost(FormView):
    template_name = "feed/post.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        print('Form valid')
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        post = Post(text=text, title=title)
        Post.save(post)
        return super().form_valid(form)