# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from homepage.models import Destination, Itenary, Adventure, Destinationpackage, UpcomingTrip, Destinationimage, Adventurepackage, Rental, Gallery, Article, Post, Addon, Inclusion, ThingsToDo, Month
from homepage.models import  Months, Adventuredestination, Adventuregear, Adventurevendor, Adventurepackage, UpcomingTripImage, Howdystays, StayAddon, Stayimage, GroupPackageitenerary, UpcomingTripItinerary, Destinationpackagehighlights, Requiredgear

# Register your models here.
class DestinationImageInline(admin.TabularInline):
    model = Destinationimage

class RequiredgearInline(admin.TabularInline):
    model = Requiredgear

class PostInline(admin.TabularInline):
    model = Post

class AddonInline(admin.TabularInline):
    model = Addon

class GroupPackageiteneraryInline(admin.TabularInline):
    model = GroupPackageitenerary

class UpcomingTripItineraryInline(admin.TabularInline):
    model = UpcomingTripItinerary

class StayAddonInline(admin.TabularInline):
    model = StayAddon

class StayimageInline(admin.TabularInline):
    model = Stayimage

class DestinationpackagehighlightsInline(admin.TabularInline):
    model = Destinationpackagehighlights

class MonthAdmin(admin.ModelAdmin):
    class Meta:
        model = Month
admin.site.register(Month, MonthAdmin)

class UpcomingTripImageInline(admin.TabularInline):
    model = UpcomingTripImage


class HowdystaysAdmin(admin.ModelAdmin):
    inlines = [StayAddonInline, StayimageInline]
    class Meta:
        model = Howdystays
admin.site.register(Howdystays, HowdystaysAdmin)


class AdventuregearAdmin(admin.ModelAdmin):
    class Meta:
        model = Adventuregear
admin.site.register(Adventuregear, AdventuregearAdmin)

class AdventurevendorAdmin(admin.ModelAdmin):
    class Meta:
        model = Adventurevendor
admin.site.register(Adventurevendor, AdventurevendorAdmin)

class DestinationAdmin(admin.ModelAdmin):
    class Meta:
        model = Destination
admin.site.register(Destination, DestinationAdmin)

class ItenaryAdmin(admin.ModelAdmin):
    class Meta:
        model = Itenary
admin.site.register(Itenary, ItenaryAdmin)

class AdventureAdmin(admin.ModelAdmin):
    class Meta:
        model = Adventure
admin.site.register(Adventure, AdventureAdmin)

class ThingsToDoAdmin(admin.ModelAdmin):
    class Meta:
        model = ThingsToDo
admin.site.register(ThingsToDo, ThingsToDoAdmin)

class DestinationpackageAdmin(admin.ModelAdmin):
    inlines = [DestinationImageInline, AddonInline, GroupPackageiteneraryInline,  DestinationpackagehighlightsInline]
    class Meta:
        model = Destinationpackage
admin.site.register(Destinationpackage, DestinationpackageAdmin)

class UpcomingTripAdmin(admin.ModelAdmin):
    inlines = [UpcomingTripImageInline, UpcomingTripItineraryInline]
    class Meta:
		model = UpcomingTrip
admin.site.register(UpcomingTrip, UpcomingTripAdmin)

class DestinationimageAdmin(admin.ModelAdmin):
    class Meta:
        model = Destinationimage
admin.site.register(Destinationimage, DestinationimageAdmin)

class AddonAdmin(admin.ModelAdmin):
    class Meta:
        model = Addon
admin.site.register(Addon, AddonAdmin)

class AdventurepackageAdmin(admin.ModelAdmin):
    inlines = [RequiredgearInline,]
    class Meta:
        model = Adventurepackage
admin.site.register(Adventurepackage, AdventurepackageAdmin)

class RentalAdmin(admin.ModelAdmin):
    class Meta:
        model = Rental
admin.site.register(Rental, RentalAdmin)

class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery
admin.site.register(Gallery, GalleryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    inlines = [PostInline,]
    class Meta:
        model = Article
admin.site.register(Article, ArticleAdmin)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)

class InclusionAdmin(admin.ModelAdmin):
    class Meta:
        model = Inclusion
admin.site.register(Inclusion, InclusionAdmin)
