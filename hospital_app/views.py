from django.contrib.auth import authenticate, login
from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.shortcuts import render, redirect
from  .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from hospital import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes , force_str
from hospital_app.models import register,patientlog,staffs,appoinment,vital,doc_sess,communication,lab_data
from .forms import MyForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from qrcode import *
import time


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.role == 'admin':
                username=user.get_username
                return redirect("/index")
            elif user.role =='doctor':
                username=user.get_username
                return redirect("/doctors")
            elif user.role =='vitals':
                username=user.get_username
                return redirect('/vitals')
            elif user.role =='reception':
                username=user.get_username
                return redirect('/index')
        else:
            messages.error(request,"invalid username or password")
            return render(request, 'hospital_app/signin.html')
    return render(request, 'hospital_app/signin.html')

@login_required
def create_user(request):
    role=request.user.role
    if role != 'admin':
        return render(request,'hospital_app/error.html')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('signin')
        else:
            form = UserRegistrationForm()
        return render(request, 'hospital_app/create_user.html', {'form': form})
@login_required
def index(request):
    return render(request,"hospital_app/index.html")

@login_required   
def reg(request):
    role=request.user.role
    if role == 'admin' or role == 'reception':
        if request.method == 'POST':
                reg=register()
                reg.id=request.POST.get('id')
                reg.firstname=request.POST.get('firstname')
                reg.middlename=request.POST.get('middlename')
                reg.surname=request.POST.get('surname')
                reg.reg_date=request.POST.get('date1')
                reg.gender=request.POST.get('gender')
                reg.dateofbirth=request.POST.get('date')
                reg.marital_status=request.POST.get('marital')
                reg.occupation=request.POST.get('occupation')
                reg.nationality=request.POST.get('nationality')
                reg.email=request.POST.get('email')
                reg.address=request.POST.get('address1')
                reg.phone=request.POST.get('phone')
                reg.state=request.POST.get('state')
                reg.emg_name=request.POST.get('emg_name')
                reg.emg_address=request.POST.get('address2')
                reg.emg_phone=request.POST.get('emg_phone')
                reg.emg_state=request.POST.get('state2')
                reg.payment=request.POST.get('payment')
                reg.age=request.POST.get('age')
                reg.identification=request.FILES.get('file')
                reg.emg_relationship=request.POST.get('emg_relationship')
                reg.past_surgeries=request.POST.get('surgries')
                reg.allergies=request.POST.get('allergies')
                reg.chronic_illness=request.POST.get('chronic_illness')
                reg.profile_photo=request.FILES.get('photo')
                reg.save()
                messages.success(request,"Registeration succesfull")
                
                
                subject="WELCOME TO HERITAGE!!"
                message = "Hello"+" "+reg.firstname+"\n"+"Welcome to HERITAGE hospital"+"\n"
                from_mail=settings.EMAIL_HOST_USER
                to_list =[reg.email]
                send_mail(subject,message,from_mail,to_list, fail_silently=True)
                return render(request, "hospital_app/reg.html") 
        else:
            return render(request,"hospital_app/reg.html")
    else:
        return render(request,'hospital_app/error.html')
        
      
@login_required  
def logs(request):
    if request.method == "POST":
        reg=patientlog()
        reg.patient_id=request.POST.get('id')
        reg.patient_name=request.POST.get('name')
        reg.date=request.POST.get('time')
        reg.activity=request.POST.get('check')
        reg.additional_info=request.POST.get('add')
        reg.save()
        messages.success(request,"Checked in")
    return render(request, "hospital_app/check_in.html")


@login_required
def signout(request):
        logout(request)
        return redirect('signin')
    
@login_required
def records(request):
    role=request.user.role
    if role == 'admin' or role == 'doctor' or role == 'pharamacist':
        records=register.objects.all()
        return render(request,"hospital_app/record.html",{'records':records})
    else:
        return render(request,'hospital_app/error.html')

@login_required
def update(request,id):
    update=register.objects.get(id=id)
    return render(request, "hospital_app/update.html",{"register":update})

@login_required
def check2(request):
    if request.method == 'POST':
            search = request.POST['search']
            records = register.objects.filter(id__icontains=search) | register.objects.filter(firstname__icontains=search)
            if records:
                context = {'records': records,"search":search}
                return render(request, 'hospital_app/record.html',context)
            else:
                return render(request, 'hospital_app/record.html', {'message': 'NO RECORD FOUND.'})
    else:
        return render(request, 'hospital_app/record.html')
    
@login_required    
def check3(request):
    if request.method == 'POST':
            search = request.POST['search']
            records = staffs.objects.filter(name__icontains=search)
            if records:
                context = {'records': records}
                return render(request, 'hospital_app/staffrec.html', context)
            else:
                return render(request, 'hospital_app/staffrec.html', {'message': 'NO RECORD FOUND.'})
    else:
        return render(request, 'hospital_app/staffrec.html')
    

