from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}, {self.code}"
    class Meta:
        verbose_name_plural = "Countries"
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    def __str__(self):
        return self.full_address()
    class Meta:
        verbose_name_plural = "Address Entries"
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[
        MinValueValidator(1), MaxValueValidator(5)
        ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)
                            #editable=False)
    published_countries = models.ManyToManyField(Country, blank=True)


    def get_absolute_url(self):
        return reverse("book-detail-page", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super.save(*args, **kwargs)
        # original_slug = slugify(self.title)
        # queryset = Book.objects.filter(slug=original_slug)
        # count = queryset.count()
        # if count > 0:
        #     self.slug = f"{original_slug}-{count + 1}"
        # else:
        #     self.slug = original_slug
        # super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"



