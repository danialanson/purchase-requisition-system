from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import POTable, POITable
# Create your views here.

@login_required
def viewPO(request):

    list = POTable.objects.filter(fo_id= request.user.username).only('po_id',)

    return render(request, 'viewPO/viewPO.html', {'list': list})

def viewPOdetails(request):

    data = POTable.objects.all()
    ilist = None
    po = None


    for i in data:
        if i.po_id in request.POST:
            po = POTable.objects.filter(po_id=i.po_id)
            ilist = POITable.objects.filter(po_id=i.po_id)

    print(po)
    print(ilist)

    return render(request, 'viewPO/viewPOdetails.html', {'po': po, 'ilist': ilist})