@login_required   
def check_in(request):
    role=request.user.role
    if role == 'admin' or role == 'reception':
        if request.method == 'POST':
            search = request.POST['search']
            registrations = register.objects.filter(id__icontains=search) | register.objects.filter(firstname__icontains=search)|register.objects.filter(surname__icontains=search)
            if registrations:
                context = {'registrations': registrations}
                return render(request, 'hospital_app/check_in.html', context)
            else:
                return render(request, 'hospital_app/check_in.html', {'message': 'NO RECORD FOUND.'})
        else:
            return render(request, 'hospital_app/check_in.html')
    else:
        return render(request,'hospital_app/error.html')
        

@login_required
def updated(request,id):
    role=request.user.role
    if role == 'admin' or role == 'reception':
        first_name=request.POST['firstname']
        middle_name=request.POST['middlename']
        sur_name=request.POST['surname']
        date=request.POST['date']
        age=request.POST['age']
        gen_der=request.POST['gender']
        marital_stats=request.POST['marital']
        job=request.POST['occupation']
        country=request.POST['nationality']
        mail=request.POST['email']
        addrss=request.POST['address1']
        phoneno=request.POST['phone']
        st=request.POST['state']
        emgname=request.POST['emg_name']
        emgaddress=request.POST['address2']
        emgphone=request.POST['emg_phone']
        emgstate=request.POST['state2']
        pay=request.POST['payment']
        profile=request.FILES.get('photo')
        identification1=request.FILES.get('file')
        if identification1 is None:
            identification1='no file uploaded'
        if profile is None:
            profile ="no photo uploaded"
        relationship=request.POST['emg_relationship']
        surgery=request.POST['surgries']
        allergy=request.POST['allergies']
        illness=request.POST['chronic_illness']
        
        upd=register.objects.get(id=id)
        upd.firstname =first_name
        upd.middlename=middle_name   
        upd.surname =sur_name
        upd.dateofbirth=date
        upd.age=age
        upd.gender=gen_der
        upd.marital_status=marital_stats
        upd.occupation=job
        upd.nationality=country
        upd.email=mail
        upd.address=addrss
        upd.phone=phoneno
        upd.state=st
        upd.emg_name=emgname
        upd.emg_address=emgaddress
        upd.emg_phone=emgphone
        upd.emg_state=emgstate
        upd.payment=pay
        if identification1 is not None:
            upd.identification=identification1
        if profile is not None:
            upd.profile_photo=profile
        upd.emg_relationship=relationship
        upd.past_surgeries=surgery
        upd.allergies=allergy
        upd.chronic_illness=illness
        
        
        upd.save()
        messages.success(request, "Record updated")
        return render(request, "hospital_app/update.html")
    else:
        return render(request,'hospital_app/error.html')
        

@login_required
def delete(request, id):
    remove=register.objects.get(id=id)
    remove.delete()
    return render(request,"hospital_app/index.html")

@login_required
def del2(request, name):
    remove = staffs.objects.get(name=name)
    remove.delete()
    return render(request, "hospital_app/index.html")

@login_required
def reg_det(request):
    return render(request ,"hospital_app/reg_det.html",{request.user.username})

@login_required
def appointment(request):
    role=request.user.role
    if role == 'admin' or role == 'reception':
        if request.method=='POST':
            id = request.POST['pid']
            sess=request.POST['sess']
            date = request.POST['dateofapp']
            time = request.POST['time']
            add=request.POST['addinfo']
            if id =='' and sess =='' and date == '' and time == '' and add=='':
                    dept =request.POST['dept']
                    check=staffs.objects.filter(department__icontains=dept)
                    if check:
                        result={"check":check,"dept":dept}
                        return render(request,"hospital_app/appointment-page.html",result)
                    else:
                        result={"message":"no personnel available","dept":dept}
                        return render(request,"hospital_app/appointment-page.html",result)
            else:
                save = appoinment()
                save.patient_id=request.POST.get('pid')
                save.session=request.POST.get('sess')
                save.department= request.POST.get('dept')
                save.doctor=request.POST.get('doctor')
                save.date=request.POST.get('dateofapp')
                save.time=request.POST.get('time')
                save.add_info=request.POST.get('addinfo')
                save.save()
                messages.success(request, "APPIONTMENT BOOKED")
                return render (request , "hospital_app/appointment-page.html")
        else:
            return render (request , "hospital_app/appointment-page.html")
    else:
        return render(request,'hospital_app/error.html')
        

