# Massage Therapy Introduction
Welcome to Massage Therapy, my 4th portfolio project. My goal is simple: make massage therapy bookings as easy as a few clicks. Built with Django and  Bootstrap, my site offers a sleek and responsive experience for all users. Whether you're booking your next relaxation session or managing your clients.

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
    * [**User Flow Diagrams:**](#user-flow-diagrams)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Color Scheme:**](#color-scheme)
    * [**Typography**:](#typography)

2 [**Agile Development Process**](#agile-development-process)

3 [**Service Features**](#service-features)
  * [**Booking System**](#booking-system)
    * [**Online Booking:**](#online-booking)
    * [**Appointment Management:**](#appointment-management)

4 [**User Experience (UX)**](#user-experience-ux)

  * [**Design Philosophy**](#design-philosophy)
  * [**Accessibility Features**](#accessibility-features)

5 [**Technologies Used**](#technologies-used)

  * [**Front-End Technologies:**](#front-end-technologies)
  * [**Back-End Technologies:**](#back-end-technologies)

6 [**Testing Phase**](#testing-phase)

  * [**Functional Testing:**](#functional-testing)
  * [**Usability Testing:**](#usability-testing)

7 [**Deployment**](#deployment)
  * [**Deployment Steps:**](#deployment-steps)

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
    - Changes are immediately reflected on the client interface.

- **As a Therapist-Admin, I can set and update my availability, so that clients only book sessions when I am available.**
  - **Acceptance Criteria**:
    - Can create and modify available time slots.
    - Availability changes update in real-time on the booking system.
    - The system prevents double-booking of time slots.

#### Client User Stories

- **As a Client, I can browse different types of massages, so that I find the service that suits my needs.**
  - **Acceptance Criteria**:
    - View a list of all available massage types with details.
    - Filter or sort massage options based on preferences.
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
    - Receive notifications for new or changed appointments.

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
