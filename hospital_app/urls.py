from django.contrib import admin
from django.urls import path, include
from hospital import settings
from hospital_app import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.user_login, name ='home'),
    path('index',views.index),
    path('signin',views.user_login, name ='signin'),
    path('create_user', views.create_user),
    path('signout', views.signout, name ='signout'),
    path('reg', views.reg, name='reg'),
    path('record',views.records, name='record'),
    path('update/<id>',views.update, name='update'),
    path('updated/<id>',views.updated,name='updated'),
    path('delete/<id>',views.delete,name='delete'),
    path('del2/<name>',views.del2),
    path('check_in',views.check_in,name='check_in'),
    path('reg_det',views.reg_det,name="reg_det"),
    path('check2',views.check2),
    path('check3',views.check3),
    path('logs',views.logs),
    path('appointment-page',views.appointment),
    path('staff',views.staff),
    path('newstaff',views.newstaff),
    path('staffrec',views.managestaff),
    path('appointments',views.appointments),
    path('vitals',views.vitals),
    path('select/<patient_id>',views.select),
    path('doctors',views.doctors),
    path('action1/<patient_id>/<patient_name>',views.action1),
    path('getdoc',views.getdoc),
    path('error',views.error),
    path('first',views.first_page),
    path('second_page',views.second_page),
    path('lab',views.lab),
    path('lab2/<id>',views.lab2),
    path('messages', views.message),
    path('message2/<subject>',views.message2),
    path('message',views.message_search),
    path('print/<id>',views.printc),
    path('qrcode',views.qr_gen),
    path('patient_details',views.p_details)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

