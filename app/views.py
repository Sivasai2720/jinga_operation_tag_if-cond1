from django.shortcuts import render

# Create your views here.
def conditions(request):
    
    #dict={'a':20} --- it is for if condition
    #dict={'a':20,'b':30}----it is for if-else condition
    #dict={'a':20,'b':20}----it is for if-elif-else condition
    dict={'a':20,'b':30,'c':40}#it is for Nested-if condition
    return render(request,'conditions.html',dict)