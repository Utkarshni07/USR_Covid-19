from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .models import CovidData


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'data.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already exist')
                return render(request, 'register.html')
            else:

                # save data in db
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'register.html')
        return redirect('/')
    else:
        return render(request, 'register.html')


def predict(request):
    if request.method == 'POST':
        DryCough = request.POST['DryCough']
        HighFever = request.POST['HighFever']
        SoreThroat = request.POST['SoreThroat']
        Difficulty_in_breathing = request.POST['Difficulty_in_breathing']

        df = pd.read_csv(r"C:\Users\theut\TechCiti\USR_Covid19\Patient\static\dataset\Covid-19.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        X_train = df[['Dry Cough', 'High Fever', 'Sore Throat', 'Difficulty in breathing']]

        Y_train = df[['Infected with Covid19']]
        X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.5)

        ran = RandomForestClassifier()
        a = ran.fit(X_train, Y_train)
        prediction = a.predict([[DryCough, HighFever, SoreThroat, Difficulty_in_breathing]])

        print("covid prediction: ", prediction)

        return render(request, 'predict.html',
                      {"data": prediction, 'DryCough': DryCough,
                       'HighFever': HighFever, 'SoreThroat': SoreThroat,
                       'Difficulty_in_breathing': Difficulty_in_breathing,
                       'prediction': prediction
                       })

    else:
        return render(request, 'predict.html')


def contact(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']

        return render(request, 'contact.html', {'username' : username})
    else:
        return render(request, 'contact.html')




