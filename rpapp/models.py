from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    address = models.CharField(max_length=200, default='unknown')

    text = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    picture = models.ImageField(upload_to="images/", blank=True, null=True)

    # rent block ----------------------------------------------------
    FREE = 'free'
    LEASED = 'leased'
    FREE_LEASE_CHOICES = (
        (None, 'unknown'),
        (FREE, 'free'),
        (LEASED, 'leased'),
    )
    rental_condition = models.CharField(max_length=6,
                                        choices=FREE_LEASE_CHOICES,
                                        default=FREE)
    # r_c will be displayed------------------------------------------

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + str(self.id)

class Arendator(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, default='unknown')
    email = models.CharField(max_length=200, default='unknown')
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Contract(models.Model):
    rent_time_day = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=timezone.now)

    rent_finish_date = models.DateTimeField(blank=True, null=True)

    price_dollar = models.IntegerField(default=0)

    payment_by_contract_dollar = models.IntegerField(default=0)

    arendator = models.ForeignKey(Arendator, on_delete=models.CASCADE)

    rent_obj = models.ForeignKey(Post, on_delete=models.CASCADE)

    contract_file = models.FileField(upload_to='contracts/', blank=True, null=True)

    FREE = 'free'
    LEASED = 'leased'
    FREE_LEASE_CHOICES = (
        (None, 'unknown'),
        (FREE, 'free'),
        (LEASED, 'leased'),
    )
    rental_condition = models.CharField(max_length=6,
                                        choices=FREE_LEASE_CHOICES,
                                        default=FREE)

    def __str__(self):
        return str(self.arendator)+ '_' + str(self.rent_obj)