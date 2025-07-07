💰 Personal Finance Manager

A simple Django-based personal finance tracking application that allows users to record, categorize, and manage their income and expenses. Built with Django and MySQL as the backend database.

📌 Features

Add, edit, delete, and view financial transactions

Track income, expenses, and current balance

Filter transactions by type, date, or keyword

Export transaction data to CSV

Responsive and simple UI with Bootstrap

Authentication system (optional, if implemented)

MySQL integration using .env for secure credentials

🛠️ Tech Stack

Backend: Django (Python)

Database: MySQL

Frontend: HTML, Bootstrap

Others: Python Dotenv, Django ORM, Git

  1. Clone the repository
   
    '''
    git clone https://github.com/yourusername/personal-finance-manager.git
    cd personal-finance-manager
    '''
  2. Create a virtual environment

    '''
    python -m venv .venv
    source .venv/bin/activate        # On Windows: .venv\Scripts\activate
    '''
     
  3. Install dependencies

    '''
    pip install -r requirements.txt
    '''

  4. Set up environment variables

    '''
    Create a .env file in the project root and define:
    '''
  5. Run migrations

    '''
    python manage.py makemigrations
    python manage.py migrate
    '''
  6. Run the development server
    Access the app at: http://localhost:8000

    '''
    python manage.py runserver
    '''


📁 Project Structure

    '''
    personal_finance_manager/
    ├── config/              # Django project settings
    ├── tracker/             # App for managing transactions
    ├── templates/           # HTML templates
    ├── .env                 # Environment variables
    ├── requirements.txt     # Python dependencies
    └── manage.py
    '''

🧠 What I Learned
    1. Structuring Django projects with reusable apps
    2. Using MySQL as a Django database backend
    3. Managing environment variables securely with python-dotenv
    4. Implementing dynamic forms, filters, and exporting to CSV
    5. SQL basics and queries for data summaries

📌 Future Improvements
    1. Add user authentication and profiles
    2. Visualization with charts for spending/income
    3. Monthly summaries
    4. REST API integration









   
