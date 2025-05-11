from django.shortcuts import render
from app.models import Quotation, Item, PurchaseOrder, User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def foviewPOlist(request):

    list = PurchaseOrder.objects.filter(finance_officer=request.user)

    return render(request, 'FOviewPO/foviewPOlist.html', {'list': list})

def foviewPOdetails(request):

    data = PurchaseOrder.objects.filter()
    po = None
    client_address = None
    vendor_address = None
    purchase_address = None
    tax_rate = None
    discount_rate = None

    for i in data:
        if i.purchase_id in request.POST:
            po = PurchaseOrder.objects.filter(purchase_id=i.purchase_id)
            client_address = po.get().quotation.client_address.split(",")
            vendor_address = po.get().quotation.vendor_address.split(",")
            purchase_address = po.get().purchase_address.split(",")
            items = Item.objects.filter(quotation_id=i.quotation_id , item_purchased=True)
            tax_rate = str(po.get().quotation.tax_rate * 100) + '%'
            discount_rate = str(po.get().quotation.discount * 100) + '%'
        
    quo = po.get().quotation

    return render(request, 'FOviewPO/foviewPOdetails.html', {'po': po.get() , 'quo': quo , 'caddress': client_address , 'vaddress': vendor_address , 'paddress': purchase_address , 'items': items , 'tax_rate': tax_rate , 'discount_rate': discount_rate})