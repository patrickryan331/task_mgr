from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Post, Status


class PostListView(ListView):
    template_name = "issues/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub_status = Status.objects.get(name="In Progress")
        context["post_list"] =  (
            Post.objects
            .filter(status=pub_status)
            .order_by("created_on").reverse()
    )
        return context




class PostDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Post
    fields = [
        "issue", "status", "summary", "description"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Post
    fields = [
        "issue", "status", "summary", "description"
    ]

    def test_func(self):
        post =  self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post =  self.get_object()
        return post.author == self.request.user


class PostUpdateToDraftView(UpdateView):
    template_name = "issues/update_status.html"
    model = Post
    fields = ["status"]