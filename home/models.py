from django.db import models
from django.core.validators import FileExtensionValidator

class HomePage(models.Model):
    slug = models.SlugField(unique=True, default="home", verbose_name="Связка")
    home_title = models.CharField(max_length=155, verbose_name="Название главной страницы")
    banner = models.CharField(max_length=155, verbose_name=" Банер")
    about_movent = models.CharField(max_length=166, verbose_name=" О движении")
    events = models.CharField(max_length=155, verbose_name="Мероприятия")
    news = models.CharField(max_length=155, verbose_name="Новости")
    brend_material = models.CharField(max_length=155, verbose_name="Бренд материал")

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return self.home_title

class Banner(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="Banner")
    title = models.CharField(max_length=100, verbose_name='Название баннера', null=False, blank=True)
    description = models.CharField(max_length=255, verbose_name='Текстовое описание')
    cta_text = models.CharField(max_length=255, verbose_name='Текст кнопки (СТА)', default='Вступить в движение')
    cta_link = models.URLField(verbose_name='Ссылка на Google Forms')
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
    
    def __str__(self):
        return self.title

class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='image')
    image = models.FileField(
        upload_to='banners/',
        verbose_name="Изображение ",
        
    )

    class Meta:
        verbose_name = "Изображение баннера"
        verbose_name_plural = "Изображения баннеров"

    def __str__(self):
        return f"{self.banner.description} - изображение"

class AboutMovement(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="about_movement")
    description = models.CharField(max_length=155, verbose_name='Описание')

    class Meta:
        verbose_name = 'О движении'
        verbose_name_plural = 'О движении'
    
    def __str__(self):
        return self.description

class Advantage(models.Model):
    about_movement = models.ForeignKey(AboutMovement, on_delete=models.CASCADE, related_name="about_movement")
    title = models.CharField(max_length=155, verbose_name="Название")
    text = models.TextField(max_length=400, verbose_name='Описание')

    class Meta:
        verbose_name = 'Карточки о движении'
        verbose_name_plural = 'Карточки о движении'
    
    def __str__(self):
        return self.title

class EventsModel(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="events_items")
    image = models.ImageField(upload_to="events/", verbose_name="Изображение")
    data = models.DateField()
    title = models.CharField(max_length=155, verbose_name="Название")
    short_text = models.TextField(max_length=255, verbose_name="Короткий текст")

    class Meta:
        verbose_name = 'Карточка мероприятия'
        verbose_name_plural = 'Карточки мероприятий'

    def __str__(self):
        return self.title
    
class NewsModel(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="news_items")
    news_image = models.ImageField(upload_to="news/", verbose_name="Изображения новостей")
    data = models.DateField()
    description = models.TextField(max_length=255, verbose_name="Описание")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"Новость от {self.data}"

class BrendMaterialModel(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="brend_items")
    image = models.ImageField(upload_to="brend_material/", verbose_name="Изображение")
    title = models.CharField(max_length=155, verbose_name="Название")
    price = models.IntegerField()
     
    class Meta:
        verbose_name = 'Бренд материал'
        verbose_name_plural = 'Бренд материалы'