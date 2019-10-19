from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Dishes, Stores, Orders, SubmittedOrders, Roles, User
from .forms import UserForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    current_user = request.user
    if current_user.is_authenticated and current_user.roles.role == 'M':
        return render(request, 'menuserver/main.html', {"manager": 1})
    if current_user.is_authenticated and current_user.roles.role == 'E':
        return render(request, 'menuserver/main.html', {"employee": 1})
    return render(request, 'menuserver/main.html')

def menu(request):
    if request.method == 'GET':
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/menu.html', {'menu' : menu})

@login_required
def menu_management(request):
    if request.method == 'GET':
        current_user = request.user
        if current_user.is_authenticated and current_user.roles.role == 'M':
            menu = Dishes.objects.order_by('name')
            return render(request, 'menuserver/menu_management.html', {'menu' : menu})
        else:
            return render(request, 'menuserver/error.html', {})
    if request.method == 'POST':
        if "change-dish" in request.POST and "dish-id" in request.POST:
            dish_id = request.POST["dish-id"]
            if Dishes.objects.filter(id=dish_id).count() == 1:
                dish = Dishes.objects.get(id=dish_id)
                context = {'name' : dish.name, 'categary' : dish.categary, 'price' : dish.price, 'id' : dish.id}
                if request.POST["change-dish"] == "edit":
                    return render(request, 'menuserver/dish.html', context)
                if request.POST["change-dish"] == "delete":
                    dish.delete()
                    menu = Dishes.objects.order_by('name')
                    return render(request, 'menuserver/menu_management.html', {'menu' : menu})
            menu = Dishes.objects.order_by('name')
            return render(request, 'menuserver/menu_management.html', {'menu' : menu})
        if "submit-dish" in request.POST:
            if request.POST["submit-dish"] == "edit-dish":
                if 'dish-id' in request.POST and 'category' in request.POST and 'dish-name' in request.POST and 'dish-price' in request.POST and 'photo-file' in request.FILES:
                    if Dishes.objects.filter(id=request.POST['dish-id']).count() == 1:
                        dish = Dishes.objects.get(id=request.POST['dish-id'])
                        dish.categary = request.POST["category"]
                        dish.name = request.POST["dish-name"]
                        dish.price = request.POST["dish-price"]
                        photo = request.FILES['photo-file']
                        fs = FileSystemStorage()
                        photoname = fs.save(photo.name, photo)
                        photo_url = fs.url(photoname)
                        dish.photo_url = photo_url
                        dish.save()
            if request.POST["submit-dish"] == "new-dish":
                if "category" in request.POST and "dish-name" in request.POST and "dish-price" in request.POST and 'photo-file' in request.FILES:
                    new_dish = Dishes(categary=request.POST["category"], name=request.POST["dish-name"], price=request.POST["dish-price"])
                    photo = request.FILES['photo-file']
                    fs = FileSystemStorage()
                    photoname = fs.save(photo.name, photo)
                    photo_url = fs.url(photoname)
                    new_dish.photo_url = photo_url
                    new_dish.save()
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/menu_management.html', {'menu' : menu})

def dish(request):
    if request.method == 'GET':
        return render(request, 'menuserver/dish.html', {})
    if request.method == 'POST' and 'submit-dish' in request.POST:
        if request.POST["submit-dish"] == "edit-dish":
            if 'dish-id' in request.POST and 'category' in request.POST and 'dish-name' in request.POST and 'dish-price' in request.POST and 'photo-file' in request.FILES:
                if Dishes.objects.filter(id=request.POST['dish-id']).count() == 1:
                    dish = Dishes.objects.get(id=request.POST['dish-id'])
                    dish.categary = request.POST["category"]
                    dish.name = request.POST["dish-name"]
                    dish.price = request.POST["dish-price"]
                    photo = request.FILES['photo-file']
                    fs = FileSystemStorage()
                    photoname = fs.save(photo.name, photo)
                    photo_url = fs.url(photoname)
                    dish.photo_url = photo_url
                    dish.save()
        if request.POST["submit-dish"] == "new-dish":
            if "category" in request.POST and "dish-name" in request.POST and "dish-price" in request.POST and 'photo-file' in request.FILES:
                new_dish = Dishes(categary=request.POST["category"], name=request.POST["dish-name"], price=request.POST["dish-price"])
                photo = request.FILES['photo-file']
                fs = FileSystemStorage()
                photoname = fs.save(photo.name, photo)
                photo_url = fs.url(photoname)
                new_dish.photo_url = photo_url
                new_dish.save()
    menu = Dishes.objects.order_by('name')
    return render(request, 'menuserver/menu_management.html', {'menu' : menu})

