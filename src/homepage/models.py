# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from fontawesome.fields import IconField
# Create your models here.

class Adventure(models.Model):
    ADVENTUREFORM_CHOICES = (
        ('landbased','Landbased'),
        ('waterbased','Waterbased'),
        ('airbased', 'Airbased'),
    )
    title = models.CharField(max_length = 50)
    logo = models.FileField(upload_to='documents/adventure')
    adventureform_choice = models.CharField(choices= ADVENTUREFORM_CHOICES, max_length= 250, blank= True, null= True)

    def __str__(self):
        return self.title



class Destination(models.Model):
    title = models.CharField(max_length=250)
    num_of_min_days = models.IntegerField()
    num_of_max_days = models.IntegerField()
    associated_adventures = models.ManyToManyField(Adventure, blank= True, related_name='destinationadventure')
    about_destination = models.TextField(blank= True, null= True)
    logo = models.CharField(max_length = 250, blank= True)

    def __str__(self):
        return self.title


class Itenary(models.Model):
    details = HTMLField()
    destination = models.ForeignKey(Destination, null= True, blank = True)

    def __str__(self):
        return self.destination.title


class Inclusion(models.Model):
    title = models.CharField(max_length = 150)
    icon = IconField()

    def __str__(self):
        return self.title


class Months(models.Model):
    title = models.CharField(max_length = 15, blank= True, null= True)

    def __str__(self):
        return self.title


class Adventuredestination(models.Model):
    title = models.CharField(max_length = 20, blank= True, null= True)
    associated_adventures = models.ManyToManyField(Adventure, blank = True)
    vendor_destination = models.ForeignKey(Destination, blank = True)

    def __str__(self):
        return self.title


class Adventuregear(models.Model):
    title = models.CharField(max_length = 50, blank = True)
    logo = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.title


class Adventurevendor(models.Model):
    name = models.CharField(max_length= 20, blank= True)
    associated_adventure = models.ForeignKey(Adventure, blank= True, null= True)
    contact_number = models.BigIntegerField()
    location = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, blank = True)

    def __str__(self):
        return self.name



class Destinationpackage(models.Model):
    SEASON_CHOICES = (
        ('summer','Summer'),
        ('winter', 'Winter'),
        ('autumn', 'Autumn'),
        ('spring', 'Spring'),
    )
    snoi = models.IntegerField(null=True, blank= True)
    title = models.CharField(max_length=250)
    logo = models.FileField(upload_to='documents/destinationpackage')
    destination = models.ForeignKey(Destination, blank=True, null= True)
    head_description = models.TextField()
    property_rating = models.IntegerField(null= True)
    package_description = models.TextField(null= True, blank= True)
    included_adventure = models.ManyToManyField(Adventure, blank=True)
    price_for_one = models.IntegerField()
    price_for_four = models.IntegerField(null= True, blank= True)
    price_for_seven = models.IntegerField(null= True, blank= True)
    price_for_twelve = models.IntegerField(null= True, blank= True)
    price_for_eighteen = models.IntegerField(null= True, blank= True)
    duration = models.IntegerField()
    duration_nights = models.IntegerField(null= True, blank= True)
    best_seasons_to_visit = models.CharField(max_length = 10, choices = SEASON_CHOICES)
    inclusions = models.ManyToManyField(Inclusion, related_name='inclusions_packages')

    def __str__(self):
        return self.title


class UpcomingTrip(models.Model):
    title = models.CharField(max_length=250)
    logo = models.FileField(upload_to='documents/')
    departure = models.CharField(max_length = 50, default = 'Delhi')
    destination = models.ManyToManyField(Destination, blank=True)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null= True, blank= True)
    head_description = models.TextField()
    associated_adventures = models.ManyToManyField(Adventure, blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank = True, null = True)
    duration = models.IntegerField()
    itenary = models.ForeignKey(Itenary, null=True, blank=True)
    inclusions = models.ManyToManyField(Inclusion, blank = True, related_name='inclusions_upcomingtrip')

    def __str__(self):
        return self.title

class UpcomingTripItinerary(models.Model):
    upcoming_trip_package = models.ForeignKey(UpcomingTrip, related_name='upcoming_trip_itinerary')
    day_detail = HTMLField()
    
class GroupPackageitenerary(models.Model):
    destination_package = models.ForeignKey(Destinationpackage, related_name='destinationitinerary')
    day_detail = HTMLField()


class Destinationimage(models.Model):
    destination = models.ForeignKey(Destinationpackage, related_name = 'destinationimages')
    image = models.CharField(max_length = 200)
    
    
