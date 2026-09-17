# Event Reservation API Requirements

## Project Goal

The goal of this project is to build an API that allows organisers to create and manage events while attendees can view events and reserve available places.
The project will focus on enforcing realistic booking rules and developing a well-structured backend application.

## Users

The system will initially have two types of users conceptually:

**Organisers** can create events with information such as the event name, description, location, date and time, and capacity.

**Attendees** can view available events and create bookings for events that still have available places.

**Note** Version 1 will not include authentication, However i might introduced it in later versions.

## Events

An event will contain the following fields:

* **id**: the unique identifier of the event
* **name**: the name of the event
* **description**: a description of the event
* **location**: the location where the event takes place
* **event_datetime**: the date and time when the event takes place
* **capacity**: the maximum number of bookings allowed for the event
* **created_at**: the time when the event was created

## Bookings

A booking will contain the following fields:

* **id**: the unique identifier of the booking
* **event_id**: the ID of the event associated with the booking
* **attendee_name**: the name of the attendee making the booking
* **attendee_email**: the email address of the attendee making the booking
* **created_at**: the time when the booking was created

## Business Rules

The system must enforce the following rules:

* A booking cannot be created if the event does not exist.
* A booking cannot be created when the event has reached its maximum capacity.
* The same attendee email cannot book the same event more than once.
* A valid booking can be cancelled.
* Cancelling a booking should make that place available again.

## Version 1 Features

Version 1 will provide the core functionality needed to manage events and bookings.

It will allow:

* Creating events
* Viewing available events
* Viewing an individual event
* Creating bookings
* Viewing bookings for an event
* Cancelling bookings
* Enforcing event capacity
* Preventing duplicate bookings
* Preventing bookings for events that do not exist
* Automated testing of the main API and business rules

Version 1 will focus on the core booking logic before authentication and more advanced features are introduced.

## Future Features

Future versions may include:

* User registration and login
* Authentication
* Organizer and attendee roles
* Authorization and ownership rules
* PostgreSQL
* Database migrations
* More advanced event management
* Logging
* CI/CD
* Deployment
* Additional production-level improvements


