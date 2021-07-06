

# Table of Contents
1. [Example](#example)
2. [Example2](#example2)
3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)


## Example
## Example2
## Third Example
## [Fourth Example](http://www.fourthexample.com) 
# **EcoShop**

The plastic waste is a big problem for our world and it is one of the biggest factor to climate change from when it is produced to going to our bins, unfortunately governments and big companies are not taking effective action therefore it is down to us to show them we are choosing zero waste path as an indivual. EcoShop is offering the alternative products to use in our daily lives from toothbrush to shampoos

# Table of Contents

1. [User Experience](#User-Experience)

    - [Goals](#Goals)
      - [Visitor Goals](#Visitor-Goals)
      - [Busines Goals](#Busines-Goals)





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
* to recieve an email after registering
* to be able to leave product reviews.
* to be able to search product with keywords.
* to be able to sort the products by categories ore price for efficient search.
*  to be able to select quantity of the product to add to the cart.
* to be able to contact to the business owner if any problem arise

As a owner I would like
* 
* 
* 
* 

## **Design**
---
### **Colour**
![(readme-doc/EcoShoppalette.png)](readme-doc/EcoShoppalette.png)

* I have created the color palette using the hero image on the website with [colors.co](https://coolors.co/006d77-83c5be-edf6f9-ffddd2-e29578) palette creator for holistic view 
*  
### **Strategy**

I wanted to answer users common questions such as "Is this what I expected to see?", "Does it offer what I want?",
"Is it valuable enough for me to return?". 
For this website I aimed to create an user friendly, intiuitive structure. To do that I tried to create a simple but visually appealing website

### **Scope**

  


### **Structure**






### **Skeleton**


### **Surface**
 




## **Features**
### **Existing Features**





### **Features Left to Implement**



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




