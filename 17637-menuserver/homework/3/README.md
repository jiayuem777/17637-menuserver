Homework5: Data Models

1. Main page

The main page of the Menuserver system. Link: http://localhost:8000.

Five buttons on the page: View Menu, Menu Management, Order, Submitted Orders and Management, which are directed to the menu page, the menu management page, the ordering page, the submitted orders page and the management page to edit/create/delete stores, managers and employees and change their relationships.

2. Menu page

User can view the menu of the stores. Since all the stores share the same menu, there's no store selector there.

The link http://localhost:8000/menu is directed to this page. The navbar on the top have five anchors: Mao's restaurant, Menu Management, Order, Submitted Orders and Management, which are directed to the main page, the menu management page, the order page, the submitted orders page and the management page respectively.

3. Menu Management page

User can edit/delete/create dishes there. The link is http://localhost:8000/menu_management

In every dish block, there are two buttons: Edit and Delete. Clicking the Delete button, the dish will be deleted from the database and disappear from the page. Clicking the Edit button, it will be directed to a new page where you can modify the dish's category, name, price and re-choose a picture for the dish. Clicking the Submit button on that page will edit the dish to a new one.

At the end of each dish category, there's an empty block with a large + button, where you can create a new dish. It will be directed to a new page where you can input the dish's category, name, price and choose a picture for the dish. Click the Submit button on that page will save new one to the database and make it appear on the menu page.

4. Order page

User can see the menu, order the dish they want and submit the orders. The link is http://localhost:8000/order

The menu on the right shows the dishes of the restaurants and user can add the dish they want by clicking the add button.

The sidebar on the left is the order part, where the users can see the dishes they have chosen and their numbers. Users can change the numbers by clicking + or - buttons. If the number turns out to be 0, the dish will disappear from the page. If the user click on the same add button multiple times, it will increase the number of that specific dish.

User can choose the store they are ordering from and enter their username to submit the orders.

5. Submitted Order page

User can see the submitted orders on this page. The link is http://localhost:8000/submitted_order

On that page, under the title "Submitted Orders", there's a button group showing all the stores. By clicking on different buttons, the page will show the submitted orders form different stores respectively.

The submitted orders from different stores are shown by dropdown menu. The title of the dropdown menu shows the order ID and the username that the order is from. By clicking on the title, the dropdown menu will show the ordered dishes and their numbers.

(P.S. The order ID has no meaning, just to saperate every order from each other. The submitted order with a smaller order ID does not mean that it was ordered first.)

There are two buttons: Fulfill and Decline on the dropdown menu. By clicking either of the two buttons, the submitted orders will disappear on that page, but the Decline button will make the submitted order remove from the database. The button Fulfill instead will make the boolean field is_fulfill in the model class SubmittedOrders to be True.

6. Management page

User can edit/create/delete stores, managers, employees on this page and also can change the relationship among the three. The link is http://localhost:8000/store_manager_employee.

There are three parts on the page: Stores, Managers and Employees.

Stores:

One block shows the information of one store including the store ID, name, address and the managers and employees belonged to that store. The title "Managers / Employees" is a dropdown menu. By clicking on that, it will show the managers and employees in that store.

On the left top of every block, there are two buttons: Edit and Delete. By clicking Delete, it will delete the store both from the page and the database. Clicking the Edit button, it will be directed to a new page, where you can change the name, address and the manegers & employees of the store.

There's an empty block with a large + button, where you can create a new store in a new page. Clicking the Submit button on that page will save a new store to the database and make it appear on the menu page.

Managers/Employees:

One block shows the information of one manager/employee including the ID, name and the stores they belong to.

On the left top of every block, there are two buttons: Edit and Delete. By clicking Delete, it will delete the manager/employee both from the page and the database. Clicking the Edit button, it will be directed to a new page, where you can change the ID, name and the stores.

There's an empty block with a large + button, where you can create a new manager/employee.



Dish pictures from:

Main:

