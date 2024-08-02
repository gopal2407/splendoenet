from django.db import models
from django.core import validators
from multiselectfield import MultiSelectField


# Create your models here.
class Review(models.Model):
    STATUS = [('Published', 'Published'), ('Non Published', 'Non Published')]
    GENRES = [('Horror', 'Horror'), ('Action', 'Action'), ('SciFi', 'SciFi'),
              ('Comedy', 'Comedy'), ('Thriller', 'Thriller')]
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=200)
    director = models.CharField(null=False, max_length=100)
    review_content = models.CharField(null=False, max_length=20)
    rating = models.IntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    created_at = models.DateField(auto_now_add=True)
    reviewer_email_id = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS)
    genres = MultiSelectField(choices=GENRES)
