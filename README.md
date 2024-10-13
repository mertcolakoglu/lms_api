# Learning Management System (LMS) API

## Project Overview

This project is a comprehensive RESTful API for a Learning Management System built using Django and Django Rest Framework. It provides a robust backend for managing courses, students, instructors, learning materials, and student progress tracking. The system is designed to facilitate online learning, course management, and student engagement.

## Features

- User authentication and authorization using Djoser and JWT
- Course creation and management
- Student enrollment system
- Lecture and assignment management
- Discussion forums for courses
- Student progress tracking
- Grading system

## Tech Stack

- Python
- Django 5.1.2
- Django Rest Framework
- Djoser for authentication
- Simple JWT for token-based authentication
- SQLite (can be easily switched to other databases)

## Project Structure

The project is organized into the following Django apps:

1. **users**: Handles user authentication, registration, and profile management
2. **courses**: Manages course information and student enrollments
3. **materials**: Handles learning materials like lectures and assignments
4. **discussions**: Manages course discussions and forums
5. **progress**: Tracks student progress and grades

## Key Features in Detail

### Authentication

- Uses Djoser for user registration, login, and management
- JWT (JSON Web Tokens) for secure, token-based authentication
- Custom user model with roles (student, instructor, admin)

### User Profiles

- Automatic profile creation using Django signals when a new user registers
- Profile model extends user information with additional fields like bio and avatar

### Course Management

- CRUD operations for courses
- Enrollment system for students
- Permissions to ensure only instructors can create and modify courses

### Learning Materials

- Structured content with lectures and assignments
- Video integration for lectures
- Assignment submission and grading system

### Discussions

- Forum-like discussion feature for each course
- Nested comments support
- CRUD operations for discussions and comments

### Progress Tracking

- Automatic progress tracking for students
- Calculates completion percentage based on lectures viewed and assignments submitted
- Provides detailed progress information per course

## API Endpoints

Here are some of the key API endpoints:

- `/auth/`: Djoser authentication endpoints
- `/api/courses/`: Course-related operations
- `/api/lectures/`: Lecture management
- `/api/assignments/`: Assignment handling
- `/api/discussions/`: Discussion forum endpoints
- `/api/progress/`: Student progress tracking

For a full list of endpoints and their usage, please refer to the API documentation.

## Setting Up the Project

1. Clone the repository:
   ```
   git clone https://github.com/mertcolakoglu/lms_api.git
   cd lms_api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The API should now be accessible at `http://localhost:8000/`.

## Environment Variables

The project uses environment variables for sensitive information. Create a `.env` file in the root directory with the following variables:

```
SECRET_KEY=your_secret_key_here
DEBUG=True
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

---

For any questions or support, please open an issue on the GitHub repository.