class Destinationpackagehighlights(models.Model):
    destination = models.ForeignKey(Destinationpackage, related_name = 'highlights')
    title = models.CharField(max_length = 200, null= True, blank= True)

class UpcomingTripImage(models.Model):
    destination = models.ForeignKey(UpcomingTrip, related_name = 'upcomingtripimages')
    image = models.CharField(max_length = 200)


class Addon(models.Model):
    title = models.CharField(max_length = 150)
    destination_package = models.ForeignKey(Destinationpackage, related_name='addons')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Month(models.Model):
    MONTH_CHOICES = (
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December'),
    )
    month_of_year = models.CharField(choices = MONTH_CHOICES, max_length=25)

    def __str__(self):
        return self.month_of_year


class Adventurepackage(models.Model):
    ADVENTURE_FORM_CHOICES = (
        ('landbased','Landbased'),
        ('waterbased','Waterbased'),
        ('airbased', 'Airbased'),
    )

    title = models.CharField(max_length= 200, blank= True, null= True)
    short_description = models.TextField(blank= True, null= True)
    adventure_form = models.CharField(choices= ADVENTURE_FORM_CHOICES, max_length = 15, null=True)
    destination = models.ForeignKey(Destination, blank= True, null= True, related_name='destinations')
    associated_adventure = models.ForeignKey(Adventure, blank= True, null= True, related_name='adventuresimilar')
    price_per_person = models.IntegerField(blank= True, null= True)
    group_prices = models.IntegerField(blank= True, null= True)
    notes_for_activity = HTMLField(blank= True, null= True)
    level_of_difficulty_on_5 = models.IntegerField(blank= True, null= True)
    required_gear = models.ManyToManyField(Adventuregear, blank= True)
    months_of_year = models.ManyToManyField(Month, blank = True)
    vendor = models.ForeignKey(Adventurevendor, blank= True, null= True)
    logo = models.FileField(upload_to='documents/adventurepackage')

    def __str__(self):
        return self.title


class Adventureimage(models.Model):
    adventure_package = models.ForeignKey(Adventurepackage, related_name = 'adventureimages')
    image = models.CharField(max_length = 200)

    def __str__(self):
        return self.adventure_package


class ThingsToDo(models.Model):
    title= models.CharField(max_length= 200)
    destination = models.ForeignKey(Destination, blank= True)
    duration = models.CharField(max_length= 50)
    logo = models.FileField(upload_to='documents/ThingsToDo')

    def __str__(self):
        return self.title


class Rental(models.Model):
    ITEM_CHOICES = (
        ('tent', 'Tent'),
        ('sleepingbag', 'Sleepingbag'),
        ('rucksack', 'RuckSack'),
        ('accessory', 'Accessory'),
    )
    title = models.CharField(max_length = 200)
    associated_adventure = models.ManyToManyField(Adventure)
    item = models.CharField(max_length = 100)
    category = models.CharField(max_length = 20, choices = ITEM_CHOICES)
    price_per_day = models.IntegerField()
    price_after_three_days = models.IntegerField()
    logo = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length = 100)
    image = models.CharField(max_length = 250)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length = 200)
    logo = models.CharField(max_length= 200)
    head_description = models.TextField(max_length = 200)
    date_published = models.DateField()
    destination = models.ManyToManyField(Destination, blank= True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.CharField(max_length = 200)
    description = HTMLField()
    article = models.ForeignKey(Article, related_name='article_posts')

    def __str__(self):
        return self.title


class Howdystays(models.Model):
    title = models.CharField(max_length = 100)
    location = models.OneToOneField(Destination, on_delete = models.CASCADE)
    property_description = HTMLField(blank= True, null = True)
    price_per_room = models.IntegerField(blank= True, null = True)
    price_deluxe_room = models.IntegerField(blank= True, null = True)
    price_suite_room = models.IntegerField(blank= True, null = True)
    capacity_allowed = models.IntegerField(blank= True, null = True)
    ep_per_person = models.IntegerField(blank= True, null= True)
    cp_per_person = models.IntegerField(blank= True, null= True)
    ap_per_person = models.IntegerField(blank= True, null= True)
    mapai_per_person = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.title


class StayAddon(models.Model):
    title = models.CharField(max_length = 150)
    destination_package = models.ForeignKey(Howdystays, related_name='Howdystaysaddons')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Stayimage(models.Model):
    destination = models.ForeignKey(Howdystays, related_name = 'Howdystaysimages')
    image = models.CharField(max_length = 200)
