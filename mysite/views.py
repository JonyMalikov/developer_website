from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import Author, Category, Service, Testimony, Work


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
    author = Author.objects.get()
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


# @require_http_methods(["GET", "POST"])
# def contact(request):
#     """Страница с формой обратной связи"""
#     if request.method == "POST":
#         if all(
#             param in request.POST
#             for param in ["name", "email", "subject", "message"]
#         ):
#             msg = Message(
#                 name=request.POST["name"],
#                 email=request.POST["email"],
#                 subject=request.POST["subject"],
#                 message=request.POST["message"],
#             )
#             msg.save()
#             messages.success(request, "Сообщение отправлено!")
#             return redirect("contact")
#         else:
#             messages.error(
#                 request, "Не все необходимые параметры были отправлены"
#             )
#             return redirect("contact")
#     else:
#         return render(request, "contact.html")


@require_http_methods(["GET", "POST"])
def contact(request):
    """Страница с формой обратной связи"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Сообщение отправлено!")
            return redirect("contact")
        else:
            messages.error(
                request, "Не все необходимые параметры были отправлены"
            )
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
