#  Event Management API

A **Django REST Framework (DRF)** project that allows users to create, view, RSVP, and review events — with secure authentication, permissions, and filtering.

---

##  Features

###  User Accounts
- User registration and login using **JWT authentication**
- Extended user profile with full name, bio, location, and profile picture

###  Event Management
- Create, view, update, and delete events
- Only the **organizer** can edit or delete their event
- Supports **public** and **private** events
- Search and filter events by title, location, or organizer
- Pagination for event listings

###  RSVP System
- RSVP to events with status: `Going`, `Maybe`, or `Not Going`
- Each user can RSVP to an event only once

###  Reviews
- Add one review per user per event
- View all reviews for a specific event
- Handles duplicate review prevention

###  Authentication & Permissions
- JWT-based authentication using `rest_framework_simplejwt`
- Custom permission to restrict editing/deleting to event organizers
- Private events accessible only to invited users

---

##  Tech Stack

- **Python 3.12+**
- **Django 5+**
- **Django REST Framework**
- **SQLite** (default, easy setup)
- **Simple JWT**
- **django-filter**

---

##  Installation & Setup

-  Clone the repository
-  Create and activate a virtual environment
-  Install dependencies
-  Apply migrations
-  Create a superuser (for Django Admin)
-  Run the development server

---

## **API Endpoints**:

- **Event API**:
  - `POST /events/`: Create a new event (authenticated users only).
  - `GET /events/`: List all public events (with pagination).
  - `GET /events/{id}/`: Get details of a specific event.
  - `PUT /events/{id}/`: Update an event (only the organizer can edit).
  - `DELETE /events/{id}/`: Delete an event (only the organizer).

- **RSVP API**:
  - `POST /events/{event_id}/rsvp/`: RSVP to an event.
  - `PATCH /events/{event_id}/rsvp/{user_id}/`: Update RSVP status.

- **Review API**:
  - `POST /events/{event_id}/reviews/`: Add a review for an event.
  - `GET /events/{event_id}/reviews/`: List all reviews for an event.
