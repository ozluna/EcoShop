

# **EcoShop**

The plastic waste is a big problem for our world and it is one of the biggest factor to climate change from when it is produced to going to our bins, unfortunately governments and big companies are not taking effective action therefore it is down to us to show them we are choosing zero waste path as an indivual. EcoShop is offering the alternative products to use in our daily lives from toothbrush to shampoos

# Table of Contents

1. [User Experience](#user-experience)

    - [Goals](#goals)
      - [Visitor Goals](#visitor-goals)
      - [Busines Goals](#busines-goals)
      - [Design](#design-choices)
2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)



## **User Experience**
***

## Goals
---
### Visitor goals
The target audience to this website  
  * Any household who are aware of the vast amount of
plastic used in daily products and want to reduce their footprints.

### Busines Goals
Attract the customers who are interested buying eco products. Convince them that they are making the right decision and keep them happy after purchase so they will return to the website.  

As a user I would like  
* be able to see a list of products in categories so I can easily search and add to my cart what I am looking for.
* to see the products in detail so I can decide whether or not I want.  
* to be able to see if I succeed to add the product to my cart.
* to be able to access the website from any device
* the website to be easy to use.
* to be able to easily register for an account.
* to be able to view my order history.
* to be able to recover my password if I forget it.
* to receive an email after registering
* to be able to leave product reviews.
* to be able to search product with keywords.
* to be able to sort the products by categories ore price for efficient search.
*  to be able to select quantity of the product to add to the cart.
* to be able to contact to the business owner if any problem arise

As a owner I would like
* to provide well designed, user-friendly platform that will benefit my business to advertise on
* to have interface that is user friendly for me to add, remove or edit a product. The admin can do that on the products or product detail page with superuser login.  
* to be able to store and see the user reviews. User has to login to leave a review so that the owner can track and store user reviews
* to be able to add, change a code for discount coupons. This can be done through the admin console on the website 

## **Design Choices**
---
I tried to create a overall user friendly design with EcoShop website. I wanted to encoruge the user to shop with confidence with that in mind I attempt to use a common ecommerce website structure.

### **Wireframes**
* Wireframes were created using balsamiq.you can find them [here](./readme-doc/wireframe)

### **Fonts**
* For the primary font I used GoogleFonts PT+Serif as a main font and Lora for headings I thought it would fit with the website. 

### **Colour**
![(readme-doc/EcoShoppalette.png)](readme-doc/EcoShoppalette.png)

* I have created the color palette using the hero image on the website with [colors.co](https://coolors.co/006d77-83c5be-edf6f9-ffddd2-e29578) palette creator for holistic view. Try to keep the colours consistent to 
* I used the _Darksalmon_ on the buttons, _Ming_ colour for heading and logo, _Bistre_ for font colour, _Seashell_ for footer and About sections.

### **Styling**
* The brand logo is important as it welcomes the customer when they land in to the website. I created the logo to represent nature and elegance using Canva website. 
* All buttons on the site fit the same bootstrap button styling in size and shape, but I added the colours I used in this project to them, so they fit in with the rest of the content.
* Material Design for bootstrab `MDB` Card design used on Products page included _Add To Cart_. The card shows image and price of the product.

## **Features**
---
### **Element on every page**

* **Top Header**
    * On the left of the header you can see the brand logo    
    ![(media/EcoShopLogo.png)](media/EcoShopLogo.png)   
    * Links for the users and search bar on the middle range and the _All Product_ which is a dropdown take you to product page andsort the products in range such as `By Price`, `By Category`. _Categories_ such as `Kitchen`. 
    * The navbar is collapsed into a burger icon on small and medium sized screens and the logo disappears there fore _Home_ button appears on the dropdown menu
    * Search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over name and description field of Product Model. it collapses to magnified icon on small and medium sized screens.
    * On the right corner there is user icon it is a dropdown button gives `Register` and `Login` options. If the user is logged in `My Profile` and `Logout`. If the user is superuser `Product Management ` option will also appear.

* **Footer**
  * Logo which is link to the home page
  * A list of navigation links users might need when viewing the footer.
  * Copyright information.
  * Social media links they are not linked at the moment but I will add them once the EcoShop social media platforms are exist.

* **Toasts**
  * Bootstrap toast feature is used to inform the user. There are 4 types of notification user can see `success`, `error`, `info` and `warning` each one of them has different colour and heading with different messages.

## **Existing Features**
### **Home Page**
The homepage is the most visited place in the webstore. It’s the page from where the customers start exploring the storefront. I want to excite the customers with my homepage content by highlighting my best-selling product, special offer and new items.
To fulfil that purpose, I added 20% discount modal, new arrival row and popular categories row.  
* A modal pops up in 3 second, gives enough time to the user a glimpse of the page before the modal pops in.
* Homepage welcomes the user with free delivery treshold banner and navigation bar.
* Hero image choosed from [canva](canva.com) There is a motto emphasis "why you should shop on this website" and a `Shop Now` button completes the image.
* New arrival row I added a line of code to the `home` app `views.py` which calls last added 4 items to the website.
* About us section introduce the site to the visitor 
* Popular categories is inprogress part of the page. It is static at the moment but in future will call the most clicked categories to the home page.
### **Product Page**
 You can come to this page either `Shop Now` button on the home page or `All Products` link from the navigation bar. Also, you can see categorised version.
 * As you land to the product page you can see how many products exist in this webstore on the left corner. On the right corner you can sort all the products by `price`, `name` and `category`
 * Each product is in a `MDB` card feature which has an image the product name and Add to cart button. If you are a `superuser` you can also `add` or `delete` a product from this page.
 * A floating button appears on the lower right of the screen when the user starts to scroll downwards. Clicking this moves the view back up to the top of the page. This added because as products populates only one page, the page can be quite long, and this gives option to go to top without scrolling manually. I influenced the scroll top button from [W3S](w3school.com)
 ### **Product Detail Page**
 * From the products page user can click to any product to see the details of it and choose quantity then `Add To Cart`.
 * Authenticated user, can leave a comment, and rate the product. If the user is not signed in, they can see the reviews and count of them but can't see the "review form" instead they are encouraging to login to leave a review.
 * If the user leaves a review this will appear with user name and user icon on the left, given rate will fill the stars and it will position next to username. On the next column user can see review headline and review subject. Every review will be divided by `hr` horizantal line.
 * Superuser if authenticated can edit and/or delete the product using `edit` and `delete` buttons which are located next to product rating.

### **Shopping Cart**
* If there is no item in the shopping cart user can see "Your cart is empty" message and `Keep Shopping` button which will take user to products page.
* If the cart has a product on the left side, it shows the products added to the cart. Customers can change the quantity or remove the products in here.
* On the bottom left of the page customer can use a discount coupon code, right now  `DISCOUNT20` will give 20% off of the cart total (delivery is not included to the discount, it will be calculated from the full price).
* On the bottom right, you can see the order summary that shows Cart Total, Delivery and Grand Total. If there is discount coupon applied customer see the before and after the discount. 
* When the customer happy with their cart `Secure Checkout` button take them to the checkout page.

### **Checkout page**
* On the checkout page, customers are asked to fill in delivery details. The customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown just before the card details.
* On the right, the customer can see order summary and Order Total, Delivery and Discount (if there is any discount code applied)
* Once the customer filled up their details, they can `Complete Order` finilaze the purchase.

### **Checkout Success Page**
* A thank you message will be displayed after the checkout process and the table that holds the order details.
* Keep Shopping button is placed at the end of the page, and if the user has been logged into their account, Back to Profile will be shown.
### **My Profile Page**
* My Profile page is available for authenticated users and will be shown in the My Account Dropdown menu at the navbar which appears when user log into their account.
* In Profile Page, authenticated users can `Edit` Delivery Information and see Order History.

### **Product Management for Superuser**
* It is limited to authenticated superusers to see the admin page admin can:
  * add products,
  * edit products, 
  * delete products.
* If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

### **Features Left to Implement**
There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.



## **Technologies Used**

  * HTML


  * CSS


  * Javascript 


  * JQuery  Used for some of the main javascript functionality.

 

  * [Bootstrap](https://getbootstrap.com/)


  * [Google Fonts](https://fonts.google.com/) *Lato*, *Oswald*, *Monoton*


  
  * [Fontawsome](https://fontawesome.com/) for the event categories icon.


  * [Materializecss](https://materializecss.com/) for the designing the card and footer.

  
### **Back-End Technologies**
* Flask - Used as the microframework.
* Jinja - template to simplify displaying data from the backend of this project smoothly and effectively in html.
* Heroku - Used to host the application
* Python - The back-end programming language.
* Pymongo - Used to connect the python with the database.
* MongoDB Atlas - Used to store the database.
* PIP - for installation of tools needed in this project.


### **Database Schema**
The application uses MongoDB for data storage. MongoDB was chosen as the database to use due to the unstructured format of the data that will be stored within it.  
The data stored in the database are the following:

* Object  
* String  
* Array  
### **Data structure**  

#### Event_categories  
| Title         | 	Key in db	    |  Data type |  
| ------------- |:-----------------:|-----------:|
| event_id      |      _id          |ObjectId    | 
| event_name    | Event name        |String      | 
| event_picture | path to the image |String      |

#### Events

| Title             | Key in bd         | Data     |
| -------------     |:-----------------:| --------:|
| event_id          | _id               | ObjectId |
| organiser_name    | Name              |   String |
| event_description | Event description |   String |
| event_date        | Event date        | String   |
| guests            | attenders details | Array    |
## **Testing**
[W3C HTML Validator](https://validator.w3.org/).  


 [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

[JSHint](https://jshint.com/) 
I tested Python code with PEP8 using it as follow:

The autopep8 extension was installed in the workspace.

To install this enter this in the terminal:
`pip3 install --upgrade autopep8`
In order for autopep8 to run, pycodestyle is also required. To instlal pycodestyle, enter this command into the terminal:

`pip3 install pycodestyle`
Once these steps are complete, you can format the code into PEP8 formatting by entering this command into the terminal:

`autopep8 --in-place --aggressive --aggressive app.py`

I have recieved no error in the end of testing

## Bugs

## **Deployment**
#### To run this project locally

In order to run this project locally, you will need to install the following:

An IDE, such as VS Code
PIP to install the app requirements.
Python3 to run the application
GIT for version control
MongoDB to develop the database.
Once this is done, you will need to download the .ZIP file of the repository, unzip this file and then in the CLI with GIT installed, enter the following command:

`https://github.com/ozluna/meet-eco.git` 
Navigate to the to path using the cd command.

Create a .env file with your credentials. Be sure to include your MONGO_URI and SECRET_KEY values.

Install all requirements from the requirements.txt file using the following command:

  `sudo -H pip3 -r requirements.txt`


You should then be able to launch your app using the following command in your terminal:

  `python app.py`

## Remote Deployment
* Create a `requirements.txt` file using the terminal command  `pip3 freeze --local > requirements.txt` .
* Create a Procfile with the terminal command `echo web: python app.py > Procfile`.
* `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.
* Head over to Heroku
* Click the "new" button, give the project a name & set the region to Europe.
* From the Heroku dashboard of your newly created application, click on `"Deploy" > "Deployment method"` and select GitHub.
* Confirm the linking of the Heroku app to the correct GitHub repository.
* In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
* Set the following config vars:

| KEY           | VALUE                              | 
| ------------- |:----------------------------------:|
| IP            | 0.0.0.0                            | 
| PORT          | 5000                               |  
| MONGODBNAME   | <database_name>                    | 
| MONGO_URI     |mongodb+srv://:@<cluster_name> -qtxun.mongodb.net/<database_name> ?retryWrites=true&w=majority |              
| SECRET KEY    | `<your_secret_key>`                 |

* In the Heroku dashboard, click "Deploy".
* Your application should now be deployed.
## **Credits**
Product page card design and footer design from [MDB](https://mdbootstrap.com/)  
Scroll top feature is from [W3](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)  
Canva was used to create the logo [Canva](https://www.canva.com/)  
For Coupon code model and functionality I have used [protutorialplus](http://www.protutorialplus.com/django-shopping-cart), [JustDjango](https://www.youtube.com/watch?v=otoKdW-lYc8&t=539s)  tutorials   
For Review model and functionality [Onthir](https://www.youtube.com/watch?v=lSX8nzu9ozg&list=PLeyK9Dw9ShReHUdt5Nh2qlgF6keN6DI7z&index=32) tutorials  
Star rating [this website](https://webdesign.tutsplus.com/tutorials/a-simple-javascript-technique-for-filling-star-ratings--cms-29450)  
For responsiveness I used [Boostrap](https://getbootstrap.com/)  
For fonts I used [Google Fonts](https://fonts.google.com/)  


## **Acknowledgements**

In the process of finishing this website I used many resources, mainly; MDN web docs, W3Schools, Stack Overflow.  
Youtube channels such as Travers media, online resources [goalkicker](https://goalkicker.com), code institute videos and last but not least my mentor and tutors help.