@login_required
def store_manager_employee(request):
    if request.method == 'GET':
        current_user = request.user
        if current_user.is_authenticated and (current_user.roles.role == 'M'):
            stores = Stores.objects.order_by('store_id')
            managers = Roles.objects.filter(role='M')
            employees = Roles.objects.filter(role='E')

            return render(request, 'menuserver/store_manager_employee.html',
                          {'stores' : stores, 'managers' : managers, 'employees' : employees})
        else:
            return render(request, 'menuserver/error.html', {})
    if request.method == 'POST':
        if "change-store" in request.POST and "change-store-id" in request.POST:
            store_id = request.POST["change-store-id"]
            store = Stores.objects.get(store_id=store_id)
            managers = Roles.objects.filter(role='M')
            employees = Roles.objects.filter(role='E')
            context = {'store_id' : store_id, 'name' : store.name,
                       'address' : store.address, 'managers' : managers, 'employees' : employees}
            if request.POST['change-store'] == 'edit':
                return render(request, 'menuserver/store.html', context)
            if request.POST['change-store'] == 'delete':
                managers = Roles.objects.filter(role='M')
                for m in managers:
                    if store in m.stores.all():
                        m.stores.remove(store)
                submitted_orders = SubmittedOrders.objects.all()
                for so in submitted_orders:
                    if so.store.store_id == store.store_id:
                        so.delete()
                store.delete()
                stores = Stores.objects.order_by('store_id')
                managers = Roles.objects.filter(role='M')
                employees = Roles.objects.filter(role='E')
                return render(request, 'menuserver/store_manager_employee.html',
                             {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "change-manager" in request.POST and "change-manager-id" in request.POST:
            id = request.POST["change-manager-id"]
            manager = Roles.objects.get(id=id)
            if manager:
                stores = manager.stores.all()
                all_stores = Stores.objects.order_by('store_id')
                context = {'manager_user' : manager.user, 'stores' : stores, 'all_stores' : all_stores}
                if request.POST['change-manager'] == 'edit':
                    return render(request, 'menuserver/manager.html', context)
                if request.POST['change-manager'] == 'delete':
                    manager.role = 'C'
                    manager.save()
                    stores = Stores.objects.order_by('store_id')
                    managers = Roles.objects.filter(role='M')
                    employees = Roles.objects.filter(role='E')
                    return render(request, 'menuserver/store_manager_employee.html',
                                 {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "change-employee" in request.POST and "change-employee-id" in request.POST:
            id = request.POST["change-employee-id"]
            if Roles.objects.get(id).exists():
                employee = Roles.objects.get(id)
                stores = employee.stores.all()
                all_stores = Stores.objects.order_by('store_id')
                context = {'employee_user' : employee.user, 'stores' : stores, 'all_stores' : all_stores}
                if request.POST['change-employee'] == 'edit':
                    return render(request, 'menuserver/employee.html', context)
                if request.POST['change-employee'] == 'delete':
                    employee.role = 'C'
                    employee.save()
                    stores = Stores.objects.order_by('store_id')
                    managers = Roles.objects.filter(role='M')
                    employees = Roles.objects.filter(role='E')
                    return render(request, 'menuserver/store_manager_employee.html',
                                 {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "submit" in request.POST:
            if request.POST['submit'] == 'edit-store':
                if 'store-id' in request.POST:
                    if Stores.objects.filter(store_id=request.POST['store-id']).count() == 1:
                        editted_store = Stores.objects.get(store_id=request.POST['store-id'])
                        editted_store.name = request.POST['store-name']
                        editted_store.address = request.POST['store-address']
                        editted_store.save()
            if request.POST['submit'] == 'new-store':
                if 'store-id' in request.POST:
                    if Stores.objects.filter(store_id=request.POST['store-id']).count() == 0:
                        new_store = Stores(store_id=request.POST['store-id'],
                                           name=request.POST['store-name'],
                                           address=request.POST['store-address'])
                        new_store.save()
            if request.POST['submit'] == 'manager':
                if 'username' in request.POST:
                    username=request.POST["username"]

                    if User.objects.filter(username=username).exists():
                        us = User.objects.get(username=username)
                        us.roles.role = "M"
                        us.roles.save()
                        store_id_list = request.POST.getlist('choose-manager-store')
                        manager = us.roles
                        for s in Stores.objects.all():
                            manager.stores.remove(s)
                        for si in store_id_list:
                            manager.stores.add(Stores.objects.get(store_id=si))
                    else:
                        stores = Stores.objects.order_by('store_id')
                        error = "User with the username does not exist."
                        return render(request, 'menuserver/manager.html', {"error": error, "all_stores": stores})
            if request.POST['submit'] == 'employee':
                if 'username' in request.POST:
                    username=request.POST["username"]
                    print(username)
                    if User.objects.filter(username=username).exists():

                        us = User.objects.get(username=username)
                        us.roles.role = "E"
                        us.roles.save()
                        store_id_list = request.POST.getlist('choose-employee-store')
                        employee = us.roles
                        store_id_list = request.POST.getlist('choose-employee-store')
                        for s in Stores.objects.all():
                            employee.stores.remove(s)
                        for si in store_id_list:
                            employee.stores.add(Stores.objects.get(store_id=si))
                    else:
                        stores = Stores.objects.order_by('store_id')
                        error = "User with the username does not exist."
                        return render(request, 'menuserver/employee.html', {"error": error, "all_stores": stores})
        stores = Stores.objects.order_by('store_id')
        managers = Roles.objects.filter(role='M')
        employees = Roles.objects.filter(role='E')
        return render(request, 'menuserver/store_manager_employee.html',
                     {'stores' : stores, 'managers' : managers, 'employees' : employees})

def store(request):
    if request.method == 'GET':
        managers = Roles.objects.filter(role='M')
        employees = Roles.objects.filter(role='E')
        return render(request, 'menuserver/store.html', {'managers' : managers, 'employees' : employees})
    if request.method == 'POST':
        if request.POST['submit'] == 'edit-store':
            if 'store-id' in request.POST:
                if Stores.objects.filter(store_id=request.POST['store-id']).count() == 1:
                    editted_store = Stores.objects.get(store_id=request.POST['store-id'])
                    editted_store.name = request.POST['store-name']
                    editted_store.address = request.POST['store-address']
                    editted_store.save()
        if request.POST['submit'] == 'new-store':
            if 'store-id' in request.POST and 'store-name' in request.POST and 'store-address' in request.POST:
                new_store = Stores(store_id=request.POST['store-id'],
                                   name=request.POST['store-name'],
                                   address=request.POST['store-address'])
                new_store.save()
    stores = Stores.objects.order_by('store_id')
    managers = Roles.objects.filter(role='M')
    employees = Roles.objects.filter(role='E')
    return render(request, 'menuserver/store_manager_employee.html',
                 {'stores' : stores, 'managers' : managers, 'employees' : employees})

def manager(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/manager.html', {'all_stores' : stores})
    if request.POST['submit'] == 'manager':
        if 'username' in request.POST:
            username=request.POST["username"]
            if Roles.objects.filter(user=User.objects.get(username=username)).exists():
                manager = Roles.objects.get(user=User.objects.get(username=username))
                manager.role = 'M'
                manager.save()
                store_id_list = request.POST.getlist('choose-manager-store')
                for s in Stores.objects.all():
                    manager.stores.remove(s)
                for si in store_id_list:
                    manager.stores.add(Stores.objects.get(store_id=si))
    stores = Stores.objects.order_by('store_id')
    managers = Roles.objects.filter(role='M')
    employees = Roles.objects.filter(role='E')
    return render(request, 'menuserver/store_manager_employee.html',
                 {'stores' : stores, 'managers' : managers, 'employees' : employees})

def employee(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/employee.html', {'all_stores' : stores})
    if request.POST['submit'] == 'employee':
        if 'username' in request.POST:
            username=request.POST["username"]
            if User.objects.filter(username=username).exists():
                employee = User.objects.get(username=username).roles
                employee.role = 'E'
                employee.save()
                store_id_list = request.POST.getlist('choose-employee-store')
                for s in Stores.objects.all():
                    employee.stores.remove(s)
                for si in store_id_list:
                    employee.stores.add(Stores.objects.get(store_id=si))
    stores = Stores.objects.order_by('store_id')
    managers = Roles.objects.filter(role='M')
    employees = Roles.objects.filter(role='E')
    return render(request, 'menuserver/store_manager_employee.html',
                 {'stores' : stores, 'managers' : managers, 'employees' : employees})

@login_required
def order(request):

    stores = Stores.objects.order_by('store_id')
    if request.method == 'GET':
        if request.user.is_authenticated:
            menu = Dishes.objects.order_by('name')
            orders = Orders.objects.filter(username=request.user.username, is_submitted=False)
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
        else:
            return render(request, 'menuserver/error.html', {})
    if request.method == 'POST':
        if "increase-num" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["increase-num"]), username=request.user.username, is_submitted=False)
            for o in order:
                o.num += 1
                o.save()
            orders = Orders.objects.filter(username=request.user.username, is_submitted=False)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
        if "decrease-num" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["decrease-num"]), username=request.user.username, is_submitted=False)
            for o in order:
                o.num -= 1
                if o.num == 0:
                    o.delete()
                else:
                    o.save()
            orders = Orders.objects.filter(username=request.user.username, is_submitted=False)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})

        if "add-dish" in request.POST and "dish-name" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["dish-name"]), username=request.user.username, is_submitted=False)

            if order.count() == 0:
                dish = Dishes.objects.get(name = request.POST["dish-name"])
                order = Orders(dish=dish, num=1, username=request.user.username, is_submitted=False)
                order.save()
            else:
                for o in order:
                    o.num += 1
                    o.save()
            orders = Orders.objects.filter(username=request.user.username, is_submitted=False)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})

        if "submit-button" in request.POST and "store" in request.POST:
            orders = Orders.objects.filter(username=request.user.username, is_submitted=False)
            if orders.count() > 0:
                o_id = 0
                oid_set = set()
                all_submitted_orders = SubmittedOrders.objects.all()
                for aso in all_submitted_orders:
                    oid_set.add(int(aso.order_id))
                while(1):
                    if set_include(o_id, oid_set) == False:
                        break
                    else:
                        o_id += 1

                store = Stores.objects.get(store_id=request.POST["store"])
                username = request.user.username
                submitted = SubmittedOrders(order_id=o_id, store=store, username=username)
                submitted.save()
                for o in orders:
                    submitted.order.add(o)
                    o.is_submitted = True
                    o.save()

                menu = Dishes.objects.order_by('name')
                orders = Orders.objects.filter(username=request.user, is_submitted=False)
                total_price = 0
                for o in orders:
                    total_price += o.dish.price * o.num
                return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
        if "checkout-order" in request.POST:
            fulfilled_order = SubmittedOrders.objects.filter(username=request.user.username, is_fulfill=True)
            processing_order = SubmittedOrders.objects.filter(username=request.user.username, is_fulfill=False, is_decline=False)
            declined_order = SubmittedOrders.objects.filter(username=request.user.username, is_decline=True)
            return render(request, 'menuserver/checkout.html', {'fulfilled_order': fulfilled_order,
                                                                'processing_order': processing_order,
                                                                'declined_order': declined_order})

        stores = Stores.objects.order_by('store_id')
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/order.html', {'menu' : menu, 'stores' : stores})

