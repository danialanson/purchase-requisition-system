from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import QTable, QITable, POTable, POITable
# Create your views here.

@login_required
def submitPO(request):

    list = QTable.objects.filter(quotation_Stats = "Approved").only('quotation_ID', 'quotation_Stats')

    return render(request, 'submitPO/submitPO.html', {'list': list})

def submitPOdetails(request):

    data = QTable.objects.all()
    ilist = None
    quo = None


    for i in data:
        if i.quotation_ID in request.POST:
            quo = QTable.objects.filter(quotation_ID=i.quotation_ID)
            ilist = QITable.objects.filter(quotation_ID=i.quotation_ID)


    return render(request, 'submitPO/submitPOdetails.html', {'quo': quo, 'ilist': ilist})

def submitPOconfirmation(request):
    
    user = request.user    
    qt = QTable.objects.all()
    qit = QITable.objects.all()
    quo = None
    quoi = None

    newfo_id = user.username
    newfo_Name = (user.first_name + ' ' + user.last_name)
    for i in qt:
        if i.quotation_ID in request.POST:
            quo = QTable.objects.filter(quotation_ID=i.quotation_ID)
            newdelv_Address = i.delv_Address
            newvendor_Name = i.vendor_Name
            newvendor_Address = i.vendor_Address
            newPO = POTable(quotation_ID= i, fo_id = newfo_id, fo_Name = newfo_Name, 
                            delv_Address = newdelv_Address, vendor_Name = newvendor_Name, 
                            vendor_Address = newvendor_Address)

    newPO.save()

    for i in qit:
        if i.quotation_ID in request.POST:
            quoi = QITable.objects.filter(quotation_ID=i.quotation_ID)
            newitem_id = i.item_id
            newitem_Description = i.item_Description
            newitem_Quantity = i.item_Quantity
            newitem_unitPrice = i.item_unitPrice
            newitem_totalPrice = i.item_totalPrice
            newPOI = POITable(item_id= newitem_id, po_id = newPO, item_Description = newitem_Description, 
                            item_Quantity = newitem_Quantity, item_unitPrice = newitem_unitPrice, 
                            item_totalPrice = newitem_totalPrice)
            newPOI.save()  
    
    return render(request,'submitPO/submitPOconfimation.html')