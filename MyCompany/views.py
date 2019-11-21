from django.shortcuts import render, render_to_response
from MyCompany.models import Buser, Jikwon, Gogek
from django.db.models.aggregates import Count

# Create your views here.
def MainFunc(request):
    return render_to_response('main.html')

def DeptListFunc(request):
    deptData = Buser.objects.all().order_by('-buser_no')
    return render(request, 'deptList.html', {"datas":deptData})

def EmpListFunc(request):
    #print(request.GET.get('no'))
    no = int(request.GET.get('no'))
    empData = Jikwon.objects.filter(buser_num = no).order_by('-jikwon_no')
    customerData = Gogek.objects.values('gogek_damsano').annotate(
        count = Count('gogek_no')
    ).values('gogek_damsano', 'count')
    
    datas = []
    for eData in empData:
        cnt = 0
        for cData in customerData:
            if eData.jikwon_no == cData["gogek_damsano"]:
                cnt = cData["count"]
        newEmpData = {}
        newEmpData["jikwon_no"] = eData.jikwon_no
        newEmpData["jikwon_name"] = eData.jikwon_name
        newEmpData["jikwon_jik"] = eData.jikwon_jik
        newEmpData["count"] = cnt
        datas.append(newEmpData)
    
    print(datas)
    
    return render(request, 'empList.html', {"datas":datas})

def CustListFunc(request):
    no = int(request.GET.get('no'))
    customerData = Gogek.objects.filter(gogek_damsano = no).order_by('-gogek_no')
    
    datas = []
    for cData in customerData:
        newEmpData = {}
        newEmpData["buser_no"] = cData.gogek_no
        newEmpData["buser_name"] = cData.gogek_name
        
        temp = cData.gogek_jumin.split("-")[1]
        gen = ""
        
        if int(temp[0]) == 1 or int(temp[0]) == 3:
            gen = "남"
        elif int(temp[0]) == 2 or int(temp[0]) == 4:
            gen = "여"
        
        newEmpData["buser_gen"] = gen
        newEmpData["buser_tel"] = cData.gogek_tel
        datas.append(newEmpData)
    
    return render(request, 'customerList.html', {"datas":datas})