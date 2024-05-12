
# Animeasy Tools E-commerce Site

## Overview

Animeasy is an e-commerce store that provides small software plugins for animation production. 
This README provides an overview of the ecommerce app, including its purpose, features, installation instructions, usage guidelines, and contact information.

## Purpose
The purpose of the ecommerce app is to provide users with a platform to browse, purchase, and manage digital products online. It aims to streamline the shopping experience for customers and simplify product management for sellers.
Animation is a costly and time consuming business. With the advent of digital animation it is largely created using computer programmes. This means that professionals can browse the web for plugins that may help them. 
In my animation career, I starte out using plugins purchased or developed by the studio, but over time I started to develop my own for more specific uses. 

## Features
### User authentication: Allow users to register, login, and manage their accounts.

- Users can make purchases without making an account, but they can make an account if they want to
![The registraion form](readme-images/readme-reg-signup-form.png)
- Returning users can log into their account 
![Log in form](readme-images/readme-reg-signup-login.png)

- Users can reset their password to recover their account if they forget 
- Users can delete their account. The initial click disables the button and confirms the action, in case they clicked it by accident 
![Delete your account section](readme-images/readme-reg-delete-button.png)
![Delete your account modal](readme-images/readme-reg-delete-modal.png)


### Profiles 
- Users can view their information from their profile page 
![Information in user profile](readme-images/readme-profile-user-info-updated.png)
- If no user information exists yet, the information section reads "none"
![Empty information](readme-images/readme-profile-user-info-empty.png)
- Users can change their information from their profile page 
![User information form](readme-images/readme-profile-user-info-form.png)
- User's order history is saved at the bottom of their profile 
- If the user has no order history, this is reflected back to them 
![The empty order section](readme-images/readme-profile-user-order-none.png)
- User's support tickets and the replies can be accessed from the profile page 

### Product browsing: Enable users to search, filter, and view products.

- Users can see all products in Animeasy store in one place 
- Users can sort products by category, depending on which software they're looking for 
- Users can search for products by title or key word 
- Users can quickly add a product to their bag from the search results page 
- A product detail page is available for each product 
- The product detail page displays a product description, the software category and any user reviews 
- Users can add multiples of a product to their bag from the product detail page 

### Shopping cart: Allow users to add and remove items from their cart.
- The items in a user's cart are displayed in a dropdown from the nav bar, so users can see what's in their cart and the total at all times 
- If there's more that 5 items in their bag, the list will be truncated and an " ... & more" will be displayed
- Users can view their bag and see the items inside 
- Users can add or remove items from their bag from the cart view 
- If there's more than one of an item in the cart, users can see the subtotal of that item
- Users can see the total of their bag 
- Users can proceed to the checkout form from the bag view 

### Checkout process: Guide users through a secure checkout process.
- Users can securely checkout  items in their bag 
- Billing information is collected 
- Registered users can choose to save their details from next time 
- A secure checkout using Stripe 
- On comfirmation of order, users are directed to a success page, showing them their details, charge and what they ordered

### Order management: Enable users to track their orders and view order history.
- From their profile, users can see their order history 
- Clicking on the order number brings them to the original checkout success page, with a message saying that this is an old order they are viewing 
- Non registered users can access this information from their order confirmation email in their inbox 

### Admin panel: Allow administrators to manage users, products, and system settings.
- If the logged in user is a superuser, the admin panel will appear in the navigation bar
- From here admin can send a newsletter to subcribers
- They can also see an archive of all newsletters 
- Admin can use this panel to add products
- Admin can use this panel to access contact form tickets sent from Animeasy users 
- 
### Contact form: Allows customers to send complaints and tracks them in an admin panel 
- Users can contact Animeasy with any queries or complaints using this form 
- The form collects the subject, content and email address of the ticket 
- The ticket is passed into a view that only the admin can see, where all tickets are stored and their status is displayed 
- Admin can choose a ticket to reply to  
- In the ticket detail view, admin can see the content of the ticket and write a reply 
- Once a reply is sent, the ticket status changes from "pending" to "resolved" 

## Installation

To install and run the app locally, follow these steps:

- Clone the repository: git clone [repository-url]
- Navigate to the project directory: cd animeasy
- Install dependencies: <code> pip install -r requirements.txt  </code>
- Set up environment variables: Create a .env file and add necessary configuration variables. 
- Run the app: <code> python3 manage.py runserver</code >

### Usage
Once the app is running, users can access it through a web browser. They can perform the following actions:

