# codings: utf-8
from django.shortcuts import render


# Create your views here.
def hello(request):

    return render(request, 'need-login.html')


def login(request):

    return render(request, 'login.html')


def login_form(request):

    return render(request, 'login-form.html')


def fault(request):

    return render(request, '404.html')


def about_us(request):

    return render(request, 'about-us.html')


def about_us2(request):

    return render(request, 'about-us-2.html')


def blog(request):

    return render(request, 'blog.html')


def blog_with_sidebar(request):

    return render(request, 'blog-with-sidebar.html')


def checkout(request):

    return render(request, 'checkout.html')


def contact(request):

    return render(request, 'contact.html')


def courses(request):

    return render(request, 'courses.html')


def event(request):

    return render(request, 'event.html')


def index(request):

    return render(request, 'index.html')


def index2(request):

    return render(request, 'index-2.html')


def index3(request):
    return render(request, 'index-3.html')


def index4(request):
    return render(request, 'index-4.html')


def instructor(request):

    return render(request, 'instructor.html')


def next_register(request):

    return render(request, 'next-register.html')


def register(request):

    return render(request, 'register.html')


def register2(request):

    return render(request, 'register2.html')


def register3(request):

    return render(request, 'register3.html')


def register_results(request):

    return render(request, 'register-results.html')


def register_results2(request):

    return render(request, 'register-results2.html')


def next_register(request):

    return render(request, 'next-register.html')


def need_login(request):

    return render(request, 'need-login.html')


def shop(request):

    return render(request, 'shop.html')


def shop_with_sidebar(request):

    return  render(request, 'shop-with-sidebar.html')


def single_blog(request):

    return render(request, 'single-blog.html')


def single_courses(request):

    return render(request, 'single-courses.html')


def single_event(request):

    return render(request, 'single-event.html')


def single_shop(request):

    return render(request, 'single-shop.html')


def update_personalinfo(request):

    return render(request, 'update-personalinfo.html')


def view_cart(request):

    return render(request, 'view-cart.html')