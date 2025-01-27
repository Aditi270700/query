from django.shortcuts import render
from .models import Student
# Create your views here.

# def aditi(request):
    # x=Student.objects.all()
    # print(x)

    #s=Student.objects.filter(stu_email="aditisaudagar17@gmail.com")
    #print(s)
    # v=Student.objects.values()
    # print(v)
    # s=Student.objects.values_list()
    # print(s)
    # s=Student.objects.exclude(stu_name='aditi')
    # print(s)
    # s=Student.objects.get(id=1)
    # print(s)
    # y=Student.objects.filter(stu_name="sanju raja")
    # print(y)
    # data={
    #     'data':y.values()
    # }
    # return render(request,'aditi.html',data)

    # first data get krne ke liye
'''
 def firstdata(request):
    data=Student.objects.first()
    print(data)
    print(data.id)
    print(data.stu_name)
    print(data.stu_email)
    print(data.stu_contact)
'''

def lastdata(request):
    data=Student.objects.last()
    print(data)
    print(data.id)
    print(data.stu_name)
    print(data.stu_email)
    print(data.stu_contact)

# def order(request):
#     data=Student.objects.order_by('stu_name')
#     print(data)

# def dec(request):
#     data=Student.objects.order_by('-stu_name')
#     print(data)


def all(request):
    data=Student.objects.order_by('-id')[0:2]
    print(data)
    