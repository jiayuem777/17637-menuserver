from django.test import TestCase, LiveServerTestCase, Client, override_settings
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from .models import Dishes, Stores, Orders, SubmittedOrders, Roles
from django.contrib.auth.models import User, Group
import unittest
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings



# Create your tests here.
class UserTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):

        #Opening the link we want to test
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/register/')
        time.sleep(2)
        #find the form element
        first_name = self.driver.find_element_by_id('id_first_name')
        last_name = self.driver.find_element_by_id('id_last_name')
        username = self.driver.find_element_by_id('id_username')
        email = self.driver.find_element_by_id('id_email')
        password1 = self.driver.find_element_by_id('id_password')
        password2 = self.driver.find_element_by_id('repeat-password')

        submit = self.driver.find_element_by_name('register-submit')

        #Fill the form with data
        first_name.send_keys('Yusuf')
        last_name.send_keys('Unary')
        username.send_keys('unaryY')
        email.send_keys('yusuf@qawba.com')
        password1.send_keys('12345678')
        password2.send_keys('12345678')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        time.sleep(5)

    def test_login(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')

        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_user_model(self):
        new_user = User.objects.create_user('new_user', 'new@user.com', 'userpassword')
        new_user.first_name = 'New'
        new_user.last_name = 'User'
        new_user.save()
        user = User.objects.get(username='new_user')
        self.assertEquals('New', user.first_name)
        self.assertEquals('User', user.last_name)
        self.assertEquals('new@user.com', user.email)


class MenuManagementTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_add(self):
        selenium = self.driver
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')

        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)
        #Opening the link we want to test
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')

        add_dish = self.driver.find_element_by_xpath("//button[@id='add-dish']").click()
        time.sleep(3)

        category = self.driver.find_element_by_name('category').send_keys('main')
        photo_file = self.driver.find_element_by_name('photo-file')
        # myfile = open('/Users/jiayuemao/Desktop/17637/homework/media/beef_noodles.jpeg','r')
        # response = self.client.post('/', {'photo-file': myfile})
        dish_name = self.driver.find_element_by_name('dish-name').send_keys('Beef Noodles1')
        dish_price = self.driver.find_element_by_name('dish-price').send_keys('13')
        submit = self.driver.find_element_by_name('submit-dish').click()
        time.sleep(5)

    def test_delete(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')
        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//button[@value='delete']").click()
        time.sleep(5)

    def test_edit(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')
        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//button[@value='edit']").click()
        time.sleep(3)
        photo_file = self.driver.find_element_by_name('photo-file')
        dish_name = self.driver.find_element_by_name('dish-name')
        dish_name.send_keys('')
        dish_name.send_keys('Beef Noodles2')
        submit = self.driver.find_element_by_name('submit-dish').click()
        time.sleep(5)

class DishTestCase(LiveServerTestCase):

    def test(self):
        new_dish = Dishes(categary='main', name='new dish', price=13)
        new_dish.photo_url = '/media/beef_noodles.jpeg'
        new_dish.save()
        dish = Dishes.objects.get(name='new dish')
        self.assertEquals('new dish', dish.name)
        self.assertEquals(13, dish.price)
        self.assertEquals('main', dish.categary)


class OrderTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_add_order(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/order/')
        time.sleep(2)

        addBtn = self.driver.find_element_by_xpath("//button[@name='add-dish']")
        addBtn.click()
        time.sleep(2)
        addBtn.click()
        time.sleep(2)
        submitBtn = self.driver.find_element_by_xpath("//button[@name='submit-button']").click()
        time.sleep(2)
        checkoutBtn = self.driver.find_element_by_xpath("//button[@name='checkout-order']").click()
        time.sleep(5)

class OrderModelTestCase(LiveServerTestCase):

    def test(self):
        new_dish = Dishes(categary='main', name='new dish', price=13)
        new_dish.photo_url = '/media/beef_noodles.jpeg'
        new_dish.save()
        dish = Dishes.objects.get(name='new dish')
        new_order = Orders(dish=dish, num=2, is_submitted=False, username='admin')
        new_order.save()
        order = Orders.objects.get(dish=dish)
        self.assertEquals('new dish', order.dish.name)
        self.assertEquals('admin', order.username)
        self.assertEquals(False, order.is_submitted)
        self.assertEquals(2, order.num)

class SubmittedOrderTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_fulfill(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/submitted_order/')
        time.sleep(2)
        storeBtn = self.driver.find_element_by_xpath("//button[@name='chosen-store']")
        storeBtn.click()
        time.sleep(2)
        dropdown = self.driver.find_element_by_xpath("//ul[@id='dropdownMenu1']").click()
        time.sleep(3)
        fulfillBtn = self.driver.find_element_by_xpath("//button[@value='fulfill']")
        fulfillBtn.click()
        time.sleep(3)

    def test_decline(self):

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/submitted_order/')
        time.sleep(2)
        storeBtn = self.driver.find_element_by_xpath("//button[@name='chosen-store']")
        storeBtn.click()
        time.sleep(2)
        dropdown = self.driver.find_element_by_xpath("//ul[@id='dropdownMenu1']").click()
        time.sleep(3)
        declineBtn = self.driver.find_element_by_xpath("//button[@value='decline']")
        declineBtn.click()
        time.sleep(3)

class SubmittedOrderModelTestCase(LiveServerTestCase):

     def test(self):
         new_dish = Dishes(categary='main', name='new dish', price=13)
         new_dish.photo_url = '/media/beef_noodles.jpeg'
         new_dish.save()

         new_dish1 = Dishes(categary='main', name='new dish1', price=15)
         new_dish1.photo_url = '/media/beef_noodles.jpeg'
         new_dish1.save()
         dish = Dishes.objects.get(name='new dish')
         dish1 = Dishes.objects.get(name='new dish1')

         new_order = Orders(dish=dish, num=2, is_submitted=False, username='admin')
         new_order.save()
         new_order1 = Orders(dish=dish1, num=2, is_submitted=False, username='admin')
         new_order1.save()
         order = Orders.objects.get(dish=dish)
         order1 = Orders.objects.get(dish=dish1)

         new_store = Stores(store_id=10, name='new store', address='new store address')
         new_store.save()
         store = Stores.objects.get(store_id=10)

         new_so = SubmittedOrders(order_id=111, store=store, username='admin', is_fulfill=False, is_decline=False)
         new_so.save()
         new_so.order.add(order)
         new_so.order.add(order1)

         so = SubmittedOrders.objects.get(order_id=111)
         self.assertEquals(new_store, so.store)
         self.assertEquals('admin', so.username)
         self.assertEquals(False, so.is_fulfill)
         self.assertEquals(False, so.is_decline)
         order_list = [new_order, new_order1]
         i = 0
         for o in so.order.all():
             self.assertEquals(order_list[i], o)
             i += 1

class StoreTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_add_store(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)
        addBtn = self.driver.find_element_by_xpath("//button[@name='add-store']")
        addBtn.click()
        time.sleep(2)
        store_id = self.driver.find_element_by_xpath("//input[@name='store-id']")
        store_name = self.driver.find_element_by_xpath("//input[@name='store-name']")
        store_address = self.driver.find_element_by_xpath("//input[@name='store-address']")
        store_id.send_keys("new store id")
        store_name.send_keys('new store name')
        store_address.send_keys('new store address')
        submit = self.driver.find_element_by_xpath("//button[@name='submit']")
        submit.click()
        time.sleep(3)


    def test_delete_store(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)

        deleteBtn = self.driver.find_element_by_xpath("//button[@value='delete']")
        deleteBtn.click()
        time.sleep(3)

    def test_edit_store(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)

        editBtn = self.driver.find_element_by_xpath("//button[@value='edit']")
        editBtn.click()
        time.sleep(2)
        store_name = self.driver.find_element_by_xpath("//input[@name='store-name']")
        store_address = self.driver.find_element_by_xpath("//input[@name='store-address']")
        store_name.send_keys('111')
        store_address.send_keys('111')
        submit = self.driver.find_element_by_xpath("//button[@name='submit']")
        submit.click()
        time.sleep(3)

class RoleTestCase(LiveServerTestCase):

    def test(self):
        new_user = User.objects.create_user('new__user', 'new@user.com', 'userpassword')
        new_user.first_name = 'New'
        new_user.last_name = 'User'
        new_user.save()
        user = User.objects.get(username='new__user')
        new_role = Roles(user=user, role='C')
        new_role.save()

        role = Roles.objects.get(user=user)
        self.assertEquals(new_user, role.user)
        self.assertEquals('C', role.role)

class ManagerTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'chromedriver'), chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_add_manager(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)
        addBtn = self.driver.find_element_by_xpath("//button[@id='add-manager']")
        addBtn.click()
        time.sleep(2)
        username = self.driver.find_element_by_xpath("//input[@name='username']")

        username.send_keys('testuser_for_manager')

        stores = self.driver.find_element_by_xpath("//input[@name='choose-manager-store']").click()
        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//button[@name='submit']")
        submit.click()
        time.sleep(3)


    def test_delete_manager(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)

        deleteBtn = self.driver.find_element_by_xpath("//button[@id='delete-manager']")
        deleteBtn.click()
        time.sleep(3)

    def test_edit_manager(self):
        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = self.driver.find_element_by_id('username')
        login_password = self.driver.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')
        submit = self.driver.find_element_by_name('login-submit')
        submit.send_keys(Keys.RETURN)

        self.driver.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
        time.sleep(2)

        editBtn = self.driver.find_element_by_xpath("//button[@id='edit-manager']").click()
        time.sleep(2)
        stores = self.driver.find_element_by_xpath("//input[@name='choose-manager-store']").click()
        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//button[@name='submit']")
        submit.click()
        time.sleep(3)







# class StoreTestCase(LiveServerTestCase):
#
# class OrderTestCase(LiveServerTestCase):
# js image ajax-csrf
# class RoleTestCase(LiveServerTestCase):
