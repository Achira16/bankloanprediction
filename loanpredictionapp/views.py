from django.shortcuts import render
from django.conf import settings
import os
import pickle
from scipy import integrate
# Create your views here.

def mlbankloanprediction(request):
    d = True
    ans = None
    if request.method == 'POST':
        a = []
        print(type(a))
        print(request.POST)
        print(len(request.POST))
        for key,value in request.POST.items():
            print(type(value))
            a.append(value)
        del a[0]
        del a[10]
        for i in range(len(a)):
            if i<5:
                a[i] = int(a[i])
            elif i>7:
                a[i] = int(a[i])
        a[5] = float(a[5])
        a[6] = float(a[6])
        a[7] = float(a[7])
        print(a)
        pi = pickle.load(open('log_model.pkl','rb'))
        b = pi.predict([a])
        print(a)
        f={1:'YES', 0:'NO'}
        val =int(b)
        ans = f[val]
        d = False
    return render(request,'mlbankloanprediction.html',{'d':d,'ans':ans})