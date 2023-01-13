# X-lease
![Screenshot](/web_static/images/Screeenshot.png)
## Description
### About
X-lease is an marketplace focused on allowing users to lease devices. It achieves this by serving as a broker between users who want to put up their devices for rent and users who wish to lease them. All devices including but not limited to:
Cameras and other filming equipment for creatives.
Microphones for podcasting and music production.
Laptops and other computers
Mobile phones and similar mobile devices.
Fittness trackers and other wearables.
Public address systems.
### Technology
The Backend is built with **python** using the **flask** framework to serve information from the **MySql** database through an API.
For administrative interaction with the system, a console has been incorporated into the system. To run the console:
```
XLEASE_MYSQL_USER=`db_username` XLEASE_MYSQL_DB=`db_name` XLEASE_MYSQL_PWD=`db_password` XLEASE_MYSQL_HOST=`db_host` ./console
```
The Frontend is built with React JS...
## Installation
### Running API server
Ensure project is cloned and all commands are run from the root directory of the project
```
gurnicorn --bind 127.0.0.1:50001 api.v1.app:app
```
## APIs and Methods
### States
```
/api/states
```
Mehtods:
	- GET - Returns the list of available states
	- POST - Creates a state object and return the created state
```
/api/states/<state_id>
```
Methods:
	- GET - Returns the  state with the specified id
	- PUT - Updates state with specified id and returns the updated state
	- DELETE - Deletes the state with specified id. If succesful an empty JSON object is returned
```
/api/countries/<country_id>/states
```
Methods:
	- GET - Returns all states within specified country
	- POST - Creates a new state with specified country id
### Users
```
/api/users
```
Methods:
	- GET - Returns a list of all availabale users
	- POST - Creates a new user and returns the new user object
```
/api/users/<user_id>
```
	- GET - Returns the  user with the specified id
	- DELETE - Deletes the  user with the specified id
	- PUT - Updates user with specified id and returns the updated user
### Reviews
```
/api/reviews
```
Methods:
	- GET - Returns the list of available reviews
	- POST -  Creates a review object and returns the created review
```
/api/reviews/<review_id>
```
Methods:
	- GET - Returns the review with the specified id
	- PUT - Updates review with specified id and returns the updated review
	- DELETE - Deletes the  review with the specified id
```
/api/users/<user_id>/reviews
```
Methods:
	- POST -  Creates a new review with specified user id and returns the new review object
	- GET - Returns all reviews made by specified user id
```
/api/users/<user_id>/reviews/<review_id>
```
Methods:
	- GET - Returns specified review made by specified user
```
/api/items/<item_id>/reviews
```
Methods:
	- GET - Returns a list of all reviews made under specified item
	- POST - Creates a new review object under specified item and returns the created item
```
/api/items/<item_id>/reviews/<review_id>
```
Methods:
	- GET - Returns specified review made under specified item
### Items
```
/api/items
```
Method:
	- GET - Returns the list of available items
	- POST - Creates an item object and returns the created item
```
/api/items/<item_id>
```
Methods:
	- GET - Returns the item with the specified id
        - PUT - Updates item with specified id and returns the updated item
        - DELETE - Deletes the item with the specified id
```
/api/categories/<category_id>/items
```
Methods:
	- GET - Returns a list of all items under specified category
	- POST - Creates a new item object under specified category and returns the created item
```
/api/categories/<category_id>/items/<item_id>
```
Methods:
	- GET - Returns specified item belonging to specified category
```
/api/users/<user_id>/items
```
Methods:
	- GET - Returns a list of all items owned by specified user
	- POST - Creates a new item object owned by specified user and returns the created item
```
/api/users/user_id/items/<item_id>
```
Methods:
	- GET - Returns specified item owned by specified user
### Countries
```
/api/countries
```
Methods:
	- GET - Returns a list of all available countries
	- POST - Creates a new country object and returns the created object
```
/api/countries/<country_id>
```
Methods:
	- GET - Returns the specified country object
	- PUT - Updates the specified country object and returns the updated object
	- DELETE - Deletes the specified country object.
### Cities
```
/api/states/<state_id>/cities
```
Methods:
	- GET - Returns a list of city objects within specified state
	- POST - Creates a new city object within specified state object.
```
/api/cities/<city_id>
```
Methods:
	- GET - Returns the specified city_id
	- DELETE - Deletes the city object specified by id
### Categories
```
/api/categories
```
Methods:
	- GET - Returns the list of available items
	- POST - Creates a new category object and returns the created object
```
/api/categories/<category_id>
```
Methods:
	- GET - Returns the specified category object
	- PUT - Updates the specified object and returns the updated object
	- DELETE - Deletes the specified object and returns an empty object if successful.