1. Bowl of chicken soup: https://images.unsplash.com/photo-1544068192-4c4af19868c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

2. Wonton noodles: https://images.unsplash.com/photo-1567619457295-814fa87f0821?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1353&q=80

3. Beef noodles: https://images.unsplash.com/photo-1568096889942-6eedde686635?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

4. vegan pad thai and gyoza: https://images.unsplash.com/photo-1565355857989-333dff0b3dc8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80

5. Noodles with eggs: https://images.unsplash.com/photo-1555232967-d2c10a468149?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

6. Hotpot noodles with shrump: https://images.unsplash.com/photo-1563379926898-05f4575a45d8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

7. Roasted Beef: https://images.unsplash.com/photo-1568046097340-56eb1e93bc1e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

8. Spicy Hot Pot: https://images.unsplash.com/photo-1562403492-454d4b075cac?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1329&q=80

9. Spicy Tofu: https://images.unsplash.com/photo-1560435726-6480fd46446b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

Pizza:

1. Pizza with berries: https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

2. Italian Sausage Pizza: https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1355&q=80

3. Pizza: https://images.unsplash.com/photo-1506354666786-959d6d497f1a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80

4. Pizza with pineapple: https://images.unsplash.com/photo-1544882907-b914cebddbf4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

5. Pepperoni Pizza: https://images.unsplash.com/photo-1542282811-943ef1a977c3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80

6. Siced Vegetable Pizza: https://images.unsplash.com/photo-1551978129-b73f45d132eb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1304&q=80

https://images.unsplash.com/photo-1528137973883-41b75386f217?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

https://images.unsplash.com/photo-1458642849426-cfb724f15ef7?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80

Burger:

1. Chicken burger with cheese: https://images.unsplash.com/photo-1546599115-c0c0815c391b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

2. Pork burger with fries: https://images.unsplash.com/photo-1558250070-363aa42f9a00?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

3. Roasted beef burger with fries: https://images.unsplash.com/photo-1512152272829-e3139592d56f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

4. Double-layer burger: https://images.unsplash.com/photo-1548946522-4a313e8972a4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1940&q=80

5. https://images.unsplash.com/photo-1551782450-17144efb9c50?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

6. https://images.unsplash.com/photo-1477617722074-45613a51bf6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

7.https://images.unsplash.com/photo-1529565214304-a882ebc5a8e6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

https://images.unsplash.com/photo-1550949987-33f716ccc232?ixlib=rb-1.2.1&auto=format&fit=crop&w=2016&q=80

https://images.unsplash.com/photo-1513185158878-8d8c2a2a3da3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

Beverage:

1. Strawberry Shake: https://images.unsplash.com/photo-1543573852-1a71a6ce19bc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

2. Grape juice: https://images.unsplash.com/photo-1513169639596-cf0480fe1bb9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

3. Strawberry juice: https://images.unsplash.com/photo-1502741224143-90386d7f8c82?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

4. Carrot juice: https://images.unsplash.com/photo-1551040078-5a2f375f9549?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

5. cappuccino: https://images.unsplash.com/photo-1544203180-4047332c3e9b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

6. Mixed juice: https://images.unsplash.com/photo-1507120366498-4656eaece7fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80

7. Orange juice: https://images.unsplash.com/photo-1524156868115-e696b44983db?ixlib=rb-1.2.1&auto=format&fit=crop&w=1946&q=80

8. Green Tea Shake: https://images.unsplash.com/photo-1564352039417-76dbfa5009e4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

https://images.unsplash.com/photo-1550247611-e651810312fe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

https://images.unsplash.com/photo-1553964692-888ccdb8aa7c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80

Background picture:

https://images.unsplash.com/photo-1546039907-7fa05f864c02?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80

https://images.unsplash.com/photo-1564675454013-6e68e6a8c0c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80

https://images.unsplash.com/photo-1556694795-b6423d3d5b28?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80

https://images.unsplash.com/photo-1564675454013-6e68e6a8c0c6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80
