<p align="center">
<img src="README_docs/logo/logo_transparent.png" width="400" height="100%">
</p>

# Table of Contents 
1. [UX](#ux)
    - [Strategy](#strategy)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)
    - [Wireframes](#wireframes)
    - [Database schema](#database-schema)
    - [Models](#models)

4. [Web marketing](#web-marketing)
    - [Newsletter](#newsletter)
    - [Facebook](#facebook)
    - [SEO](#seo)

5. [Surface](#surface)

6. [Technologies Used](#technologies-used)

7. [Code validation](#code-validation)

8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)

11. [Credits](#credits)


responsive image and link to live site


# About
This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript. I created a website for 'JoyfulBookstore' which is designed to sell children's books


# UX
## Strategy
Using the core UX principles I first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'JoyfulBookstore' are:

- parents, relatives or friends who would like to buy books children/friends
- children age 0 - 18

These users will be looking for:
- An informative website, with information that is easy-to-find & concise
- A website that offers children's books
- Ability to view & purchase books that are for sale
- Ability to make a user account in order to see billing history, make whish list and write reviews 
- A way to sign up for the bookstore newsletter

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories

**Epic: Admin/Store Owner**

| ID  | Content     |
| --- | ----------- |
| 1   | As a **store owner** I can log in/log out from of the admin panel so that I can connect or disconnect from the website
| 2   | As a **store owner** I can log in so that I have full access to the store backend
| 3   | As a **store owner** I can add new products to the shop so that I can make sure the website is up to date
| 4   | As a **store owner** I can edit/delete products so that I can make sure the website it up to date
| 5   | As a **store owner** I can send out newsletter via email so that I keep customers updated with new products
| 6   | As a **store owner** I have created Facebook shop page to increase traffic on my website

**Epic: First time User**


| ID  | Content     |
| --- | ----------- |
| 7   | As a **first time user** I can see an interesting home page so that I can understand what shop sells
| 8   | As a **first time user** I can easily navigate through the site so that I can view desired content
| 9   | As a **first time user** I can find a navigation bar and footer so that I can see what content there is on the website
| 10  | As a **first time user** I can register and create account so that I can view my orders, save delivery details, create whish list and leave feedback


**Epic: User**

| ID  | Content     |
| --- | ----------- |
| 11  | Aa a **user** I can easily see list of products so that I can view what shop can offer
| 12  | As a **user** I can sort product by category so that I can easily find what I'm looking for
| 13  | As a **user** I can filter products by rating, price and name so that I can easily find what I'm looking for
| 14  | As a **user** I can search for products using the search form so that I can find products by name, author or description
| 15  | As a **user** I can see the product details page, which displays the product name, rating, price, short description and comments
| 16  | As a **user** I can select quantity of the desire product that I want to purchase
| 17  | As a **user** I can see rating and reviews so that I can read other users opinions
| 18  | As a **user** I am notified about any changes I have made so that I have a clear understanding of what has been completed/updated/failed
| 19  | As a **user** I can add selected item into the shopping bag
| 20  | As a **user** I can see shopping bag summury and total cost so that I can see how much I will spend
| 21  | As a **user** I can remove items from shopping bag so that I don't buy what I don't want
| 22  | As a **user** I can put in my card details so that I can pay for my goods
| 23  | As a **user** I receive order confirmations to be sure my order has been processed

**Epic: Logged-in User**

| ID  | Content     |
| --- | ----------- |
| 24  | As a **logged-in User** I can easily see if I'm logged-in or logged-out so that I can be sure what my status is
| 25  | As a **logged-in User** I can log in/out off my account if I wish so that I can connect or disconnect from the website
| 26  | As a **logged-in User** I can have my details saved so that I don't have to re type my address every time
| 27  | As a **logged-in User** I can create whish list so that I can save selected products for later purchase
| 28  | As a **logged-in User** I can leave reating and reviews so that I can leave my feedback


# Scope

## Features

### **Home Page**

*Navigation bar:*
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'All Books', 'Categories' and icons for search bar, account and shopping bag

*Account - Login/Register:*
- The Login/Register feature is located in the upper right corner and offers the user to log in or register for an account as well as log out of the site
- When the user is logged in links for 'Login' and 'Register' will change to 'My Profile' and 'Logout', add Whish list
- The admin user has extra access that allow them to add, update and remove books from the store

*Shopping bag:*
- The shopping bag is also situated on the top right corner of the site and it is always visible for the user throughout all the pages. With one click they can access their    shopping bag to see what is in there, update the quantities of book they wish to purchase or to delete them from the shopping bag.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

*Carousel:*
- The carousel welcomes the user with a short message and background image advertising what the website is about
- The 'Shop Now' button will take users to the all books page

*New releases:*
- The New Releases section displays the latest books the bookstore has in store so users can quickly see new books
- Each book card displayes an image, book title, author and price
- Each book card also had an "Add to Bag" button so the user could quickly add the book to their shopping bag

*Footer:*
- Appears on every page snd contains social links
- Links are opened in a new tab to avoid dragging users from our site

### **All Books**

- The All Books page shows all the books that the bookstore sells
- Each book has an image, book title, author, rating and price
- The site will paginate all books cards to display 10 per page
- Each book card takes users to the book details page 


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
- Page main body of the page will display book cover image, title, rating, author, book type, size, category, description
- After the main body content user can select quantity and add product to the shopping bag or whish list
- Commenting section is located at the end of the page, only logged in users can leave a comment

### **Checkout Page**
- The checkout page is accessible through the shopping bag
- Once the site users have made their last decision about what to purchase and they are happy with it. At the checkout the site user can enter and save their personal details and see a summary of what they are about to purchase before entering their card details.

### **Admin User**
- Admin user can preform full CRUD functionalliy without having to enter the default 'admin panel' from django. 
- Admin user can add books from 'Book Managment' link in the account menu from the navigation bar 
- Admin user can edit/delete books from all books page and books details page
