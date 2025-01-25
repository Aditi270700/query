from django.shortcuts import render
from .models import Student
# Create your views here.

def aditi(request):
    # x=Student.objects.all()
    # print(x)

    #s=Student.objects.filter(stu_email="aditisaudagar17@gmail.com")
    #print(s)
    # v=Student.objects.values()
    # print(v)
    # s=Student.objects.values_list()
    # print(s)
    s=Student.objects.exclude(stu_name='aditi')
    print(s)
    # y=Student.objects.filter(stu_name="sanju raja")
    # print(y)
    # data={
    #     'data':y.values()
    # }
    # return render(request,'aditi.html',data)

