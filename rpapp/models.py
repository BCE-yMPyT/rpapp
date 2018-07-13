from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # author of post, will be not display
    title = models.CharField(max_length=200)
    # title, will be displayed
    text = models.TextField()
    # description, will be displayed only in details
    created_date = models.DateTimeField(
            default=timezone.now)
    # CD, will be displayed only in admin panel
    published_date = models.DateTimeField(
            blank=True, null=True)
    # PD will be displayed only in details
    picture = models.ImageField(upload_to='staticfiels/', blank=True, null=True)
    # picture be displayed
    help_picture_text = "Please use PNG format, and file-size not more 2mb."
    # h_p_t will be displayed only in admin panel
    contract = models.FileField(upload_to='staticfiels/', blank=True, null=True)
    help_contract_text = "Please use PDF format, and file-size not more 2mb."
    # h_c_t will be displayed only in admin panel
    # rent block ----------------------------------------------------
    FREE = 'fr'
    LEASED = 'ld'
    FREE_LEASE_CHOICES = (
        (None, 'unknown'),
        (FREE, 'free'),
        (LEASED, 'leased'),
    )
    rental_condition = models.CharField(max_length=2,
                                        choices=FREE_LEASE_CHOICES,
                                        default=FREE)
    # r_c will be displayed------------------------------------------


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title