from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('enter the topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()


    return HttpResponse('topic is created successfully')



''''def insert_webpage(request):
    tn=input('enter the topic')
    n=input('enter the name')
    u=input('enter the url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created successfully')'''

def insert_webpage(request):
    tn=input('enter the topic')
    n=input('enter the name')
    u=input('enter the url')
    #TO=Topic.objects.get(topic_name=tn)
    '''we can use get method to get the parents table object but if parent table object is not available it throws an error '''
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        return HttpResponse('webpage is created successfully')
    else:
        return HttpResponse('given topic is not present in parent table')












def insert_record(request):
    tn=input('enter the topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter the name')
    u=input('enter the url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    
    
    n=input('enter the name')
    d=input('enter the date')
    a=input('enter the author')
    AO=AccessRecord.objects.get_or_create(name=WO,date='1994-04-25',author='rahul')[0]
    AO.save()
    return HttpResponse('accessrecord is created successfully')

