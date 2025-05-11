from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from app.models import PRTable, PRITable
# Create your views here.

@login_required
def viewPR(request):

    list = PRTable.objects.filter(emp_id = request.user.username).only('pr_id', 'form_Date', 'form_Stats')

    return render(request, 'viewPR/viewPR.html', {'list': list})

def viewPRdetails(request):

    data = PRTable.objects.all()
    ilist = None
    pr = None


    for i in data:
        if i.pr_id in request.POST:
            pr = PRTable.objects.filter(pr_id=i.pr_id)
            ilist = PRITable.objects.filter(pr_id=i.pr_id)

    print(pr)
    print(ilist)

    return render(request, 'viewPR/viewPRdetails.html', {'pr': pr, 'ilist': ilist})