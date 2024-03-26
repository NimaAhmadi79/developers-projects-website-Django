
# Django Developer Marketplace

This project is a web platform where developers can create accounts, upload their projects as products, and showcase them to potential buyers. Other users can browse through the listed projects and make purchases as needed. The project is built using Django, a high-level Python web framework, providing a robust and scalable solution for managing user accounts, product listings, and interactions.

## Features

- **User Authentication**: Developers can create accounts and log in securely to manage their projects.
- **Product Management**: Users can create, update, and delete their project listings with ease.
- **Project Listings**: Projects are displayed with details such as title, description, demo link, source link, and tags for easy browsing.
- **Comments and Voting**: Users can leave comments and vote on projects, enhancing interaction and feedback.
- **Tagging System**: Projects can be tagged with relevant keywords for better categorization and searchability.
- **Media Upload**: Developers can upload images to showcase their projects effectively.

## Installation

To run the project locally, follow these steps:

1. **Clone the Repository**: 
    ```
    git clone <repository-url>
    ```

2. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Database Setup**:
    - Ensure you have a PostgreSQL database configured. Update the `DATABASES` settings in `nima/settings.py` accordingly.
    - Run migrations:
        ```
        python manage.py migrate
        ```

4. **Run the Development Server**:
    ```
    python manage.py runserver
    ```

5. **Access the Application**:
    Open a web browser and go to `http://localhost:8000` to access the application.

## Usage

1. **User Registration**:
    - Navigate to the registration page and create a new account.

2. **Project Management**:
    - Once logged in, users can create new projects by providing details such as title, description, demo link, source link, and tags.
    - Projects can be updated or deleted as needed.

3. **Browsing Projects**:
    - Browse through the listed projects on the home page.
    - Click on a project to view its details, including comments and voting options.

4. **Interaction**:
    - Leave comments on projects to provide feedback or ask questions.
    - Vote on projects to indicate interest or quality.

5. **Searching**:
    - Utilize the search functionality to find projects based on keywords or tags.

## Contributing

Contributions to the project are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request.




