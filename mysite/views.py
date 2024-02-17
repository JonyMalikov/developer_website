from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import Author, Category, Message, Service, Testimony, Work


def index(request):
    """Главная страница"""
    context = {
        "categories": Category.objects.all(),
        "works": Work.objects.all(),
        "services": Service.objects.all(),
        "testimonies": Testimony.objects.all(),
    }

    return render(request, "index.html", context)


def about(request):
    """Страница с информацией об авторе"""
    author = Author.objects.first()
    return render(request, "about.html", {"author": author})


def work_detail(request, slug):
    """Страница с детальной информацией о работе"""
    work = Work.objects.get(slug=slug)
    testimonies = Testimony.objects.all()
    context = {
        "work": work,
        "testimonies": testimonies,
    }
    return render(request, "work_detail.html", context)


@require_POST
def contact(request):
    """Страница с формой обратной связи"""
    msg = Message(
        name=request.POST["name"],
        email=request.POST["email"],
        subject=request.POST["subject"],
        message=request.POST["message"],
    )
    msg.save()
    messages.success(request, "Сообщение отправлено!")
    return redirect("contact")
