from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Category, Message, Service, Testimony, Work


def index(request):
    """Главная страница"""
    categories = Category.objects.all()
    works = Work.objects.all()
    services = Service.objects.all()
    testimonies = Testimony.objects.all()

    context = {
        "categories": categories,
        "works": works,
        "services": services,
        "testimonies": testimonies,
    }

    return render(request, "index.html", context)


def about(request):
    """Страница о нас"""
    author = Author.objects.get()
    return render(request, "about.html", {"author": author})


def work_detail(request, slug):
    """Страница с детальной информацией о работе"""
    work = get_object_or_404(Work, slug=slug)
    testimonies = Testimony.objects.all()
    context = {
        "work": work,
        "testimonies": testimonies,
    }
    return render(request, "work_detail.html", context)


def contact(request):
    """Страница с формой обратной связи"""
    if request.method == "POST":
        msg = Message(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"],
        )
        msg.save()
        messages.success(request, "Сообщение отправлено!")
        return redirect("contact")

    return render(request, "contact.html")
