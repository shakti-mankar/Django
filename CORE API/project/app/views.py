
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
from django.http import JsonResponse,HttpResponse

from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def emp_list(req):
    if req.method=='POST':
        data = req.body
        # print(data)
        # print(type(data))
        p_data = json.loads(data)
        # print(p_data)
        # print(type(p_data))
        n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
        # print(n,e,c,a,sep=',')
        Employee.objects.create(name=n,email=e,contact=c,age=a)
        # p_data['msg']="data created successfully"
        # print(p_data)
        d={'msg':'object created successfully.......','data':p_data}
        j_data = json.dumps(d)
        # print(j_data)
        # print(type(j_data))
        return HttpResponse(j_data,content_type='application/json')

    emp_data = Employee.objects.all()   
    print(emp_data)
    p_data = list(emp_data.values())
    print(p_data)
    j_data = json.dumps(p_data)
    print(j_data)
    print(type(j_data))
    # return JsonResponse(j_data,safe=False) 
    return HttpResponse(j_data,content_type='application/json')

@csrf_exempt
def detail(req,pk):
    user = Employee.objects.filter(id=pk)
    if user:
        if req.method=='PUT':
            data = req.body
            p_data = json.loads(data)
            n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
            # if n and e and c and a:
            if 'name' in p_data and 'email' in p_data and 'contact' in p_data and 'age' in p_data:
                old_obj = Employee.objects.get(id=pk)
                old_obj.name = n
                old_obj.email = e 
                old_obj.contact = c
                old_obj.age = a
                old_obj.save()
                d={'msg':'Object updated successfully.........'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            else:
                d={'msg':'Some required filelds are missing'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')

        elif req.method=='PATCH':
            data = req.body
            p_data = json.loads(data)
            if p_data:
                # p_data = json.loads(data)
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('contact'),p_data.get('age')
                old_obj = Employee.objects.get(id=pk)
                if 'name' in p_data:
                    old_obj.name = n
                if 'email' in p_data:
                    old_obj.email = e
                if 'contact' in p_data:
                    old_obj.contact = c
                if 'age' in p_data:
                    old_obj.age = a
                old_obj.save()
                d={'msg':'Object partially updated successfully.........'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            else:
                d={'msg':'We need atleast one field to update but we don"t provide '}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')

        elif req.method=='DELETE':
            old_obj = Employee.objects.get(id=pk)
            old_obj.delete()
            d={'msg':'Object deleted successfully........!'}
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
        emp_data = Employee.objects.get(id=pk)
        p_data = model_to_dict(emp_data)
        j_data = json.dumps(p_data)

        return HttpResponse(j_data,content_type='application/json')
    else:
        d={'msg':'Given id is not present in our database'}
        j_data = json.dumps(d)
        return HttpResponse(j_data,content_type='application/json')