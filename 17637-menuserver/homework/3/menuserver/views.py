from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Dishes, Stores, Managers, Employees, Orders, SubmittedOrders

# Create your views here.
global o_id
o_id = 0

def main(request):
    return render(request, 'menuserver/main.html')

def menu(request):
    if request.method == 'GET':
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/menu.html', {'menu' : menu})

def menu_management(request):
    if request.method == 'GET':
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/menu_management.html', {'menu' : menu})
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
    if request.method == 'POST' and 'submit' in request.POST:
        if request.POST["submit"] == "Submit":
            if "category" in request.POST and "dish-name" in request.POST and "dish-price" in request.POST and "photo-url" in request.POST:
                new_dish = Dishes(categary=request.POST["category"], name=request.POST["dish-name"], price=request.POST["dish-price"], photo_url=request.POST["photo-url"])
                new_dish.save()
    menu = Dishes.objects.order_by('name')
    return render(request, 'menuserver/menu_management.html', {'menu' : menu})

def store_manager_employee(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        managers = Managers.objects.order_by('manager_id')
        employees = Employees.objects.order_by('employee_id')

        return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})
    if request.method == 'POST':
        if "change-store" in request.POST and "change-store-id" in request.POST:
            store_id = request.POST["change-store-id"]
            store = Stores.objects.get(store_id=store_id)
            managers = Managers.objects.order_by('manager_id')
            employees = Employees.objects.order_by('employee_id')
            context = {'store_id' : store_id, 'name' : store.name, 'address' : store.address, 'managers' : managers, 'employees' : employees}
            if request.POST['change-store'] == 'edit':
                return render(request, 'menuserver/store.html', context)
            if request.POST['change-store'] == 'delete':
                managers = Managers.objects.all()
                for m in managers:
                    if store in m.stores.all():
                        m.stores.remove(store)
                submitted_orders = SubmittedOrders.objects.all()
                for so in submitted_orders:
                    if so.store.store_id == store.store_id:
                        so.delete()
                store.delete()
                stores = Stores.objects.order_by('store_id')
                managers = Managers.objects.order_by('manager_id')
                employees = Employees.objects.order_by('employee_id')
                return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "change-manager" in request.POST and "change-manager-id" in request.POST:
            manager_id = request.POST["change-manager-id"]
            if Managers.objects.filter(manager_id=manager_id).count() == 1:
                manager = Managers.objects.get(manager_id=manager_id) #need validation here
                stores = manager.stores.all()
                all_stores = Stores.objects.order_by('store_id')
                context = {'manager_id' : manager_id, 'name' : manager.name, 'stores' : stores, 'all_stores' : all_stores, 'id' : manager.id}
                if request.POST['change-manager'] == 'edit':
                    return render(request, 'menuserver/manager.html', context)
                if request.POST['change-manager'] == 'delete':
                    manager.delete()
                    stores = Stores.objects.order_by('store_id')
                    managers = Managers.objects.order_by('manager_id')
                    employees = Employees.objects.order_by('employee_id')
                    return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "change-employee" in request.POST and "change-employee-id" in request.POST:
            employee_id = request.POST["change-employee-id"]
            if Employees.objects.filter(employee_id=employee_id).count() == 1:
                employee = Employees.objects.get(employee_id=employee_id)
                stores = employee.stores.all()
                all_stores = Stores.objects.order_by('store_id')
                context = {'employee_id' : employee_id, 'name' : employee.name, 'stores' : stores, 'all_stores' : all_stores, 'id' : employee.id}
                if request.POST['change-employee'] == 'edit':
                    return render(request, 'menuserver/employee.html', context)
                if request.POST['change-employee'] == 'delete':
                    employee.delete()
                    stores = Stores.objects.order_by('store_id')
                    managers = Managers.objects.order_by('manager_id')
                    employees = Employees.objects.order_by('employee_id')
                    return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})
        if "submit" in request.POST:
            if request.POST['submit'] == 'edit-store':
                if 'store-id' in request.POST:
                    if Stores.objects.filter(store_id=request.POST['store-id']).count() == 1:
                        editted_store = Stores.objects.get(store_id=request.POST['store-id'])
                        editted_store.name = request.POST['store-name']
                        editted_store.address = request.POST['store-address']
                        editted_store.save()
                        manager_id_list = request.POST.getlist('choose-store-manager')
                        for m in Managers.objects.all():
                            editted_store.managers_set.remove(m)
                        for mi in manager_id_list:
                            editted_store.managers_set.add(Managers.objects.get(manager_id=mi))
                        employee_id_list = request.POST.getlist('choose-store-employee')
                        for e in Employees.objects.all():
                            editted_store.employees_set.remove(e)
                        for ei in employee_id_list:
                            editted_store.employees_set.add(Employees.objects.get(employee_id=ei))
            if request.POST['submit'] == 'new-store':
                if 'store-id' in request.POST:
                    if Stores.objects.filter(store_id=request.POST['store-id']).count() == 0:
                        new_store = Stores(store_id=request.POST['store-id'], name=request.POST['store-name'], address=request.POST['store-address'])
                        new_store.save()
                        manager_id_list = request.POST.getlist('choose-store-manager')
                        for mi in manager_id_list:
                            new_store.managers_set.add(Managers.objects.get(manager_id=mi))
            if request.POST['submit'] == 'edit-manager':
                if 'id' in request.POST:
                    if Managers.objects.filter(id=request.POST['id']).count() == 1:
                        editted_manager = Managers.objects.get(id=request.POST['id'])
                        editted_manager.manager_id = request.POST['manager-id']
                        editted_manager.name = request.POST['manager-name']
                        editted_manager.save()
                        store_id_list = request.POST.getlist('choose-manager-store')
                        for s in Stores.objects.all():
                            editted_manager.stores.remove(s)
                        for si in store_id_list:
                            editted_manager.stores.add(Stores.objects.get(store_id=si))
            if request.POST['submit'] == 'new-manager':
                if 'manager-id' in request.POST:
                    if Managers.objects.filter(manager_id=request.POST['manager-id']).count() == 0:
                        store_id_list = request.POST.getlist('choose-manager-store')
                        new_manager = Managers(manager_id=request.POST['manager-id'], name=request.POST['manager-name'])
                        new_manager.save()
                        for si in store_id_list:
                            new_manager.stores.add(Stores.objects.get(store_id=si))
            if request.POST['submit'] == 'edit-employee':
                if 'id' in request.POST:
                    if Employees.objects.filter(id=request.POST['id']).count() == 1:
                        editted_employee = Employees.objects.get(id=request.POST['id'])
                        editted_employee.employee_id = request.POST['employee-id']
                        editted_employee.name = request.POST['employee-name']
                        editted_employee.save()
                        store_id_list = request.POST.getlist('choose-employee-store')
                        for s in Stores.objects.all():
                            editted_employee.stores.remove(s)
                        for si in store_id_list:
                            editted_employee.stores.add(Stores.objects.get(store_id=si))
            if request.POST['submit'] == 'new-employee':
                if 'employee-id' in request.POST:
                    if Employees.objects.filter(employee_id=request.POST['employee-id']).count() == 0:
                        store_id_list = request.POST.getlist('choose-employee-store')
                        new_employee = Employees(employee_id=request.POST['employee-id'], name=request.POST['employee-name'])
                        new_employee.save()
                        for si in store_id_list:
                            new_employee.stores.add(Stores.objects.get(store_id=si))
        stores = Stores.objects.order_by('store_id')
        managers = Managers.objects.order_by('manager_id')
        employees = Employees.objects.order_by('employee_id')
        return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})

