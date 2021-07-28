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