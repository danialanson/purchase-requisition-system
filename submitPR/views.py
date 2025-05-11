from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import PRTable, PRITable
# Create your views here.

@login_required
def submitPR(request):
    context = {
    'title':'Submit Purchase Requisition Form',
    'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'submitPR/submitPRform.html',context)

def submitPRconfirmation(request):
    user = request.user
    newpr_id = request.POST['pr_id']
    newemp_id = user.username
    newemp_Name = (user.first_name + ' ' + user.last_name)
    newform_Date = date.today()
    newdelv_Date = request.POST['delivery_date']
    newdelv_Address = request.POST['delivery_address']

    newPR = PRTable(pr_id = newpr_id, emp_id = newemp_id, emp_Name = newemp_Name, form_Date = newform_Date, delv_Date = newdelv_Date, delv_Address = newdelv_Address)
    newPR.save()

    item1_id = request.POST['item_id1']
    item1_Description = request.POST['item_desc1']
    item1_Quantity = request.POST['item_quantity1']
    item1_unitPrice = request.POST['item_price1']
    item1_totalPrice = float(item1_unitPrice)*float(item1_Quantity)

    PRI1 = PRITable(item_id = item1_id, pr_id = newPR, item_Description = item1_Description, item_Quantity = item1_Quantity, item_unitPrice = item1_unitPrice, item_totalPrice = item1_totalPrice)
    PRI1.save()

    item2_id = request.POST['item_id2']
    if item2_id != "":
        item2_Description = request.POST['item_desc2']
        item2_Quantity = request.POST['item_quantity2']
        item2_unitPrice = request.POST['item_price2']
        item2_totalPrice = float(item2_unitPrice)*float(item2_Quantity)

        PRI2 = PRITable(item_id = item2_id, pr_id = newPR, item_Description = item2_Description, item_Quantity = item2_Quantity, item_unitPrice = item2_unitPrice, item_totalPrice = item2_totalPrice)
        PRI2.save()

    item3_id = request.POST['item_id3']
    if item3_id != "":
        item3_Description = request.POST['item_desc3']
        item3_Quantity = request.POST['item_quantity3']
        item3_unitPrice = request.POST['item_price3']
        item3_totalPrice = float(item3_unitPrice)*float(item3_Quantity)

        PRI3 = PRITable(item_id = item3_id, pr_id = newPR, item_Description = item3_Description, item_Quantity = item3_Quantity, item_unitPrice = item3_unitPrice, item_totalPrice = item3_totalPrice)
        PRI3.save()

    return render(request,'submitPR/submitPRconfirmation.html')