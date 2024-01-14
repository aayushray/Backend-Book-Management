# Project Name

This project contains the backend components for Online Book Management System. The backend is built using Django.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (version 3.10)

To set up the backend, follow these steps:

1. Create a virtual environment:
    ```bash
    python -m venv myenv
    ```

2. Activate the virtual environment:
    ```bash
    source myenv/bin/activate
    ```

3. Install Django:
    ```bash
    pip install django
    ```

## Getting Started

To get started with the project, follow these steps:

### Backend

1. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. To generate and replace the secret key in the Django settings, follow these steps:

    1. Open the `Backend_Book_Management_System/settings.py` file.
    2. Locate the section with the comment `# SECURITY WARNING`.
    3. Generate a New Secret Key:
        1. Open a Python shell, and run the following commands:

            ```python
            import secrets
            secrets.token_urlsafe(50)
            ```
        2. Copy the generated secret key.

    3. Replace the line `SECRET_KEY = config('DJANGO_SECRET_KEY')` with the following code:

        ```python
        SECRET_KEY = 'your_generated_secret_key'
        ```

        Replace `'your_generated_secret_key'` with the actual secret key you generated.

    4. Save the `settings.py` file.

    It is important to keep the secret key confidential and not share it publicly.

3. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

    The backend server should now be running on `http://localhost:8000`.

## User Authentication

    To create different types of users for authentication purposes, you can follow these steps:

### Create Superuser

1. Open a terminal and navigate to the project directory.
2. Run the following command to create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
3. Enter a username, email (optional), and password for the superuser when prompted.
4. The superuser will be created and can be used to access the Django admin panel.

### Create Admin User

1. Log in to the Django admin panel using the superuser credentials.
2. Navigate to the "Users" section.
3. Click on "Add user" to create a new user.
4. Enter the required details for the admin user, such as username, email, and password.
5. Assign the user the "Staff status" and "Superuser status" to grant administrative privileges.
6. Save the user details.

### Create Normal User

1. Log in to the Django admin panel using the superuser or admin user credentials.
2. Navigate to the "Users" section.
3. Click on "Add user" to create a new user.
4. Enter the required details for the normal user, such as username, email, and password.
5. Save the user details.

Now you have created different types of users for authentication purposes. The superuser and admin user can access the Django admin panel, while the normal user can interact with the API endpoints based on their permissions.


## API Endpoints

- http://localhost:8000/api/book/ : Book List (Authenticated for Admins only)
- http://localhost:8000/api/book/1/ : View Book with specific Id (Authenticated for Admins only)
- http://localhost:8000/api/author/ : Authors List (Authenticated for Admins only)
- http://localhost:8000/api/author/1/ : View Author with specific Id (Authenticated for Admins only)
- http://localhost:8000/api/place-order/ : Place Order (Authenticated for All registered users)
- http://localhost:8000/api/orders/ : View Customer Order List (Authenticated for All registered users)
- http://localhost:8000/api/orders/1/ : View Customer Order with specific Id (Authenticated for All registered users)

## Usage

- Use the backend API endpoints at `http://localhost:8000/api/` for interacting with the backend API.
- Use [Postman](https://www.postman.com/) to make HTTP requests and test the API endpoints for the best usage possible.