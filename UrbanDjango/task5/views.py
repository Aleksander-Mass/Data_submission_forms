

# Create your views here.

from django.shortcuts import render

users = ["existing_user1", "existing_user2"]  # Пример списка существующих пользователей



def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in users:
            info['error'] = "Пользователь уже существует"
        else:
            return render(request, 'fifth_task/success.html', {"username": username})

    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request):
    from .forms import UserRegister
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
            else:
                return render(request, 'fifth_task/success.html', {"username": username})
        else:
            info['form'] = form
    else:
        info['form'] = UserRegister()

    return render(request, 'fifth_task/registration_page.html', info)
