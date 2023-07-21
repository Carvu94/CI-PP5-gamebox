# GAMEBOX
(Developer: Matej Car)

![Mockup image](docs/am_i_responsive.png)


[View live website](https://ci-pp5-gamebox-7df162bca61b.herokuapp.com/)

## Table of Contents
0. [About](#about)
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Project Structure](#project-structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
    7. [Agile Design](#agile-design)
4. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries and Tools](#libraries--tools)
5. [Features](#features)
6. [Future Features](#future-features)

7. [Validation](#validation)
    1. [CSS](#css)
    2. [Html](#html)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Chrome Dev Tools Lighthouse](#lighthouse)
    6. [WAVE Validation](#wave)
8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## About

Gamebox is a Django full stack e-commerce app for purposes of Project Portfolio 5 with Code Institute. Gamebox is a fictional e-commerce site which provides gamers with a selection of video games for different consoles. 
***
## Project Goals

- To offer users purchase of products listed on a web-store.
- To allow site owner to add, edit and remove products.
- To give users a great user experience while visiting a web-store.
- To give users option for buying as a guest or a registered user.
- To give users option to contact site owner as a guest or registered user.
- To allow user creating or updating an account.
- To give users option to check the order history.
- To give users option to add,edit and delete a product review.
- To give users option to add and remove products to a wishlist.
- To give users option to signup for newsletter.

### User Goals

- View and search for products.
- Filter products based on criteria.
- Register and log into/out of an account.
- View and edit account profile.
- Add products to the shopping bag and make purchases.
- View order history.
- Write, edit, and delete product reviews.
- Create and manage a wishlist.
- Contact the site owner or customer support.
- Sign up for a newsletter.


## Business Model
***

Gamebox project was developed out of want to help passionate gamer community to easier find new and cheap video games and in future the consoles as well.

- Value Proposition:
    - Offer a curated selection of most popular video games.
    - Make video games more accessible to a broader range of customers who appreciate gaming and quality of the products.

- Target market:
    - Gamers of all ages.
    - Individuals seeking high-quality services for personal use or gifts.

- Customer Relationships:
    - Engage with customers through social media, email newsletters, and personalized communications to foster brand loyalty.
    -  Encourage customer feedback and reviews to continuously improve the product selection and overall shopping experience.

- Communication channels:
    - E-commerce website: Provide a user-friendly online platform where customers can browse, select, and purchase video games.
    - Social media platforms: Utilize platform as Facebook to engage with the audience, and drive traffic to the web-shop.

### SEO

![SEO keywords HTML](docs/seo.png)


### Marketing

#### Facebook business page
- To assist with marketing the website and further boost its visibility, I have included a link to the web-shop's own Facebook Business Page in the footer section. This reciprocal link establishes a connection between the website and its social media presence, allowing visitors to easily access the Facebook page for additional updates, promotions, and engagement with the brand. You can visit the web-shop's Facebook page by clicking [here]()

![Facebook business1]()
![Facebook business2]()


### Target audience

- Video game enthusiasts.
- Individuals seeking new and popular video games for personal use or gifts.


##### Back to [top](#table-of-contents)

## User Experience

##### Back to [top](#table-of-contents)

### User stories

## Unregistered User

1. As an unregistred user, I want to be able to view a list of products so that I can select some to purchase
2. As an unregistred user, I want to be able to view product details so that I can identify the price, description, rating and image
3. As an unregistred user, I want to be able to view total of my purchases at any time so that I am aware of how much I am spending
4. As an unregistred user, I want to be able to register for an account so that I have a personal account and can view my profile
5. As an unregistred user, I want to be able to view products by categories so that I can find products in specific category
6. As an unregistred user, I want to be able to add products that i wish to buy to shopping bag so that I can continue shopping
6. As a unregistered user I can sort products so that I can optimize my products view
7. As an unregistered user I can easily see what I have searched and the number of results so that I can quickly decide whether the products I want are available
8. As an unregistered user I can see messages on different pages so that I am aware of the success or failure of my actions
9. 
10. As a unregistered I can contact the site owner so that I can get in touch with the site owner.
11. As an unregistred user, I want to be able to view my shopping bag and edit quanity of products so I can add more or remove products from my shopping bag
12. As an unregistred user, I want to be able to search for products by name or description so that I can find a specific product I would like to purchase
13. As an unregistred user, I want to be able to easily see what I have searched and number of results so that I can quickly decide whether the products I want is available
14. As an unregistred user, I want to be able to pick the console for games so that I can purchase a game for certain console
15. As an unregistred user, I want to be able to easily enter my payment information so that I can check out quickly
16. As an unregistred user, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes
17. As an unregistred user, I want to be able to receive an email confirmation of order after checkout so that I can keep the information for my records

## Registered User

18. As a registered user, I want to be able to login or logout so that I can access my account information
19. As a registered user I can view my wishlist so that I can see and access products that are on my wishlist
20. As a registered user I can add products to my wishlist so that I can access them easier once I decide to buy
21. As a registered user I can leave a review on products so that I can give feedback regarding products I purchased
22. As a registered user I can edit my review on products so that I can update my review
23. As a registered user I can delete my review on products so that my review is not visible anymore
24. As a registered user, I want to be able to recover my password so that I can recover access to my account
25. As a registered user, I want to be able to receive an email confirmation after registering so that I can verify my account
26. As a registered user I can remove products from my wishlist so that I can remove unwanted products from my wishlist
27. As a registered user, I want to be able to have a personalized user profile so that I can view my personal order history and other info
28. As a registered user, I want to be able to to save my payment information so that I can my future purchases are faster
29. As a registered user I can recover my password so that I can recover access to my account
30. As a registered user, I want to be able to edit my profile info so that I can update my profile
31. As a registered user, I want to be able to delete my profile so that my profile does not exist on site anymore

## Site Owner 

32. As a site owner, I want to be able to add a product so that I can add new items to my store
33. As a site owner, I want to be able to edit/update a product so that I can change prices, description, image and other
34. As a site owner, I want to be able to delete a product so that I can remove items that are no longer available
24. As a site owner, I want to be able to edit/remove reviews so that I can manage content on my web site.



| id  |  content | Github issue Numb
| ------ | ------ | ------ |
|  [#0]() | As an unauthenticated user/customer I would Like|  |
|  [#1]() | As an unauthenticated user/customer I would Like|  |
|  [#2]() | As an unauthenticated user/customer, I would like|  |
|  [#3]() | As an unauthenticated user/customer, I would like|  |
|  [#4]() | As an unauthenticated user/customer, I would like|  |
|  [#5]() | As an unauthenticated user/customer, I would like||
|  [#6]() | As an unauthenticated user/customer, I would like|  |
|  [#7]() | As an unauthenticated user/customer, I would like|  |
|  [#8]() |  As an unauthenticated user/customer, I would like| |
|  [#9]() | As an unauthenticated user/customer, I would like|  |
|  [#10]() | As an authenticated user/customer, I would like|  |
|  [#11]() | As an authenticated user/customer, I would like|  |
|  [#12]() | As user/customer, I would like |  |



## Design
***
### Colours

### Fonts

## Project Structure


##### Back to [top](#table-of-contents)

## Database
***


### Data Models



####  model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|


####  model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|


####  model
| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|
|user       | user     | OneToOneField|  User|


### Wireframes

<details><summary>images</summary>

<details><summary>Home page</summary>

</details>