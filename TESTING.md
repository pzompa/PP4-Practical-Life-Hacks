# Testing Documentation

## Table of Content
1. [Functional Testing](#functional-testing)
    1. [Authentication](#authentication)
    2. [Hacks](#hacks)
    3. [Favorite Hacks](#favorite-hacks)
    4. [Like a Hack](#like-a-hack)
    5. [Comment a Hack](#comment-a-hack)
2. [Negative Testing](#negative-testing)
3. [Unit Testing](#unit-testing)
4. [Accessibility](#accessibility)
5. [Validator Testing](#validator-testing)
6. [PEP8 Testing](#pep8-testing)
7. [Lighthouse Testing](#lighthouse-testing)
8. [Manual Testing](#manual-testing)

---
## Functional Testing
### Authentication
- register a user
- login a user
- logout a user
- delete a user

### Hacks
- browse hacks
- add hacks
- edit hacks
- delete hacks

### Favorite Hacks
- add Hack to Favorite list
- remove a Hack from Favorite list

### Like a Hack
- Like a Hack
- Unlike a Hack

### Comment a Hack
- add a comment 
- remove a comment

---
## Negative Testing
### Hacks
1. User cannot create a new Hack without logging in.
2. If the user is not logged in and be the creator of the specific Hack, the user cannot edit the specific Hack.
3. If the user is not logged in and be the creator of the specific Hack, the user cannot delete the specific Hack.

### Like a Hack
1. If the user is not logged in, the user cannot like a specific Hack
2. if the user is not logged in, the user cannot unlike a specific Hack

### Add Hack to Favorite list
1. if the user is not logged in, the user cannot add a specific Hack to the users Favorite list
2. if the user is not logged in, the user cannot remove a specific Hack from the users Favorite list

### Comment a Hack
1. if the user is not logged in, the user cannot comment on a Hack
2. if the user is not logged inand be the creator of the comment, the user cannot delete the comment

## Unit Testing

### Hacks
#### Create a Hack test

#### Edit a Hack test
#### Read a Hack test
#### Delete a Hack test

### Like
#### Like a Hack test
#### Unlike a Hack test

### Favorite
#### Add a Hack to Favorite list test
#### Remove a Hack from Favorite list test

### Comment a Hack
#### Add a Comment to a Hack
#### Remove a Comment from a Hack



## Accessibility

## Validator Testing

## PEP8 Testing

## Lighthouse Testing

## Manual Testing

### Testing "Home" page
| Element              | Action       | Expected Result                             | Pass/Fail |
| -------------------- | ------------ | ------------------------------------------- | --------- |
| HTTP Request         | receive      | receive GET request                         | Pass      |
| URL routing: url.py  | analyze URL  | match view name "home"                      | Pass      |
| views.py             | invoke       | invoke "class Index" in home app            | Pass      |
| template file        | render       | render "home/index.html in home app         | Pass      |
|                      |              |                                             |           |
| Navbar               | display      | display Navbar menu                         | Pass      |
| Navbar               | display      | display Navbar burger menu for small screen | Pass      |
| Footer               | display      | display social links                        | Pass      |
| Footer               | click        | forward to social links                     | Pass      |
|                      |              |                                             |           |
| Image / Text / Links | display      | display image, text and links               | Pass      |
|                      |              |                                             |           |
| Explore link         | click        | forward to "Browse Hacks" page              | Pass      |
|                      | generate URL | use tag  {% url 'hacks' %}                  | Pass      |
|                      | result       | URL path:  "/hacks/hacks/"                  | Pass      |
|                      | analyze URL  | match view name "hacks"                     | Pass      |
|                      | invoke       | invoke "class Hacks" in hacks app           | Pass      |
|                      | render       | render "hacks/hacks.html in hacks app       | Pass      |
|                      |              |                                             |           |
| Logo link            | click        | forward to "Home" page                      | Pass      |
|                      | generate URL | use tag  {% url 'home' %}                   | Pass      |
|                      | result       | URL path:  "/"                              | Pass      |
|                      | analyze URL  | match view name "home"                      | Pass      |
|                      | invoke       | invoke "class Index" in home app            | Pass      |
|                      | render       | render "home/index.html in home app         | Pass      |


### Testing "Browse Hacks" page
| Element             | Action       | Expected Result                                  | Pass/Fail |
| ------------------- | ------------ | ------------------------------------------------ | --------- |
| template tag        | generate URL | use tag   {% url 'hacks' %}                      | Pass      |
|                     | result       | URL path:  "/hacks/hacks/"                       | Pass      |
|                     |              |                                                  |           |
| Browse Hacks link   | click        | received GET request with path:  "/hacks/hacks/" | Pass      |
| URL routing: url.py | analyze URL  | match view name "hacks"                          | Pass      |
| views.py            | invoke       | invoke "class Hacks" in hacks app                | Pass      |
|                     |              | (authentication not required)                    | Pass      |
| template file       |              | render "hacks/hacks.html" in hacks app           | Pass      |
|                     |              |                                                  |           |
| Navbar              | display      | display Navbar menu                              | Pass      |
| Navbar              | display      | display Navbar burger menu for small screen      | Pass      |
| Footer              | display      | display social links                             | Pass      |
| Footer              | click        | forward to social links                          | Pass      |
|                     |              |                                                  |           |
| all Hacks           | display      | display multiple Hacks                           | Pass      |
| each Hack           | display      | display title, posted by and created on          | Pass      |
| each Hack           | display      | display link count and comment count             | Pass      |
| each Hack           | display      | display "Find out more" link                     | Pass      |
|                     |              |                                                  |           |
| template tag        | generate URL | use tag   {% url 'hack_detail' hack.id %}        | Pass      |
|                     | result       | URL path:   e.g.  "/hacks/33/"                   | Pass      |
|                     |              |                                                  |           |
| "Find out more"     | click        | forward to "Hack Detail" page                    | Pass      |
|                     |              |                                                  |           |
| Pagination          | display      | display previous page and next page link         | Pass      |
| Pagination          | display      | display page of pages                            | Pass      |


### Testing "Add Hack" page
| Element             | Action         | Expected Result                                       | Pass/Fail |
| ------------------- | -------------- | ----------------------------------------------------- | --------- |
| template tag        | generate URL   | use tag   {% url 'create_hack' %}                     | Pass      |
|                     | result         | URL path:  "/hacks/"                                  | Pass      |
|                     |                |                                                       |           |
| Add Hack link       | click          | received GET request with path:  "/hacks/"            | Pass      |
| URL routing: url.py | analyze URL    | match view name "create_hack"                         | Pass      |
| views.py            | Invoke         | invoke "class CreateHack" in hacks app                | Pass      |
| LoginRequiredMixin  | access control | verify authentication/authorization                   | Pass      |
| LoginRequiredMixin  | SELECT query   | query "django_session" for authorization              | Pass      |
| template file       | render         | render  "hacks/create_hack.html" in hacks app         | Pass      |
|                     |                |                                                       |           |
| Navbar              | display        | display Navbar menu                                   | Pass      |
| Navbar              | display        | display Navbar burger menu for small screen           | Pass      |
| Footer              | display        | display social links                                  | Pass      |
| Footer              | click          | forward to social links                               | Pass      |
|                     |                |                                                       |           |
| Add Hack page       | display        | display title, ingredients, description, dropdown box | Pass      |
| Category dropdown   | click          | display category options from "hacks_hacks" table     | Pass      |
| Image               | click          | select image to upload                                | Pass      |
|                     |                |                                                       |           |
| Submit/Cancel       | display        | display submit and cancel button                      | Pass      |
| Submit              | click          | load Hack object into database                        | Pass      |
| Cancel              | click          | forward to "Home" page                                | Pass      |


### Testing "My Favorite Hacks" page
| Element                | Action         | Expected Result                                          | Pass/Fail |
| ---------------------- | -------------- | -------------------------------------------------------- | --------- |
| template tag           | generate URL   | use tag   {% url 'favorite_hacks' %}                     | Pass      |
|                        | result         | URL path:   "/hacks/favorite_hacks/"                     | Pass      |
|                        |                |                                                          |           |
| My Favorite Hacks link | click          | receive GET request with path:  "/hacks/favorite_hacks/" | Pass      |
| URL routing: url.py    | analyze URL    | match view name "favorite_hacks"                         | Pass      |
| views.py               | invoke         | invoke "class FavoriteHacksView" in hacks app            | Pass      |
| LoginRequiredMixin     | access control | verify authentication/authorization                      | Pass      |
| LoginRequiredMixin     | SELECT query   | query "django_session" for authorization                 | Pass      |
| template file          | render         | render "hacks/favorite_hacks.html" in hacks app          | Pass      |
|                        |                |                                                          |           |
| Navbar                 | display        | display Navbar menu                                      | Pass      |
| Navbar                 | display        | display Navbar burger menu for small screen              | Pass      |
| Footer                 | display        | display social links                                     | Pass      |
| Footer                 | click          | forward to social links                                  | Pass      |
|                        |                |                                                          |           |
| all Hacks              | display        | display multiple Hacks                                   | Pass      |
| each Hack              | display        | display title, posted by and created on                  | Pass      |
| each Hack              | display        | display link count and comment count                     | Pass      |
| each Hack              | display        | display "Find out more" link                             | Pass      |
|                        |                |                                                          |           |
| "Find out more"        | click          | forward to "Hack Detail" page                            | Pass      |
|                        | generate URL   | use tag   {% url 'hack_detail' hack.id %}                | Pass      |
|                        | result         | URL path:   "/hacks/33/"                                 | Pass      |
|                        |                |                                                          |           |
| Pagination             | display        | display previous page and next page link                 | Pass      |
| Pagination             | display        | display page of pages                                    | Pass      |


### Testing "Logout" link
| Element        | Action       | Expected Result                        | Pass/Fail |
| -------------- | ------------ | -------------------------------------- | --------- |
| Logout link    | display      | display Logout option in Navbar        | Pass      |
| Logout         | click        | forward to "Sign Out" page             | Pass      |
| Sign Out page  | display      | display confirm button to sign out     | Pass      |
| Confirm button | click        | forward to "Home" page                 | Pass      |
|                |              | user is signed out                     | Pass      |
|                |              | update entry in django_session table   | Pass      |
|                | generate URL | use tag  {% url 'home' %}              | Pass      |
|                | result       | URL path:  "/"                         | Pass      |
|                | analyze URL  | match view name "home"                 | Pass      |
|                | invoke       | invoke "class Index" in home app       | Pass      |
|                | render       | render "home/index.html in home app    | Pass      |
|                |              |                                        |           |
| Message        | display      | display "You have signed out." message | Pass      |


### Testing "Login" link
| Element            | Action       | Expected Result                                         | Pass/Fail |
| ------------------ | ------------ | ------------------------------------------------------- | --------- |
| Login link         | display      | display Login option in Navbar                          | Pass      |
|                    | click        | forward to "Sign In" page                               | Pass      |
|                    |              |                                                         |           |
| Sign In page       | display      | display sign in page                                    | Pass      |
| Login and Password | display      | display login and password                              | Pass      |
|                    |              |                                                         |           |
| Sign In button     | display      | display Sign In button                                  | Pass      |
| Sign In button     | click        | foward to "Home" page                                   | Pass      |
|                    |              | create entry in django_session table                    | Pass      |
|                    |              | update last_login field in auth_user table              | Pass      |
|                    |              |                                                         |           |
|                    | generate URL | use tag  {% url 'home' %}                               | Pass      |
|                    | result       | URL path:  "/"                                          | Pass      |
|                    | analyze URL  | match view name "home"                                  | Pass      |
|                    | invoke       | invoke "class Index" in home app                        | Pass      |
|                    | render       | render "home/index.html in home app                     | Pass      |
|                    |              |                                                         |           |
| Message            | display      | display "Successfully signed in as <username>." message | Pass      |


### Testing "Register/Sign Up" link
| Element        | Action       | Expected Result                                    | Pass/Fail |
| -------------- | ------------ | -------------------------------------------------- | --------- |
| Sign Up link   | display      | display "register" option in Navbar                | Pass      |
|                | click        | forward to "Sign Up" page                          | Pass      |
|                |              |                                                    |           |
| Sign Up page   | display      | display e-mail,  username, password fields         | Pass      |
| Sign Up button | display      | display sign up button                             | Pass      |
|                | click        | forward to "Home" page                             | Pass      |
|                |              | create entry in django_session table               | Pass      |
|                |              | create User in database                            | Pass      |
|                |              | update last_login field in auth_user table         | Pass      |
|                | generate URL | use tag  {% url 'home' %}                          | Pass      |
|                | result       | URL path:  "/"                                     | Pass      |
|                | analyze URL  | match view name "home"                             | Pass      |
|                | invoke       | invoke "class Index" in home app                   | Pass      |
|                | render       | render "home/index.html in home app                | Pass      |
|                |              |                                                    |           |
| Message        | display      | display "Successfully signed in as tashi." message | Pass      |


### Testing "Edit Hack" link - Hack Detail page
| Element            | Action         | Expected Result                                       | Pass/Fail |
| ------------------ | -------------- | ----------------------------------------------------- | --------- |
| Edit Hack button   | display        | display edit hack button on the Hack Detail page      | Pass      |
|                    |                |                                                       |           |
| template tag       | generate URL   | use tag   {% url 'edit_hack' hack.id %}               | Pass      |
|                    | result         | URL path:  e.g. "/hacks/edit/44/"                     | Pass      |
|                    |                |                                                       |           |
| Edit Hack button   | click          | forward to "Edit Hack" page                           | Pass      |
| URL routing        | analyze URL    | match view name "edit_hack"                           | Pass      |
| EditHack.as_view() | invoke         | invoke "class EditHack" in hack app                   | Pass      |
| LoginRequiredMixin | access control | verify authentication/authorization                   | Pass      |
| LoginRequiredMixin | SELECT query   | query "django_session" for authorization              | Pass      |
| template file      | render         | render  "hacks/edit_hack.html" in hacks app           | Pass      |
|                    |                |                                                       |           |
| Navbar             | display        | display Navbar menu                                   | Pass      |
| Navbar             | display        | display Navbar burger menu for small screen           | Pass      |
| Footer             | display        | display social links                                  | Pass      |
| Footer             | click          | forward to social links                               | Pass      |
|                    |                |                                                       |           |
| Edit Hack page     | display        | display title, ingredients, description, dropdown box | Pass      |
| Category dropdown  | click          | display category options from "hacks_hacks" table     | Pass      |
| Image              | click          | select image to upload                                | Pass      |
|                    |                |                                                       |           |
| Submit/Cancel      | display        | display submit and cancel button                      | Pass      |
| Submit             | click          | load Hack object into database                        | Pass      |
| Cancel             | click          | forward to "Home" page                                | Pass      |


### Testing "Delete Hack" link - Hack Detail page
| Element               | Action         | Expected Result                                            | Pass/Fail |
| --------------------- | -------------- | ---------------------------------------------------------- | --------- |
| Delete Hack button    | display        | display "delete hack" button on the Hack Detail page       | Pass      |
|                       |                |                                                            |           |
| Delete Hack button    | click          | forward to "confirm hack deletion" page                    | Pass      |
| URL routing: url.py   | analyze URL    | match view name "delete_hack_confirm"                      | Pass      |
| views.py              | invoke         | invoke "class DeleteHack" in hack app                      | Pass      |
| LoginRequiredMixin    | access control | verify authentication/authorization                        | Pass      |
| LoginRequiredMixin    | SELECT query   | query "django_session" for authorization                   | Pass      |
|                       |                |                                                            |           |
| Confirm Hack Deletion | display        | display text and button                                    | Pass      |
| Confirm button        | click          | POST request with path:  e.g.  "/hacks/delete/39/"         | Pass      |
|                       | DELETE query   | Cascaded Hack object delete as designed                    | Pass      |
|                       |                |    DELETE FROM "hacks_comment"                             | Pass      |
|                       |                |    DELETE FROM "hacks_favorite"                            | Pass      |
|                       |                |    DELETE FROM "hacks_like"                                | Pass      |
|                       |                |    DELETE FROM "hacks_hack"                                | Pass      |
|                       |                |    COMMIT                                                  | Pass      |
|                       |                |                                                            |           |
|                       | success_url    | GET request, path /hacks/hacks/                            | Pass      |
| URL routing: url.py   | analyze URL    | match view name "hacks"                                    | Pass      |
| views.py              | invoke         | invoke "class Hacks" in hacks app                          | Pass      |
| template file         | render         | render  "hacks/hacks.html"                                 | Pass      |
| Message               | display        | display "Your hack has been deleted successfully." message | Pass      |
|                       |                |                                                            |           |
| Navbar                | display        | display Navbar menu                                        | Pass      |
| Navbar                | display        | display Navbar burger menu for small screen                | Pass      |
| Footer                | display        | display social links                                       | Pass      |
| Footer                | click          | forward to social links                                    | Pass      |
|                       |                |                                                            |           |
| all Hacks             | display        | display multiple Hacks                                     | Pass      |
| each Hack             | display        | display title, posted by and created on                    | Pass      |
| each Hack             | display        | display link count and comment count                       | Pass      |
| each Hack             | display        | display "Find out more" link                               | Pass      |
|                       |                |                                                            |           |
| "Find out more"       | click          | forward to "Hack Detail" page                              | Pass      |
|                       | generate URL   | use tag   {% url 'hack_detail' hack.id %}                  | Pass      |
|                       | result         | URL path:   "/hacks/33/"                                   | Pass      |
|                       |                |                                                            |           |
| Pagination            | display        | display previous page and next page link                   | Pass      |
| Pagination            | display        | display page of pages                                      | Pass      |


### Testing "Like Hack" link - Hack Detail page
| Element             | Action         | Expected Result                                            | Pass/Fail |
| ------------------- | -------------- | ---------------------------------------------------------- | --------- |
| Like Hack button    | display        | display "like hack" button on the Hack Detail page         | Pass      |
|                     |                |                                                            |           |
| template tag        | generate URL   | use tag   {% url 'like_hack' hack.id %}                    | Pass      |
|                     | result         | URL path: e.g.   "/hacks/like/44/"                         | Pass      |
|                     |                |                                                            |           |
| Like Hack button    | click          | forward to "Hack Detail" page                              | Pass      |
|                     | request        | POST reqeust with path:  "/hacks/like/44/",   302 Redirect | Pass      |
| URL routing: url.py | analyze URL    | match view name "like_hack"                                | Pass      |
| views.py            | invoke         | invoke "class LikeHackView" in hack app                    | Pass      |
|                     | access control | verify authentication/authorization                        | Pass      |
|                     | SELECT query   | query "django_session" for authorization                   | Pass      |
|                     | INSERT query   | insert Like object into Like table                         | Pass      |
|                     | COMMIT         |                                                            | Pass      |
|                     |                |                                                            |           |
|                     | request        | GET request with path: e.g. /hacks/34/                     | Pass      |
| URL routing: url.py | analyze URL    | match view name "hack_detail"                              | Pass      |
| views.py            | invoke         | invoke "class HackDetail" in hacks app                     | Pass      |
|                     | access control | verify authentication/authorization                        | Pass      |
|                     | SELECT query   | query "django_session" for authorization                   | Pass      |
|                     | render         | render  "hacks/hack_detail.html"                           | Pass      |
|                     |                |                                                            |           |
| Hack Detail page    | display        | display "Hack Detail" page                                 | Pass      |
| Message             | display        | display "Successfully liked this Hack" message             | Pass      |


### Testing "Unlike Hack" link - Hack Detail page
| Element             | Action         | Expected Result                                                   | Pass/Fail |
| ------------------- | -------------- | ----------------------------------------------------------------- | --------- |
| Unlike Hack button  | display        | display "unlike hack" button on the Hack Detail page              | Pass      |
|                     |                |                                                                   |           |
| template tag        | generate URL   | use tag   {% url 'unlike_hack' hack.id %}                         | Pass      |
|                     | result         | URL path: e.g.   "/hacks/unlike/44/"                              | Pass      |
|                     |                |                                                                   |           |
| Unlike Hack button  | click          | forward to "Hack Detail" page                                     | Pass      |
|                     | request        | POST reqeust with path: e.g.   "/hacks/unlike/44/",  302 Redirect | Pass      |
| URL routing: url.py | analyze URL    | match view name "unlike_hack"                                     | Pass      |
| views.py            | invoke         | invoke "class UnlikeHackView" in hack app                         | Pass      |
|                     | access control | verify authentication/authorization                               | Pass      |
|                     | SELECT query   | query "django_session" for authorization                          | Pass      |
|                     |                |                                                                   |           |
|                     | DELETE query   | delete Like object from Like table                                | Pass      |
|                     |                |                                                                   |           |
| URL routing: url.py | analyze URL    | match view name "hack_detail" with hack id                        | Pass      |
| views.py            | invoke         | invoke "class HackDetail" in hacks app                            | Pass      |
|                     | access control | verify authentication/authorization                               | Pass      |
|                     | SELECT query   | query "django_session" for authorization                          | Pass      |
| template file       | render         | render  "hacks/hack_detail.html"                                  | Pass      |
|                     |                |                                                                   |           |
| Hack Detail page    | display        | display hack detail page                                          | Pass      |
| Message             | display        | display "Successfully unliked this Hack" message                  | Pass      |


### Testing "Add Comment" link - Hack Detail page
| Element                  | Action         | Expected Result                                                    | Pass/Fail |
| ------------------------ | -------------- | ------------------------------------------------------------------ | --------- |
| Add Comment button       | display        | display "add comment" button on the Hack Detail page               | Pass      |
|                          |                |                                                                    |           |
| template tag             | generate URL   | use tag   {% url 'create_comment' hack_id=hack.id %}               | Pass      |
|                          | result         | URL path: e.g.   "/hacks/create_comment/44/"                       | Pass      |
|                          |                |                                                                    |           |
| Add Comment button       | click          | forward to "Add Comment" page                                      | Pass      |
|                          | request        | GET reqeust, example: path /hacks/create_comment/40/               | Pass      |
| URL routing: url.py      | analyze URL    | match view name "create_comment"                                   | Pass      |
| views.py                 | invoke         | invoke "class CreateComment" in hack app                           | Pass      |
|                          | access control | verify authentication/authorization                                | Pass      |
|                          | SELECT query   | query "django_session" for authorization                           | Pass      |
| template file            | render         | render  "hacks/create_comment.html"                                | Pass      |
|                          |                |                                                                    |           |
| Add Comment page         | display        | display add comment page                                           | Pass      |
| Username field           | display        | display username as read-only                                      | Pass      |
| Comment text field       | display        | display comment field                                              | Pass      |
|                          |                |                                                                    |           |
| (if Submit button click) |                |                                                                    |           |
| Submit button            | display        | display submit button                                              | Pass      |
| Submit button            | Click          | forward to "Hack Detail" page                                      | Pass      |
|                          |                | POST request, path: example hacks/create_comment/40/, 302 Redirect | Pass      |
| URL routing: url.py      | analyze URL    | match view name "create_comment"                                   | Pass      |
| views.py                 | invoke         | invoke "class CreateComment" in hack app                           | Pass      |
|                          | access control | verify authentication/authorization                                | Pass      |
|                          | SELECT query   | query "django_session" for authorization                           | Pass      |
|                          | INSERT query   | insert Comment object into hacks_comment table                     | Pass      |
|                          | request        | GET request with path: example /hacks/40/                          | Pass      |
| URL routing: url.py      | analyze URL    | match view name "hack_detail"                                      | Pass      |
| views.py                 | invoke         | invoke "class HackDetail" in hacks app                             | Pass      |
|                          | access control | verify authentication/authorization                                | Pass      |
|                          | SELECT query   | query "django_session" for authorization                           | Pass      |
| template file            | render         | render  "hacks/hack_detail.html"                                   | Pass      |
| Hack Detail page         | display        | display hack detail page                                           | Pass      |
|                          |                |                                                                    |           |
| (if Cancel button click) |                |                                                                    |           |
| Cancel button            | display        | display cancel button                                              | Pass      |
| Cancel button            | click          | forward to "Hack Detail" page                                      | Pass      |
|                          |                | GET request, path: example /hacks/40/                              | Pass      |
| URL routing: url.py      | analyze URL    | match view name "hack_detail"                                      | Pass      |
| views.py                 | invoke         | invoke "class HackDetail" in hacks app                             | Pass      |
|                          | access control | verify authentication/authorization                                | Pass      |
|                          | SELECT query   | query "django_session" for authorization                           | Pass      |
| template file            | render         | render  "hacks/hack_detail.html"                                   | Pass      |
|                          |                |                                                                    |           |
| Hack Detail page         | display        | display hack detail page                                           | Pass      |
| Message                  | display        | display "Your comment has been added successfully." message        | Pass      |


### Testing "Add to Favorite" link - Hack Detail page
| Element                | Action         | Expected Result                                                           | Pass/Fail |
| ---------------------- | -------------- | ------------------------------------------------------------------------- | --------- |
| Add to Favorite button | display        | display "add to favorite" button on the Hack Detail page                  | Pass      |
|                        |                |                                                                           |           |
| template tag           | generate URL   | use tag   {% url 'add_to_favorite' hack.id %}                             | Pass      |
|                        | result         | URL path:  "/hacks/add_to_favorite/44/"                                   | Pass      |
|                        |                |                                                                           |           |
| Add to Favorite button | click          | GET request with path: e.g. "/hacks/add_to_favorite/44/",    302 Redirect | Pass      |
| URL routing: url.py    | analyze URL    | match view name "add_to_favorite"                                         | Pass      |
| views.py               | Invoke         | invoke "class AddToFavoritesView" in hack app                             | Pass      |
|                        | access control | verify authentication/authorization                                       | Pass      |
|                        | SELECT query   | query "django_session" for authorization                                  | Pass      |
|                        | INSERT query   | insert Favorite object into hacks_favorite table                          | Pass      |
|                        | COMMIT         |                                                                           | Pass      |
|                        |                |                                                                           |           |
|                        | request        | GET request, path example /hacks/40/, 200 Ok                              | Pass      |
| URL routing: url.py    | analyze URL    | match view name "hack_detail"                                             | Pass      |
|                        |                |                                                                           |           |
| template file          | invoke         | invoke "class HackDetail" in hacks app                                    | Pass      |
|                        | access control | verify authentication/authorization                                       | Pass      |
|                        | SELECT query   | query "django_session" for authorization                                  | Pass      |
| template file          | render         | render  "hacks/hack_detail.html"                                          | Pass      |
|                        |                |                                                                           |           |
| Hack Detail page       | display        | display hack detail page                                                  | Pass      |
| Message                | display        | display "You've added this hack to my favorite list." message             | Pass      |


### Testing "Remote from Favorite" link - Hack Detail page
| Element                     | Action         | Expected Result                                                         | Pass/Fail |
| --------------------------- | -------------- | ----------------------------------------------------------------------- | --------- |
| Remove from Favorite button | display        | display "remove from favorite" button on the Hack Detail page           | Pass      |
|                             |                |                                                                         |           |
| template tag                | generate URL   | use tag   {% url 'remove_from_favorite' hack.id %}                      | Pass      |
|                             | result         | URL path:  "/hacks/remove_from_favorite/44/"                            | Pass      |
|                             |                |                                                                         |           |
| Remove from Favorite button | click          | GET request, path example /hacks/remove_from_favorite/40/, 302 Redirect | Pass      |
| URL routing: url.py         | analyze URL    | match view name "remove_from_favorite"                                  | Pass      |
| template file               | invoke         | invoke "class RemoveFromFavoritesView" in hack app                      | Pass      |
|                             | access control | verify authentication/authorization                                     | Pass      |
|                             | SELECT query   | query "django_session" for authorization                                | Pass      |
|                             | DELETE request | delete Favorite object from hacks_favorite table                        | Pass      |
|                             | COMMIT         |                                                                         | Pass      |
|                             |                |                                                                         |           |
|                             | request        | GET request with path example /hacks/40/, 200 Ok                        | Pass      |
| URL routing: url.py         | analyze URL    | view name "hack_detail" has been properly matched                       | Pass      |
| HackDetail.as_view()        | invoke         | invoke "class HackDetail" in hacks app                                  | Pass      |
|                             | access control | verify authentication/authorization                                     | Pass      |
|                             | SELECT query   | query "django_session" for authorization                                | Pass      |
|                             | render         | render  "hacks/hack_detail.html"                                        | Pass      |
|                             |                |                                                                         |           |
| Hack Detail page            | display        | display hack detail page                                                | Pass      |
| Message                     | display        | display "Successfully removed from favorites." message                  | Pass      |


### Testing "Show/Hide Comments" link - Hack Detail page
| Element             | Action         | Expected Result                                                            | Pass/Fail |
| ------------------- | -------------- | -------------------------------------------------------------------------- | --------- |
| Comments counter    | display        | display "comments counter"                                                 | Pass      |
| Fields and Buttons  | display        | display fields and buttons on the Hack Detail page                         | Pass      |
|                     |                |                                                                            |           |
| Show/Hide Comments  | click          | display individual comments                                                | Pass      |
|                     |                |                                                                            |           |
| Remove Comment      | click          | GET request, path example /hacks/hacks/40/comments/43/delete, 302 Redirect | Pass      |
| URL routing: url.py | analyze URL    | match view name "delete_comment"                                           | Pass      |
| views.py            | Invoke         | match "class DeleteCommentView" in hack app                                | Pass      |
|                     | access control | verify authentication/authorization                                        | Pass      |
|                     | SELECT query   | query "django_session" for authorization                                   | Pass      |
|                     | DELETE request | delete Comment object from hacks_comment table                             | Pass      |
|                     | request        | GET request, path example /hacks/40/, 200 Ok                               | Pass      |
|                     |                |                                                                            |           |
| URL routing: url.py | analyze URL    | match view name "hack_detail"                                              | Pass      |
| views.py            | invoke         | invoke "class HackDetail" in hacks app                                     | Pass      |
|                     | access control | verify authentication/authorization                                        | Pass      |
|                     | SELECT query   | query "django_session" for authorization                                   | Pass      |
|                     | render         | render  "hacks/hack_detail.html"                                           | Pass      |
|                     |                |                                                                            |           |
| Hack Detail page    | display        | display hack detail components page                                        | Pass      |
| Message             | display        | display "Your comment has been deleted successfully." message              | Pass      |


### Testing "Find out more" link - My Favorite page and Browse Hack page
| Element             | Action         | Expected Result                                      | Pass/Fail |
| ------------------- | -------------- | ---------------------------------------------------- | --------- |
| "Find out more"     | display        | display "find out more" link                         | Pass      |
|                     |                |                                                      |           |
| template tag        | generate URL   | use tag   {% url 'hack_detail' hack.id %}            | Pass      |
|                     | result         | URL path:  "/hacks/44/"                              | Pass      |
|                     |                |                                                      |           |
| "Find out more"     | click          | GET request with path:  e.g.  "/hacks/40/",   200 ok | Pass      |
| URL routing: url.py | analyze URL    | match view name "hack_detail"                        | Pass      |
| views.py            | invoke         | invoke "class HackDetail" in hacks app               | Pass      |
|                     | access control | verify authentication/authorization                  | Pass      |
|                     | SELECT query   | query "django_session" for authorization             | Pass      |
| template file       | render         | render  "hacks/hack_detail.html"                     | Pass      |
|                     |                |                                                      |           |
| Hack Detail page    | display        | display hack detail page                             | Pass      |



