from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import QTable, QITable
# Create your views here.

@login_required
def viewQuo(request):

    list = QTable.objects.filter(purchaser_id = request.user.username).only('quotation_ID', 'quotation_Stats')

    return render(request, 'viewQuo/viewQuo.html', {'list': list})

def viewQuodetails(request):

    data = QTable.objects.all()
    ilist = None
    quo = None


    for i in data:
        if i.quotation_ID in request.POST:
            quo = QTable.objects.filter(quotation_ID=i.quotation_ID)
            ilist = QITable.objects.filter(quotation_ID=i.quotation_ID)

    print(quo)
    print(ilist)

    return render(request, 'viewQuo/viewQuodetails.html', {'quo': quo, 'ilist': ilist})