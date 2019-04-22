# Object Relational Mapping (<img src="https://bit.ly/2VYSpUn" height="50" align="center">)

The following exercises demonstrate implementation and usage of our own tiny ORM.

----
## Excercise 1 

### Specification of the entities <img src="https://bit.ly/2W5KggZ" height="25" align="center">

```json
{"schemaName": "MicroShop",
  "entities": [
  	{"Customer": {
  		"name": "String",
  		"orders" :"*Order"}},
  	{"Order" :{
  		"date": "String",
  		"total": "Number",
  		"customer": "Customer",
  		"lines": "*OrderLine" }},
  	{"OrderLine" : {
  		"order": "Order",
  		"product": "Product",
  		"count": "Number",
  		"total": "Number" }},
  	{"Product" : {
  		"name": "String",
  		"price" :"Number"}}
  ]
}
```
> The '*' in front of some of the entity types means that there is a list of entities. </br> &nbsp;&nbsp;&nbsp;&nbsp;For example a Customer has a list of Orders.

</br>

We have used Python <img src="https://www.python.org/static/opengraph-icon-200x200.png" height="25"> to create our compiler.
The script for it can be found [here](./ORMConverter.py). </br>When executing `python ORMConverter.py` through the terminal <img src="https://bit.ly/2GAl3Wo" height="18" align="center"> (in the same directory where the python script is located), the following files will be generated:
- **MicroShop.sql** - A file which defines the necessary MySQL schema with tables.
- **Customer.cs** - A <img src="https://www.brandeps.com/logo-download/C/C-Sharp-01.png" height="25" align="center"> file with class definitions
- **Order.cs** - -||-
- **OrderLine.cs** - -||-
- **Product.cs** - -||-
<br/>

----
## Excercise 2 

### Query language

We will make a very simple one with the following syntax:

* `Customer` returns a collection of all Customers
* `Customer.name` returns a collection of all names of Customers
* `(Customer|name='Joe')` returns a collection of all Customers named Joe.
* `(Customer|name='Joe').Order` returns a collection of all Joe's Orders.
* `(Customer|name='Joe').Order.OrderLine.Product` returns a collection of all Products in all of Joe's Orders.
* `(Orders|total > 200).Customer.name` returns a list of all Customers with an Order above 200.

</br>

For the query language we decided to rely on REGEX <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/OOjs_UI_icon_regular-expression-progressive.svg/1024px-OOjs_UI_icon_regular-expression-progressive.svg.png" height="20" align="center"> for patterns that would build up to an SQL string. The team didn’t introduce any connection methods on this program's functionality but the resulting scripts are presented on the screen (after executing `python queryLanguage.py`) and can be as easily copied and executed over MySQLWorkbench <img src="https://www.macupdate.com/images/icons256/31829.png" height="20"> for example. 

</br> Here are some of the examples:

> myQuery("Customer")
```sql
SELECT *
FROM Customer
```
</br>

> myQuery("(Customer|name='Joe').Orders.OrderLine.Product")
```sql
SELECT Product.*
FROM Customer
WHERE name='Joe'
INNER JOIN Order ON Orders.customer_id = Customer.customer_id
INNER JOIN OrderLine ON OrderLine.orders_id = Order.orders_id
INNER JOIN Product ON Product.product_id = OrderLine.product_id
```
</br>

> myQuery("(Orders|total > 200).Customer.name")

```sql
SELECT Customer.name
FROM Orders
WHERE total > 200
INNER JOIN Customer ON Customer.customer_id = Order.customer_id
```
</br>

___
> #### Assignment made by:   
`David Alves 👨🏻‍💻 ` :octocat: [Github](https://github.com/davi7725) <br />
`Elitsa Marinovska 👩🏻‍💻 ` :octocat: [Github](https://github.com/elit0451) <br />
> Attending "Databses for Developers" course of Software Development bachelor's degree