- Register a new account or login with existing credentials.
- Browse products by category or search for specific items.
- Add products to the shopping cart and proceed to checkout.
- View and manage orders in the user account dashboard.
- Sellers can log in to the seller dashboard to manage products and orders.
- Administrators can access the admin panel to manage users and system settings.

## Agile method
###  User Stories 

I added the following user stories to my kanban board
<ul> 
    <li>
    <strong>User Story 1: User Registration</strong>
            <ul>
                <li>
                    As a customer of the Animeasy, I want to be able to create an account where I can access information about my previous purchases and opt in to promotional emails and updates about projects, along with special offers.
                </li>
            </ul>
        </li>
    <li>
    <strong>User Story 2: Products</strong>
        <ul>
            <li>
            As a potential customer of Animeasy, I want to see what products are available to purchase
            </li>
        </ul>
    </li>
    <li>
    <strong>>User Story 3: Purchasing/Cart</strong>
        <ul>
            <li>
            As a customer, I can purchase items from Animeasy
            </li>
        </ul>
    </li>
    <li>
    <strong>User Story 4: Navigation</strong>
    </li>
    <ul>
        <li>
        As a potential customer of Animeasy, I want to easily explore and find products on the site
        </li>
    </ul>
    <li>
    <strong>User Story 5: User Profile</strong>
    </li>
    <ul>
        <li>
        As a user, I can create a profile that allows me to purchase items easily
        </li>
    </ul>
    <li>
    <strong>User Story 6: Review</strong>
    </li>
    <ul>
        <li>As a customer of Animeasy, I want to be able to leave reviews on products I have purchased to share my experience with other users.
        </li>
    </ul>
    <li>
    <strong>User Story 7: Admin Permissions</strong>
    </li>
    <ul>
        <li>
        As a store owner, I can add, edit or delete products
        </li>
    </ul>
    <li>
    <strong>User Story 8: Newsletter</strong>
    </li>
    <ul>
        <li>
        As a marketer of animeasy, I want to be able to reach out to my interested leads with offers and announcements of new products via email.
        </li>
    </ul>
    <li>
    <strong>User Story 9: Contact Form</strong>
    </li>
    <ul>
        <li>
        As a seller, I would like a place to handle any issues from my customers
        </li>
        <li>
        As a customer, I would like a place to contact the seller should the need arise
        </li>
    </ul>
    <li>
    <strong>User Story 10: SEO & Marketing</strong>
    </li>
    <ul>
        <li>
        As a potential customer, I would like to be able to find Animeasy when I search for ways to make my animation workflow faster
        </li>
        <li>
        As a seller, I would like to reach more people who might benefit from using my products
        </li>
    </ul>
    <li>
    <strong>User Story 11: Help and FAQs</strong>
    </li>
    <ul>
        <li>
        As a customer of Animeasy, I would like to be able to access an install guide for my new products
        </li>
    </ul>
</ul>

### Kanban Board 
- Created an issue for each user story 
- Created issues for other tasks, like "Extras" and "Testing"
- Extras are tasks that would improve Animeasy but not essential to it's core functions
- Labelled user stories as Must Have, Could Have or Won't Have
- Testing is labelled as "Testing"
- Extras are labelled as "Could Have" 
- Main features are labelled as Must Have 
- Extras for each section are separated out into their own issues and marked as Could Have
- Each user story has a checklist of Acceptance Criteria and Tasks

#### Kanban Board Gallery

![The Issues page](readme-images/readme-kanban-issues.png)
![The Kanban Board](readme-images/readme-kanban-board.png)
![The Checklist](readme-images/readme-kanban-checklist.png)


## AWS Integration
- This project uses Amazon Web Services to serve static files and images 
- I used S3 for serving static files and images to the Heroku app. 
## GDPR 


## Marketing 
### Email marketing 

For my marketing strategy I chose email. 

Because of my past experience with social media marketing, I know that the social media I would typically run a successful campaign on (Instagram and Tiktok) will not have the market I'm targeting. Animeasy is designed as a B2B business, where the desired customers would be animation studios and freelance professionals looking to speed up their workflow. 

For professionals, the better strategy is to target email inboxes. Professionals in animation cannot afford not to check their inboxes for both current client correspondence and potential offers, so this is where Animeasy would be most likely to grab their attention. The value proposition of Animeasy is also not something that would "pop" in a social media setting. Marketing in the animation field generally consists of behind-the-scenes or sizzle reels. The tedious animation process is left out. Animeasy needs to target professionals who know the real problems they may face in the animation pipeline, not the fans of the product. 

