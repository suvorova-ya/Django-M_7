from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import Product, Category  # Дополнительно импортируем категорию, чтобы пользователь мог её выбрать
from .filters import ProductFilter
from .forms import ProductForm
from django.views import View
from django.core.mail import send_mail, EmailMultiAlternatives, mail_managers, mail_admins
from datetime import datetime
from .models import Appointment

class Products(ListView):
    model = Product
    template_name = 'internet_shop/products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1
    form_class = ProductForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'internet_shop/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            user_name=request.POST['user_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # получаем наш html
        html_content = render_to_string(
            'internet_shop/appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        mail_admins(
            subject=f'{appointment.user_name} {appointment.date.strftime("%d %m %Y")}',
            message=appointment.message,
        )

        return redirect('internet_shop:make_appointment')

