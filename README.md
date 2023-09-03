# Umar's Imaginary Woodworking

![Mockups](./readme_images/mockups.png)

Umar's Imaginary Woodworking is inspired by my uncle and my brother. My uncle is an avid woodworker and has produced some awesome pieces andmy brother is starting on is journey. Unfortunately, I have been unable to include much of their work at this time. This is a little site as if we are woodworker and carpenter taking bookings for consultations and work. We are able to upload and showcase our projects and visitors to the site are able to login and make and manage bookings for consultations/appointments with us. Hence the webpage now says Hassam Woodworking

**Live site: [HERE](https://umars-woodworking-78c6e707aec6.herokuapp.com/)**

## Contents

- [Umar's Imaginary Woodworking](#umars-imaginary-woodworking)
  - [Contents](#contents)
  - [UX Design](#ux-design)
    - [The Strategy Plane](#the-strategy-plane)
    - [The Scope Plane](#the-scope-plane)
    - [The Structure Plane](#the-structure-plane)
    - [The Skeleton Plane](#the-skeleton-plane)
    - [The Surface Plane](#the-surface-plane)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Testing](#testing)
  - [Deployment, forking, cloning](#deployment-forking-cloning)
  - [References](#references)

## UX Design

I identified 4 potential types of users:

1. Just browsing - this is someone who just happens on the page and may be drawn in
1. Someone looking for a specific project - this is someone who has arrived with a purpose that we may be able to fulfill
1. Already has an account, book and manage consultations and appointments - a satisfied and returning
1. The admin user - in this imaginary situation - would be myself and eventually a hired administrator

### The Strategy Plane

The vision is to provide a family the ability to showcase their woodworking that they're passionate about in order to get customers and start a conversation. The design should be robust and practical - suitable for people interested in durable and sustainable wooden products.

### The Scope Plane

- The admin user should be able to easily manage the products loaded and visible on the website
- The visitor should be able to view the portfolio of projects curated by the admin
- The visitor/user should be able to login
- The visitor/user should be able to book a consultation and view booked consultations

### The Structure Plane

[Link to full data model](./readme_images/django-data-model.png)

The core model I designed and utilised:
![Core data model](./readme_images/core-models.png)

Key things to note is the relation between the Booking and the User. I opted against uploading images for bookings at this stage but considered it as a possibility. Some people may find it useful, but the impact would be low as the next stage of the User Journey is to speak 'offline' and this could be covered more effectively with the expertise required. A picture would be less necessary and could be a blocker on the user journey.

The Project Model is separate and would be for the admin to manage and upload an image and give a blurb to advertise it to visitors to the website

### The Skeleton Plane

I used lucidchart to draw some basic wireframes to cover the main pages

![Wireframes](./readme_images/wireframes.png)

In words: the aim is to keep this simple, both as this is a Minimum Viable Product (MVP) and in line with the aesthetic of the main audience that is likely to be more practical. The main page is the homepage, with a simple navbar and footer, a brief 'sales pitch' and the portfolio of projects. From here users can click to login or sign up from the Nav bar and then this reveals the link to 'Book a Consultation' (a form page). It also allows the user to see their own bookings when they click 'View Bookings'

While this view is helpful for the admin, the main page him/her is the 'Manage Projects' page. This view allows visibility of all projects and and whether or not they are publically visible at a glance. It also links to forms to edit or delete as needed. Similarly the admin has access to all upcoming consultation bookings on another page to be able to contact customers about their enquiries and bookings and edit and/or approve as necessary. 

### The Surface Plane

As alluded throughout, the aim is to be simple. I selected the 'ADLaM Display' Google font for the the 'logo' or name as it looks a little like it could be an engraving. I also opted for a brown collour. This stylised name is to be used in both the navbar and footer. A similar lightened brown colour will be used for the paragraph and any instructions at the top of the pages

## Features

Homepage
Example Projects - manage and display
submit a project/meeting request
respond to requests

## Technologies

## Testing

Testing detailed in [TESTING.md](TESTING.md)

## Deployment, forking, cloning

## References

Hero Image? - Photo by Lum3n from Pexels: <https://www.pexels.com/photo/wood-chips-227577/>
<https://mdbootstrap.com/learn/mdb-foundations/bootstrap/hero-image/> - hero image help
<https://www.w3schools.com/howto/howto_css_hero_image.asp>
Bing Chat to generate some fluff text
<https://stackoverflow.com/questions/35751772/setting-current-user-on-django-vanilla-createview>
<https://stackoverflow.com/questions/63550890/how-to-pass-logged-users-id-to-createview>
<https://stackoverflow.com/questions/66248147/could-someone-explain-why-we-return-super-form-validform-in-form-valid-metho>
[Form date field fix](https://forum.djangoproject.com/t/cant-change-type-attribute-in-django-crispy-forms/10054/11)
[Top 5 errors accoring to Google](https://www.pingdom.com/blog/the-5-most-common-http-errors-according-to-google/)
[remove bootstrap button line](https://stackoverflow.com/questions/66436957/how-to-remove-the-small-blue-line-in-bootstrap-buttons)
Image by <a href="https://pixabay.com/users/clker-free-vector-images-3736/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=24260">Clker-Free-Vector-Images</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=24260">Pixabay</a>
[Footer from here](https://startbootstrap.com/snippets/sticky-footer-flexbox)
[footer stick to bottom](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14)
[active nav link](https://stackoverflow.com/questions/19268727/django-how-to-get-the-name-of-the-template-being-rendered)
[Mock-Up Generator](https://techsini.com/multi-mockup/index.php)