def store(request):
    if request.method == 'GET':
        managers = Managers.objects.order_by('manager_id')
        employees = Employees.objects.order_by('employee_id')
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
                new_store = Stores(store_id=request.POST['store-id'], name=request.POST['store-name'], address=request.POST['store-address'])
                new_store.save()
    stores = Stores.objects.order_by('store_id')
    managers = Managers.objects.order_by('manager_id')
    return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers})

def manager(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/manager.html', {'all_stores' : stores})
    if request.method == 'POST':
        if 'submit' in request.POST:
            if request.POST["submit"] == "submit-manager":
                new_manager = Managers(manager_id=request.POST['manager-id'], name=request.POST['manager-name'])
                new_manager.save()
                if 'choose-manager-store' in request.POST:
                    store_id_list = request.POST.getlist['choose-manager-store']
                    for si in store_id_list:
                        new_manager.add(Stores.objects.get(store_id=si))
    stores = Stores.objects.order_by('store_id')
    managers = Managers.objects.order_by('manager_id')
    return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers})

def employee(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/employee.html', {'all_stores' : stores})
    if request.method == 'POST':
        if 'submit' in request.POST:
            if request.POST["submit"] == "submit-employee":
                new_employee = Employees(employee_id=request.POST['employee-id'], name=request.POST['employee-name'])
                new_employee.save()
                if 'choose-employee-store' in request.POST:
                    store_id_list = request.POST.getlist('choose-employee-store')
                    for si in store_id_list:
                        new_employee.stores.add(Stores.objects.get(store_id=si))
    stores = Stores.objects.order_by('store_id')
    managers = Managers.objects.order_by('manager_id')
    employees = Employees.objects.order_by('employee_id')
    return render(request, 'menuserver/store_manager_employee.html', {'stores' : stores, 'managers' : managers, 'employees' : employees})


# global oid_set
# oid_set = set()
# all_orders = Orders.objects.all()
# all_submitted_orders = SubmittedOrders.objects.all()
# for ao in all_orders:
#     oid_set.add(int(ao.order_id))
# for aso in all_submitted_orders:
#     oid_set.add(int(aso.order_id))

def order(request):
    global o_id
    # global oid_set
    stores = Stores.objects.order_by('store_id')
    if request.method == 'GET':
        # To have an unique order_id
        oid_set = set()
        all_orders = Orders.objects.all()
        all_submitted_orders = SubmittedOrders.objects.filter(is_fulfill=False)
        for ao in all_orders:
            oid_set.add(int(ao.order_id))
        for aso in all_submitted_orders:
            oid_set.add(int(aso.order_id))
        while(1):
            if set_include(int(o_id), oid_set) == False:
                break
            else:
                o_id += 1
        print("get: ",o_id)
        oid_set.add(int(o_id))

        menu = Dishes.objects.order_by('name')
        orders = Orders.objects.filter(order_id=o_id)
        total_price = 0
        for o in orders:
            total_price += o.dish.price * o.num
        return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
    if request.method == 'POST':
        if "increase-num" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["increase-num"]), order_id=str(o_id))
            for o in order:
                o.num += 1
                o.save()
            orders = Orders.objects.filter(order_id=o_id)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
        if "decrease-num" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["decrease-num"]), order_id=str(o_id))
            for o in order:
                o.num -= 1
                if o.num == 0:
                    o.delete()
                else:
                    o.save()
            orders = Orders.objects.filter(order_id=o_id)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})

        if "add-dish" in request.POST and "dish-name" in request.POST:
            order = Orders.objects.filter(dish=Dishes.objects.get(name=request.POST["dish-name"]), order_id=str(o_id))
            print("add: ", o_id)
            if order.count() == 0:
                dish = Dishes.objects.get(name = request.POST["dish-name"])
                order = Orders(dish=dish, num=1, order_id=o_id)
                order.save()
            else:
                for o in order:
                    o.num += 1
                    o.save()
            orders = Orders.objects.filter(order_id=o_id)
            menu = Dishes.objects.order_by('name')
            total_price = 0
            for o in orders:
                total_price += o.dish.price * o.num
            return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})

        if "submit-button" in request.POST and "store" in request.POST and "username" in request.POST:
            orders = Orders.objects.filter(order_id = o_id)
            if orders.count() > 0:
                store = Stores.objects.get(store_id=request.POST["store"])
                username = request.POST['username']
                submitted = SubmittedOrders(order_id=o_id, store=store, username=username)
                submitted.save()
                for o in orders:
                    submitted.order.add(o)

                # To have an unique order_id
                oid_set = set()
                all_orders = Orders.objects.all()
                all_submitted_orders = SubmittedOrders.objects.filter(is_fulfill=False)
                for ao in all_orders:
                    oid_set.add(int(ao.order_id))
                for aso in all_submitted_orders:
                    oid_set.add(int(aso.order_id))
                while(1):
                    if set_include(int(o_id), oid_set) == False:
                        break
                    else:
                        o_id += 1
                oid_set.add(int(o_id))
                print("submit: ", o_id)

                menu = Dishes.objects.order_by('name')
                orders = Orders.objects.filter(order_id=o_id)
                total_price = 0
                for o in orders:
                    total_price += o.dish.price * o.num
                return render(request, 'menuserver/order.html', {'menu' : menu, 'orders' : orders, 'stores' : stores, 'total_price' : total_price})
        stores = Stores.objects.order_by('store_id')
        menu = Dishes.objects.order_by('name')
        return render(request, 'menuserver/order.html', {'menu' : menu, 'stores' : stores})

