# **Testing**

## **Automated Testing**
[W3C HTML Validator](https://validator.w3.org/) used to validate the html codes (I ignored the error cused by jinja).  


 [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  
 [CSS Beautifier](https://codebeautify.org/css-beautify-minify)

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

User Stories Tested:
AS A/AN	I WANT TO BE ABLE TO ...	SO THAT I CAN...
Site User/ Shopper	access the website with any devices	Use the website anytime and anywhere
Shopper	All the important services are accessible from nav bar	Don't need to scroll to find important information
Shopper	Have a shopping cart icon on nav bar	Always check the current order and checkout when I want
Test conducted:
Access each page in the site with different screen sizes with Google Dev Tool's Emulator and check the layout and format of site elements
Result:
Navbar: I have the search bar collapsed for smaller than medium screen size (width < 992px) because the search bar with input field conflicted with other navbar components. 'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
Home page: The image size responsiveness on Carousel at landing(home) page was adjusted by media queries.
Verdict:
Passed all tests.

Landing Page
User Stories Tested:
AS A/AN	I WANT TO BE ABLE TO ...	SO THAT I CAN...
Shopper	Easily see what services are offered	Find the service I want to use