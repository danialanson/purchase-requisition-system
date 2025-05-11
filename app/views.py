from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required

from app.models import PRITable, PRTable, QTable, QITable

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'PR System',
            'message':'This system is for user to make a Purchase Requisition, Submit Quotation and Purchase Order',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()
    check_manager = request.user.groups.filter(name='manager').exists()
    check_purchaser = request.user.groups.filter(name='purchaser').exists()
    check_finance_officer = request.user.groups.filter(name='finance officer').exists()

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'is_manager': check_manager,
            'is_purchaser': check_purchaser,
            'is_finance_officer': check_finance_officer, 
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)

def arviewPR(request):
    pr_list = PRTable.objects.all().only('pr_id', 'form_Date', 'form_Stats')

    context = {
        'title':'View Purchase Requisition',
        'year':datetime.now().year,
        'pr_list': pr_list,
    }
    return render(request, 'app/viewPR.html', context)

def larviewPR(request):
    pr_list = PRTable.objects.all().only('pr_id', 'form_Date', 'form_Stats')

    context = {
        'title':'View Purchase Requisition',
        'year':datetime.now().year,
        'pr_list': pr_list,
    }
    return render(request, 'app/lviewPR.html', context)

def arapprovePR(request):
    #DATA BEFORE
    # dataP = PurchaseOrder.objects.filter(poStatus__in=['Pending']).values()
    # dataAp = PurchaseOrder.objects.filter(poStatus__in=['Approved']).values()
    # print(dataP)
    # print(dataAp)

    #GET SELECTED PO
    currentPR = PRTable.objects.filter(pr_id=request.POST.get("purchaseRequisition"))
    print(currentPR)
    currentPR.update(form_Stats='Approved')

    #DATA AFTER
    # print(dataP)
    # print(dataAp)

    context = {
        'currentPR':currentPR         
    }
    return render(request, 'app/messagePR.html', context)

def selectPr(request):
    data = PRTable.objects.filter()
    pr = None

    for i in data:
        if i.pr_id in request.POST:
            pr = PRTable.objects.filter(pr_id=i.pr_id)
            products = PRITable.objects.filter(pr_id=i.pr_id)
            form_Date = pr.get().form_Date
            delv_Date = pr.get().delv_Date
            delv_Address = pr.get().delv_Address
            form_Stats = pr.get().form_Stats
            print(form_Stats)
    
    quo = pr.get().pr_id 

    context = {
        'pr': pr.get(), 'quo': quo, 
        'products': products, 
        'form_Date': form_Date,
        'delv_Date': delv_Date, 
        'delv_Address':delv_Address,
        'formStatus':form_Stats, 
    }
    return render(request, 'app/selectPR.html', context)


def arrejectPR(request):
    #DATA BEFORE
    # dataP = PurchaseOrder.objects.filter(poStatus__in=['Pending']).values()
    # dataAp = PurchaseOrder.objects.filter(poStatus__in=['Approved']).values()
    # print(dataP)
    # print(dataAp)

    #GET SELECTED PO
    currentPR = PRTable.objects.filter(pr_id=request.POST.get("purchaseRequisition"))
    print(currentPR)
    currentPR.update(form_Stats='Rejected')

    #DATA AFTER
    # print(dataP)
    # print(dataAp)

    context = {
        'currentPR':currentPR         
    }
    return render(request, 'app/messagePR.html', context)

##############################################################################################


def arviewQ(request):
    q_list = QTable.objects.all().only('quotation_ID', 'quotation_Date', 'quotation_Stats')

    context = {
        'title':'View Quotation',
        'year':datetime.now().year,
        'q_list': q_list,
    }
    return render(request, 'app/viewQ.html', context)

def larviewQ(request):
    q_list = QTable.objects.all().only('quotation_ID', 'quotation_Date', 'quotation_Stats')

    context = {
        'title':'View Purchase Requisition',
        'year':datetime.now().year,
        'q_list': q_list,
    }
    return render(request, 'app/lviewQ.html', context)

def arapproveQ(request):
    #DATA BEFORE
    # dataP = PurchaseOrder.objects.filter(poStatus__in=['Pending']).values()
    # dataAp = PurchaseOrder.objects.filter(poStatus__in=['Approved']).values()
    # print(dataP)
    # print(dataAp)

    #GET SELECTED PO
    currentQ = QTable.objects.filter(quotation_ID=request.POST.get("Quotation"))
    print(currentQ)
    currentQ.update(quotation_Stats='Approved')

    #DATA AFTER
    # print(dataP)
    # print(dataAp)

    context = {
        'currentQ':currentQ         
    }
    return render(request, 'app/messageQ.html', context)

def selectQ(request):
    data = QTable.objects.filter()
    q = None

    for i in data:
        if i.quotation_ID in request.POST:
            q = QTable.objects.filter(quotation_ID=i.quotation_ID)
            products = QITable.objects.filter(quotation_ID=i.quotation_ID)
            purchaser_Name = q.get().purchaser_Name
            vendor_Name = q.get().vendor_Name
            delv_Address = q.get().delv_Address
            quotation_Stats = q.get().quotation_Stats
            print(quotation_Stats)
    
    quo = q.get().quotation_ID 

    context = {
        'q': q.get(), 'quo': quo, 
        'products': products, 
        'purchaser_Name': purchaser_Name,
        'vendor_Name': vendor_Name, 
        'delv_Address':delv_Address,
        'quotation_Stats':quotation_Stats, 
    }
    return render(request, 'app/selectQ.html', context)


def arrejectQ(request):
    currentQ = QTable.objects.filter(quotation_ID=request.POST.get("Quotation"))
    print(currentQ)
    currentQ.update(quotation_Stats='Rejected')

    context = {
        'currentQ':currentQ         
    }
    return render(request, 'app/messageQ.html', context)