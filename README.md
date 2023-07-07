# PP4-Practical-Life-Hacks

Practical life hack is a website designed to help people seeking productivity hacks, beauty tips, health tips, or creativity boosters. 
<br>It acts as a repository for all kinds of hacks, whether it is seeking productivity hacks, health tips, or creativity boosters,  turning everyday challenges into opportunities, making life more efficient, and above all, enjoyable for the user. 

This site is aimed at users who are committed to self-improvement and innovation.
<br>The live site can be found [here](https://pp4lifehacks-cf7bb63fe093.herokuapp.com/)

![alt text](/docs/readme_images/sitemockup.png)

## Table of Contents


1. [User Experience(UX)](#user-experienceux)
    1. [Agile Planning](#agile-planning)
        1. [Epics or Milestone](#epics-or-milestone)
        2. [User Stories](#user-stories)
2. [Design](#design)
    1. [Color Scheme](#color-scheme)
    2. [Typography](#typography)
    3. [Imagery](#imagery)
    4. [Wireframe](#wireframes)
3. [Technologies](#technologies)
    1. [Pthon Modules Used](#python-modules-used)
    2. [Languages](#languages)
    3. [External Python Modules](#external-python-modules)
    
4. [Database Design](#database-design)



5. [Testing](TESTING.md#table-of-content)
    1. [Functional Testing](TESTING.md#functional-testing)
    2. [Negative Testing](TESTING.md#negative-testing)
    3. [Unit Testing](TESTING.md#unit-testing)
    4. [Accessibility](TESTING.md#accessibility)
    5. [Validator Testing](TESTING.md#validator-testing)
    6. [PEP8 Testing](TESTING.md#pep8-testing)
    7. [Lighthouse Testing](TESTING.md#lighthouse-testing)
    8. [Manual Testing](TESTING.md#manual-testing)
6. [Security Features and Defensive Design](#security-features-and-defensive-design)
7. [Features](#features)
    1. [Header](#header)
    2. [Logo](#logo)
    3. [Navigation menu](#navigation-menu)
    4. [Footer](#footer)
    5. [Home Page](#home-page)
    6. [User Sign up Page](#user-sign-up-page)
    7. [Log in page](#log-in-page)
    8. [Logout page](#logout-page)
    9. [Browse all Hacks](#browse-all-hacks)
    10. [Hack Detail Page](#hack-detail-page)
    11. [Custom Error Pages](#custom-error-pages)
8. [Deployment](#deployment)
    1. [Version Control](#version-control)
    2. [Heroku Deployment](#heroku-deployment)
    3. [Cloning the Repository](#cloning-the-repository)
    4. [Fork Project](#fork-project)
9. [Credits](#credits)
10. [Acknowledgement](#acknowledgement)





---
# User Experience(UX)
This website is aimed at someone who is mostly an adult and are very keen in learning new things in life and are not afraid of trying new things.


This site is also aimed at users who are committed to self-improvement and innovation. 

## Agile Planning
This project was developed based on agile methodologies. 

###  Epics or Milestone

#### EPIC: Base Setup

- The base setup has all the user stories essential for the build up of the foundation of the application. 
- A base template as a basis for all the other templates are created in this epic.
- Static file is created to keep all the custom css, icons and favicons

#### EPIC : Authentication

- This Epic includes all the user storis relating to , user being able to register, login and after authentication can access contents and perform specific actions.
- By tying actions and activities to specific authenticated identities, a system can maintain an audit trail of what each user does.

#### EPIC : Stand alone pages

- This Epic contains all the webpages that is independent or self-contained and designed to fulfill its function without requiring the visitor to visit other parts of the site. 


#### EPIC : Hacks

- This Epic has all the stories that has to do with Creating, Deleting, Editing and viewing Hacks. 
- Not logged in users can view all the hacks
- A logged in user can manage its own hacks.
- Admin can manage all the activities


#### EPIC : Favorite

This Epic includes all the user stories that enables 
- a user to favorite a Hack 
- a user to remove a hack from his/her favorite list
- A search function for the website is also included in this epic.

#### EPIC: Comment and Likes

This Epic includes all the stories which enables 
- the user to comment on a post 
- the user to delete his own comment if he wishes to. 
- The user has to be logged in to add or delete comment.
- User can also like or unlike a hack.


#### EPIC :  Deployment

- This Epic is for all the User stories relating to deploying the application to Heroku so that the site is live for everyone.

#### EPIC: Documentation

- This Epic for all the Document related stories that is needed to document the development process of the application.


### User Stories
All user stories were assigned to epics, prioritized with labels, must have, should have and could have.

The 8 Epics listed below were documented within the Github Project as Milestones.


A Github issue was created for each User Story which was then added to a Milestone. 

Each User Story has its own Acceptance Criteria to make it clear when the User story is completed.

The Kanban board was created using github projects and can be located [here](https://github.com/pzompa/PP4-Practical-Life-Hacks/projects?query=is%3Aopen).

![alt text](/docs/readme_images/userstories.png)

The following user stories were completed.

##### EPIC : Base Setup

- As a developer, I need to set up the django project so that I can develop and deploy the app.

- As a developer, I need to create the base.html page and structure so that they can be reused throughout the project

- As a developer, I need to create static file so that images, css and javascript can stored and ensure that they work on the website

- As a developer, I need to create the footer with social media links so that people can know more about the app

- As a developer, I need to create the navbar so that users can navigate to any pages on  the website from any device
- As a developer, I need to create a search function where the user can easily serach for a hack based on title, description or a word without having to search the whole hacks.

##### EPIC : Authentication

- As a developer, I need to implement allauth so that users can sign up and have access to various features of the websites

- As a developer, I want to prompt the user to sign in if they are not and wants to comment or like on a hack

- As a site owner, I would like the allauth pages customized to match the overall look of the site


##### EPIC : Stand Alone Pages

- As a Site owner I want a Homepage so that users can view the Hacks and favorite the hack to try later

- As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

- As a developer, I need to implement a 500 error page to alert users when an internal server error occurs

- As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

##### EPIC : Hacks

- As a Site User, I can input my add a Hack onto the app through an easy to use interface so that I can share them with other users.

- As a Site User, I can edit and delete my Hacks that I have created so that I can easily make changes without having to start over.

- As a user, I would like to receive feedback when I create a Hack or edit so I know it was completed successfully


- As a Site User I can view my Favorited Hacks so I can find them easily in the one location.

- As a Site User I can like any Hack and unlike it if I prefer.

- As a Site User I can like and favorite hacks from other people to view later.

- As a Site User I can comment on any Hacks and delete my comments.

- As a Site User I can view all the Hacks created by all the users.
##### EPIC : Comment and Likes

- As a user, I can comment on a hack after loggin in.
- As a user, I can delete my comments
- As a user, I can like a hack after loggin in.
- As a user, I can remove my like from a hack.
- As a user, I can see how many likes and comments a hack has.
- If a user is not logged in the user will be directed to log in or signup


##### EPIC : Deployment

- As a developer, I need to set up whitenoise so that my static files are served in Deployment

- As a developer, I need to deploy the project to Heroku so that it is live for all users.

##### EPIC : Documentation

- Complete readme documentation 

- Complete testing documentation 

##### User stories not implemented
- Email verification after a user register to the website was not done due to time constraint. 
- Which is intented to be implemented in the future.

##### Future planned features
- A possibilty to filter the hacks according to their category is a feature which will be implemented in future.
##### Favicon 
- A favicon was added to clearly identify the website in the browser when multiple tabs are open.

---
# Design:

- The site has a very simple yet soothing design purposely kept aesthetically clean and calming to give the user a sense of Calm without being overloaded with information.

### Color Scheme

- The main color schemes for the website are pale cream, pink with black fonts and the buttons are kept dark on hover to match the font colors of the website.

### Typography

- The Roboto font is the main font used for the body of the website and Lato for the Headings. Sans Serif is the backup font, in case for any reason the main font isn't being imported correctly.
These fonts were imported via Google Fonts.

### Imagery

- The Website logo was made on looka.com.

- The hero image and the default hack image were taken from the pexels.com
- User will upload their own image when creating a hack
---
## Wireframes:  
### Home page

![alt text](/docs/wireframes/homepage.png)

### Sign up page

![alt text](/docs/wireframes/signup.png)

### Log in page
![alt text](/docs/wireframes/login.png)
### Log out page
![alt text](/docs/wireframes/signout.png)

### Add Hack
![alt text](/docs/wireframes/addhack.png)

### Edit Hack
![alt text](/docs/wireframes/edithack.png)
### Delete Hack
![alt text](/docs/wireframes/hackdeleteconfirm.png)
### Browse all hack
![alt text](/docs/wireframes/browseallhack.png)

### My favorite Hacks
![alt text](/docs/wireframes/favorite.png)

### Favorite add success message
![alt text](/docs/wireframes/favoritesuccess.png)

### Favorite remove success message
![alt text](/docs/wireframes/removefavorite.png)
### 404 error page
![alt text](/docs/wireframes/404error.png)
### 403 error page
![alt text](/docs/wireframes/403error.png)
### 500 error page
![alt text](/docs/wireframes/500error.png)
### Hack add success message
![alt text](/docs/wireframes/hackaddsuccess.png)
### Hack edit success message
![alt text](/docs/wireframes/hackeditsuccess.png)


---
# Technologies

- Gitpod - The website was developed using Gitpod

- GitHub - Source code is hosted on GitHub

- Git - Used to commit and push code during the development of the Website

- Font Awesome - This was used for various icons throughout the site

- Favicon.io - favicon files were created at this website

- [Balsamiq](https://balsamiq.com/)- wireframes were created using balsamig
- [Lucidchart](https://www.lucidchart.com/pages/)- was used to create the data schema
- [looga.com](https://looka.com/) - Logo was created on this website.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts used on the page
- [W3C](https://validator.w3.org/) - Used for HTML and CSS validation
- [CI PEP8](https://pep8ci.herokuapp.com/) CI Python Lynter Validator
- [AmIResponsive](https://ui.dev/amiresponsive) -  Site mockup generator
- [TinyPNG](tinypng.com) - This was used to compress hero image for optimal load times
- [Cloudinary](https://cloudinary.com/) - the image hosting service used to upload images
- Crispy Forms - used to manage Django Forms

## Languages

- HTML

- CSS

- JavaScript

- Python

###  Python Modules Used
- Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
- Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions
- messages - Used to pass messages to display feedback to the user upon actions

### External Python Modules

- asgiref==3.7.2
- black==23.3.0
- certifi==2023.5.7
- cffi==1.15.1
- charset-normalizer==3.1.0
- click==8.1.3
- cloudinary==1.33.0
- crispy-bootstrap5==0.7
- cryptography==41.0.1
- defusedxml==0.7.1
- dj-database-url==2.0.0
- Django==4.2.2
- django-allauth==0.54.0
- django-cloudinary-storage==0.3.0
- django-crispy-forms==2.0
- django-debug-toolbar==4.1.0
- django-extensions==3.2.3
- django-richtextfield==1.6.1
- django-tinymce4-lite==1.8.0
- gunicorn==20.1.0
- idna==3.4
- jsmin==3.0.1
- mypy-extensions==1.0.0
- oauthlib==3.2.2
- packaging==23.1
- pathspec==0.11.1
- Pillow==9.5.0
- platformdirs==3.7.0
- psycopg2==2.9.6
- pycparser==2.21
- PyJWT==2.7.0
- python3-openid==3.2.0
- requests==2.31.0
- requests-oauthlib==1.3.1
- six==1.16.0
- sqlparse==0.4.4
- typing_extensions==4.6.3
- urllib3==1.26.16
- whitenoise==6.5.0

---
# Database Design:
Object Oriented Programming principles were followed throughout this project and Django's Class Based Views (CBVs) were used for the App Views.

Django AllAuth was used for the user authentication system. 

The hack data is stored and implemented with a Hack model. The Hacks model has a foreign key to the User model. Only an authenticated user can create a new Hack entry. An indivitual hack can only refer to one user in the User model. 

Each Hack can have zero or more comments. To make a comment, you have to be logged in. The comment data is stored and implemented with a Comment model. It has one foreign key to the User model, and another foreign key to the Hack model. A comment can only refer to one user and one hack. 

Each Hack can have zero or more likes. To like a hack, you have to be logged in. The like data is stored and implemented with a Like model. It has one foreign key to the User model, and another foreign key to the Hack model. A like can only refer to one user and one hack.

It's possible to mark a hack as a favorite. To do so, you need to be logged in. The favorite data is stored and implemented using a Favorite model. It has one foreign key to the User model, and another foreign key to the Hack model. A favorite can only refer to one user and one hack.

The diagram below details the database schema.

![Database Schema](/docs/testing_images/databaseschema.jpeg)


---
# Testing Documentation:
- Testing and results can be found [here](TESTING.md)
---
# Security Features and Defensive Design

- Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository.

- In production, these variables were added to the heroku config vars within the project.
- Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.
---
## User Authentication
- Django's LoginRequiredMixin is used to restrict any not authenticated users from accessing secure pages. They will be redirected to the error page with a customized message

- Django’s UserPassesTestMixin is used to limit access based on certain permission criteria to ensure that only the author of the hacks or comments are allowed to edit/delete. If the user doesn’t pass the test they are show an error page with customized message.
---
# Features


### Logo: 
- A customized logo was generated on looka.com website
- The logo is positioned in the top left of the navigation menu. The logo is linked to the home page so that user can come to the homepage from anywhere on the website.

### Header:
![](/docs/readme_images/header1.png)

### Navigation menu:
![](/docs/readme_images/header.png)

- The nav menu is present at the top of every page and include links to all the other pages.
- Navigation bar is responsive and collapsing in hamburger menu for mobile screens.
![](/docs/readme_images/hamburgermenu.png)

When a user is not logged in:
- The navbar shows Home, Browse Hacks, Add hack, Register and Login menu
- If the user tries to add a hack, like a hack or favorite a hack, they will be redirected to Signup or login page


When a user is logged in:
- The nav bar shows Home, Browse Hacks, Add hack, Add to Favorite and Logout menu
- More option such as My favorite Hacks become available on the menu bar


### Footer:
- ![](/docs/readme_images/footer.png)

- The footer section includes links to Facebook, Instagram and Youtube.
- When clicked, opens in a new tab.

### Home Page
![](/docs/readme_images/homepage.png)
- Home page is deliberately kept simple with a hero image and a brief information of the site and a button which takes the user to the browse hacks page

### User Sign up Page
![](/docs/readme_images/signup.png)


### Log in page
![](/docs/readme_images/login.png)

### Logout page
![](/docs/readme_images/logout.png)

### Browse all Hacks
![](/docs/readme_images/browsehacks.png)

- This page displays all the hacks with the most recent hacks displayed first.
- The Hack cards are paginated after every 8 hacks.
- Each Hack shows the Hack Title, category, Posted by time and date, like icon with counter and comment icon with counter.
- It also has a button to ‘Find out more’, when clicked will take you to the hacks detailed  page

### Hack Detail Page
![](/docs/readme_images/hackdetail.png)
- This page shows the picture of the hack with the Title of the Hack, Posted by and time and date of the post.
- It also shows the category of the hack
- Ingredients and Description of the hacks
### Custom Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![](/docs/readme_images/403error.png)

- 404 Bad Request - Page you have requested cannot be found
- 403 Page Forbidden -You are not authorized to perform this action
- 500 Server Error - currently unable to handle this request
---
# Deployment
### Version Control
- The site was created using the Gitpod IDE and pushed to github to the remote repository ‘pp4lifehacks'

- The following git commands were used throughout development to push code to the remote repo:

    - git add <file> - This command was used to add the file(s) to the staging area before they are committed.

    - git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

    - git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter your new app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
- SECRET_KEY: (Your secret key)
- DATABASE_URL: (This should already exist with add on of postgres)
- CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy
- The app should now be deployed.


### Cloning the Repository
- To clone a Repository to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
Type git clone copied-git-url into the IDE terminal
The project will now of been cloned on your local machine for use

### Fork Project
By forking the GitHub Repository we make a copy of the original repository by using the following steps...

- Go to the GitHub repository.
- Click on 'Fork' button in upper right hand corner.
- Select 'Create new fork' from the drop-down menu.
- A copy of the repository is now created in your GitHub Repository.
---
## Credits
The Images were taken from pexels.

- Stack Overflow
- [Django documentation](https://docs.djangoproject.com/en/4.2/intro/)
- [python official docs](https://docs.python.org/3/tutorial/index.html)
- [Pexels](Pexels.com): All imagery on the site was sourced from Pexel
- I relied on the youtube Tutorials like:  
- [Dee MC](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
- [Very Academy](https://www.youtube.com/watch?v=dXkmPAnqnTE)

- [Codemy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
- [netsetos ](https://www.youtube.com/watch?v=L6boPI7Zy60)
- google

---
## Acknowledgement
- My mentor Gereth McGirr from Code Institute as always has been very helpful with tips and advices.
- My Family for their patience, support.






 






 


