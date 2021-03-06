[![Build Status](https://travis-ci.org/hurter3/LionsTour2021SA.svg?branch=master)](https://travis-ci.org/hurter3/LionsTour2021SA)

# **British and Irish Lions tour of South Africa 2021**<br>

<div align="center">
    <img src="documentation/images/readme-header.png" alt="Readme header pic" aria-label="readme header pic" />
</div>

- [**Table of Contents**](#table-of-contents)
	- [**Lions Tour 2021 SA**](#lionstour2021sa)
	- [**Project Overview**](#project-overview)
    - [**Project Requirement**](#project-requirement)
	- [**UX**](#ux)
	- [**Project Details**](#project-details)
        - [Utilised Technologies](#utilised-technologies)
        - [Pages](#pages)
        - [Database updates](#database-updates)
    - [**Testing**](#testing)
        - [Code inspection](#code-inspection)
        - [Python testing](#python-testing)
        - [Travis testing](#travis-testing)
        - [Functional testing](#functional-testing)
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

## **Project overview**

*The British and Irish Lions tours encapsulate all areas of the exciting rugby union game.*
*I have chosen to do this project as there was a lack of sport through the Covid-19 pandemic and hence there would be a hunger from supporters to get involved.*
*The idea is to get the user registered and involved by entering the free score prediction competition with prizes.*
*They will need to register but not required to make any aditional purchases but as they get involved they might make an impulsive purchase.*
*Once they are registered, the additional maketing via emails can commence to keep the users informed with Ticket sales and tour progress to encourage them to visit the website and hopefully make further purchases.*<br>
*The landing page has a carousel of 4 images.*<br>
*This project offers CRUD capability where the user can register, login, update their profile or even delete their profile which will CASCADE across the competition and order models.*<br>
*There are 6 apps : accounts, cart, checkout, competition, home & products.*
*The products are added via the Django admin panel and not accessed by any user other than viewing the items through the website.*


## **Project Requirements**

- **Main Technologies to be used**

    - HTML, CSS, JavaScript, Python+Django
    - Relational database (recommending MySQL or Postgres)
    - Stripe payments
    - Additional libraries and APIs

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

*With the Covid-19 virus taking over our lives, sport has been forgotten. This project is designed to get the user involved with the Lions 2021 tour.*
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

## **Project Details**

### Utilised Technologies

#### Languages
- HTML5: As mark-up language
- CSS3: For styling
- JavaScript: To add functionality the front-end
- Python3: Back-end processing

#### Frameworks
- Django 1.11.29
- Bootstrap 4 

#### Database
- PostgresSql: Production Database from Heroku
- SQLite3: Test Database from Django

#### API
- Stripe - 2.47.0 : For payment processing


#### Other Tools
- jQuery: JavaScript library
- Github: hosts the website
- Git: version control
- Heroku: app Deployment
- Gunicorn - 20.0.4 : runs Python applications (web gunicorn LionsTour.wsgi:application)
- Travis CI: continuous integration
- AWS S3 Bucket: cloud storage
- Boto3 - 1.13.1: for the usage of Amazon S3
- botocore - 1.16.1
- Psycopg2 - 2.8.5: to connect Python to the database
- Pillow  - 5.4.1: stores images with the usage of django on the website
- Crispy Forms - 1.9.0 to style django forms
- [Favicon converter](https://favicon.io/favicon-converter/)


### Pages

- There are 18 pages to the project.

  - **Navigation**
    -   The same Navbar and feel is used for all the pages
    -   The user does not need to register or login to explore the website.
    -   The user will need to register and login if they wish to enter the competition or make a purchase.
    -   The same background image and form styling is used to register, login, Contact Us or change their email
    -   Every page uses the base.html extended capability.
    
- **Home app.**
    - ***Landing page (home.html)***
        -   The user is presented a carousel of 4 images to remind them of the passion the lions tour encompasses. 
   
    - ***Fan Zone, is a drop down list.***
        -   History page (history.html) 
            -   Which provides the rugby union passion, past and present statistics sourced completely from Wikipedia.
        -   Fixtures page (fixtures.html) 
            -   8 Match fixture table with some optional youtube footage.
        -   Tickets page (tickets.html)
            -   Although tickets are not available this is the latest update of the current status.
        -   Media page (Extenal link with a new tab) 
            -   An external link to build the excitment of the up and coming tour.

    - ***Contact Us page (contact.html)***
        -   A form that sends an email to lionssa33@gmail.com.
        -   Same background and form styling as register, login and change email pages. 
    
- **Accounts app.**
    -   This app was cloned from the e-commerce mini-project and tailored accordingly. 
        - ***Register page (register.html)***
            -   A form that captures username, email and password.
            -   This tab is only displayed when the user has not logged in.
            -   Same background and form styling as login, change email & contact us pages. 
        - ***Login page (login,html)***
            -   A form to enter your username and password.
            -   This tab is only displayed when the user has not logged in.
            -   Same background and form styling as register, change email and contact us pages. 
        - ***Account (profile.html)***
            -   A profile where the user can change their email and password. It will also list their order history which they can expand on. There is also a profile delete option which will CASCADE and delete any order, order items and competitions details.
            -   This tab is only displayed when the user is logged in.
        - ***Change Email (profile_change_email.html)***
            -   Same background and form styling as register, login and contact us pages.     
        - ***Order detail (order_detail.html)***
            -   This expands on an order with the order item listing.   
        - ***Logout (Logout.html)***
            -   Logs the user out and presents them with a screen similiar to the home page.
            -   This tab is only displayed when the user is logged in.
        - ***Delete profile***
            -   Deletes the users profile and any other models linked to the user (Competition, Order and OrderLineItem if applicable).
            -   The delete process does have a Confirmation modal to prevent it accidentally being triggered.

    - **Cart app**
        - ***cart.html***
            -   The listing of intended items to be purchased. This is held in the users session memory and accessible from any page until they power down.
            -   The user can update or delete any item before going to checkout.
            -   If the cart is clicked when empty then it will provide a user message and take them to a listing of all the products.

    - **Checkout app**
        - ***checkout.html***
            -   This take billing and card details to be processed by stripe to finalise the purchase.
            -   In this transaction, the order and order line items models are populated if athe correct details are provided otherwise the relavent error messages are displayed. 
            -   The checkout has 2 models.
                                class Order(models.Model):
                            
                            SUBMITTED = 'Submitted'
                            PROCESSED =  'Processed'
                            SHIPPED = 'Shipped'
                            CANCELLED = 'Cancelled'
                        
                            STATUS_CHOICES = [
                                (SUBMITTED, 'Submitted'),
                                (PROCESSED, 'Processed'),
                                (SHIPPED, 'Shipped'),
                                (CANCELLED, 'Cancelled'),
                            ]    

                            customer = models.ForeignKey(User, on_delete=models.CASCADE)
                            full_name = models.CharField(max_length=50, blank=False)
                            phone_number = models.CharField(max_length=20, blank=False)
                            country = models.CharField(max_length=40, blank=False)
                            postcode = models.CharField(max_length=20, blank=True)
                            town_or_city = models.CharField(max_length=40, blank=False)
                            street_address1 = models.CharField(max_length=40, blank=False)
                            street_address2 = models.CharField(max_length=40, blank=False)
                            county = models.CharField(max_length=40, blank=False)
                            date_ordered = models.DateTimeField(default=datetime.datetime.today, null=True)
                            total_quantity = models.IntegerField(blank=False)
                            total_cost = models.IntegerField(blank=False)
                            status = models.CharField(max_length=15,choices=STATUS_CHOICES,default=SUBMITTED)

                            def __str__(self):
                                return "{0}-{1}-{2}".format(self.id, self.customer, self.date_ordered)

                            def get_absolute_url(self):
                                return ('order_details', (), { 'order_id': self.id }) 

                        class OrderLineItem(models.Model):
                            order = models.ForeignKey(Order, null=False)
                            product = models.ForeignKey(Product, null=False)
                            quantity = models.IntegerField(blank=False)

                            def __str__(self):
                                return "{0} {1} @ {2}".format(
                                    self.quantity, self.product.title, self.product.price)

    - **Competition App (the fun zone to attract users to enter with the incentive to make a purchase)**
        - ***competition-rules.html***
            -   This is the competition main page that describes what the user needs to do to complete an entry form and how point are allocated with links to the terms and conditions and the entry form.
        - ***competition-terms.html***
            -   This contains the terms and conditions of the competition.
            -   The terms were used from last world cup but modified to the sites requirements.
        - ***competition.html***
            -   The user will need to have registered and logged in to enter the competition.
            -   If they have not entered before they will be presented with an empty form to add their score predictions.
            -   If they have enter the competition they will be presented with their predictions form which they can update until the day before the 1st match is played.
            -   There is date restriction by which all competition entries and changes need to be submitted by.<br>
                (Midnight 2 July 2021)

                    submit_date = datetime.date.today()
                    closing_date = datetime.date(2021, 7, 2)
                    if submit_date > closing_date:
                        messages.warning(request, 'Competition date closed')
                        return render(request, "competition.html",
                            {'form': form, 'points':points,'highest_points':highest_points,'total_entries':total_entries})
                    else:    
                        if request.method == "POST":
            -   I have added One entry form with newusers2 having 28 points to be displayed in the statistics section otherwise it won't look like it is required. Realistically this will be zero until the matches start.
            -   There will be a backend process to be run after every match to aggregate the users accrued_points. 
            -   In the model there is a home and away score for every match.
            -   As well as the matchpoints per game and the aggregate of each match being add to points_accrued.  
            -   First points scored is a selection list in the form in the Competition model

                    FIRST_POINTS_SELECT = (
                        ('NO POINTS SCORED', 'No Points Scored'),
                        ('HOME TEAM TRY', 'Home Team Try'),
                        ('HOME TEAM PENALTY', 'Home Team Penalty'),
                        ('HOME TEAM DROP GOAL', 'Home Team Drop Goal'),
                        ('LIONS TEAM TRY', 'Lions Try'),
                        ('LIONS PENALTY', 'Lions Penalty'),
                        ('LIONS DROP GOAL', 'Lions Drop Goal'),
                    )


                    class Competition(models.Model):

                        customer = models.ForeignKey(User, on_delete=models.CASCADE)
                        sascore1 = models.PositiveSmallIntegerField(default=0)
                        lionsscore1 = models.PositiveSmallIntegerField(default=0)
                        firstpoints1 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints1 = models.PositiveSmallIntegerField(default=0)
                        sascore2 = models.PositiveSmallIntegerField(default=0)
                        lionsscore2 = models.PositiveSmallIntegerField(default=0)
                        firstpoints2 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints2 = models.PositiveSmallIntegerField(default=0)
                        sascore3 = models.PositiveSmallIntegerField(default=0)
                        lionsscore3 = models.PositiveSmallIntegerField(default=0)
                        firstpoints3 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints3 = models.PositiveSmallIntegerField(default=0)
                        sascore4 = models.PositiveSmallIntegerField(default=0)
                        lionsscore4 = models.PositiveSmallIntegerField(default=0)
                        firstpoints4 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints4 = models.PositiveSmallIntegerField(default=0)
                        sascore5 = models.PositiveSmallIntegerField(default=0)
                        lionsscore5 = models.PositiveSmallIntegerField(default=0)
                        firstpoints5 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints5 = models.PositiveSmallIntegerField(default=0)
                        sascore6 = models.PositiveSmallIntegerField(default=0)
                        lionsscore6 = models.PositiveSmallIntegerField(default=0)
                        firstpoints6 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints6 = models.PositiveSmallIntegerField(default=0)
                        sascore7 = models.PositiveSmallIntegerField(default=0)
                        lionsscore7 = models.PositiveSmallIntegerField(default=0)
                        firstpoints7 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints7 = models.PositiveSmallIntegerField(default=0)
                        sascore8 = models.PositiveSmallIntegerField(default=0)
                        lionsscore8 = models.PositiveSmallIntegerField(default=0)
                        firstpoints8 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
                        matchpoints8 = models.PositiveSmallIntegerField(default=0)
                        points_accrued = models.PositiveSmallIntegerField(default=0)
                        
                        submit_date = models.DateField(default=datetime.date.today)    

                        def __str__(self):
                            return self.customer.username
                    


    - **Products App**
        - *** This is via the Shop tab on the navbar which has a drop down menu list of 5 categories.
            -   All Categories, Men's, Woman, Children and Souvenir's.
            - 
                        class Product(models.Model):
                        """ Model for product instances """

                        MEN = "Men"
                        WOMAN = "Woman"
                        CHILDREN = "Children"
                        SOUVENIRS = "Souvenirs"
                        CATEGORY_CHOICES = [
                            (MEN , "Men"),
                            (WOMAN , "Woman"),
                            (CHILDREN , "Children"),
                            (SOUVENIRS , "Souvenirs"),
                        ]
                        category = models.CharField(
                            max_length=20,
                            choices=CATEGORY_CHOICES,
                            default=MEN,
                        )
                        title = models.CharField(max_length=100,blank=True)
                        product_image1 = models.ImageField(upload_to="images", blank=True)
                        description = models.TextField()
                        price = models.DecimalField(max_digits=6, decimal_places=2) 
    
    - ***products.html (which is the listView)***
        -   This is generic code that takes a category argument and filters on All products or Men products or Women products or Children products or Souviners.
        -   Pagination is used for the user to navigate through the products.
    - ***product_detail.html (which is the DetailView)***
        -   This is expands on the selected item which the user can add to the cart.

    -   When a succesful order is placed it has a status of submitted. Pocessed, shipped and cancelled will be manually updated on the backend when staff process the orders. 

    
### Database updates (CRUD)

<table>
    <tr>
        <th>Models</th>
        <th>User</th>
        <th>Order</th>
        <th>OrderLineItem</th>
        <th>Competition</th>
        <th></th>
    </tr>
    <tr>
        <td>Initial DB data</td>
        <td> Superuser and backend users </td>
        <td> - </td>
        <td> - </td>
        <td> 1 sample form for competition statistics </td>
        <td></td>
    </tr>
    <tr>
        <td>Register</td>
        <td> Insert </td>
        <td> - </td>
        <td> - </td>
        <td> - </td>
        <td></td>
    </tr>
    <tr>
        <td>Login</td>
        <td>Retrieve user and check credientials</td>
        <td> - </td>
        <td> - </td>
        <td> - </td>
        <td></td>
    </tr>
    <tr>
        <td>Checkout</td>
        <td>Need to be registered</td>
        <td>Insert</td>
        <td>Insert</td>
        <td> - </td>
        <td></td>
    </tr>
    <tr>
        <td>View Account</td>
        <td>Retrieve and display user details</td>
        <td>Retrieve and list order history</td>
        <td> - </td>
        <td> - </td>
        <td></td>
    </tr>
    <tr>
        <td>View order</td>
        <td> - </td>
        <td>Retrieve and display details</td>
        <td>Retrieve and display details</td>
        <td> - </td>
        <td></td>
    </tr>
    <tr>
        <td>Change Email address</td>
        <td> Update </td>
        <td> - </td>
        <td> - </td>
        <td> - </td>
        <td></td>
    </tr>
     <tr>
        <td>Change Password</td>
        <td> Update </td>
        <td> - </td>
        <td> - </td>
        <td> - </td>
        <td></td>
    </tr>
     <tr>
        <td>Submit Competition Entry</td>
        <td> Need to be registered </td>
        <td> - </td>
        <td> - </td>
        <td> Insert </td>
        <td></td>
    </tr>
     <tr>
        <td>Modify Competition Entry</td>
        <td> Need to be registered </td>
        <td> - </td>
        <td> - </td>
        <td> Update </td>
        <td></td>
    </tr>
     <tr>
        <td>Delete Profile</td>
        <td> Delete </td>
        <td> Delete </td>
        <td> Delete </td>
        <td> Delete </td>
        <td></td>
    </tr>
</table>

<hr />

## **Testing**

### Code inspection 

- [W3C Markup Validation Service](https://validator.w3.org/)
    Due to Django being used I needed to run the app and then view the page source to cut and paste the code into the validator to check. 
    - All HTML page Output checked : Document checking completed. No errors or warnings to show.

- [JSHint](https://jshint.com/) 
    - Output :
        - stripe.js file
            - There are 3 functions in this file.
            - Function with the largest signature take 2 arguments, while the median is 0.
            - Largest function has 11 statements in it, while the median is 4.
            - The most complex function has a cyclomatic complexity value of 2 while the median is 1..
        - main.js file    
            - There are 3 functions in this file.
            - Function with the largest signature take 0 arguments, while the median is 0.
            - Largest function has 3 statements in it, while the median is 2.
            - The most complex function has a cyclomatic complexity value of 2 while the median is 1.

- [CSS Validator](http://csslint.net/)
    - Output - CSS lint found 0 errors and 13 warnings for "Disallow IDs in selectors" but the ID's were required and work so I have left them.

### Python Testing

#### How to run Python tests

To run the existing Python tests:
1. Activate your virtual environment.
2. In the terminal enter the following command:

python manage.py test

3. If you wish to run the tests within a specific app only you can specify: 

python manage.py test <app name here>

4. The test results will be shown within the terminal.

    I wrote tests to resolve all the Views and URLS, here are the results:
  
        gitpod /workspace/LionsTour2021SA $ python3 manage.py test
        Database URL not found. Using SQLite instead
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        Ran 35 tests in 0.271s

        OK 
        Destroying test database for alias 'default'...



### Travis

- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site. The [Travis Documentation](https://docs.travis-ci.com/) provides all the info needed to set it up.
- I set the heroku deployment settings for this project to only allow deployment when the travis had passed the latest push to the master branch on GitHub.

### Functional Testing

<table>
    <tr>
        <th>Action</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Clicking on badge on the left of the navbar takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Clicking on Home tab takes user to homepage</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Clicking on the Fan Zone tab will display a menu list</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Click on Shop will display a list of categories to choose from.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Pagination will display First, Previous, Page counter, Next and Last for the appropriate page.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>Selecting the title link of an item take you to the detail view.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>If the user adds an item to the cart there will be a badge counter on the right of the cart.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The badge counter is adjusted when the user make any updates to their cart.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The continue button will take the user back to shopping.</td>
        <td>Successful</td>
    </tr>
     <tr>
        <td>The checkout button will display a form to capture billing and card details.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>If the user has previously placed an order their billing details will be pre populated.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>To process a payment you can use a test credit card 4242 4242 4242 4242 with 111 as test security code and a valid future date. </td>
        <td>Successful</td>
    </tr>
     <tr>
        <td>Once the user has placed their order they will receive an appropriate message and if successful they will see the order listed in their account.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>At any time if the cart is clicked it will display the items in the shopping cart otherwise provide a message that the basket is empty and display a product listing.</td>
        <td>Successful</td>
    </tr>
        <td>The badge counter is adjusted when the user make any updates to their cart.</td>
        <td>Successful</td>
    </tr>
     <tr>
        <td>When the competition tab is clicked the user will be displayed the rules about entering with 2 links, 1 being terms and conditions and the other the entry form.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The entry form has required fields which must be filled in and submitted.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>If a user has entered the competition they will be presented with their predicted scores which they can change an re-submit.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The accounts tab will display the users profile with a list of past orders with links to expand on the details.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The delete profile button will delete the user / competition entry and any order history but with a conrirmation modal.</td>
        <td>Successful</td>
    </tr>
    <tr>
        <td>The 'Contact us' tab will display a form for the user to email the company.</td>
        <td>Successful</td>
    </tr>
</table>


### General Testing

While developing I used DEBUG=TRUE to help iron out all the routing and undefined issues.
Print and console.log were extensively used to ensure the correct data was being passed.
The developer tool was used to test various media sizes so the elements gave a good UX.  
Tested with different input data and selections to ensure the appropriate messages were displayed.

[**To top**](#Table-of-Contents)


<hr />

## **Deployment**

This project was developed in Gitpod with the committed code being pushed to Github to maintain version control as features were developed.
The project is hosted on [Heroku](https://heroku.com) which was linked to Github for automatic updated:

  - created requirements.txt (https://github.com/Hurter3/LionsTour2021SA/requirements.txt) that **Heroku** knows which packages are required for the application to run and install them.
  - created Procfile (https://github.com/Hurter3/LionsTour2021SA/master/Procfile) that **Heroku**  knows what kind of application it is.

  - **Settings**
    - Added **Config Vars**
      - IP
      - PORT
      - STRIPE_PUBLISHABLE
      - STRIPE_SECRET
      - SECRET_KEY
      - DATABASE_URL
      - AWS_STORAGE_BUCKET_NAME
      - AWS_S3_REGION_NAME
      - AWS_ACCESS_KEY_ID
      - AWS_SECRET_ACCESS_KEY
      - EMAIL_HOST
      - EMAIL_HOST_USER
      - EMAIL_PASSWORD
      - EMAIL_PORT
      - DISABLE_COLLECTSTATIC

    - **Deploy**

Ensure in your app you have in your app files in GitHub a Procfile with the following: 'web: python app.py', and you project requirements in a requirements.txt file.
In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy.
Choose either automatic or manual deploys.

Install requirements with $ pip3 install -r requirements.txt
Run the app with $ python3 manage.py runserver
          
[**To top**](#Table-of-Contents)

<hr />

## ** Known issues ** 

            remote: 
            remote: GitHub found 3 vulnerabilities on hurter3/LionsTour2021SA's default branch (2 moderate, 1 low). To find out more, visit:
            remote:      https://github.com/hurter3/LionsTour2021SA/network/alerts
            remote: 

            3 pillow vulnerabilities found in requirements.txt on May 5
            Remediation
            Upgrade pillow to version 6.2.2 or later. For example:

            pillow>=6.2.2

-   I investigated and found that Pillow was 5.4.1 in my requirements file but if i changed it to 6.2.2 then Travis failed so I left it at 5.4.1   

## **Future Enhancments**

-   Expand on the product detail view to incorporate size selection and add additional thumbnails.
-   Incorporate stock management and control.
-   Automate the backend process to aggregate each users accrued_points after every match played.

<hr />


[**To top**](#Table-of-Contents)

## **Credits**

The code institute tutors must be mentioned for their valuable recomendations and patience. <br>
The guidance from my mentor Aaron Sinnott was valuable.<br>
I used www.w3schools.com , www.stackoverflow.com and youtube tutorials from Corey Schafer and JustDjango in conjuction with the CI mini projects. <br>
The product images where sourced from google image searches with no copyright restictions that I could see. I received approval from Cantebury the main product supplier. I also received approval from @Lionsrugby.com to use their badge logo for internal use.<br>
All images in this project are for educational use only.  


<hr />

<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">


[**To top**](#Table-of-Contents)