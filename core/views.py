from django.shortcuts import render
from shop.models import *
# Create your views here.
def home(request):
    return home_with_language(request,'mm')

def home_with_language(request,lang):
    item = None
    webcontent = Webcontent.objects.all()

    if lang == 'mm':
        lead1 = webcontent[0].lead_1_mm
        lead2 = webcontent[0].lead_2_mm
        topic1 = webcontent[0].topic_1_mm
        topic2 = webcontent[0].topic_2_mm
        topic3 = webcontent[0].topic_3_mm
        content1 = webcontent[0].content_1_mm
        content2 = webcontent[0].content_2_mm
        content3 = webcontent[0].content_3_mm
    elif lang == 'eng':
        lead1 = webcontent[0].lead_1
        lead2 = webcontent[0].lead_2
        topic1 = webcontent[0].topic_1
        topic2 = webcontent[0].topic_2
        topic3 = webcontent[0].topic_3
        content1 = webcontent[0].content_1
        content2 = webcontent[0].content_2
        content3 = webcontent[0].content_3
    else:
        return redirect('/language_does_not_exist')
    
    try:
        item = Item.objects.filter(is_feature=True)
    except:
        item = []
        
    context = {'item':item,
                'lang':lang,
                'lead1':lead1,
                'lead2':lead2,
                'topic1':topic1,
                'topic2':topic2,
                'topic3':topic3,
                'content1':content1,
                'content2':content2,
                'content3':content3,}
    
    return render(request,"core/home.html",context)


    
    