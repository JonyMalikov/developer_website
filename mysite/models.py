from django.db import models


class Skill(models.Model):
    """список навыков"""

    name = models.CharField(max_length=30, verbose_name="Название навыка")
    level = models.CharField(max_length=3, verbose_name="Уровень навыка")

    class Meta:
        ordering = ["id"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Category(models.Model):
    """список категорий"""

    engname = models.CharField(
        max_length=25, verbose_name="Название категории"
    )
    rusname = models.CharField(
        max_length=25, verbose_name="Название категории"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.rusname


class Work(models.Model):
    """список работ"""

    title = models.CharField(max_length=150, verbose_name="Название работы")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="URL")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="works",
        verbose_name="Категория",
    )
    image = models.ImageField(upload_to="works", verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    stack = models.TextField(verbose_name="Технологии")
    link = models.URLField(
        max_length=200, blank=True, verbose_name="Ссылка на работы"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.title


class Service(models.Model):
    """список видов сервиса"""

    name = models.CharField(max_length=25, verbose_name="Название сервиса")
    icon = models.CharField(max_length=50, verbose_name="Иконка")
    description = models.CharField(max_length=200, verbose_name="Описание")

    class Meta:
        ordering = ["id"]
        verbose_name = "Сервис"
        verbose_name_plural = "Виды сервиса"

    def __str__(self):
        return self.name


class Item(models.Model):
    """список инструментов"""

    name = models.CharField(max_length=150, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"

    def __str__(self):
        return self.name


class Author(models.Model):
    """список авторов"""

    name = models.CharField(max_length=15, verbose_name="Имя")
    lastname = models.CharField(max_length=15, verbose_name="Фамилия")
    about = models.TextField(verbose_name="О себе")
    skills = models.ManyToManyField(
        Skill, related_name="author", verbose_name="Навыки"
    )
    image = models.ImageField(upload_to="author", verbose_name="Изображение")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Message(models.Model):
    """список сообщений"""

    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    subject = models.CharField(max_length=100, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Создано"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от {self.name}: {self.subject}"


class Testimony(models.Model):
    """список отзывов"""

    name = models.CharField(max_length=15, verbose_name="Имя")
    lastname = models.CharField(max_length=15, verbose_name="Фамилия")
    image = models.ImageField(upload_to="clients", verbose_name="Изображение")
    text = models.TextField(verbose_name="Текст отзыва")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return f"{self.name} {self.lastname}"
