# Django Real Estate Project

## Overview

Welcome to the Django Real Estate Project, a comprehensive web application designed to streamline the process of listing, searching, and booking real estate properties. This project leverages Django on the backend and HTML/CSS/JavaScript on the frontend to create a dynamic and user-friendly platform tailored for the real estate industry.

## Distinctiveness and Complexity

### Distinctive Features:

1. **Real Estate Focus:**
   - The project is exclusively dedicated to real estate management, distinguishing it from other projects in the course.
   - Provides a specialized platform for property owners and seekers, facilitating property listing, viewing, and booking.

2. **Advanced Filtering:**
   - Implements an advanced filtering system to enhance user experience.
   - Users can search for properties based on a variety of parameters, including the number of rooms, city, region, property type, and more.

3. **Booking System:**
   - Features a robust booking mechanism that allows users to reserve properties.
   - Automatic balance adjustments for users and real-time property status updates.

### Complexity Highlights:

1. **Modular Architecture:**
   - Utilizes a modular structure with two distinct apps: `real_estate` and `users`.
   - Encapsulates property-related functionalities in the `real_estate` app and user-related features in the `users` app.

2. **Django Models:**
   - Implements Django models for efficient database management.
   - Models include listings, property types, bookings, and a custom user model.

3. **Mobile-Responsive Design:**
   - Ensures a seamless user experience across devices with a mobile-responsive design.
   - Adapts to various screen sizes and resolutions for optimal usability.

4. **JavaScript Integration:**
   - Incorporates JavaScript on the frontend to enhance interactivity.
   - Enables dynamic updates and smooth user interactions.

## File Structure

### `real_estate` App:

- **`admin.py`:**
  - Configures the admin interface for property listings and images.

- **`forms.py`:**
  - Defines forms for property creation, editing, and image handling.

- **`models.py`:**
  - Contains Django models for listings, property types, images, bookings, and more.

- **`urls.py`:**
  - Defines URL patterns for property-related views.

- **`views.py`:**
  - Implements views for listing creation, filtering, and booking.

### `users` App:

- **`admin.py`:**
  - Configures the admin interface for the custom user model.

- **`forms.py`:**
  - Defines forms for user creation and modification.

- **`models.py`:**
  - Contains a custom user model extending Django's AbstractUser.

- **`urls.py`:**
  - Defines URL patterns for user-related views.

- **`views.py`:**
  - Implements views for user registration, login, and profile.

### Project-level Files:

- **`urls.py`:**
  - Defines the main URL patterns for the entire project.

- **`settings.py`:**
  - Configures Django project settings, including installed apps, middleware, and database settings.

- **`views.py` (project-level):**
  - Implements project-level views such as the index and authentication-related redirects.

## How to Run

To run the application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Navigate to the project directory and run `python manage.py migrate` to apply database migrations.
4. Create a superuser account using `python manage.py createsuperuser`.
5. Start the development server with `python manage.py runserver`.

Visit `http://localhost:8000` in your web browser to access the application.

## Additional Information

- **Database:**
  - SQLite is used as the default database for simplicity in the development environment.
  - The `DATABASES` configuration in `settings.py` can be modified for production use.

- **Media Files:**
  - Property images are stored in the `media` directory.
  - The `MEDIA_URL` and `MEDIA_ROOT` settings in `settings.py` can be adjusted based on deployment requirements.

- **Email Backend:**
  - The project uses the console email backend for development purposes.
  - Configure the `EMAIL_BACKEND` setting in `settings.py` for production email handling.
