from django.test import TestCase, LiveServerTestCase, Client, override_settings
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from .models import Dishes, Stores, Orders, SubmittedOrders, Roles
from django.contrib.auth.models import User, Group
import unittest
from django.core.files.uploadedfile import SimpleUploadedFile
import env

# Create your tests here.
class UserTestCase(LiveServerTestCase):
    def setUp(self):
        driverLocation = '/env/bin/chromedriver'
        self.selenium = webdriver.Chrome(executable_path='/chromedriver.exe')

    def tearDown(self):
        self.selenium.quit()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://maojoymenuserverhw5.azurewebsites.net/register/')
        time.sleep(2)
        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password')
        password2 = selenium.find_element_by_id('repeat-password')

        submit = selenium.find_element_by_name('register-submit')

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
        selenium = self.selenium
        selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
        login_username = selenium.find_element_by_id('username')
        login_password = selenium.find_element_by_id('password')
        login_username.send_keys('manager1')
        login_password.send_keys('manager111')

        submit = selenium.find_element_by_name('login-submit')
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

#
# class MenuManagementTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#
#     def tearDown(self):
#         self.selenium.quit()
#
#     def test_add(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#         #Opening the link we want to test
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')
#
#         add_dish = selenium.find_element_by_xpath("//button[@id='add-dish']").click()
#         time.sleep(3)
#
#         category = selenium.find_element_by_name('category').send_keys('main')
#         photo_file = selenium.find_element_by_name('photo-file')
#         # myfile = open('/Users/jiayuemao/Desktop/17637/homework/media/beef_noodles.jpeg','r')
#         # response = self.client.post('/', {'photo-file': myfile})
#         dish_name = selenium.find_element_by_name('dish-name').send_keys('Beef Noodles1')
#         dish_price = selenium.find_element_by_name('dish-price').send_keys('13')
#         submit = selenium.find_element_by_name('submit-dish').click()
#         time.sleep(5)
#
#     def test_delete(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')
#         time.sleep(2)
#         submit = selenium.find_element_by_xpath("//button[@value='delete']").click()
#         time.sleep(5)
#
#     def test_edit(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/menu_management/')
#         time.sleep(2)
#         submit = selenium.find_element_by_xpath("//button[@value='edit']").click()
#         time.sleep(3)
#         photo_file = selenium.find_element_by_name('photo-file')
#         dish_name = selenium.find_element_by_name('dish-name')
#         dish_name.send_keys('')
#         dish_name.send_keys('Beef Noodles2')
#         submit = selenium.find_element_by_name('submit-dish').click()
#         time.sleep(5)

class DishTestCase(LiveServerTestCase):

    def test(self):
        new_dish = Dishes(categary='main', name='new dish', price=13)
        new_dish.photo_url = '/media/beef_noodles.jpeg'
        new_dish.save()
        dish = Dishes.objects.get(name='new dish')
        self.assertEquals('new dish', dish.name)
        self.assertEquals(13, dish.price)
        self.assertEquals('main', dish.categary)


# class OrderTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#
#     def tearDown(self):
#         self.selenium.quit()
#
#     def test_add_order(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/order/')
#         time.sleep(2)
#
#         addBtn = selenium.find_element_by_xpath("//button[@name='add-dish']")
#         addBtn.click()
#         time.sleep(2)
#         addBtn.click()
#         time.sleep(2)
#         submitBtn = selenium.find_element_by_xpath("//button[@name='submit-button']").click()
#         time.sleep(2)
#         checkoutBtn = selenium.find_element_by_xpath("//button[@name='checkout-order']").click()
#         time.sleep(5)

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

