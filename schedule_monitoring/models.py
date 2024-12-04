from django.db import models

# Create your models here.
class Source(models.Model):
    filename = models.CharField(
        unique = False,
        blank = True,
        null = True,
        max_length = 500,
        verbose_name="Имя файла"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name = "Дата сохранения?",
    )

    last_changed = models.DateTimeField(
        auto_now_add = False,
        verbose_name = "Дата изменений",
    )

    url = models.TextField(
        verbose_name = "URL"
    )

    hashsum = models.CharField(
        unique = False,
        blank = False,
        null = False,
        max_length= 500,
        verbose_name="Хеш сумма",
    )

    mimetype = models.CharField(
        max_length= 45,
        verbose_name="mimetype??????"
    )

    unique_key = models.CharField(
        unique = True,
        blank=True,
        null=True,
        max_length=500,
        verbose_name="???"
    )

    is_latest_version = models.BooleanField(

        verbose_name="Последняя версия или нет",
    )

    def __str__(self):
        return self.filename
    
    
class Storage(models.Model):
    name = models.CharField(
        unique=False,
        blank=True,
        null=True,
        max_length=500,
        verbose_name="Название",
    )

    last_changed = models.CharField(
        unique = False,
        blank=True,
        null=True,
        max_length = 500,
        verbose_name="Последнее изменение",
        )

    storage_type = models.CharField(
        unique  = False,
        blank = False,
        null = False,
        max_length = 500,
        verbose_name="Тип хранения ??????????",
    )

    header_path = models.CharField(
        unique  = False,
        blank = True,
        null = True,
        max_length = 500,
        verbose_name="Путь заголовков на странице",
    )

    path = models.CharField(
        unique=False,
        blank = True,
        null = True,
        max_length = 500,
        verbose_name="Путь до файла"
    )
    
    download_url = models.CharField(
        unique=False,
        blank = True,
        null = True,
        max_length = 500,
        verbose_name="Ссылка на скачивание"
    )

    resource_url = models.CharField(
        unique = False,
        blank = True,
        null = True,
        max_length = 500,
        verbose_name="Ссылка верхнего уровня ?????????"
    )

    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


