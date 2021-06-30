from django.contrib import messages
from django.shortcuts import render, redirect

from manager.views import manager_home
from task.models import ManagerLogin, WebsiteName


def manager_login(request):
    if 'userid' in request.session:
        messages.success(request, "Already Logged In ")
        return redirect(manager_home)
    else:
        if request.method == "POST":
            userid = request.POST['userid']
            password = request.POST['password']
            if ManagerLogin.objects.filter(userid=userid, password=password).exists():
                request.session['userid'] = userid
                try:
                    all_website = WebsiteName.objects.all()
                    website_name = all_website[0].name_of_website
                except:
                    website_name = ""
                messages.success(request, "login Success")
                return render(request, "manager/manager_home.html", {"website_name": website_name})
            else:
                messages.error(request, "login failed")
                return render(request, "manager_login.html")
        else:
            return render(request, "manager_login.html")