# class SubmittedOrderTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#
#     def tearDown(self):
#         self.selenium.quit()
#
#     def test_fulfill(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/submitted_order/')
#         time.sleep(2)
#         storeBtn = selenium.find_element_by_xpath("//button[@name='chosen-store']")
#         storeBtn.click()
#         time.sleep(2)
#         dropdown = selenium.find_element_by_xpath("//ul[@id='dropdownMenu1']").click()
#         time.sleep(3)
#         fulfillBtn = selenium.find_element_by_xpath("//button[@value='fulfill']")
#         fulfillBtn.click()
#         time.sleep(3)
#
#     def test_decline(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/submitted_order/')
#         time.sleep(2)
#         storeBtn = selenium.find_element_by_xpath("//button[@name='chosen-store']")
#         storeBtn.click()
#         time.sleep(2)
#         dropdown = selenium.find_element_by_xpath("//ul[@id='dropdownMenu1']").click()
#         time.sleep(3)
#         declineBtn = selenium.find_element_by_xpath("//button[@value='decline']")
#         declineBtn.click()
#         time.sleep(3)

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

# class StoreTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#
#     def tearDown(self):
#         self.selenium.quit()
#
#     def test_add_store(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#         addBtn = selenium.find_element_by_xpath("//button[@name='add-store']")
#         addBtn.click()
#         time.sleep(2)
#         store_id = selenium.find_element_by_xpath("//input[@name='store-id']")
#         store_name = selenium.find_element_by_xpath("//input[@name='store-name']")
#         store_address = selenium.find_element_by_xpath("//input[@name='store-address']")
#         store_id.send_keys("new store id")
#         store_name.send_keys('new store name')
#         store_address.send_keys('new store address')
#         submit = selenium.find_element_by_xpath("//button[@name='submit']")
#         submit.click()
#         time.sleep(3)
#
#
#     def test_delete_store(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#
#         deleteBtn = selenium.find_element_by_xpath("//button[@value='delete']")
#         deleteBtn.click()
#         time.sleep(3)
#
#     def test_edit_store(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('manager1')
#         login_password.send_keys('manager111')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#
#         editBtn = selenium.find_element_by_xpath("//button[@value='edit']")
#         editBtn.click()
#         time.sleep(2)
#         store_name = selenium.find_element_by_xpath("//input[@name='store-name']")
#         store_address = selenium.find_element_by_xpath("//input[@name='store-address']")
#         store_name.send_keys('111')
#         store_address.send_keys('111')
#         submit = selenium.find_element_by_xpath("//button[@name='submit']")
#         submit.click()
#         time.sleep(3)

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

# class ManagerTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         self.selenium = webdriver.Chrome()
#
#     def tearDown(self):
#         self.selenium.quit()
#
#     def test_add_manager(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('aaa')
#         login_password.send_keys('aaapassword')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#         addBtn = selenium.find_element_by_xpath("//button[@id='add-manager']")
#         addBtn.click()
#         time.sleep(2)
#         username = selenium.find_element_by_xpath("//input[@name='username']")
#
#         username.send_keys('testuser_for_manager')
#
#         stores = selenium.find_element_by_xpath("//input[@name='choose-manager-store']").click()
#         time.sleep(2)
#         submit = selenium.find_element_by_xpath("//button[@name='submit']")
#         submit.click()
#         time.sleep(3)
#
#
#     def test_delete_manager(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('aaa')
#         login_password.send_keys('aaapassword')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#
#         deleteBtn = selenium.find_element_by_xpath("//button[@id='delete-manager']")
#         deleteBtn.click()
#         time.sleep(3)
#
#     def test_edit_manager(self):
#         selenium = self.selenium
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/login/')
#         login_username = selenium.find_element_by_id('username')
#         login_password = selenium.find_element_by_id('password')
#         login_username.send_keys('aaa')
#         login_password.send_keys('aaapassword')
#         submit = selenium.find_element_by_name('login-submit')
#         submit.send_keys(Keys.RETURN)
#
#         selenium.get('http://maojoymenuserverhw5.azurewebsites.net/store_manager_employee/')
#         time.sleep(2)
#
#         editBtn = selenium.find_element_by_xpath("//button[@id='edit-manager']").click()
#         time.sleep(2)
#         stores = selenium.find_element_by_xpath("//input[@name='choose-manager-store']").click()
#         time.sleep(2)
#         submit = selenium.find_element_by_xpath("//button[@name='submit']")
#         submit.click()
#         time.sleep(3)
#
#





# class StoreTestCase(LiveServerTestCase):
#
# class OrderTestCase(LiveServerTestCase):
# js image ajax-csrf
# class RoleTestCase(LiveServerTestCase):
