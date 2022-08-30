<h1 align="center">JOYFULBOOKSTORE</h1>


<p align="center">
<img src="assets/documents/README_docs/responsive-site.png" width="800" height="100%">
</p>


# Table of Contents

1. [UX](#ux)

   - [Strategy](#strategy)
   - [User Stories](#user-stories)

2. [Scope](#scope)

   - [Features](#features)
   - [Future Features](#future-features)

3. [Structure](#structure)

   - [Sitemap](#sitemap)
   - [Wireframes](#wireframes)
   - [Database schema](#database-schema)
   - [Business Model](#business-model)
   - [Marketing](#marketing)

4. [Surface](#surface)

5. [Technologies Used](#technologies-used)

6. [Testing](#testing)

7. [Bugs](#bugs)

8. [Deployment](#deployment)

9. [Credits](#credits)

responsive image and link to live site

# About

This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript. I created a website for 'JoyfulBookstore' which is designed to sell children's books

# UX

## Strategy

Using the core UX principles I first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'JoyfulBookstore' are:

- adults who buy books for their children. It can be parents, uncles, aunts, grandparents, teachers - anyone

These users will be looking for:

- An informative website, with information that is easy-to-find & concise
- A website that offers children's books
- Ability to view & purchase books that are for sale
- Ability to make a user account in order to see billing history, make whishlist and write reviews
- A way to sign up for the bookstore newsletter

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories

**Epic: Admin/Store Owner**

| ID  | Content                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | As a **store owner** I can log in so that I have full access to the store backend                                                                         |
| 2   | As a **store owner** I can add new product to the shop so that I can make sure the website is up to date                                                  |
| 3   | As a **store owner** I can add new categories to the shop so that I can make sure the website is up to date                                               |
| 4   | As a **store owner** I can add FAQ's to the site so that I can make sure that the user can find answer on the page before contacting the customer         |service                                                                                                                                                           |
| 5   | As a **store owner** I can edit/delete products so that I can make sure the website is up to date                                                         |
| 6   | As a **store owner** I can edit/delete categories so that I can make sure the website is up to date                                                       |
| 7   | As a **store owner** I can edit/delete questions so that I can provide users with information about common questions and concerns                                                                                                                                                          |
| 8   | As a **store owner** I can send out a newsletter via email so that I keep customers updated with new books                                                |
| 9   | As a **store owner** I have created Facebook shop page to increase traffic on my website                                                                  |
| 10  | As a **store owner** I can read and respond to users questions send by contact form                                                                       |
| 11  | As a **store owner** I can unsubscribe subscribers from newsletter                                                                               |

**Epic: Navigation**

| ID  | Content                                                                                                                      |
| --- | ---------------------------------------------------------------------------------------------------------------------------- |
| 12  | As a **user** I can see an interesting home page so that I can understand what shop sells                                    |
| 13  | As a **user** I can easily navigate through the site so that I can view desired content                                      |
| 14  | As a **user** I can easily find a navigation bar and footer so that I can see what content there is on the website           |
| 15  | Aa a **user** I can easily see the products list so that I can see what the store has to offer                               |
| 16  | As a **user** I can search products by category so that I can easily find what I'm looking for                               |
| 17  | As a **user** I can sort products by rating, price and name so that I can easily find what I'm looking for                   |
| 18  | As a **user** I can search for products using the search form so that I can find the products I'm specifically looking for   |
| 19  | As a **user** I can see the book details page so that I can see the book name, rating, price, short description and ratings  |
| 20  | As a **user** I can read the FAQ's so that I can find the answer to my question or concern before contacting the bookstore   |

**Epic: Purchase**
| ID | Content |
| --- | ----------- |
| 21 | As a **user** I can select the quantity of the desired product so that I can buy more product of the same kind
| 22 | As a **user** I can add a selected book into the shopping bag so that I can keep track of what I am spending
| 23 | As a **user** I can see the shopping bag summary and total cost so that I can see how much I will spend
| 24 | As a **user** I can remove items from shopping bag so that I don't buy what I don't want
| 25 | As a **user** I can put in my card details so that I can pay for my goods
| 26 | As a **user** I receive order confirmations so that I can be sure my order has been processed

**Epic: User Interaction**

| ID  | Content                                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 27  | As a **user** I can see rating and reviews so that I can read the opinions of other users                                              |
| 28  | As a **user** I am notified about any changes I have made so that I have a clear understanding of what has been completed/updated      |
| 29  | As a **user** I can connect to the social media sites so that I can follow them and keep up to date with their products and promotions |
| 30  | As a **user** I can sign up for the website's newsletter so that I can keep up to date with new products and promotions                |
| 31  | As a **user** I can unsubscribe from newsletter if I don't want to receive stors newsletters                                           |
| 32  | As a **user** I can contact the bookstore so that I can find out any information that I require                                        |
| 33  | As a **user** I can receive a contact confirmation email to let me know that my email has been sent                                    |
| 34  | As a **logged-in User** I can leave reating and reviews so that I can share my experience with others                                  |
| 35  | As a **logged-in User** I can save selected products to my whishlist for later purchase                                                |

**Epic: Accounts**

| ID  | Content                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------ |
| 36  | As a **user** I can easily see if I'm logged-in or logged-out so that I can be sure what my status is                    |
| 37  | As a **user** I can log in/out off my account if I wish so that I can connect or disconnect from the website             |
| 38  | As a **user** I can register for an account so that I can use features for logged-in users                               |
| 39  | As a **user** I can receive a confirmation email when creating an account so that I know the registration was successful |
| 40  | As a **logged-in User** I can have my details saved so that I don't have to retype my address every time                 |

# Scope

## Features

### **Home Page**

_Navigation bar:_

- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'All Books', 'Categories', 'Special Offers and icons for search bar, account and shopping bag

_Account - Login/Register:_

- The Login/Register feature is located in the upper right corner and offers the user to log in or register for an account as well as log out of the site
- When the user is logged in links for 'Login' and 'Register' will change to 'My Profile', 'Logout' and add Whishlist
- The admin user has extra access that allow them to add, update and remove books from the store

_Shopping bag:_

- The shopping bag is also situated on the top right corner of the site and it is always visible for the user throughout all the pages. With one click they can access their shopping bag to see what is in there, update the quantities of book they wish to purchase or to delete them from the shopping bag
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size


_Footer:_

- Appears on every page and contains FAQ's, Shipping Info, Privacy Policy, Subscribe form, Contact Link and Social links
- Social links are opened in a new tab to avoid dragging users from our site


<p align="center">
<img src="assets/documents/README_docs/gifs/home-page.gif" width="900" height="100%">
</p>

### **User Profile**

- A logged-in user can access the My account link, this page displayed links to personal details, previous orders and wishlist
- The personal details page is where the user can update their default shipping/billing address, change email address and password
- The previous order displays a list of all the orders previously made by the user
- Wishlist displays the list of items the user has saved to their wishlist, with the ability to remove the product

<p align="center">
<img src="assets/documents/README_docs/gifs/user-profile.gif" width="900" height="100%">
</p>



### **Admin**

- Admin can preform full CRUD functionalliy without having to enter the default 'admin panel' from django
- Admin can add books from 'Book Managment' link in the account menu from the navigation bar
- Admin can add category from 'Book Managment' link
- Admin can add FAQ's from 'FAQ's' link
- Admin can send Newsletter to subscribed users
- Admin can unsubscribe user
- Admin can edit/delete books from all books page and books details page
- Admin can edit/delete category from 'Category Management' link
- Admin can edit/delete FAQ from 'FAQ Managemnt' and FAQ's page, mark them as published or draft

<p align="center">
<img src="assets/documents/README_docs/gifs/admin.gif" width="900" height="100%">
</p>


### **All Books**

- The All Books page shows all the books that the bookstore sells
- Each book has an image, book title, author, rating and price
- Each book card takes users to the book details page

<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic_navigation/book-list.png" width="900" height="100%">
</p>

### **Categories**

- Categories dropdown from Navbar, allowing the user to access specific categories
- Categories:
  - Board Books
  - Pitcure Story Books
  - First Reads
  - Early Readers
  - Fiction Books
  - Non Fiction Books



### **Special Offers**
- Special Offers dropdown from Navbar, allowing the user to access specific offer
- From the dropdown menu user can select :
    - Sale
    - New arrivals

### **Book Details Page**

- The Book Details Page displays all the information about the selected book
- Page main body of the page will display book cover image, title, rating, author, book type, size, suitable for ages, category, description
- After the main body content user can select quantity and add product to the shopping bag or whishlist
- Review section is located at the end of the page, only logged in users can leave a comment

<p align="center">
<img src="assets/documents/README_docs/gifs/book-details.gif" width="900" height="100%">
</p>

### **Checkout Page**

- The checkout page is accessible through the shopping bag
- Once the site users have made their last decision about what to purchase and they are happy with it. At the checkout the site user can enter and save their personal details and see a summary of what they are about to purchase before entering their card details
- If the checkout was successful the user is taken to the 'checkout success' page, which displays the order number and delivery details

<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic_purchase/order-confirmation.png" width="600" height="100%">
</p>


### **Shopping Bag**

- The shopping bag page provides an overview of all of the items added by the user
- The information is displayed in a table that has product name, image, quantity, price and subtotal
- The user can amend the quantity of each product and also remove it whilst on this page
- Buttons to proceed to the checkout or to keep shopping are located at the end of the page

<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic_purchase/shopping-bag.png" width="600" height="100%">
</p>


## Future Features

- Gift Card
- School and craft materials
- Stock app
- Owner can see send newsletters

#

# Structure

In the children's book market, the target audience isn't made up of children but the bigs who purchase the books for them. That might be parents, uncles, aunts, grandparents,teachers — whomever so the structure idea for JoyfullBookstore was to keep it simple. Simplicity helps users to quickly and easily access the app and navigate within the app.

The website is made from 8 apps:

- Books
- Checkout
- Home
- Newsletter
- Profiles
- Questions
- Shopping Bag
- Wishlist

# Sitemap

<p align="center">
<img src="assets/documents/README_docs/sitemap.png" width="1000" height="100%">
</p>

- Full CRUD functonality for Category model was added lately in the project, correct site map should containe "Add Category" at "Store Owner Account" page

# Wireframes

All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:

- [Desktop](assets/documents/README_docs/Desktop-wireframes.pdf)
- [Mobile](assets/documents/README_docs/Mobile-wireframes.pdf)

# Database schema

<p align="center">
<img src="assets/documents/README_docs/database.png" width="1000" height="100%">
</p>

- I added the category to the database later so the admin could have full CRUD functionality

# Business Model

The business model for this store would be a B2C (Business to Customer) model, as the business would be selling products directly from themselves to the customer

# Marketing 
- Links to all the social media sites can be found both inside the footer and on the contact page.
- The facebook link takes you to the Dry Drops business page which can be found [here](https://www.facebook.com/JoyfulBookstore.Dublin).


<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic-admin/facebook-page-bookstore2.png" width="1000" height="100%">
</p>

- The newsletter sign up form can also be found in the footer

<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic_navigation/footer.png" width="1000" height="100%">
</p>

# Search Engine Optimisation
I have created a sitemap.xml and robots.txt file to help aid search engines locate the site. To keep user's information safe, any pages that could contain sensitive information has been disallowed in the robots.txt.


# Surface

## Design choice
Bootstrap provides a flexible framework for building upon and wherever possible its structure has been used and modified to achieve the desired functionality and feel.

## Color schema

The color scheme is green, because it is neutral and the page looks cheerful, the combination of white, green and gray gives the page a nice but also cheerful look

Color pallet from [Colors](https://coolors.co/139035-696969-ffd700-d7b500-252525)

- #139035 - green color for site logo
- #252525 - footer color, fit nicely with the page
- #FFD700- used for sale and new labels
- #D7B500 - used for review stars
- #252525 - used for btn hover background

<p align="center">
<img src="assets/documents/README_docs/color-palett.png" width="1000" height="100%">
</p>

The aim was to provide a solid colour base which could bring the other elements on the site to life.

## Fonts 
- Playfair Display - welcome message heading, modal title and navbar-brand
- Roboto Slab - nav and footer links 
- Work Sans - main font 


# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)




## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[AWS](https://aws.amazon.com/) – was used to store static files 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[jQuery](https://jquery.com/) - Used to write JS code

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

## Extensions 

[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - was used to to create, configure, and manage AWS services

[Pillow](https://pillow.readthedocs.io/en/stable/) - This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

[Stripe](https://stripe.com/docs) - was used to make and process payments


# Testing 

Testing and results can be found [here](TESTING.md).

## Deployment

### Github

First you will need to create a new repository.

1. Log into Github.
2. On the 'Repositories' tab click 'New'. This takes you to the create a new repository page.
3. Name the repository and click 'Create repository'.
4. Your new repository is now set up and ready to use.

#### Forking

To fork the project you must;
1. Sign in to Github and go to my [repository](https://github.com/Iris-Smok/JoyfulBookstore-PP5)
2. Locate the Fork button at the top right of the page.
3. Click the button then click 'Create fork'. 
4. The fork is now in your repositories.

#### Clone
To clone the project you must;

1. Sign in to Github and go to my [repository](https://github.com/Iris-Smok/JoyfulBookstore-PP5)
2. Above the list of files click 'Code'.
3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
4. Open git bash
5. Type 'git clone' and then paste the URL you copied. Press Enter.

For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Django

This project uses the Django framework. To install django, follow these steps:

1. In your IDE type the command:  
    `pip3 install django`
2. Then to name your project type:  
    `django-admin startproject *Your project name here*`  
This will add your django project folder to your file explorer
3. Next you will need to add a gitignore file. To do this enter the command line:  
    `touch .gitignore`
4. Inside this file add these 3 lines:  
    ``` 
    *.sqlite3
    *.pyc
    __pycache__
    ```
5. To check everything is up and running, run the command:  
    `python3 manage.py runserver`
    This should expose port 8000. Open that port and you should be welcomed by Django's success page.
6. Next you need to perform the initial migrations. This is done by running the command:
    `python3 manage.py migrate`
7. Finally, in order to have access to the admin panel you will need to create a superuser. This is done by running the command:
    `python3 manage.py createsuperuser`
    This will then ask you to create a username and password with an optional email address.
8. Once these steps are completed you can push your changes to github by running the commands, in order:
    ```
    git add .
    git commit -m "initial commit"
    git push
    ```

#### All Auth

Inside the django framework is a package called Allauth. This package handles all the registration and sign in processes. The steps to install Allauth can be found [here](https://django-allauth.readthedocs.io/en/latest/installation.html).



### Heroku

Heroku is used to deploy the final project.

1. First you will need to sign in to Heroku. If you do not have an account you can sign up for free [here](https://signup.heroku.com/).
2. Once you are logged in, click the button 'New' and select 'Create new app'.
3. Name the app, then select what region is closest to you and click 'Create App'.
4. Then on the resources tab, navigate to the 'Add-ons' section and search for 'Heroku Postgres'.
5. Select 'Heroku Postgres', then under 'Plan name' choose 'Hobby Dev - Free' and click 'Submit Order Form'.

To use Postgres you will need to install dj_database_url and psycopg2. This should be done in whatever IDE you are using.

1. In your IDE type the command:  
    `pip3 install dj_database_url`
2. Then once that is installed type the command:  
    `pip3 install psycopg2-binary`
3. Then, to make sure Heroku install all your apps requirements when you deploy it, run the command:  
    `pip3 freeze > requirements.txt`
4. Next, navigate to your setting.py file in your main project folder. At the top of the file add the line:  
    ```
    import dj_database_url
    ```
5. Then scroll down the file till you find your database settings. Comment out the default configuration and underneath insert the code:  
    ```
    DATABASES = {
        'default': dj_database_url.parse(*Enter Database URL here*)
    }
    ```
    The database URL can be found in the settings tab of your app in heroku, under Config Vars. Make sure to have the link in quotation marks.  
    **Important!** If you want to migrate any data from your current database to the Postgres database in Heroku, make sure you run this line before connecting to Postgres:  
    `./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`  
6. Once that's saved, you will now need to run migrations because you have connected to a new database. This is done by running the command:  
    `python3 manage.py migrate`
    If you had previously saved your data to import into the postgres database, you can now run the command:  
    `./manage.py loaddata db.json`
7. Now that's setup you will now need to create a superuser for the new database. The command is:  
    `python3 manage.py createsuperuser`
    *Note, once the superuser is created, it's a good idea to sign into the admin panel, locate the user, and check the option that says their email is verified. This is needed otherwise Allauth won't allow the user to sign into the store.* 
8. Before you commit these changes, you will need to remove the Databases section in the settings.py and uncomment the original database. This is to stop your Postgres database URL from ending up in version control.
9. Now we can create an if statement in our settings.py to run the postgres database when using the app on heroku or sqlite if not. Scroll back to the database section and refactor the code to look like this:  
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    ```
10. Next we will have to install another package called gunicorn, which will act as our web server. To do so, run the command:  
    `pip3 install gunicorn`
    And then remember to freeze the requirements with:  
    `pip3 freeze > requirements.txt`
11. Now we can create our Procfile to tell Heroku to create a web dyno. In your root directory create a file named 'Procfile' and inside insert the code:  
    `web: gunicorn **'your_projects_name_here'**.wsgi:application
12. Then, back in heroku, navigate to settings and in the config vars input the key DISABLE_COLLECTSTATIC with the value 1, and click 'Add'.
This is to stop heroku from collecting any static files when you deploy.
13. You will also need to add heroku to your allowed hosts in your settings.py. Back in your project, in the settings file, scroll down to ALLOWED_HOSTS, and inside the brackets insert the url to your app, followed by 'localhost'. It should look something like this:     
    ```
    ALLOWED_HOSTS = ['your-project-name.herokuapp.com', 'localhost']
    ```
14. Now add, commit and push these changes, followed by a push to heroku with the command:  
    `git push heroku main'
    Your app will now be deployed, albeit without any static files, but this will be fixed when setting up AWS, documented below. 
15. If you want your project to be automatically deployed to heroku when pushing your work to github you can. To do so, In heroku go to the deploy tab, and in the 'deployment method' section connect it to github. You will need to search for your repository and once found click 'connect'. Then scroll down and click 'Enable automatic deploys'. Now when you push to github your code will automatically deploy to Heroku as well. 


### AWS

Amazon web services are used to store all our static and media files. 

#### S3

1. First you will need to sign up to AWS which you can do [here](https://aws.amazon.com/).
2. Once you have created an account and logged in, under the All Services>Storage menu, click the link that says S3.
3. On the S3 page you will need to create a new bucket. To do this click the orange button that says 'Create Bucket'.
4. Name the bucket and select the closest region to you. To keep things simple I recommend naming the bucket after your project's name.
5. Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred. 
6. Uncheck the 'Block all public access' checkbox and check the warning box to acknowledge that the bucket will be made public, then click create bucket. 
7. Once created, click the bucket's name and navigate to the properties tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
8. Now navigate to the permissions tab, scroll down to the Cross-origin resource sharing (CORS) section, click edit and paste in the following code:  
    ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
9. Then scroll back up to the 'Bucket Policy' section. Click 'edit' and then 'Policy generator'. This should open the AWS policy generator page.
10. From here under the 'select type of policy' dropdown menu, select 'S3 Bucket Policy'. Then inside 'Principle' allow all principals by typing a *.
11. From the 'Actions dropdown menu select 'Get object'. Then head back to the previous tab and locate the Bucket ARN number. Copy that, return to the policy generator and paste it in the field labelled Amazon Resource Name (ARN).
12. Once that's completed click 'Add statement', then 'Generate Policy'. Copy the policy that's been generated and paste it into the bucket policy editor.
13. Before you click save, add a '/*' at the end of your resource key. This is to allow access to all resources in this bucket.
14. Once those changes are saved, scroll down to the Access control list (ACL) section and click 'edit'.
15. Next to 'Everyone (public access)', check the 'list' checkbox. This will pop up a warning box that you will also have to check. Once that's done click 'save'. 

#### IAM

1. Now that your bucket is ready we need to create a user to access it. In the search bar at the top of the window, search for IAM and select it.
2. Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'.
3. Name the group 'manage-*your-project-name*' and click 'Create group' at the bottom of the page. 
4. Then from the sidebar click 'Policies', then 'Create policy'.
5. Go to the JSON tab and click 'import managed policy'. Search for 'S3' and select 'AmazonS3FullAccess' and click import.
6. Once this is imported you will need to edit it slightly. Go back to your bucket and copy your ARN number. Head back to this policy and update the Resource key to include your ARN, and another line with your ARN followed by a /*. It should end up looking something like this: 
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "YOUR-ARN-NO-HERE",
                    "YOUR-ARN-NO-HERE/*"
                ]
            }
        ]
    }
    ```
7. Click 'Next: Tags', 'Next: Review', and on this page give the policy a name. This could be something as simple as the project name followed by the word policy, and then a short description eg: Access to S3 bucket for 'YOUR PROJECT' static files. Then click 'Create policy'. 
8. This will take you back to the policy page where you should be able to see your newly created policy. Now we need to attach it to the group we created.  
9. Click 'User groups', and click the group you created earlier. Go to the permissions tab and click 'Add permission' and from the dropdown click 'Attach policies'. 
10. Find the policy you just created, select it and click 'Add permissions'.
11. Finally you need to create a user to put in the group. Select users from the sidebar and click 'Add user'.  
12. Give your user a user name, check 'Programmatic Access', then click 'Next: Permissions'. 
13. Select your group that has the policy attached and click 'Next: Tags', 'Next: Review', then 'Create user'.
14. On the next page, download the CSV file. This contains the user's access key and secret access key which you will need later. 

#### Connecting AWS to django

Now that you have created a S3 bucket with its user group attached, we need to connect it to django.

1. First you will need to install two packages. Boto3 and Django storages. Do this by running these commands:  
    ```
    pip3 install boto3
    pip3 install django-storages
    ```
    And remember to freeze the requirements with:  
    ```
    pip3 freeze > requirements.txt
    ```
2. You will then need to add 'storages' to your installed apps section inside your settings.py file. Do that now. 
3. Next, we will need to add some additional settings to the same file to let django know what bucket it's communicating with. 
4. Somewhere near the bottom of the file you should write an if statement to check if there is an environment variable called USE_AWS. This variable does not exist yet but we will add it later. Inside the if statement, write the following settings so it looks like this:  
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
        AWS_S3_REGION_NAME = 'insert-your-region-here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
5. Next, hop back to heroku and in the settings tab, under config vars, you will need to add some keys with values that were downloaded earlier in the CSV file.
6. Add the key, AWS_ACCESS_KEY_ID with the value that was generated in the CSV file earlier. Then add the key AWS_SECRET_ACCESS_KEY, and again add the value that was generated in the CSV file. Once they have both been added, add the key USE_AWS, and set the value to True.
7. You can now also remove the DISABLE_COLLECTSTAIC variable, since django should now collect static files automatically and upload them to S3.
8. Now head back to the settings.py file in your django project and head back to the if statement we wrote earlier and inside the statement add this line setting:  
    ```
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
    This is to tell django where our static files will be coming from in production.
9. Next we need to create a file to tell django that we want to use S3 to store our static files whenever someone runs collectstatic and also that we want any uploaded product images to go there also.
10. In the root directory of your project create a file called 'custom_storages.py'. Inside this file you will need to import your settings as well as the s3boto3 storage class. So at the top of the file insert the code:  
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    ```
11. Then underneath the imports insert these two classes:  
    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
    The STATICFILES_LOCATION and MEDIAFILES_LOCATION have yet to be defined, so lets do that now.
12. Back in the settings.py file, underneath the bucket config settings but still inside the if statement, add these lines:  
    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
13. Next, you will also need to override and explicitly set the URLs for static and media files using your custom domain and new locations. To do this add these two lines inside the same if statement:  
    ```
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
14. If you now save, add, commit and push your changes, you should see that your S3 bucket now has a static folder with all your static files inside. Next, we need to handle the Media files but first, inside the if statement add the following code. This helps to speed things up by letting the browser know that its ok to cache static files for a long time:    
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    ```
15. Back in S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
16. Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
17. Then under 'Permissions' select the option 'Grant public-read access' and click upload. You may need to also check an acknowledgment warning checkbox too. 
18. Once that is finished you're all set. All your static files and media files should be automatically linked from django to your S3 bucket.

s
### Stripe

Stripe is needed to handle the checkout process when a payment is made. You will need a stripe account which you can sign up for [here](https://stripe.com/en-gb).

#### Payments

1. To set up stripe payments you can follow their guide [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

#### Webhooks

1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
2. Then in the side-nav under the Developers title, click on 'Webhooks', then 'Add endpoint'.
3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:  
    ```
    https://your-app-name.herokuapp.com/checkout/wh/
    ```
4. Then click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
6. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
7. Add these values under these keys:  
    ```
    STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
    STRIPE_SECRET_KEY = 'insert your secret key'
    STRIPE_WH_SECRET = 'insert your webhooks secret key'
    ```
8. Finally, back in your setting.py file in django, insert the following near the bottom of the file:  
    ```
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```