@login_required
def getdoc(request):
    role=request.user.role
    if role == 'admin'or role =='doctor':
        if request.method == 'POST':
            dept =request.POST['dept']
            check=staffs.objects.filter(department__icontains=dept)
            if check:
                result={"check":check,"dept":dept}
                return render(request,"hospital_app/appointment-page.html",result)
            else:
                result={"message":"no personnel available","dept":dept}
                return render(request,"hospital_app/appointment-page.html",result)
        else:
            return render(request,"hospital_app/appointment-page.html")
    else:
        return render(request,'hospital_app/error.html')
        

@login_required
def staff(request):
    role=request.user.role
    if role == 'admin':
        return render(request, "hospital_app/staff.html")
    else:
        return render(request,'hospital_app/error.html')
        

@login_required
def newstaff(request):
    role=request.user.role
    if role == 'admin':
        if request.method == "POST":
            save = staffs()
            save.name = request.POST.get('name')
            save.email =request.POST.get('email')
            save.phone = request.POST.get('phone')
            save.job = request.POST.get('job')
            save.department = request.POST.get('dept')
            save.date= request.POST.get('date')
            save.save()
            messages.success(request , "Registered successfully")
        return render(request, "hospital_app/newstaff.html")
    else:
        return render(request,'hospital_app/error.html')

@login_required
def managestaff(request):
    role=request.user.role
    if role == 'admin':
        records=staffs.objects.all()
        return render(request,"hospital_app/staffrec.html",{"records":records})
    else:
        return render(request,'hospital_app/error.html')

@login_required
def appointments(request):
    role=request.user.role
    if role == 'admin' or role == 'reception':
        records = appoinment.objects.all()
        return render(request , "hospital_app/appointments.html",{"records":records})
    else:
        return render(request,'hospital_app/error.html')

@login_required
def vitals(request):
    role=request.user.role
    if role == 'admin' or role =='vitals':
        import datetime
        from time import gmtime,strftime
        search = datetime.datetime.now().strftime("%y/%m/%d")
        patients = patientlog.objects.filter(date__icontains=search)
        if patients:
            context = {'patients': patients}
            return render(request, 'hospital_app/vitals.html', context)
        else:
            res={'search':search,'message': 'NO RECORD FOUND.'}
            return render(request, 'hospital_app/vitals.html',res)
    else:
        return render(request,'hospital_app/error.html')
    
    
@login_required
def select(request,patient_id):
    role=request.user.role
    if role == 'admin'or role =='vitals':
        if request.method=="POST":
            vitals = vital()
            vitals.date=request.POST.get('date')
            vitals.name=request.POST.get('name')
            vitals.blood_pressure=request.POST.get('bp')
            vitals.sugar_level=request.POST.get('sugar')
            vitals.height=request.POST.get('height')
            vitals.heart_rate=request.POST.get('heart')
            vitals.temperature=request.POST.get('temp')
            vitals.weight=request.POST.get('weight')
            vitals.respiration=request.POST.get('resp') 
            vitals.save()
            messages.success(request, "DATA COLLECTED")
        vitals=patientlog.objects.get(patient_id=patient_id)
        return render(request, "hospital_app/vitals.html",{"vitals":vitals})      
    else:
        return render(request,'hospital_app/error.html')


@login_required
def doctors(request):
    role=request.user.role
    if role == 'admin'or role =='doctor':
        import datetime
        from time import gmtime,strftime
        date =strftime("%y%m%d")
        name=request.user.username
        search = datetime.datetime.now().strftime("%y/%m/%d")
        patients = patientlog.objects.filter(date__icontains=search)
        check =appoinment.objects.filter(doctor__icontains=name)
        if patients:
            context = {'patients': patients,'get':check,}
            return render(request, 'hospital_app/doctor.html', context)
        else:
            message={"message":"No Data Found",'get':check,}
            return render(request,"hospital_app/doctor.html",message)
    else:
        return render(request,'hospital_app/error.html')

    



def action1(request,patient_id,patient_name):
    role=request.user.role
    import datetime
    search = datetime.datetime.now().strftime("%y/%m/%d")
    if role == 'admin'or role =='doctor':
        if request.method == 'POST':
            save1=doc_sess()
            save1.id=request.POST.get('id')
            save1.name=request.POST.get('name')
            save1.date=request.POST.get('date')
            save1.cheif_complaint=request.POST.get('complaint')
            save1.message=request.POST.get('message')
            save1.recipient=request.POST.get('recipient')
            save1.save()
            messages.success(request, "DONE")
        names = patient_name
        patient=register.objects.filter(id=patient_id)
        check =vital.objects.filter(date__icontains=search) & vital.objects.filter(name__icontains=names)
        if check:
            result = {'check':check,"data":patient}
            return render(request,'hospital_app/action1.html',result)
        else:
            err={'message':"no data","data":patient}
            return render(request,'hospital_app/action1.html',err)
    else:
        return render(request,'hospital_app/error.html')

