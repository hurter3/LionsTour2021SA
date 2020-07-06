[![Build Status](https://travis-ci.org/hurter3/LionsTour2021SA.svg?branch=master)](https://travis-ci.org/hurter3/LionsTour2021SA)

<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# **British and Irish Lions tour of South Africa 2021**<br>


- [**Table of Contents**](#table-of-contents)
	- [**Lions Tour 2021 SA**](#lionstour2021sa)
	- [**Project Requirement**](#project-requirement)
	- [**UX**](#ux)
	- [**Project Overview**](#project-overview)
			- [Database](#database)
			- [Pages](#pages)
    - [**Testing**](#testing)
			- [Code inspection](#code-inspection)
			- [Navigational testing](#navigational-testing)
            - [Database updates](#database-updates)
			- [General Testing](#general-testing)
     - [**Deployment**](#deployment)
     - [**Future Enhancements**](#future-enhancements)
     - [**Credits**](#credits)
<hr />

## **Lions Tour 2021 SA**

Welcome to my Full Stack Frameworks with Django Milestone Project as part of my [Code Institute (CI)](https://courses.codeinstitute.net/) course.<br>
The github repository is: https://github.com/hurter3/LionsTour2021SA.<br>
Heroku git URL is https://git.heroku.com/lionstour2021sa.git<br>
Final deployed site is here: https://lionstour2021sa.herokuapp.com/<br>
<hr />

## **Project Requirements**

- **Main Technologies**
    ## Utilised Technologies
### Languages
- HTML5: As mark-up language
- CSS3: For styling
- JavaScript: To add functionality the front-end
- Python3: Back-end processing

### Frameworks
- Django 1.11.24
- Bootstrap 4 

### Database
- PostgresSql: Production Database from Heroku
- SQLite3: Test Database from Django

### API
- Stripe: For payment processing


### Other Tools
- jQuery: JavaScript library
- Github: hosts the website
- Git: version control
- Heroku: app Deployment
- Gunicorn: runs Python applications
- Travis CI: continuous integration
- AWS S3 Bucket: cloud storage
- Boto3: for the usage of Amazon S3
- Psycopg2-Binary: to connect Python to the database
- Pillow: stores images with the usage of django on the website
- Crispy Forms
- [Favicon converter](https://favicon.io/favicon-converter/)

### Validators
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

- **Mandatory Requirements**
  - Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
  - Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
  - Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course
  - User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
  - User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
  - Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
  - Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
  - Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
  - Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
  - Version Control: Use Git & GitHub for version control.
  - Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
  - Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
  - Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.


<hr />

## **UX**

*With the Covid-19 vius taking over our lives, sport has been forgotten. This project is designed to get the user involved with the Lions 2021 tour.*
*The user,*<br>
*does not need to register or login to explore the website.*<br>
*does not need to register or login to shop or add items to their cart.*<br>
*does not need to purchase any items.*<br><br>
*The user will need to register and login,*<br>
*if they need to checkout and pay for products in their cart.*<br>
*if they would like to enter the free score prediction competition.*<br>
*to view their account and order history or to change their email address or password.*<br>
*The user, will be able to amend or delete any items in their cart while the session is available before they checkout.*<br>
*If the user has entered the competition they can view their entry form and amend it until the start of the first match.*<br>
*If the user has previously ordered something their billing details will be pre-populated when they purchase additional items.*<br>  


## **Project overview**

*The British and Irish Lions 2021 tour is to get the user involved with the excitement of this event and offer them the opportunity to puchase items.*
*The landing page has a carousel of 4 images.*<br>
*This project offers CRUD capability where the user can register, login, update their profile or even delete their profile which will CASCADE accross the competition and order models.*
*There are 6 apps : accounts, cart, checkout, competition, home & products.*

### Pages

- There are 12 pages to the project.

  - **Navigation**
    - The same Navbar and feel is used for all the pages
    - The user does not need to register or login to explore the website.
    - The user will need to register and login if they ish to enter the competition and make a purchase.
    - The same background image and form styling is used to register, login, Contact Us or change their email
    - Every page uses the base.html extended capability.
    
  - **Home app.**
    - ***Landing page (home.html)***
        - The user is presented a carousel of 4 images to remind them of the passion the lions tour encompasses. 
   
    - ***Fan Zone, is a drop down list.***
        - History page (history.html) 
            - Which provides the rugby union passion, past and present statistics sourced completely from Wikipedia.
        - Fixtures page (fixtures.html) 
            - 8 Match fixture table with some optional youtube footage.
        - Tickets page (tickets.html)
            - Although tickets are not available this is the latest update of the current status.
        - Media page (Extenal link with a new tab) 
            - An external link to build the ecitment of the up and coming tour.
    - *** Contact Us page (contact.html) ***
        - A form that sends an email to lionssa33@gmail.com (and it works).
        - Same background and form styling as register, login and change email pages. 
    - *** Register page (register.html) ***
        - A form that captures username, email and password.
        - This tab is only displayed when the user has not logged in.
        - Same background and form styling as login, change email & contact us pages. 
   - *** Login page (login,html) ***
        - A form to enter your username and password.
        - This tab is only displayed when the user has not logged in.
        - Same background and form styling as register, change email and contact us pages. 
    - *** Account (profile.html) ***
        - A profile where the user can change their email and password. It will also list their order history which they can expand on. There is also a profile delete option which will CASCADE and delete any order, order items and competitions details.
        - This tab is only displayed when the user is logged in.
    - *** Change Email (profile_change_email.html) ***
        -  Same background and form styling as register, login and contact us pages.     
    - *** Order detail (order_detail.html) ***
        - This expands on an order with the order item listing.   
    - *** Logout ***
        - Logs the user out and presents them with a screen similiar to the home page.
        - This tab is only displayed when the user is logged in.

  - **Add page (addreview.html)**
    - The username and movie title will be prepopulated and read only fields.
    - The Genre and rating selection boxes are mongoDB collections.
    - The Add review will add the review to the reviews collections and display the reviews screen.
    - When the user navigates to the home page the movie they reviewed will be the FIRST in the listing and badge count will be incremented.

  - **Edit page (editreview.html)**
    - This presents the user with the ability of changing their review or rating.

  - **Delete page (deletereview.html)**
    - The user can only delete their own review and will be presented a confirm / cancel modal **still to be built**.

  - **Delete Confirm page (deletconfirm.html)**
    - Confirm or cancel the delete functionality.
  
  - **Search page (search.html)**
    - The user can search for a title or part of a tile / person that does a API get to TMDB (The Movie Data Base - open) and present the user with a listing. If they select a movie that has is has reviews in the mongoDB collection then they will be presented the reviews page otherwise they will be display the addreview screen to entice the user to write a review.
  
  - **Login page (login.html)**
    - Displays the login screen for a username and password that has appropriate flash messages.

  - **Register page (register.html)**
    - Displays a basic register page username,password and confirm password that has appropriate flash messages but the password is just a visible string in the users collection and merely used to control the ability for users to add, edit or delete reviews.


<hr />

## **Testing**

### Code inspection 

  - [W3C Markup Validation Service](https://validator.w3.org/)
    Due to using Flask I needed to run the app and then view the page source to cut and paste the code into the validator to check. 
    - Output : Document checking completed. No errors or warnings to show.

  - [JSHint](https://jshint.com/) 
    - Output :

    There are 5 functions in main.js.
    Function with the largest signature take 1 arguments, while the median is 1.
    Largest function has 26 statements in it, while the median is 4.
    The most complex function has a cyclomatic complexity value of 7 while the median is 1.
    26 warnings.

#### Navigational Testing

<table>
    <tr>
        <th>Action</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Clicking on Movie Review Hub title takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Clicking on Home tab takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Clicking on Search takes user to search form</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Click on Access provides the Login and Register dropdown to relevant pages.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>On home page clicking on any movie will take you to the reviews page.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>On reviews page clicking on 'add' will take you to add review page with 2 buttons.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>On reviews page there will be a edit and delete button for all reviews made by the user and NOT for any other user.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The delete button will take you to a delete confirmation screen.</td>
        <td>Successful</td>
    </tr>
</table>

#### Database updates

<table>
    <tr>
        <th>Collections</th>
        <th>Movie</th>
        <th>Reviews</th>
        <th>Users</th>
        <th>Categories</th>
        <th>Ratings</th>
    </tr>
    <tr>
        <td>Initial DB data</td>
        <td> - </td>
        <td> - </td>
        <td> - </td>
        <td>Selection List</td>
        <td>Selection List</td>
    </tr>
    <tr>
        <td>Register</td>
        <td> - </td>
        <td> - </td>
        <td>Insert</td>
        <td> - </td>
        <td> - </td>
    </tr>
    <tr>
        <td>Add review</td>
        <td>Insert reviews_count set to 1</td>
        <td>Insert</td>
        <td>Update review_made incremented</td>
        <td> - </td>
        <td> - </td>
    </tr>
    <tr>
        <td>Add 2nd review</td>
        <td>Update reviews_count incremented</td>
        <td>Insert</td>
        <td>Update review_made incremented</td>
        <td> - </td>
        <td> - </td>
    </tr>
    <tr>
        <td>Delete review</td>
        <td>Update reviews_count decreased</td>
        <td>Delete</td>
        <td>Update review_made decreased</td>
        <td> - </td>
        <td> - </td>
    </tr>
    <tr>
        <td>Delete 2nd review</td>
        <td>Delete</td>
        <td>Delete</td>
        <td>Update review_made decreased</td>
        <td> - </td>
        <td> - </td>
    </tr>
</table>


#### General Testing

While developing I used DEBUG=TRUE to help iron out all the routing and undefined issues.
Print and console.log were extensively used to ensure the correct data was being passed.
The developer tool was used to test various media sizes so the elements gave a good UX.  
Tested with different input data and selections to ensure the appropriate FLASH messages were displayed.

[**To top**](#Table-of-Contents)


<hr />

## **Deployment**

In your Heroku account, create a new app.
GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.
The site has been deployed using Heroku. The process for deploying to Heroku is as follows:

  - created [requirements.txt](https://github.com/Hurter3/MovieReviewHub/requirements.txt) that **Heroku** knows which packages are required for the application to run and install them.
  - created [Procfile](https://github.com/Hurter3/MovieReviewHub/master/Procfile) that **Heroku**  knows what kind of application is this.

  - **Settings**
    - Added **Config Vars**
      - IP `0.0.0.0`
      - PORT `5000`
      - MONGO_URI
      - SECRET_KEY
      - APIKEY

    - **Deploy**

Ensure in your app you have in your app files in GitHub a Procfile with the following: 'web: python app.py', and you project requirements in a requirements.txt file.
In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy.
Choose either automatic or manual deploys.

Install requirements with $ pip3 install -r requirements.txt
Run the app with $ python3 manage.py runserver
          
[**To top**](#Table-of-Contents)

<hr />

## **Future Enhancments**

ERROR handling and introduce TV programs.

<hr />


[**To top**](#Table-of-Contents)

## **Credits**

The code instute tutors must be mentioned for their valuable recomendations and patience.<br>
Appreciation must also be said to The Movie DataBase (TMDB) for their open API data which was used for this project.
I used www.w3schools.com and www.stackoverflow in conjuction with the CI Task manager mini project for the accordian effect.
The favicon was generated by using https://www.favicon-generator.org/.

<hr />


[**To top**](#Table-of-Contents)