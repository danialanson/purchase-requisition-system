from django.shortcuts import render
from app.models import Quotation, Item, PurchaseOrder, User
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.

@login_required
def foviewquotation(request):

    list = Quotation.objects.filter(selected=True , generated=False).only('quotation_id', 'valid_days', 'total')

    return render(request, 'FOviewquotation/foviewquotation.html', {'list': list})

def view_quotation_details(request):

    data = Quotation.objects.filter(selected=True)
    items = None
    list = None
    client_address = None
    vendor_address = None

    for i in data:
        if i.quotation_id in request.POST:
            list = Quotation.objects.filter(quotation_id=i.quotation_id)
            client_address = list.get().client_address.split(",")
            vendor_address = list.get().vendor_address.split(",")
            items = Item.objects.filter(quotation_id=i.quotation_id)
            tax_rate = str(list.get().tax_rate * 100) + '%'
            discount_rate = str(list.get().discount * 100) + '%'

    print(items)

    return render(request, 'FOviewquotation/foviewdetails.html', {'list': list , 'caddress': client_address , 'vaddress': vendor_address , 'items': items , 'tax_rate': tax_rate , 'discount_rate': discount_rate})

def generatePOconfirmation(request):
    payment = request.POST.get('payment')
    current_quotation = Quotation.objects.filter(quotation_id=request.POST.get("quotation"))
    po_id = "po" + "{:04}".format(PurchaseOrder.objects.count() + 1)
    data = request.POST.getlist('POitems')
    items = Item.objects.filter(item_id__in=data)
    subtotal= 0
    purchase_address = request.POST.get('purchase_address' , '01 Jln Default, 47130 Puchong, Selangor')
    purchase_contact = request.POST.get('purchase_contact' , '011-1101010')
    purchase_email = request.POST.get('purchase_email' , 'default@gmail.com')

    if purchase_address == '':
        purchase_address = "01 Jln Default, 47130 Puchong, Selangor"
    if purchase_contact == '':
        purchase_contact = "011-1101010"
    if purchase_email == '':
        purchase_email = "default@gmail.com"

    items.update(item_purchased = True)
    current_quotation.update(generated=True)

    for i in items:
        subtotal += i.item_total_cost
    
    total = subtotal * (1 - current_quotation.get().discount) * (1 - current_quotation.get().tax_rate)

    paddress = purchase_address.split(",")

    purchase_order = PurchaseOrder(purchase_id=po_id , finance_officer=request.user , quotation=current_quotation.get() , purchase_date=date.today() , payment_type=payment , purchase_subtotal=subtotal , purchase_total=total , purchase_address=purchase_address , purchase_contact=purchase_contact , purchase_email=purchase_email)
    purchase_order.save()

    return render(request, 'FOviewquotation/fogeneratedPO.html' , {'purchase_order': purchase_order , 'items' : items , 'paddress' : paddress})