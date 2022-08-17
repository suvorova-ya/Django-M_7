from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.template.loader import render_to_string
from .filters import PostFilter
from .forms import PostForm
from .utils import *
from .tasks import *
from django.http import HttpResponse

class news(ListView):
    model = Post
    template_name = 'news_portal/news.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 3
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['title'] = 'Главная страница'
        context['postCategory'] = 0
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый пост
            form.save()

        return super().get(request, *args, **kwargs)

class NewsDetail(DetailView):
    model = Post
    template_name = 'news_portal/details_view.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data



def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('details_view', args=[str(pk)]))

class PostCreateView(PermissionRequiredMixin,CreateView):
    model = Post
    template_name = 'news_portal/news_create.html'
    form_class = PostForm
    permission_required = 'news_portal.add_post'

    def form_valid(self, form):
        form.save()

        notify_post_create.apply_async([self.request.user.id, form.instance.title, form.instance.text], countdown=10, expires=30)
        return super(PostCreateView,self).form_valid(form)



class PostUpdateView(PermissionRequiredMixin,UpdateView):
    model = Post
    template_name = 'news_portal/news_create.html'
    form_class = PostForm
    permission_required = 'news_portal.change_post'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



# дженерик для удаления статьи
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news_portal/news_delete.html'
    success_url = '/news/'


def about(request):
    return render(request,'news_portal/about.html')




class Subscribers(ListView):
    model = Category
    template_name = 'news_portal/list_category.html'
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'category'
    ordering = 'name'
    queryset = Category.objects.order_by('name')
    # print(queryset)


    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['category'] = Category.objects.all()
        user_cat = list()
        for u in Category.objects.all():
            print(u)
            if (u.subscribers.filter(id=user.id).exists()):
                user_cat.append(u.name)
        context['user_category'] = user_cat
        return context


@login_required
def subscribe_user(request):
    user = request.user
    category = Category.objects.get(id=request.POST['id_cat'])
    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)
    else:
        category.subscribers.add(user)

    print(f'{user} подписан на категорию {category}')

    return redirect('subscribers')



