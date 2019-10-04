**********Use one-day grace day**********


**********The branch is "hw4"**********


Homework 4: Deployment, Template inheritance, and media

http://maojoymenuserver.azurewebsites.net

Menu page: http://maojoymenuserver.azurewebsites.net/menu/

Menu Management Page: http://maojoymenuserver.azurewebsites.net/menu_management/

Order Page: http://maojoymenuserver.azurewebsites.net/order/

Submitted order page: http://maojoymenuserver.azurewebsites.net/submitted_order/

Management page: http://maojoymenuserver.azurewebsites.net/management/

1. Main page

The main page of the Menuserver system. 

Five buttons on the page: View Menu, Menu Management, Order, Submitted Orders and Management, which are directed to the menu page, the menu management page, the ordering page, the submitted orders page and the management page to edit/create/delete stores, managers and employees and change their relationships.

2. Menu page

User can view the menu of the stores. Since all the stores share the same menu, there's no store selector there.

The link http://localhost:8000/menu is directed to this page. The navbar on the top have five anchors: Mao's restaurant, Menu Management, Order, Submitted Orders and Management, which are directed to the main page, the menu management page, the order page, the submitted orders page and the management page respectively.

3. Menu Management page

User can edit/delete/create dishes there. 

In every dish block, there are two buttons: Edit and Delete. Clicking the Delete button, the dish will be deleted from the database and disappear from the page. Clicking the Edit button, it will be directed to a new page where you can modify the dish's category, name, price and re-choose a picture for the dish. Clicking the Submit button on that page will edit the dish to a new one.

At the end of each dish category, there's an empty block with a large + button, where you can create a new dish. It will be directed to a new page where you can input the dish's category, name, price and choose a picture for the dish. Click the Submit button on that page will save new one to the database and make it appear on the menu page.

4. Order page

User can see the menu, order the dish they want and submit the orders. 

The menu on the right shows the dishes of the restaurants and user can add the dish they want by clicking the add button.

The sidebar on the left is the order part, where the users can see the dishes they have chosen and their numbers. Users can change the numbers by clicking + or - buttons. If the number turns out to be 0, the dish will disappear from the page. If the user click on the same add button multiple times, it will increase the number of that specific dish.

User can choose the store they are ordering from and enter their username to submit the orders.

5. Submitted Order page

User can see the submitted orders on this page. 

On that page, under the title "Submitted Orders", there's a button group showing all the stores. By clicking on different buttons, the page will show the submitted orders form different stores respectively.

The submitted orders from different stores are shown by dropdown menu. The title of the dropdown menu shows the order ID and the username that the order is from. By clicking on the title, the dropdown menu will show the ordered dishes and their numbers.

(P.S. The order ID has no meaning, just to saperate every order from each other. The submitted order with a smaller order ID does not mean that it was ordered first.)

There are two buttons: Fulfill and Decline on the dropdown menu. By clicking either of the two buttons, the submitted orders will disappear on that page, but the Decline button will make the submitted order remove from the database. The button Fulfill instead will make the boolean field is_fulfill in the model class SubmittedOrders to be True.

6. Management page

User can edit/create/delete stores, managers, employees on this page and also can change the relationship among the three. 

There are three parts on the page: Stores, Managers and Employees.

Stores:

One block shows the information of one store including the store ID, name, address and the managers and employees belonged to that store. The title "Managers / Employees" is a dropdown menu. By clicking on that, it will show the managers and employees in that store.

On the left top of every block, there are two buttons: Edit and Delete. By clicking Delete, it will delete the store both from the page and the database. Clicking the Edit button, it will be directed to a new page, where you can change the name, address and the manegers & employees of the store.

There's an empty block with a large + button, where you can create a new store in a new page. Clicking the Submit button on that page will save a new store to the database and make it appear on the menu page.

Managers/Employees:

One block shows the information of one manager/employee including the ID, name and the stores they belong to.

On the left top of every block, there are two buttons: Edit and Delete. By clicking Delete, it will delete the manager/employee both from the page and the database. Clicking the Edit button, it will be directed to a new page, where you can change the ID, name and the stores.

There's an empty block with a large + button, where you can create a new manager/employee.



