### CodeDais (E-Learning Platform)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Files and Folders](#files-and-folders)
- [Manual Testing](#manual-testing)
- [Usage](#usage)
- [Future Work](#future-work)

### Description
CodeDais is an e-learning platform designed to provide a comprehensive and intuitive user experience for students and educators. The platform leverages Python, Django, HTML5, CSS3 (Bootstrap), and MySQL to deliver robust functionality and secure data management.

### Features
- **User Authentication and Authorization:** Implemented secure authentication using Django’s built-in system, ensuring user data integrity and protection.
- **Optimized Database Interactions:** Utilized Django ORM for seamless data retrieval and storage.
- **User Functionalities:** Enabled registration, login, course purchases, and personalized dashboard views.
- **User-Centric Dashboard:** Crafted a dynamic dashboard to display enrolled courses.

### Technologies Used
- **Backend:** Python, Django, MySQL
- **Frontend:** HTML5, CSS3 (Bootstrap)
- **Template Engine:** Jinja2
- **Database Management:** Django ORM (Object Relational Mapper)

### Files and Folders
- **CodeDais/:**
  - `settings.py`: Contains project settings such as database configuration, installed apps, static files configuration, etc.
  - `urls.py`: Main URL configuration for the project, including routing to app-level URLs.
  
- **elearning/ (Django App):**
  - `models.py`: Defines Django models for the application, including users, courses, enrollments, etc.
  - `forms.py`: Automatically generates forms based on models, reducing redundancy and ensuring consistency.
  - `views.py`: Contains business logic for handling requests, rendering templates, processing forms, etc.
  - `urls.py`: App-level URL configuration for routing requests to appropriate view functions.
    
- **static/:** Folder containing CSS files, images, JavaScript, or other static assets used in the application.
  - `style.css`: Custom CSS styles for the application.
  - `images/`: Folder containing image assets used in the application.
    
- **templates/:** Folder containing HTML templates for rendering views and pages.
  - `base.html`: Base template containing common elements like header, footer, etc.
  - Other HTML files for specific pages or components.

### Manual Testing
- **Register a New Account:**
  - Open the application in your web browser.
  - Click on the "Register" link to create a new account.
  - Enter your details and submit the form.
  
- **Log In to Your Account:**
  - After registering, log in using your credentials.
  - Verify that you can successfully access your account dashboard.
  
- **Enroll in a Course:**
  - Browse available courses and select one to enroll.
  - Complete the purchase process to enroll in the course.
  
- **View Enrolled Courses:**
  - Navigate to your dashboard to see the list of courses you are enrolled in.
  - Access course materials and track your progress.

### Usage
- **Run the Django development server:**
  - `python manage.py runserver`
- **Open your web browser and visit:**
  - `http://localhost:8000/`
  - Register or log in with your credentials to start using the e-learning platform.

### Future Work
In future iterations of the project, there is a plan to implement the following features:
- **Advanced Analytics:** Integrate analytics on the home page to show user engagement, popular courses, and performance metrics.
- **Course Recommendations:** Implement a recommendation system to suggest courses based on user preferences and activity.

For any questions or feedback, feel free to contact the project owner.

Happy learning! 🚀
