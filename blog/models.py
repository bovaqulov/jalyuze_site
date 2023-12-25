from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Maxsulot")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan vaqti')
    prise = models.FloatField(verbose_name="Narxi")
    colour = models.CharField(max_length=150, verbose_name='Rangi')

    def __str__(self):
        return self.title

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].image.url
            except:
                return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

class Productimages(models.Model):
    image = models.ImageField(upload_to='"/img/image/"', verbose_name='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"








