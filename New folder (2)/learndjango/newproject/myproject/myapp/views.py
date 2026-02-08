from django.shortcuts import render,redirect
from myapp.models import dep,emp,query
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.views.decorators.cache import never_cache
# /ad/de/d
# Create your views here.
@never_cache
def landing(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'landing.html', {'data': a_data})
        else:
            return render(req,'landing.html')

@never_cache
def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
                req.session['admin_e'] = e
                req.session['admin_p'] = p
                req.session['admin_n'] = 'admin'
                return redirect('admindpanel')
        else:
            user = emp.objects.filter(email=e)
            if user:
                user=emp.objects.get(email=e)         
                if e==user.email and p==user.mobile:
                    # req.session['emp_e'] = e
                    # req.session['emp_p'] = p
                    # req.session['emp_n'] = 'emp'
                    req.session['emp_id']=user.id
                    return redirect('emppanel')
                else:
                    x={'g':"wrong passord or username"}
                    return render(req,'login.html',{'data':x})
            else:
                x={'g':"Invalid Email"}
                return render(req,'login.html',{'data':x})
    return render(req, 'login.html')

@never_cache
def admindpanel(req):
    # Admin Session Check
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        deptdata=dep.objects.all()
        all_emp=emp.objects.all()
        return render(req, 'admindpanel.html', {'data': a_data,'deptdata':deptdata,'all_emp':all_emp})   
    else:
        return redirect('login')
    

@never_cache
def logout(req):
    if 'admin_e' in req.session or 'emp_id' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')
   
@never_cache
def about(req):
       if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req,'about.html', {'data': a_data})
       else:
            return render(req,'about.html')
@never_cache
def services(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
         a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
         return render(req,'services.html', {'data': a_data})
        else:
            return render(req,'services.html')


@never_cache
def sin(req):
          if 'admin_e' in req.session and 'admin_p' in req.session:
           a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
           return render(req,'sin.html', {'data': a_data})
          else:
               return render(req,'sin.html')
 
@never_cache
def free(req):
            if 'admin_e' in req.session and 'admin_p' in req.session:
             a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        } 
             return render(req,'free.html', {'data': a_data})
            else:
                 return render(req,'free.html')
@never_cache
def xbox(req):
         if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'xbox.html', {'data': a_data})
         else:
              return render(req,'xbox.html')

# form wala
@never_cache
def save_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data={
                'email': req.session['admin_e'],
                'password': req.session['admin_p'],
                'name': req.session['admin_n']
            } 
        if req.method=='POST':
            dname=req.POST.get('dept_name')
            dcode=req.POST.get('dept_code')
            dhead=req.POST.get('dept_head')
            dbudget=req.POST.get('dept_budget')
            ddesc=req.POST.get('dept_desc')
            deptdata=dep.objects.filter(dept_name=dname)
            if not deptdata:
                dep.objects.create(dept_name=dname,dept_code=dcode,dept_head=dhead,dept_budget=dbudget,dept_desc=ddesc)
                messages.success(req,"department added")
                return render(req,'admindpanel.html',{'a_data':a_data,'add_department':True})
            else:
                messages.error(req,"department as already present")
                return render(req,'admindpanel.html',{'a_data':a_data,'add_department':True})
                
    else:
     return redirect('login')

@never_cache
def addemp(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
            a_data = {
                    'email': req.session['admin_e'],
                    'password': req.session['admin_p'],
                    'name': req.session['admin_n']
                } 
            if req.method=='POST':
                fname=req.POST.get('fname')
                lname=req.POST.get('lname')
                email=req.POST.get('email')
                img=req.FILES.get('img')
                adhaar=req.FILES.get('adhaar')
                code=req.POST.get('code')
                mobile=req.POST.get('mobile')
                DOB=req.POST.get('DOB')
                gender=req.POST.get('gender')
                edu=req.POST.getlist('edu')
                dept=req.POST.get('dept')
                user=emp.objects.filter(code=code)
                al=dep.objects.all()
                if user :
                    deptdata=dep.objects.all()
                    messages.error(req,"these employee id is alreay ocuur")
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
                if not al.exists():
                    deptdata=dep.objects.all()
                    messages.error(req,"please add depertment first")
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
                else:
                    emp.objects.create(fname=fname,lname=lname,email=email,img=img,adhaar=adhaar,code=code,mobile=mobile,DOB=DOB,gender=gender,edu=edu,dept=dept)
                    deptdata=dep.objects.all()
                    messages.success(req,"added employee")
                    send_mail(
                    "testing from django",
                    f'hello {email} your added as a employee at microsoft your password was {mobile}',
                    "jattfact@gmail.com",
                    [email],
                    fail_silently=False,
                    )
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
        else:
            return redirect('login')


# buttons wale
@never_cache
def add_anlytics(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,'add_anlytics':True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def  add_setting(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,'add_setting':True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def  add_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
         
          deptdata=dep.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def  all_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          all_emp = emp.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"all_employees":True,'all_emp':all_emp})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def  remove_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        } 
          empl=emp.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"remove_employees":True,'empl':empl})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def removeemp(req,pk):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          em=emp.objects.filter(id=pk)
        #   q=query.objects.filter(id=pk)
        #   q.delete()
          em.delete()
          empl=emp.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"remove_employees":True,'empl':empl})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

