from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import QTable, QITable
# Create your views here.

@login_required
def submitQuo(request):
    context = {
    'title':'Submit Quotation Form',
    'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'submitQuo/submitQuoform.html',context)

def submitQuoconfirmation(request):
    user = request.user
    newquo_id = request.POST['quotation_ID']
    newpurchaser_id = user.username
    newpurchaser_Name = (user.first_name + ' ' + user.last_name)
    newdelv_Address = request.POST['delivery_address']
    newvendor_Name = request.POST['vendor_name']
    newvendor_Address = request.POST['vendor_address']
    newquo_Date = date.today()

    newQuo = QTable(quotation_ID = newquo_id, purchaser_id = newpurchaser_id, 
                    purchaser_Name = newpurchaser_Name, delv_Address = newdelv_Address, 
                    vendor_Name = newvendor_Name, vendor_Address = newvendor_Address, quotation_Date = newquo_Date)
    newQuo.save()

    item1_id = request.POST['item_id1']
    item1_Description = request.POST['item_desc1']
    item1_Quantity = request.POST['item_quantity1']
    item1_unitPrice = request.POST['item_price1']
    item1_totalPrice = float(item1_unitPrice)*float(item1_Quantity)

    QRI1 = QITable(item_id = item1_id, quotation_ID = newQuo, item_Description = item1_Description, 
                    item_Quantity = item1_Quantity, item_unitPrice = item1_unitPrice, item_totalPrice = item1_totalPrice)
    QRI1.save()

    item2_id = request.POST['item_id2']
    if item2_id != "":
        item2_Description = request.POST['item_desc2']
        item2_Quantity = request.POST['item_quantity2']
        item2_unitPrice = request.POST['item_price2']
        item2_totalPrice = float(item2_unitPrice)*float(item2_Quantity)

        QRI2 = QITable(item_id = item2_id, quotation_ID = newQuo, item_Description = item2_Description, 
                        item_Quantity = item2_Quantity, item_unitPrice = item2_unitPrice, item_totalPrice = item2_totalPrice)
        QRI2.save()

    item3_id = request.POST['item_id3']
    if item3_id != "":
        item3_Description = request.POST['item_desc3']
        item3_Quantity = request.POST['item_quantity3']
        item3_unitPrice = request.POST['item_price3']
        item3_totalPrice = float(item3_unitPrice)*float(item3_Quantity)

        QRI3 = QITable(item_id = item3_id, quotation_ID = newQuo, item_Description = item3_Description, 
                        item_Quantity = item3_Quantity, item_unitPrice = item3_unitPrice, item_totalPrice = item3_totalPrice)
        QRI3.save()

    return render(request,'submitQuo/submitQuoconfirmation.html')