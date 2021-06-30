from PIL import Image
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
import manager

from task.models import WebsiteName, Menu, Sliders, Images, Footer


def manager_home(request):
   if 'userid' in request.session:
      try:
         website_name = WebsiteName.objects.get()
      except:
         website_name = ""
      return render(request,"manager/manager_home.html",{'website_name':website_name})
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")



def delete_menu_item(request,id):
   if 'userid' in request.session:
      data = Menu.objects.get(id=id)
      data.delete()
      messages.success(request, "Menu Item Deleted Succssfully")
      return redirect(add_menu)
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")

def update_menu_item_con(request):
   if 'userid' in request.session:
      if request.method =='POST':
         id  = request.POST['id']
         menu_name = request.POST['menuname']
         data = Menu.objects.get(id=id)
         data.name_of_nav_item = menu_name
         data.save()
         messages.success(request, "Menu Name Updated Succssfully")
         return redirect(add_menu)
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")


def update_menu_item(request,id):
   if 'userid' in request.session:
      data = Menu.objects.get(id=id)
      return render(request, "manager/update_menu_item.html",{'menu_data':data,'id':id})
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")



def add_menu(request):
   if 'userid' in request.session:
      data = WebsiteName.objects.all()
      if request.method=="POST":
         website=request.POST['website']
         name_of_nav_item=request.POST['name_of_nav_item']
         obj=WebsiteName.objects.get(name_of_website=website)
         website_id=obj.id
         if Menu.objects.filter(name_of_nav_item=name_of_nav_item,website_id=website_id).exists():
            messages.error(request,"Already Added")
            return redirect(add_menu)
         else:
            data = Menu(website=WebsiteName.objects.get(id=website_id),name_of_nav_item=name_of_nav_item,website_id=website_id)
            data.save()
            messages.success(request, "Add Successfullly")
            return redirect(add_menu)
      try:
         obj = WebsiteName.objects.all()
         website_id = obj[0].id
         menudata = Menu.objects.filter(website=WebsiteName.objects.get(id=website_id))
         website_name = obj[0].name_of_website
         return render(request, "manager/add_menu.html", {"datas": data,"menu":menudata,'website_name':website_name})
      except:
         pass
      return render(request,"manager/add_menu.html",{"datas":data})
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")




def add_sliders(request):
   if 'userid' in request.session:
      data=WebsiteName.objects.all()
      if request.method=="POST":
         website=request.POST['website']
         Slider1=request.FILES['Slider1']
         Slider2=request.FILES['Slider2']
         Slider3=request.FILES['Slider3']
         check1 = image_validator(request, Slider1, '1')
         check2 = image_validator(request, Slider2, '2')
         check3 = image_validator(request, Slider3, '3')
         if check1 == True:
            if check2 == True:
               if check3 == True:
                  obj=WebsiteName.objects.get(name_of_website=website)
                  website_id=obj.id
                  if Sliders.objects.filter(website_id=website_id).exists():
                     try:
                        pre_slider = Sliders.objects.get(website_id=website_id)
                     except:
                        pre_slider=""
                     return render(request,"manager/add_sliders.html",{"pre_sliders":pre_slider})
                  else:
                     data = Sliders(website=WebsiteName.objects.get(id=website_id),Slider1=Slider1,Slider2=Slider2,Slider3=Slider3,website_id=website_id)
                     data.save()
                     try:
                        pre_slider = Sliders.objects.get(website_id=website_id)
                     except:
                        pre_slider = ""
                     messages.success(request, "Add Successfullly")
                     return render(request, "manager/add_sliders.html", {"pre_sliders": pre_slider})

               else:
                  messages.error(request, "Tip : resize the image")
                  return redirect(add_sliders)
            else:
               messages.error(request, "Tip : resize the image")
               return redirect(add_sliders)
         else:
            messages.error(request, "Tip : resize the image")
            return redirect(add_sliders)
      else:

         try:
            pre_slider = Sliders.objects.get(website_id=data[0].id)
         except:
            pre_slider = ""
         return render(request, "manager/add_sliders.html", {"pre_sliders": pre_slider,"datas":data})

   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")



def add_images(request):
   if 'userid' in request.session:
      data = WebsiteName.objects.all()
      if request.method=="POST":
         website=request.POST['website']
         image1=request.FILES['image1']
         image2=request.FILES['image2']
         image3=request.FILES['image3']
         image4 = request.FILES['image4']
         image5 = request.FILES['image5']
         image6 = request.FILES['image6']
         obj=WebsiteName.objects.get(name_of_website=website)
         website_id=obj.id
         if Images.objects.filter(website_id=website_id).exists():
            try:
               pre_image = Images.objects.get(website_id=website_id)
            except:
               pre_image = ""
               web_name=WebsiteName.objects.all()
               webname=web_name[0].name_of_website
            return render(request,"manager/add_images.html",{"pre_image":pre_image,"datas":webname})
         else:
            data = Images(website=WebsiteName.objects.get(id=website_id),image1=image1,image2=image2,image3=image3,image4=image4,image5=image5,image6=image6)
            data.save()
            messages.success(request, "Add Successfullly")
            return redirect(add_images)
      else:
         try:
            obj = WebsiteName.objects.all()
            website_id = obj[0].id
            webname = obj[0].name_of_website
         except:
            webname = ""
         try:
            pre_image = Images.objects.get(website_id=website_id)
         except:
            pre_image = ""
         return render(request, "manager/add_images.html", {"pre_image": pre_image, "datas": webname})
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")