@never_cache
def  remove_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          depdata=dep.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"remove_department":True,'deptdata':depdata})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
@never_cache
def removedept(req,pk):
      if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        deprt=dep.objects.get(id=pk)
        empindept=emp.objects.filter(dept=deprt.dept_name)
        if empindept:
            deptdata=dep.objects.all()
            messages.error(req,"in this deprtment employee is working")
            return render(req,'admindpanel.html', {'data': a_data,'remove_department':True,'deptdata':deptdata})
        else:
            deprt.delete()
            deptdata=dep.objects.all()
            messages.success(req,"department removed")
            return render(req,'admindpanel.html', {'data': a_data,'remove_department':True,'deptdata':deptdata})

      else:
          return redirect("login")


        
@never_cache
def add_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"add_department":'add_department'})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    
 
@never_cache
def all_department(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          deptdata=dep.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"all_department":True,'deptdata':deptdata})
    
        else:
         msg={'msg':'login first'}
         return render(req,"login.html",{'msg':msg})
@never_cache
def all_quries(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          qdata=query.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,'qdata':qdata,"all_quries":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    
@never_cache
def payroll(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"payroll":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    


    


     



          
          

#   employeeee

@never_cache
def emppanel(req):
    if 'emp_id' in req.session:
     emp_id=req.session.get('emp_id')
     emp_data=emp.objects.get(id=emp_id)
     data={
        'fname':emp_data.fname,
        'email':emp_data.email,
        'DOB':emp_data.DOB,
        'gender':emp_data.gender,
        'mobile':emp_data.mobile,
    }
     return render(req,'emppanel.html',{'data':data})
    else:
        return redirect('login')
    
@never_cache
def forget(req):
    return render(req,"forget.html")


@never_cache
def forgot_password(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        ed=emp.objects.filter(email=email)
        if ed:
          em=emp.objects.get(email=email)
          if str(em.email)==str(email):
              otp_code=random.randint(111111,999999)
              req.session['email']=email
              req.session['otp']=otp_code
              send_mail(
                  subject="Forget password",
                  message=f'User Email OTP: {otp_code}',
                  from_email="jattfact@gmail.com",  
                  recipient_list=[email],
                  fail_silently=False,
               )
              req.session.set_expiry(60)   # 1 minute
              return redirect('otp')
        else:
          messages.error(req,"thse email is not valid in databases")
          return redirect('forget')

    return render(req, 'forget.html')


@never_cache
def otp(req):
     return render(req,'otp.html')



@never_cache
def newpassword(req):
    if req.method == 'POST':
        user_otp = req.POST.get('otp')
        store_otp = req.session.get('otp')

        if str(user_otp) == str(store_otp):
            email = req.session.get('email')
            return render(req, 'confirm.html',{'email':email})
        
        else:
            messages.error(req,"invalid otp")
            return render(req,'otp.html')
    email = req.session.get('email')
    return render(req,'confirm.html',{'email':email})

@never_cache
def confirm(req):
    return render(req,'confirm.html')


@never_cache
def newpass(req):
    if req.method=='POST':
        e = req.POST.get('email')
        p = req.POST.get('new_password')
        cp = req.POST.get('confirm_password')
        if p == cp:
            userdata = emp.objects.get(email=e)
            userdata.mobile=p
            userdata.save()
            messages.info(req,'Password reset successfully')
            req.session.pop('otp')
            return redirect('landing')
        else:
            messages.info(req,'Password and conform password not matched')
            return render(req,'confirm.html',{'email':e})
        
@never_cache
def resend_otp(req):
    otp_code=random.randint(111111,999999)
    req.session.pop('otp')
    req.session['otp']=otp_code
    email=req.session.get('email')
    send_mail(
        subject="Forget password",
        message=f'User Email OTP: {otp_code}',
        from_email="jattfact@gmail.com",  
        recipient_list=[email],
        fail_silently=False,
               )
    req.session.set_expiry(60)   # 1 minute
    return redirect('otp')



# qurry
@never_cache
def apply_query(req):
    if 'emp_id' in req.session:
       emp_id=req.session.get('emp_id')
       emp_data=emp.objects.get(id=emp_id)
       data={
        'fname':emp_data.fname,
        'email':emp_data.email,
        'DOB':emp_data.DOB,
        'gender':emp_data.gender,
       'mobile':emp_data.mobile,
      }
       depd=dep.objects.all()   
       print(depd)
       return render(req,'emppanel.html',{'apply_query':True,'data':data,'depd':depd})


@never_cache
def profile(req):
    if 'emp_id' in req.session:
       emp_id=req.session.get('emp_id')
       emp_data=emp.objects.get(id=emp_id)
       data={
        'fname':emp_data.fname,
        'email':emp_data.email,
        'DOB':emp_data.DOB,
        'gender':emp_data.gender,
       'mobile':emp_data.mobile,
      }
       depd=dep.objects.all()   
       print(depd)
       return render(req,'emppanel.html',{'profile':True,'data':data,'depd':depd})
    else:
        return redirect('login')




@never_cache
def submit_query(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        message=req.POST.get('message')
        dept=req.POST.get('dept')
        query.objects.create(Name=name,Email=email,Query=message,department=dept)
        messages.success(req,'query raised')
        if 'emp_id' in req.session:
            emp_id=req.session.get('emp_id')
            emp_data=emp.objects.get(id=emp_id)
            data={
            'fname':emp_data.fname,
            'email':emp_data.email,
            'DOB':emp_data.DOB,
            'gender':emp_data.gender,
            'mobile':emp_data.mobile,
         }
        depd=dep.objects.all()  
        return render(req,'emppanel.html',{'data':data,'depd':depd,'apply_query':True})
    return render(req,'emppanel.html',{'data':data,'depd':depd,'apply_query':True})

    
@never_cache
def show_query(req):
     if 'emp_id' in req.session:
       emp_id=req.session.get('emp_id')
       emp_data=emp.objects.get(id=emp_id)
       data={
        'fname':emp_data.fname,
        'email':emp_data.email,
        'DOB':emp_data.DOB,
        'gender':emp_data.gender,
       'mobile':emp_data.mobile,
      }
       empe=emp_data.email
       qdata=query.objects.filter(Email=empe)
    #    return render(req,'emppanel.html',{'data':data,'show_query':qdata})
       return render(req,'emppanel.html',{'data':data,'show_query':True,'qdata':qdata})

@never_cache
def a_reply(req,pk):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        qdata=query.objects.get(id=pk)
        return render(req, 'admindpanel.html', {'data': a_data,'qdata':qdata,'a_reply':True})   
    else:
        return redirect('login')
    

@never_cache
def reply_query(req,pk):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        if req.method=='POST':
            name=req.POST.get('name')
            email=req.POST.get('email')
            Query=req.POST.get('query')
            department=req.POST.get('department')
            admin_reply=req.POST.get('admin_reply')
            qdata=query.objects.get(id=pk)
            if admin_reply:
                old_data=query.objects.get(id=pk)
                old_data.admin_rep=admin_reply
                old_data.status='done'
                old_data.save()
            # return redirect('admindpanel')
            messages.success(req,"reply successfully")
            return redirect('all_quries')   

                
    else:
        return redirect('login')



@never_cache
def pending_query(req):
     if 'emp_id' in req.session:
        emp_id=req.session.get('emp_id')
        emp_data=emp.objects.get(id=emp_id)
        data={
         'fname':emp_data.fname,
         'email':emp_data.email,
         'DOB':emp_data.DOB,
         'gender':emp_data.gender,
        'mobile':emp_data.mobile,
        }
        empe=emp_data.email
        qdata=query.objects.filter(Email=empe,status="pending")
       
        return render(req,'emppanel.html',{'data':data,'pending_query':True,'qdata':qdata})


@never_cache
def done_query(req):
     if 'emp_id' in req.session:
        emp_id=req.session.get('emp_id')
        emp_data=emp.objects.get(id=emp_id)
        data={
         'fname':emp_data.fname,
         'email':emp_data.email,
         'DOB':emp_data.DOB,
         'gender':emp_data.gender,
        'mobile':emp_data.mobile,
        }
        empe=emp_data.email
        qdata=query.objects.filter(Email=empe,status="done")
       
        return render(req,'emppanel.html',{'data':data,'done_query':True,'qdata':qdata})

@never_cache
def Edit(req,pk):
      if 'emp_id' in req.session:
        emp_id=req.session.get('emp_id')
        emp_data=emp.objects.get(id=emp_id)
        data={
         'fname':emp_data.fname,
         'email':emp_data.email,
         'DOB':emp_data.DOB,
         'gender':emp_data.gender,
        'mobile':emp_data.mobile,
        }
        q=query.objects.get(id=pk)
        return render(req,"emppanel.html",{'data':data,'Edit':q})

@never_cache
def Edit_query(req,pk):
    if 'emp_id' in req.session:
        emp_id=req.session.get('emp_id')
        emp_data=emp.objects.get(id=emp_id)
        data={
         'fname':emp_data.fname,
         'email':emp_data.email,
         'DOB':emp_data.DOB,
         'gender':emp_data.gender,
        'mobile':emp_data.mobile,
        }
        if req.method=='POST':
         message=req.POST.get('message')
         empq=query.objects.get(id=pk)
         empq.Query=message
         empq.save()
         messages.success(req,"Edit successfully")
         return redirect('pending_query')
        
    
@never_cache    
def Del(req,pk):
      if 'emp_id' in req.session:
         emp_id=req.session.get('emp_id')
         emp_data=emp.objects.get(id=emp_id)
         data={
          'fname':emp_data.fname,
          'email':emp_data.email,
          'DOB':emp_data.DOB,
          'gender':emp_data.gender,
         'mobile':emp_data.mobile,
         }
         qd=query.objects.get(id=pk)
         qd.delete()
         return redirect('pending_query')
      else:
        return redirect('login')


    
        