def error(request):
    return render(request,'hospital_app/error.html')




def first_page(request):
    form = MyForm()
    return render(request, 'hospital_app/first.html', {'form': form})

def second_page(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            field1_data = form.cleaned_data['field1']
            field2_data = form.cleaned_data['field2']
            return render(request, 'hospital_app/second_page.html', {'field1_data': field1_data, 'field2_data': field2_data})
    else:
        form = MyForm()
    return render(request, 'hospital_app/second_page.html', {'form': form})

def lab(request):
    role=request.user.role
    if role == 'admin'or role =='laboratory':
        check =doc_sess.objects.filter(recipient__icontains='laboratory')
        if check:
            result={'check':check}
            return render(request,"hospital_app/lab.html",result)
        else:
            message = {'message':"no patients"}
            return render(request,"hospital_app/lab.html",message)
    else:
        return render(request,'hospital_app/error.html')
        
def lab2(request,id):
    import datetime
    time= datetime.datetime.now().strftime("(%H:%M:%S)%d/%m/%y")
    if request.method == 'POST':
        
        rec=lab_data()
        rec.id= request.POST.get('id')
        rec.name = request.POST.get('name')
        rec.report=request.POST.get('report')
        rec.reciever=request.POST.get('recieve')
        rec.file = request.FILES['document']
        rec.time=time
        rec.save()
        
        mes=communication()
        mes.sender=request.user.username
        mes.receiver=request.POST.get('recieve')
        mes.subject=request.POST.get('subject')
        mes.message=request.POST.get('report')
        mes.file=request.FILES['document']
        mes.time = time
        mes.save()
        
        
    result=register.objects.filter(id=id)
    records=staffs.objects.filter(job__icontains='Doctor')
    if result:
        display ={'patient':result,'records':records}
        return render(request,"hospital_app/lab2.html",display)
    else:
        return render(request ,"hospital_app/lab2.html")
    
def message(request):
    import datetime
    time= datetime.datetime.now().strftime("(%H:%M:%S)%d/%m/%y")
    check =communication.objects.filter(receiver__icontains=request.user.username)
    if request.method=="POST":
        mes=communication()
        mes.sender=request.user.username
        mes.subject=request.POST.get('subject')
        mes.receiver=request.POST.get('receiver')
        mes.message=request.POST.get('message')
        mes.file=request.FILES['document']
        mes.time = time
        mes.save()
        messages.success(request, "DATA COLLECTED")
        return render(request , "hospital_app/message2.html")
    if check:
        display={'check':check}
        return render(request , "hospital_app/messages.html",display)
    else:
        message = communication.objects.all()
        return render (request,"hospital_app/messages.html",{"message":message})
    
def message2(request,subject):
        import datetime
        time= datetime.datetime.now().strftime("(%H:%M:%S)%d/%m/%y")
        
        role = request.user.role
        if role == 'doctor':
            get =communication.objects.filter(receiver__icontains=request.user.username)
            message=communication.objects.filter(subject=subject)
            display={'message':message,"check":get}
            if request.method=="POST":
                mes=communication()
                mes.sender=request.user.username
                mes.subject=request.POST.get('subject')
                mes.receiver=request.POST.get('receiver')
                mes.message=request.POST.get('message')
                file=request.FILES.get('document')
                if file is None:
                    mes.file=''
                else:
                    mes.file=request.FILES.get('document')
                mes.time = time
                mes.save()
                messages.success(request, "DATA COLLECTED")
                return render(request , "hospital_app/message2.html")
            return render(request , "hospital_app/message2.html",display)     
        else:
            return render(request,'hospital_app/error.html')
        
def message_search(request):
    if request.method == 'POST':
            search = request.POST['search']
            check = communication.objects.filter(sender__icontains=search)
            if records:
                context = {'check':check,"search":search}
                return render(request, 'hospital_app/messages.html',context)
            else:
                return render(request, 'hospital_app/messages.html', {'message': 'NO RECORD FOUND.'})
    else:
        return render(request, 'hospital_app/messages.html')

def printc(request,id):
    pr = register.objects.get(id=id)
    return render(request ,"hospital_app/print.html",{"print":pr})


def qr_gen(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        return render(request,'hospital_app/qrcode.html', {'img_name': img_name})
    return render(request,'hospital_app/qrcode.html')

def p_details(request):
    search = register.objects.filter(id__icontains=id)
    if search:
        return render(request , "patient_details.html",{"details":search})
    else:
        return render(request ,"hospital_app/patient_details",{"message":"SOMETHING WENT WRONG"})