@login_required
def submitted_order(request):
    if request.method == 'GET':
        current_user = request.user
        if current_user.is_authenticated and current_user.roles.role != 'C':
            stores = Stores.objects.order_by('store_id')
            return render(request, 'menuserver/submitted_order.html', {'stores': stores})
        else:
            return render(request, 'menuserver/error.html', {})
    if request.method == 'POST':
        s_id = ""
        if "chosen-store" in request.POST:
            s_id = request.POST["chosen-store"]
            stores = Stores.objects.order_by('store_id')
            submitted_order = SubmittedOrders.objects.filter(store = Stores.objects.get(store_id=s_id),
                                                             is_fulfill = False, is_decline=False).order_by('order_id')
            return render(request, 'menuserver/submitted_order.html', {'stores': stores, 'submitted_order' : submitted_order})
        if "order-choice" in request.POST and "submitted-order-id" in request.POST:
            if SubmittedOrders.objects.filter(order_id=request.POST["submitted-order-id"]).count()== 1:
                if request.POST["order-choice"] == "fulfill":
                    so = SubmittedOrders.objects.get(order_id=request.POST["submitted-order-id"])
                    so.is_fulfill = True
                    so.save()
                if request.POST["order-choice"] == "decline":
                    so = SubmittedOrders.objects.get(order_id=request.POST["submitted-order-id"])
                    so.is_decline = True
                    so.save()
                if Stores.objects.filter(store_id=s_id).count() > 0: # validation
                    submitted_order = SubmittedOrders.objects.filter(store = Stores.objects.get(store_id=s_id),
                                                                     is_fulfill = False, is_decline=False).order_by('order_id')
                    stores = Stores.objects.order_by('store_id')
                    return render(request, 'menuserver/submitted_order.html', {'stores': stores, 'submitted_order' : submitted_order})
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/submitted_order.html', {'stores': stores})


