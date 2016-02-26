from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)
	

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,
		null=True,
		blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	POST = 'PO'
	WEDLINY = 'WE'
	GARMAZERIA = 'GA'
	ART_SPOZYWCZE = 'AS'
	NAPOJE = 'NA'
	KATEGORIA_CHOICES = (
		(WEDLINY, 'Wedliny'),
		(GARMAZERIA, 'Garmazeria'),
		(ART_SPOZYWCZE, 'Artykuly spozywcze'),
		(NAPOJE, 'Napoje'),
		(POST, 'Posty'),
	)
	
	kategoria = models.CharField(max_length=2,
									choices=KATEGORIA_CHOICES,
									default=ART_SPOZYWCZE)

# Query ktory ma filtrowac tylko posty z kategorii napoje.
# napoje_query = Post.objects.filter(kategoria=Post.NAPOJE)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]
