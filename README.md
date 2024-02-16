# Massage Therapy Introduction
Welcome to Massage Therapy, my 4th portfolio project. My goal is simple: make massage therapy bookings as easy as a few clicks. Built with Django and  Bootstrap, my site offers a sleek and responsive experience for all users. Whether you're booking your next relaxation session or managing your clients.

![home-page](./documentation/images/wireframes/introduction.png)

[Live Website](https://massage-therapy-fc86f4f7c039.herokuapp.com/)

# **Table Of Contents**
1 [**Planning Phase**](#planning-phase)
  * [**Strategy**](#strategy)
    * [**Service Aims:**](#service-aims)
    * [**Opportunities:**](#opportunities)
  * [**Scope**](#scope)
  * [**Structure**](#structure)
    * [**User Stories:**](#user-stories)
  * [**Skeleton**](#skeleton)
    * [**Wireframes:**](#wireframes)
    * [**User Flow Diagram:**](#user-flow-diagram)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Color Scheme:**](#color-scheme)
    * [**Typography**:](#typography)

2 [**Agile Development Process**](#agile-development-process)

3 [**Features**](#features)
  
4 [**User Experience (UX)**](#user-experience-ux)

  * [**Design Philosophy**](#design-philosophy)

5 [**Technologies Used**](#technologies-used)

  * [**Front-End Technologies:**](#front-end-technologies)
  * [**Back-End Technologies:**](#back-end-technologies)

6 [**Testing Phase**](#testing-phase)

7 [**Deployment**](#deployment)

8 [**Future Development**](#future-development)

9 [**Credits**](#credits)
  * [**Acknowledgements:**](#acknowledgements)


# Planning Phase

## Strategy
### Service Aims:
- To create a streamlined, user-friendly system for booking and managing massage appointments.

## Opportunities
- Enhance booking experience for clients.
- Efficient scheduling and management for therapists.
- Robust admin features for overall management and insights.

## Scope
### Functional Requirements:
- Dynamic booking system that allows clients to view available services and book appointments based on real-time availability.
### Content Requirements:
- Information about massage services, therapist details, personalized user dashboards.

## Structure
- User-friendly UI with easy navigation for clients, therapists, and admins.

## User Stories:
The goal is to create a user-friendly, secure, and efficient platform that allows for easy management of massage services, bookings, and user accounts.

### Sprint 1: Basic Setup and User Authentication

**Goals**: Establish the foundational framework and secure login functionality. 2 days.

#### User Stories

- **Therapist-Admin**
  - **As a Therapist-Admin, I can securely access the system to manage my business operations, so that the integrity and efficiency of business management are ensured.**
    - **Acceptance Criteria**:
      - Ability to log in and log out of the system.
      - Access to administrative features upon logging in.

#### Client User Stories

- **As a Client, I can register and log in with ease, so that I can efficiently manage my massage bookings.**
  - **Acceptance Criteria**:
    - Ability to register for an account with a username and password.
    - Ability to log in and log out of the web page.

### Sprint 2: Service and Appointment Models

**Goals**: Develop and integrate core functionalities for managing services and appointments. 3 days.

#### Therapist-Admin User Stories

- **As a Therapist-Admin, I can manage massage types, so that I offer various options to my clients.**
  - **Acceptance Criteria**:
    - Ability to add, edit, and delete massage types.
    - Each massage type includes picture, name, duration, price, and description.
    - Changes are immediately visible to clients on the booking platform.

- **As a Therapist-Admin, I can set and update my availability, so that clients only book sessions when I am available.**
  - **Acceptance Criteria**:
    - Availability changes update in real-time on the booking system.
    - The system prevents double-booking of time slots.

#### Client User Stories

- **As a Client, I can browse different types of massages, so that I find the service that suits my needs.**
  - **Acceptance Criteria**:
    - View a list of all available massage types with details.
    - Easy navigation to book selected massage services.

### Sprint 3: Booking Functionality

**Goals**: Implement functionality for clients to schedule appointments based on availability. 4 days.

#### Client User Stories

- **As a Client, I can book appointments based on the therapist's availability, so that I schedule a session conveniently.**
  - **Acceptance Criteria**:
    - Select desired massage type and view available slots.
    - Book an appointment with immediate confirmation.
    - View and manage upcoming appointments.

#### Therapist-Admin User Stories

- **As a Therapist-Admin, I can manage client appointments, so that I keep track of my daily schedule.**
  - **Acceptance Criteria**:
    - View upcoming and past appointments.
    - Reschedule or cancel appointments as needed.
    - Receive notifications after changing appointments.

### Sprint 4: Enhancements and User Interface

**Goals**: Finalize development with a focus on testing, UI/UX improvements, and user-friendly interface enhancements. 4 days.

#### General User Stories

- **As a User (Therapist-Admin, Client), I want a user-friendly and intuitive interface, so that interacting with the system is straightforward and pleasant.**
  - **Acceptance Criteria**:
    - The interface is easy to navigate.
    - Essential functions are accessible within a few clicks.
    - The design is responsive and works on various devices and screen sizes.

#### Therapist-Admin Specific Stories

- **As a Therapist-Admin, I can view and manage client profiles, so that I maintain up-to-date client information.**
  - **Acceptance Criteria**:
    - Access client contact information and booking history.
    - Update client information if needed.
    - Secure handling of client data.

#### Total time planned 13 days.

## Skeleton
### Wireframes
#### Home and Massage detail page.
<img src="./documentation/images/wireframes/wireframes1.jpg">

#### About and Booking page (only for users).
<img src="./documentation/images/wireframes/wireframes2.jpg">

#### User info for user and for superuser.
<img src="./documentation/images/wireframes/wireframes3.jpg">

## User Flow Diagram
<img src="./documentation/images/wireframes/flow.png">

## Database Schema

### AboutPage Model

| Field       | Type            | Description                                       |
|-------------|-----------------|---------------------------------------------------|
| name        | CharField       | The name or title of the about page content.      |
| description | TextField       | A detailed description of the massage therapy service. |
| image       | CloudinaryField | An optional image field for storing related imagery. |

### Massage Model

| Field          | Type            | Description                                       |
|----------------|-----------------|---------------------------------------------------|
| name           | CharField       | The name of the massage service.                  |
| featured_image | CloudinaryField | An image representing the massage service, with a default placeholder. |
| description    | TextField       | A brief description of the massage service.       |
| details        | TextField       | Additional details about the massage service.     |
| price          | DecimalField    | The cost of the massage service.                  |
| duration       | IntegerField    | The length of time the massage service takes, in minutes. |

### Booking Model

| Field    | Type         | Description                                                        |
|----------|--------------|--------------------------------------------------------------------|
| user     | ForeignKey   | A link to the Django user model, indicating which user made the booking. |
| massage  | ForeignKey   | A link to the `Massage` model, specifying the type of massage booked. |
| date     | DateField    | The date of the booking.                                           |
| time_slot| CharField    | The time slot of the booking, selected from predefined choices.    |
| status   | CharField    | The status of the booking (e.g., pending, approved, rejected), with default being 'pending'. |

#### Entity Relationship Diagram
<img src="./documentation/images/wireframes/diagram.png">

### Surface

#### **Color Scheme:**
- **Primary text color**: `#070808` - Used for the main body text, ensuring high contrast and readability.
- **Navigation and card text color**: `#202525` - Provides subtle contrast with lighter backgrounds for elegance and accessibility.
- **Active link color**: `rgb(139, 0, 104)` - A vibrant color highlighting active navigation links, aiding user orientation.
- **Information text on card styling color**: `rgb(22, 13, 13)` - A softer color for differentiating informational text from primary content.

#### **Typography:**
- **Main Fonts Used**: `Roboto`, sans-serif. Roboto is used throughout the site for its modern, readable appearance, applied to body texts, headers, navigation elements, and cards for consistency.
- **Font Weights**:
  - Body text is in standard weight for readability.
  - Headers (`h5`) are bolded with a weight of `900` for emphasis.
  - The `navbar-brand` has a weight of `700` for a balanced, noticeable presence.
- **Fallback Font**: Sans-serif. This generic font family ensures the site remains visually appealing and text is readable where Roboto is not available.


## Agile Development Process

From the start, I embraced an Agile development approach to bring this massage therapy booking platform to life. Agile's iterative nature allowed me to adapt to changes quickly, incorporate feedback efficiently, and ensure that the project continually moved forward in alignment with user needs and project goals.

### Embracing Agile Principles
I committed to the core principles of Agile development, focusing on delivering working software frequently, welcoming changing requirements

### Sprints and Iterations
The project was broken down into several sprints, each with specific goals and deliverables:

- **Sprint 1: Basic Setup and User Authentication** - The foundation was laid, focusing on secure login functionality and basic navigation. 2 days.
- **Sprint 2: Service and Appointment Models** - Core functionalities were developed, including managing services and setting up appointment models. 3 days.
- **Sprint 3: Booking Functionality** - Implemented the crucial booking system, allowing users to schedule appointments based on real-time availability. 4 days.
- **Sprint 4: Enhancements and User Interface** - Finalized the project with a focus on UI/UX improvements, making the interface as user-friendly and responsive as possible. 4 days

- **Overall Reflection on Planned Days**
Throughout the development process, I aimed to adhere closely to the planned durations for each sprint. While I was generally accurate in my estimations, I learned the importance of flexibility and the value of allocating additional time for debugging and enhancing features based on user feedback. This approach not only improved the quality of the platform but also enriched my development skills and project management capabilities.

### Agile Tools and Practices
- **Kanban Board:** Initially overwhelmed by the project's scope, I opted for a written plan, believing it would suffice for managing the development process. However, upon completing the project, I recognized the value of visual organization and transferred all user stories to a digital Kanban board. This shift not only helped me reflect on the project's workflow and scope but also became a pivotal tool for planning future enhancements, providing me with a clear, visual overview of the project's achievements.
- **Daily Standups:** Although working independently, I maintained the discipline of daily standups (with myself), reviewing what was accomplished the previous day and setting goals for the current day.
- **User Stories:** These were crucial in guiding the development process, ensuring that every feature developed served a direct user need or improved the user experience in a meaningful way.
- **Retrospectives:** At the end of each sprint, I took time to reflect on what went well, what could be improved, and how to make the next sprint even more productive.

### Continuous Feedback and Adaptation
Feedback loops were integrated throughout the development process. By presenting working versions of the software to my mentor and friends, I gathered invaluable insights that informed future development decisions and feature improvements.

### Looking Forward
Using the Agile method in this project taught me a lot about flexibility and quick adaptation. The Agile approach's benefits are clear and will definitely guide how I work on future projects.


## Features

### Home Page
The first thing you see on our site. It's designed to be welcoming. You can easily find your way around from here.

- **Navigation:** Helps you get around the site without hassle.
- **Social Media Links:** Check us out on social media through the links in the footer.

![Home Page Screenshot](./documentation/images/features/home_page.png)

### Massage Detail Page
- When you're curious about a specific massage service, the "Learn More" button takes you here. This page dives into the details of the service, including benefits, duration, and price. It's your go-to for getting to know exactly what each massage offers before making your appointment.

![Massage Detail Screenshot](./documentation/images/features/detail.png)

### About Page
- Discover more about our skilled therapist on the About Page, where you can learn about his expertise and passion for massage therapy. This section also provides direct contact information, making it easy for you to reach out with any questions or to discuss your specific needs.

![About Screenshot](./documentation/images/features/about.png)

### Booking Page
- Here's where you book your appointments. If you're logged in, just fill out the form and you're all set. You get confirmation message after you book.

![Booking Screenshot](./documentation/images/features/booking.png)

- You cannot book if the day is fully booked.
![Booking Screenshot](./documentation/images/features/fully_booked.png)


## Manage Appointments: user
- This is for users to see all their bookings. You can change details or cancel if you need to, keeping you in control of your schedule.

![Manage Appointments Screenshot](./documentation/images/features/manage_booking_user.png)

- If you press edit it brings you to edit booking page with current massage information. After coosing new booking it will brings you back to your bookings where you can see confirmation message. Also if status of booking was "approved" it will change to "pending" after editing.
![Manage Appointments Screenshot](./documentation/images/features/edit_booking.png)
![Manage Appointments Screenshot](./documentation/images/features/edit_confirm.png)

- Before you delete an appointment, a confirmation modal appears, asking if you're sure about your decision. This safety feature prevents accidental deletions, ensuring you have a moment to confirm your action.
![Manage Appointments Screenshot](./documentation/images/features/modal.png)

## Manage Appointments: superuser 
- When logged in as superuser, you'll get a list of all bookings from all users sorted by date. You can edit, delete, approve status of booking or reject booking. 
![Superuser Screenshot](./documentation/images/features/superuser.png)

## Navigation Menu
- Navigation menu inculdes:

- **Home**: Everyone can see this.
- **About**: Open for all visitors.
- **Booking**: For users who are logged in.
- **User Info**: Only visible for logged in users.
- **Login/Logout/Register**: Depending on whether you're logged in or not.

![navigation Screenshot](./documentation/images/features/navbar.png)

- Footer includes contact information and social links:
![footer Screenshot](./documentation/images/features/footer.png) 


## User Experience (UX)

In creating this massage therapy booking platform, I focused on delivering an experience that feels both welcoming and effortless. From the moment you land on the site to the moment you complete a booking, my goal is to ensure you find what you need with minimal fuss.

### Design Philosophy
My design approach is all about simplicity and functionality. I wanted to make sure that navigating through the platform is intuitive, making wellness accessible to everyone, no matter their tech-savviness.

### Key UX Considerations
- **Intuitive Navigation:** I made it a priority to organize the site in a way that's easy to understand and use. Finding and booking your next massage should be simple, whether it's your first visit or your hundredth.
- **Responsive Design:** With Bootstrap's help, I ensured that the site looks great and operates smoothly across all devices. It's important to me that you can book a massage from your phone just as easily as from your desktop.
- **Accessibility:** I've taken steps to make the website accessible to as many people as possible, following best practices for web accessibility. This is an ongoing effort, and I'm committed to improving it further.
- **Feedback Loops:** Clear and immediate feedback is crucial. Whether it's confirming your booking or alerting you to a form error, I made sure the website communicates effectively with you at every step.

### Research and Testing
Early on, I gathered feedback from potential users to understand their needs and preferences. This feedback was invaluable, shaping many of the design choices you see. Usability testing helped refine these ideas, ensuring the platform not only meets but exceeds user expectations.

### Future UX Goals
I'm always looking for ways to enhance your experience on the platform. Based on user feedback and the latest in UX best practices, I plan to continue evolving the site.
 


## Technologies Used

### Front-End Technologies:
- **HTML5**: Used for structuring the content and layout of the web pages.
- **CSS3**: Utilized for styling the web pages, enabling responsive design.
- **JavaScript**: Employed to add interactivity to the web pages.
- **Bootstrap 5**: A front-end framework used for creating responsive and mobile-first websites.

### Back-End Technologies:
- **Django 4.2.9**: The core web framework used for building the project.
- **Cloudinary**: Integrated for media management, allowing efficient upload, storage, and delivery of images.
- **PostgreSQL (via psycopg2 2.9.9)**: Selected as the production database.
- **Gunicorn 20.1.0**: Used as the WSGI HTTP server for deploying the Django application.

### Development and Deployment Tools:
- **Git**: Used for version control.
- **GitHub**: Hosts the project repository.
- **Heroku**: Used for deploying the application.
- **Whitenoise 6.6.0**: Utilized for serving static files efficiently in conjunction with Django.

### Django Extensions and Utilities:
- **django-allauth 0.57.0**: Integrated for authentication.
- **django-crispy-forms 2.1 & crispy-bootstrap5 2023.10**: Used for rendering forms.
- **django-summernote 0.8.20.0**: Added to provide a rich-text editing experience in admin forms.

### Other Technologies:
- **FontAwesome**: Used for icons.
- **favicon.io**: Used to create the favicon.
- **imageresizer.com**: Used to resize pictures for project.
- **chatGPT**: Used to generate content for a site.


## Testing Phase

I created separated file for testind [Testing.md](https://github.com/matus42/Massage-Therapy/blob/main/Testing.md).

## Deployment

### Deploy with Heroku

1. Visit the [Heroku website](https://www.heroku.com/). If you already have an account, [log in](https://id.heroku.com/login). If not, [sign up](https://signup.heroku.com/) for a new account.
2. Once logged in, navigate to your dashboard and click on the "New" button located at the top right corner. From the drop-down, select "Create new App."
3. Provide a unique name for your app in the "App name" field.
4. Choose a region closest to you in the "Choose a region" field for better performance.
5. Click the "Create app" button to proceed.
6. On the next page, at the top center, click on the "Settings" tab.
7. Scroll down to the "Config Vars" section and click on the "Reveal Config Vars" button.
8. Here, you'll enter the environment variables that are stored in your `env.py` file locally. These include:
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`
   - `CLOUDINARY_NAME`
   - `CLOUDINARY_URL`
   - `DATABASE_URL`
   - `SECRET_KEY`
9. Copy and paste these variables into the KEY field and their respective values into the VALUE field.
10. Return to the top of the page and select the "Deploy" tab.
11. In the "Deployment method" section, choose "GitHub" to connect your GitHub repository.
    1. Use the "Search" button under "Connect to GitHub" to find your project repository, then click "Connect" next to the correct repository.
    2. At the bottom of the page, click "Deploy Branch" to start the deployment process.
12. A build log will appear at the bottom of the screen. Upon successful build, a link to your deployed app will be displayed.

**Note:** Ensure your Heroku app link is added to `ALLOWED_HOSTS` in the `settings.py` file of your Django project. Also, set `DEBUG` to `False` for production, and verify that `requirements.txt` and `Procfile` are up to date and committed to your GitHub repository before deploying.

### Steps to Clone the Site

To create a personal copy of the repository on your GitHub account, follow these streamlined steps:

1. Go to the [repository page on GitHub](https://github.com/matus42/Massage-Therapy).
2. Locate the 'Fork' button at the top right corner of the page and click on it.
3. A copy of the repository will now be available in your GitHub account, allowing you to make modifications and experiment with the project independently.



## Future Development

As the Massage Therapy project continues to evolve, there are key areas identified for future development to enhance functionality, user experience, and overall service quality. Below are the planned enhancements:

### Enhanced Availability Management
To streamline the booking process and offer greater flexibility for both clients and therapists, we plan to introduce a more sophisticated availability management system. This system will allow therapists to dynamically update their available slots in real-time, providing clients with up-to-date options for scheduling their appointments. By implementing this feature, we aim to:

- Minimize booking conflicts and optimize the appointment scheduling process.
- Enable therapists to easily manage their schedules, accommodating both regular hours and exceptions (such as vacations or special events).
- Improve the overall efficiency of appointment management, leading to higher satisfaction for both clients and therapists.

### Detailed User Profiles
Recognizing the importance of personalization in enhancing the user experience, the next phase of development will focus on creating more detailed user profiles. These enriched profiles will serve as a foundation for several new features, including:

- Personalized treatment recommendations based on user preferences and treatment history.
- The ability to track and visualize progress over time, for both clients and therapists.
- Enhanced communication tools for therapists to provide feedback or follow-up care instructions to clients.

## Credits

- [Stack overflow](https://stackoverflow.com/questions/48508750/how-to-force-https-in-a-django-project-using-cloudinary) to help with Cloudinary and debugging,
- [This tutorial by John Abdsho on YouTube](https://www.youtube.com/watch?v=s5xbtuo9pR0&ab_channel=JohnAbdsho) served as a key inspiration for the booking system,
- The Code Institute's walkthrough project, `I Think Therefore I Blog`, was instrumental in laying the foundational knowledge and skills necessary for developing this project,
- My mentor, David Bowers, for his unwavering support and guidance throughout the project. His expertise and feedback were pivotal in navigating challenges and refining the project's direction,
- [Favicon generator](https://favicon.io/) to create my favicon,
- [chatGBT](https://chat.openai.com/) for generating content for my site and as my personal assistent,
- [Bootstrap](https://getbootstrap.com/) a powerful front-end framework for faster and easier web development.


### Acknowledgements:

I extend my deepest thanks to all who contributed to the success of my fourth project:

- **Code Institute and its Slack community**: Your educational resources and collaborative spirit have been foundational to my learning and project development.

- **Family and Friends**: Your engagement, feedback, and support have been invaluable. Thank you for your patience and encouragement.

- **David Bowes**: As my mentor, your guidance and wisdom have been crucial. Your support has been unwavering, and I am profoundly grateful.

- **John Whitehead**: A special thanks to you for reviewing my project and offering essential improvements. Your expertise has been a great help.

- **My Partner**: Thank you for your understanding and support as I dedicated myself to this project. Your patience means the world to me.

Your collective support has been instrumental in bringing this project to fruition.