def set_include(x, y):
    for item in y:
        if item == x:
            return True
    return False

def register(request):

    if request.method == "GET":
        user_form = UserForm()
        return render(request, 'menuserver/register.html', {'user_form': user_form})

    if request.method == 'POST':
        ctx={}
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if "repeat-password" in request.POST and  user.password == request.POST["repeat-password"]:
                user.set_password(user.password)
                user.save()
                user_role = Roles(user=user, role='C')
                user_role.save()
                login(request, user)
                return render(request, 'menuserver/main.html', {})

            else:
                User.objects.filter(username=user.username).delete()
                ctx["error"] = "Two passwords are not matching!"
        ctx["user_form"] = user_form
        return render(request, 'menuserver/register.html', ctx)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'menuserver/login.html', {})

    if request.method == 'POST':
        ctx={}
        if "username" in request.POST and "password" in request.POST:
        # First get the username and password supplied
            username = request.POST["username"]
            ctx["username"] = username
            password = request.POST["password"]
            ctx["password"] = password

            user = authenticate(username=username, password=password)
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    if user.roles.role == 'M':
                        return render(request, 'menuserver/main.html', {"manager": 1})
                    elif user.roles.role == 'E':
                        return render(request, 'menuserver/main.html', {"employee": 1})
                    else:
                        return render(request, 'menuserver/main.html', {})
                else:
                    # If account is not active:
                    ctx["error"] = "Your account is not active."
            else:
                ctx["error"] = "Invalid login details supplied."
        else:
            ctx["username"] = request.POST.get('username', '')
            ctx["password"] = request.POST.get('password', '')
            ctx["error"] = "All fields need to be filled."

        return render(request, 'menuserver/login.html', ctx)


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'menuserver/main.html', {})

def error(request):
    return render(request, 'menuserver/error.html', {})