def submitted_order(request):
    if request.method == 'GET':
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/submitted_order.html', {'stores': stores})
    if request.method == 'POST':
        if "chosen-store" in request.POST:
            global s_id
            s_id = request.POST["chosen-store"]
            stores = Stores.objects.order_by('store_id')
            submitted_order = SubmittedOrders.objects.filter(store = Stores.objects.get(store_id=s_id), is_fulfill = False).order_by('order_id')
            return render(request, 'menuserver/submitted_order.html', {'stores': stores, 'submitted_order' : submitted_order})
        if "order-choice" in request.POST and "submitted-order-id" in request.POST:
            if SubmittedOrders.objects.filter(order_id=request.POST["submitted-order-id"]).count()== 1:
                if request.POST["order-choice"] == "fulfill":
                    so = SubmittedOrders.objects.get(order_id=request.POST["submitted-order-id"])
                    so.is_fulfill = True
                    so.save()
                    orders = so.order.all()
                    for o in orders:
                        o.delete()
                    so.delete()
                if request.POST["order-choice"] == "decline":
                    so = SubmittedOrders.objects.get(order_id=request.POST["submitted-order-id"])
                    orders = so.order.all()
                    for o in orders:
                        o.delete()
                    so.delete()
                stores = Stores.objects.order_by('store_id')
                if Stores.objects.filter(store_id=s_id).count() > 0: # validation
                    submitted_order = SubmittedOrders.objects.filter(store = Stores.objects.get(store_id=s_id), is_fulfill = False).order_by('order_id')
                    return render(request, 'menuserver/submitted_order.html', {'stores': stores, 'submitted_order' : submitted_order})
        stores = Stores.objects.order_by('store_id')
        return render(request, 'menuserver/submitted_order.html', {'stores': stores})


def set_include(x, y):
    for item in y:
        if item == x:
            return True
    return False
