# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Destinationpackage, UpcomingTrip, Adventurepackage, Rental, Gallery, Post, Article, ThingsToDo, Howdystays
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template.context_processors import csrf
from homepage.forms import TravelFreeForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from homepage.forms import UpcomingtripForm
import json
import csv
from homepage.models import Adventurepackage, Destination, Adventure
from homepage.forms import LoginForm, HotSellingForm
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def login_page(request):
    form = LoginForm(request.POST or None)
    template = 'auth/login.html'
    context = {
    'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect("/userprofile")
        else:
            print("Error")
    return render(request, template, context)


@login_required
def userprofile(request):
    context = locals()
    template = 'userprofilehome.html'
    return render(request, template, context)

def hotsellingquery(request, id=None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_hotsell')
        query_user_email = request.POST.get('email_hotsell')
        query_user_phone = request.POST.get('phone_hotsell')
        query_hotsell = request.POST.get('query_hotsell')
        query_numberofpeople = request.POST.get('num_people_hotselling')
        query_startdate = request.POST.get('start')
        query_enddate = request.POST.get('end')
        queryfor_package = Destinationpackage.objects.get(id= id)
        package_title = queryfor_package.title
        subject = 'Message from MYSITE.COM'
        subject2 = 'Message from HowdyHighlands'
        regard_text = "Thanks for submitting your query to HowdyHighlands for " + package_title + ". Our team will get back shortly to you."
        message = '%s \n %s \n %s \n %s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_numberofpeople, query_hotsell, package_title, query_startdate, query_enddate)
        emailFrom = query_user_email
        emailTo = ['tusharblogger12@gmail.com']
        emailFrom2 = 'howdyhighlands@gmail.com'
        email_client = [query_user_email]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        send_mail(subject2, regard_text, emailFrom2, email_client, fail_silently= True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+package_title +"submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded. Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
    return HttpResponseRedirect("/destination", {'messages':messages,})

def adventurepackagequery(request, id=None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_activity')
        query_user_email = request.POST.get('email_activity')
        query_user_phone = request.POST.get('phone_activity')
        query_hotsell = request.POST.get('query_activity')
        query_numberofpeople = request.POST.get('numpeople_upcomingtrip')
        queryfor_package = Adventurepackage.objects.get(id= id)
        package_title = queryfor_package.title
        subject = package_title + ' query for activity.'
        subject2 = 'Message from HowdyHighlands'
        regard_text = "Thanks for submitting your query to HowdyHighlands for " + package_title + ". Our team will get back shortly to you."
        message = '%s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_hotsell, package_title)
        emailFrom = query_user_email
        emailFrom2 = 'howdyhighlands@gmail.com'
        emailTo = ['tusharblogger12@gmail.com']
        email_client = [query_user_email]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        send_mail(subject2, regard_text, emailFrom2, email_client, fail_silently= True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+package_title +"submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded. Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
    return HttpResponseRedirect("/adventureactivitylist", {'messages':messages,})


def upcomingtripquery(request, id=None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_upcomingtrip')
        query_user_email = request.POST.get('email_upcomingtrip')
        query_user_phone = request.POST.get('phone_upcomingtrip')
        query_hotsell = request.POST.get('query_upcomingtrip')
        queryfor_package = UpcomingTrip.objects.get(id= id)
        package_title = queryfor_package.title
        subject = package_title +' query for activity.'
        message = '%s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_hotsell, package_title)
        emailFrom = query_user_email
        emailTo = ['howdyhighlands@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+package_title +"submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded. '+ query_username + ' , our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
    return HttpResponseRedirect('/upcomingtripdetail/%d' % (queryfor_package.id), {'messages':messages,})


def adventurepackagebook(request, id=None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_bookactivity')
        query_user_email = request.POST.get('email_bookactivity')
        query_user_phone = request.POST.get('phone_bookactivity')
        query_hotsell = request.POST.get('query_bookactivity')
        queryfor_package = Adventurepackage.objects.get(id= id)
        package_title = queryfor_package.title
        subject = package_title +' book for activity.'
        message = '%s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_hotsell, package_title)
        emailFrom = query_user_email
        emailTo = ['howdyhighlands@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+ package_title + "submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your booking request has been successfully recorded. Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
    return HttpResponseRedirect("/adventureactivitylist", {'messages':messages,})

def hotsellingbook(request, id=None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_hotsellbook')
        query_user_email = request.POST.get('email_hotsellbook')
        query_user_phone = request.POST.get('phone_hotsellbook')
        query_numberofpeople = request.POST.get('num_people_hotselling')
        query_hotsell = request.POST.get('query_hotsellbook')
        bookfor_package = Destinationpackage.objects.get(id= id)
        package_title =  bookfor_package.title
        destination_packageid = bookfor_package.destination.id
        subject = 'Message from HowdyHighlands'
        subject2 = 'Confirmation on receving your query'
        message = '%s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_hotsell, package_title)
        emailFrom = query_user_email
        emailTo = ['howdyhighlands@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+ package_title + "submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded for ' +  str(package_title) + '.Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
            '/filter_analysis/?%s' % (filterconfig.filterstring)
    return HttpResponseRedirect('/searchdestinationpage/%d' % (destination_packageid), {'messages':messages,})

def upcomingtripbook(request, id= None):
    check = 0
    if request.method == 'POST':
        query_username = request.POST.get('user_hotsellbook')
        query_user_email = request.POST.get('email_hotsellbook')
        query_user_phone = request.POST.get('phone_hotsellbook')
        query_numberofpeople = request.POST.get('num_people_hotselling')
        query_hotsell = request.POST.get('query_hotsellbook')
        bookfor_package = UpcomingTrip.objects.get(id= id)
        package_title =  bookfor_package.title
        subject = 'Message from HowdyHighlands'
        subject2 = 'Confirmation on receving your query'
        message = '%s \n %s \n %s \n %s \n'%(query_username, query_user_email, query_hotsell, package_title)
        emailFrom = query_user_email
        emailTo = ['tusharblogger12@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+ package_title + "submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded for ' +  str(package_title) + '.Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
            '/filter_analysis/?%s' % (filterconfig.filterstring)
    return HttpResponseRedirect('/upcomingtripdetail/%d' % (bookfor_package.id), {'messages':messages,})

def destinationpackagebook(request, id=None):
    check = 0
    if request.method == 'POST':
        query_user_email = request.POST.get('email_hotsellbook')
        query_user_phone = request.POST.get('phone_hotsellbook')
        query_numberofpeople = request.POST.get('num_people_hotselling')
        query_startdate = request.POST.get('start')
        query_enddate = request.POST.get('end')
        add_on_query = request.POST.getlist('checks[]')
        bookfor_package = Destinationpackage.objects.get(id= id)
        package_title =  bookfor_package.title
        destination_packageid = bookfor_package.destination.id
        subject = 'Message from HowdyHighlands'
        subject2 = 'Confirmation on receving your query'
        message = '%s \n %s \n %s \n %s \n %s \n %s \n'%(add_on_query, query_user_email, query_user_phone, query_startdate, query_enddate, package_title)
        emailFrom = query_user_email
        emailTo = ['howdyhighlands@gmail.com']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        success_text = "Query for "+ package_title + "submitted!!"
        check = 1
        if check == 1:
            messages.success(request, 'Your request has been successfully recorded for ' +  str(package_title) + '.Our team will get in touch with you shortly.')
        else:
            messages.success(request, 'Your process could not be completed.')
            '/filter_analysis/?%s' % (filterconfig.filterstring)
    return HttpResponseRedirect('/searchdestinationpage/%d' % (destination_packageid), {'messages':messages,})


def home(request):
    upcoming_trips = UpcomingTrip.objects.all().order_by('start_date')
    best_destinations = Destinationpackage.objects.all()[:3]
    rental_items = Rental.objects.all()[:3]
    template = 'homepage.html'
    args = {}
    args.update(csrf(request))
    args['upcoming_trips'] = UpcomingTrip.objects.all().order_by('start_date')
    args['rental_items'] = Rental.objects.all()[:3]
    args['best_destinations'] = best_destinations
    args['adventure_landbased'] = Adventure.objects.filter(adventureform_choice='landbased')
    args['adventure_waterbased'] = Adventure.objects.filter(adventureform_choice='waterbased')
    args['adventure_airbased'] = Adventure.objects.filter(adventureform_choice='airbased')
    args['adventure_package'] = Adventurepackage.objects.all()[:4]
    #context = {
    #    'adventure_landbased' : adventure_landbased,
    #    'adventure_waterbased' : adventure_waterbased,
    #    'adventure_airbased' : adventure_airbased,
    #}
    #print(destination_json)
    #context = {
    #    'upcoming_trips' : upcoming_trips,
    #    'best_destinations' : best_destinations,
    #    'rental_items': rental_items,
    #}
    return render_to_response('homepage.html', args,)

#def load_adventures(file_path):
#    reader = csv.DictReader(open(file_path))
#    for row in reader:
#        adventure = Adventurepackage(title=row['Title'], destination=row['Destination'], duration=row['Duration'], adventure=row['Adventure'], price_per_person=row['Price per person'], logo=row['Logo'])
#        adventure.save()

def searchdestination(request):
    if request.method == 'POST':
        search_destination_text = request.POST['search_destination_text']
    else:
        search_destination_text = ''
    destination_list =  Destinationpackage.objects.filter(title__icontains = search_destination_text)
    print(destination_list)
    return render_to_response('ajax_search.html', {'destination_list' : destination_list})


def searchactivity(request):
    if request.method == 'POST':
        search_activity_text = request.POST['search_activity_text']
    else:
        search_activity_text = ''
    result = Adventurepackage.objects.filter(title__icontains=search_activity_text).distinct()
    count = len(result)
    print(result)
    return render_to_response('ajaxactivity_search.html', {'result' : result,})


def searchdestinationlist(request):
    if request.method == 'GET':
        query = request.GET.get('searchdestination')
        results = Destinationpackage.objects.filter(Q(title__icontains = query))
        count = len(results)
        activity_related = Adventurepackage.objects.filter(title__icontains=query)
        context = {
              'results':results,
              'count':count,
              'activity_related':activity_related,
              'query': query,
        }
        return render(request, "homepage/destinationpackage_list.html", context)

    else:
        return render(request, "homepage/destinationpackage_list.html", {'results':results})


def searchdestinationpage(request, id=None):
    destination_search = Destinationpackage.objects.filter(destination__id=id)
    destinationtitle = destination_search[0].destination
    count = len(destination_search)
    activity_related = Adventurepackage.objects.filter(destination__id=id)
    article_destination = Article.objects.filter(destination__id=id)
    context = {
        'destination_search' : destination_search,
        'activity_related' : activity_related,
        'count' : count,
        'article_destination':article_destination,
        'destinationtitle' : destinationtitle,
    }
    template = 'homepage/searchdestinationpage.html'
    return render(request, template, context)


def searchactivitylist(request):
    if request.method == 'GET':
        querytwo = request.GET.get('searchactivity')
        result = Adventurepackage.objects.filter(Q(title__icontains=querytwo))
        count = len(result)
        rentalitem = Rental.objects.filter(associated_adventure__title__icontains=querytwo).distinct()
        context = {
            'result':result,
            'rentalitem':rentalitem,
            'querytwo': querytwo,
            'count': count,
            'querytwo': querytwo,
            }
        return render(request, "homepage/activitysearch_list.html", context)
    else:
        return render(request, "homepage/activitysearch_list.html", context)


def activity_singlepackage_all(request, pk1):
    activity = Adventurepackage.objects.get(id = pk1)
    associated_adventure_id = activity.associated_adventure.id
    result = Adventurepackage.objects.filter(associated_adventure__id = associated_adventure_id)
    result = result.exclude(id = activity.id)
    result2 = Adventurepackage.objects.filter(associated_adventure__id = associated_adventure_id)
    rentalitem = Rental.objects.filter(associated_adventure__id= pk1).distinct()
    count = len(result)
    context = {
        'activity' : activity,
        'result2' : result2,
        'result':result,
        'count' : count,
        'rentalitem': rentalitem,
    }
    return render(request, "adventuresingle_package.html", context)

def singleadventure(request, pk1):
    result = Adventurepackage.objects.filter(associated_adventure__id = pk1)
    count = len(result)
    context = {
        'result' : result,
        'count' : count,
    }
    return render(request, "activityform_base.html", context)


def destinationmore(request, id=None):
    destination_look = get_object_or_404(Destination, id=id)
    context = {
        'destination_look' : destination_look
    }
    return render(request, 'modal.html', context)


def destinationactivity(request, id):
    destination_adventure = Adventurepackage.objects.filter(destination__id=id)
    context = {
        'associated_adventure_sports' : destination_adventure
    }
    return render(request, 'modalbox.html', context)


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Adventurepackage.objects.filter(title_startswith=q)
        results = []
        print q
        for r in search_qs:
            results.append(r.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def destinationdetails(request, pk):
    detail_package = Destinationpackage.objects.get(pk= pk)
    template = 'destinationdetails.html'
    destination_images = detail_package.destinationimages.all()
    itinerary_day_detail = detail_package.destinationitinerary.all()
    destination_add_ons = detail_package.addons.all()
    inclusions = detail_package.inclusions.all()
    adventurethings_to_do = Adventurepackage.objects.filter(destination= detail_package.destination)
    things_to_do = ThingsToDo.objects.filter(destination = detail_package.destination)
    context = {
        'detail_package' : detail_package,
        'destination_images' : destination_images,
        'destination_add_ons': destination_add_ons,
        'inclusions' : inclusions,
        'adventurethings_to_do': adventurethings_to_do,
        'things_to_do' : things_to_do,
        'itinerary_day_detail':itinerary_day_detail,
    }
    return render(request, template, context)

    #package_list = Destinationpackage.objects.all()
    #package_filter = PackageFilter(request.GET, queryset = package_list)
    #template = 'dummy.html'
    #return render(request, template, {'filter': package_filter})


def upcomingtripdetail(request, pk=None):
    upcoming_tripdetail = UpcomingTrip.objects.get(id= pk)
    upcoming_trip_images = upcoming_tripdetail.upcomingtripimages.all()
    upcoming_trip_itinerary = upcoming_tripdetail.upcoming_trip_itinerary.all()
    inclusions = upcoming_tripdetail.inclusions.all()
    upcoming_departures = UpcomingTrip.objects.all()
    article_similar = Article.objects.filter(destination__id= pk)
    destinationtitle = upcoming_tripdetail.destination.first()
    best_destinations = Destinationpackage.objects.all()[:3]
    template = 'upcomingtripdetail.html'
    context = {
        'upcoming_tripdetail' : upcoming_tripdetail,
        'upcoming_trip_images' : upcoming_trip_images,
        'inclusions' : inclusions,
        'upcoming_departures':upcoming_departures,
        'article_similar' : article_similar,
        'destinationtitle' : destinationtitle,
        'upcoming_trip_itinerary' : upcoming_trip_itinerary,
        'best_destinations' : best_destinations
    }
    return render(request, template, context)


def gallery(request):
    collection = Gallery.objects.all()
    collection2 = collection
    collection3 = collection
    template = 'gallery.html'
    context = {
        'collection': collection,
        'collection2' : collection2,
        'collection3' : collection3,
    }
    return render(request, template, context)

def travelfree(request):
    form = TravelFreeForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        contact = form.cleaned_data['contact']
        number_of_people = form.cleaned_data['number_of_people']
        destination = form.cleaned_data['destination']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.COM'
        message = '%s \n %d \n %s \n %d'%(name, number_of_people, destination, contact)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None
    template = 'travelfree.html'
    return render(request, template, {'form':form, 'confirm_message': confirm_message})

def destination(request):
    destination_list = Destination.objects.all()
    package_list = Destinationpackage.objects.all()
    template = 'destinationlist.html'
    context = {
        'destination_list':destination_list,
        'package_list' : package_list,
    }
    return render(request, template, context)

def traveldiaries(request):
    article_list = Article.objects.all()
    template = 'articleslist.html'
    context = {
        'article_list' : article_list,
    }
    return render(request, template, context)

def postdetail(request, pk):
    article = Article.objects.get(pk = pk)
    template = 'post_detail.html'
    post_list = article.article_posts.all()
    context = {
        'article' : article,
        'post_list' : post_list,
    }
    return render(request, template, context)



def upcomingtrip_form_upload(request):
    if request.method == 'POST':
        form = UpcomingtripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpcomingtripForm()
    return render(request, 'upcomingtrip_form_upload.html', {'form': form})


def adventureactivity_list(request):
    result = Adventurepackage.objects.all()
    rentalitem = Rental.objects.all()
    context = {
        'result':result,
        'rentalitem':rentalitem,
        }
    return render(request, "adventureactivitylist.html", context)



def destinationabout(request, id):
    package_destination = Destinationpackage.objects.filter(destination__id=id)
    template = 'aboutdestination.html'
    context = {
        'package_destination':package_destination,
    }
    return render(request, template, context)


def howdystayslist(request):
    property_list = Howdystays.objects.all()
    template = 'howdystayslist.html'
    context = {
        'property_list' : property_list,
    }
    return render(request, template, context)
