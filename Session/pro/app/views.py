from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method=='POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('pass')
        # print(n,e,p)

        req.session['name'] = n
        req.session['email'] = e 
        req.session['pass'] = p

        return render(req,'landing.html')
    return render(req,'set.html')

def get(req):
    n = req.session['name']
    e = req.session['email']
    p = req.session['pass']
    # print(n,e,p)
    {'name':n,'email':e,'pass':p}

    return render(req,'landing.html')
    

def delete(req):
    req.session.flush()
    return render(req,'landing.html')



    