### Facebook Page 

I created a Facebook page for Animeasy. It's a business page.

To keep the page appealing, I added a cover photo of an animation desk. 

![Cover of page](readme-images/readme-facebook-cover.png)

I created a custom thumbnail logo to go in the profile picture spot.

![Profile picture](readme-images/readme-facebook-thumb.png)

I added links to the website and some contact details. 

![About section](readme-images/readme-facebook-contact.png)

Finally I added a sample post, advertising the product and adding a call to action for the user to visit the site. 

![Sample post](readme-images/readme-facebook-post.png)

The page can be found [here](https://www.facebook.com/profile.php?id=61559552969497)


### LinkedIn Page 

I followed a similar procedure to create a LinkedIn profile for Animeasy. 

LinkedIn's userbase is professionals looking to market themselves, so this fits Animeasy's target market. 

I created a very simple page for Animeasy, and populated it with the same data as the Facebook page 

![Linkedin profile](readme-images/readme-linkedin.png)

[Linkedin page](https://www.linkedin.com/company/animeasy/)


## Testing 

### Manual Testing 

I did the following manual testing of Animeasy: 

### Linting 

The following is the results from the [W3 Schools HTML validation service](https://validator.w3.org/)

About Page
![About Page results](readme-images/readme-linting-about.png)

Add Product 
![Add Product results](readme-images/readme-linting-add-product-duplicate-id-error.png)
This error is caused from the image thumbnail uploader. It needs to have a duplicate ID to work with the custom scripting/styling

![Edit product results](readme-images/readme-linting-edit-product-duplicate-id-error.png)
Same error as the add product page

Bag
![Bag results](readme-images/readme-linting-bag-errors.png)

Checkout 
![Checkout results](readme-images/readme-linting-checkout-errors-spinner-div.png)
HTML does not like the "empty" h3 heading that the loading spinner is under.

Checkout Success
![Checkout Success results](readme-images/readme-linting-checkout-success.png)

Contact Form
![Contact Form results](readme-images/readme-linting-contact-form.png)

Contact Success
![Contact Success results](readme-images/readme-linting-contact-success.png)

Contact Tickets
![Contact Ticketsresults](readme-images/readme-linting-contact-tickets.png)

Edit Product
![Edit Product results](readme-images/readme-linting-edit-product-duplicate-id-error.png)

FAQ
![FAQ results](readme-images/readme-linting-faq.png)

Home page
![Home page results](readme-images/readme-linting-index.png)

Installation Guide
![Installation Guide results](readme-images/readme-linting-installpng.png)

Newsletter Archive
![Newsletter Archive results](readme-images/readme-linting-newsletter-archive.png)

Newsletter Detail
![Newsletter Detail results](readme-images/readme-linting-newsletter-detail.png)

Newsletter Success
![Newsletter Success results](readme-images/readme-linting-contact-success.png)

Newsletter Unsubscribe 
![Newsletter Unsubscribe results](readme-images/readme-linting-newsletter-unsubscribe.png)

Newsletter Creator 
![Newsletter Creator results](readme-images/readme-linting-newsletter.png)

Privacy Policy
![Privacy Policy results](readme-images/readme-linting-privacy-policy.png)

Product Detail
![Product Detail results](readme-images/readme-linting-product-detail.png)

Products
![Products results](readme-images/readme-linting-products.png)

Profile
![Profile results](readme-images/readme-linting-profile.png)

Terms and Conditions
![Terms and Conditions results](readme-images/readme-linting-terms-and-conditions.png)

Contact Ticket Detail 
![Contact Ticket results](readme-images/readme-linting-ticket-details.png)



## Future Features 
### Reviews 
- In the future, I would like to let users enter reviews of the product. The product model is set up with a rating system in anticipate adding this in the future.
- Users could rate the products by giving them a start rating 
- Reviews written about the product would be written below the project 

### File Downloads
- I would like to send users a link to download their purchased files 
- Animeasy would generate a token to prevent fraud 
- The link would be sent in the confirmation email 

## Known Issues 
- With the way the confirmation email is currently called, if you refresh on the confirmation page you get an email every time you refresh 
## Contact
For any questions, feedback, or support issues, please contact me at carlalennon@gmail.com .

## Sources: 
https://www.youtube.com/watch?v=hWtlskOaFNI newsletter
https://www.grokcode.com/819/one-click-unsubscribes-for-django-apps/ Unsubscribe
Linter HTML https://validator.w3.org/
#