
# import json
# # Create your views here.


# def landing(req):
#     return render(req,'landing.html')


# # p_data = {
# #     'active1' : True,
# #     'active2' : False,
# #     'active3' : None,
    
# # }

# # j_data = json.dumps(p_data)
# # print(j_data)
# # print(type(j_data))


# j_data = '{"active1":true, "active2":false,"active3":null}'

# p_data = json.loads(j_data)
# print(p_data)
# print(type(p_data))


from django.shortcuts import render
from django.http import JsonResponse

from .models import Employee
import json


def emp_list(req):
    emp_data = Employee.objects.all()
    print(emp_data)
    p_data = list(emp_data.values())
    print(p_data)
    j_data = json.dumps(p_data)
    print(j_data)
    print(type(j_data))
    return JsonResponse(j_data,safe=False)




def detail(req,pk):
    pass