def update_slider(request,slider_value):
   if request.method=="POST":
      website=WebsiteName.objects.all()
      website_data=website[0].id
      slider_update = Sliders.objects.get(website_id=website_data)

      if slider_value=='1':
         slider_update.Slider1=request.FILES['Slider1']
         check1 = image_validator(request, slider_update.Slider1, '1')
         if check1 == True:
            slider_update.save()
            messages.success(request,"Update Slider 1 Image")
            return redirect(add_sliders)
         else:
            messages.error(request, "Tip : resize the image")
            return redirect(add_sliders)
      elif slider_value=='2':
         slider_update.Slider2 = request.FILES['Slider2']
         check2 = image_validator(request, slider_update.Slider2, '2')
         if check2 == True:
            slider_update.save()
            messages.success(request,"Update Slider 2 Image")
            return redirect(add_sliders)
         else:
            messages.error(request, "Tip : resize the image")
            return redirect(add_sliders)

      else:
         slider_update.Slider3 = request.FILES['Slider3']
         check3 = image_validator(request, slider_update.Slider3, '3')
         if check3 == True:
            slider_update.save()
            messages.success(request,"Update Slider 3 Image")
            return redirect(add_sliders)
         else:
            messages.error(request, "Tip : resize the image")
            return redirect(add_sliders)

   else:
      return redirect(add_sliders)



def update_image(request,image_value):
   if request.method=="POST":
      website=WebsiteName.objects.all()
      website_data=website[0].id
      image_update = Images.objects.get(website_id=website_data)

      if image_value=='1':
         image_update.image1=request.FILES['image1']
         image_update.save()
         messages.success(request,"Update body first Image")
         return redirect(add_images)
      elif image_value=='2':
         image_update.image2 = request.FILES['image2']
         image_update.save()
         messages.success(request,"Update Slider 2 Image")
         return redirect(add_images)
      elif image_value=='3':
         image_update.image3 = request.FILES['image3']
         image_update.save()
         messages.success(request,"Update Slider 3 Image")
         return redirect(add_images)
      elif image_value=='4':
         image_update.image4 = request.FILES['image4']
         image_update.save()
         messages.success(request,"Update Slider 4 Image")
         return redirect(add_images)
      elif image_value=='5':
         image_update.image5 = request.FILES['image5']
         image_update.save()
         messages.success(request,"Update Slider 5 Image")
         return redirect(add_images)
      else:
         image_update.image6 = request.FILES['image6']
         image_update.save()
         messages.success(request,"Update Slider 6 Image")
         return redirect(add_images)

   else:
      return redirect(add_sliders)




def add_footer(request):
   if 'userid' in request.session:
      data = WebsiteName.objects.all()
      if request.method == "POST":
         web_id = request.POST['website']
         web_name_get = WebsiteName.objects.get(id=web_id)
         contact_number = request.POST['contact_number']
         email_id = request.POST['email_id']
         address = request.POST['address']
         if Footer.objects.filter(website=web_id).exists():
            update_footer=Footer.objects.get(website=web_id)
            update_footer.contact_number=contact_number
            update_footer.email_id=email_id
            update_footer.address=address
            update_footer.save()
            messages.success(request, 'Footer Update Successfully !!')
            return redirect(add_footer)
         else:
            datass = Footer(website=web_name_get, contact_number=contact_number, email_id=email_id,
                                           address=address)
            datass.save()
            messages.success(request, 'Footer Added Successfully')
            return redirect(add_footer)
      else:
         try:
            footer_data = Footer.objects.get(website=data[0].id)
         except:
            footer_data = ""
         return render(request, 'manager/add_footer.html', {'datas': data,'footer_data':footer_data})
   else:
      return render(request,"manager_login.html")


def add_websitename(request):
   if 'userid' in request.session:
      if request.method=="POST":
         name_of_website=request.POST['name_of_website']
         try:
            if WebsiteName.objects.get().id:
               update_website_name = WebsiteName.objects.get(id = WebsiteName.objects.get().id)
               update_website_name.name_of_website=name_of_website
               update_website_name.save()
               messages.success(request,"Website Name Update successfully")
         except:
            data = WebsiteName(name_of_website=name_of_website)
            data.save()
            messages.success(request, "Add Successfullly")
         # try:
         #    update_website_name=WebsiteName.objects.get()
         #    update_website_name.name_of_website=name_of_website
         #    update_website_name.save()
         #    messages.success(request,"Website Name Update successfully")
         # except:
         #    data = WebsiteName(name_of_website=name_of_website)
         #    data.save()
         #    messages.success(request, "Add Successfullly")
         try:
            all_website = WebsiteName.objects.all()
            website_name=all_website[0].name_of_website
         except:
            website_name = ""
         return render(request, "manager/manager_home.html",{"website_name":website_name})
      else:

         try:
            all_website = WebsiteName.objects.all()
            website_name=all_website[0].name_of_website
         except:
            website_name = ""
         return render(request, "manager/manager_home.html",{'website_name':website_name})
   else:
      messages.error(request,"Session expire Please login Again")
      return render(request, "manager_login.html")



def logout(request):
   request.session.flush()
   messages.success(request,"Logout")
   return redirect(manager_home)


#validate function of image
def image_validator(request, image, i):
   my_image = Image.open(image)
   w, h = my_image.size
   if w < 1000 :
      msg = "Image " + i + " Width Should Be 1000px-1600px "
      messages.warning(request, msg)
      return redirect(add_sliders)
   elif w > 1600:
      msg = "Image " + i + " Width Should Be 1000px-1600px "
      messages.warning(request, msg)
      return redirect(add_sliders)
   elif h < 200:
      msg = "Image  " + i + " Height Should Be 200px - 300px"
      messages.warning(request, msg)
      return redirect(add_sliders)
   elif h > 250:
      msg = "Image " + i + " Height Should Be 200px - 300px"
      messages.warning(request, msg)
      return redirect(add_sliders)
   else:
      return True


