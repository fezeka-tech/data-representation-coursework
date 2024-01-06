# datarepresentationcoursework
H. Dip
Certainly! Below is a basic README template for your Flask application. Please customize it according to your specific application details and requirements.

---

# Flask RESTful API with Database

This is a simple Flask web application with a RESTful API that links to one or more database tables. The application uses Flask, SQLAlchemy, and SQLite to demonstrate basic CRUD (Create, Read, Update, Delete) operations on a database.

## Getting Started

Follow the instructions below to set up and run the Flask application on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fezeka-tech/data-representation-coursework.git
   cd data-representation-coursework
   ```

2. Host my Flask application on PythonAnywhere byfollowing these steps:

- Create an Account on PythonAnywhere:
- Upload my Files:
- Upload my app.py file and the templates folder to my PythonAnywhere account. 
- Ensure that both app.py and the templates folder are in the same directory.

3. Create a virtual environment:

Open a Bash console on PythonAnywhere.

Navigate to the directory where your files are located,and create virtual envirenment.
    
  ```bash
  mkvirtualenv --python=/usr/bin/python3.8 myvirtualenv  # Use the appropriate Python version
  ```

4. ```bash
   workon myvirtualenv
   ```

5. Install dependencies:

   ```bash
   pip install Flask
   pip install SQLAlchemy
   ```

6. import sys
   path = '/home/fezekan/mysite/app.py'  # Update this path
  if path not in sys.path:
      sys.path.append(path)

from app import app as application

7. Run the Flask application:

   ```bash
   python app.py
   ```
   

## Project Structure

- `app.py`: Main Flask application file containing routes, models, and database configurations.
- `templates/`: Folder containing HTML templates for rendering web pages.
- `venv/`: Virtual environment folder (ignored by version control).
- `requirements.txt: List of Python dependencies.

## Usage

- The web application provides a simple interface to perform CRUD operations on books.
- The API can be accessed at `/api/books` for book-related operations.

## Additional Notes

- Modify the database URI in `app.py` to use an absolute path.
- Ensure the Flask application has the necessary permissions to read and write to the database directory.

---

## Web address: 
https://eu.pythonanywhere.com/user/fezekan/files/home/fezekan/mysite
