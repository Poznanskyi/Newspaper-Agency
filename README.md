# Newspaper Agency

Welcome to the **Newspaper Agency**! This site is in the early stages of production, designed to post fictional news created purely for fun. Our mission is to entertain and provide a light-hearted take on the world of news.

## Live Site

You can access the site at: [Newspaper Agency](https://newspaper-agency-cict.onrender.com).

## Superuser Credentials

For testing purposes, you can use the following superuser account or create another one:

- **Username**: `qwerty`
- **Password**: `qpwoeiruty1234`

## Installation & Run

### Set Up the Environment

To run the project, you need to set up a virtual environment. Follow the instructions based on your operating system.

#### On Windows:

1. Open your command prompt or PowerShell.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   
3. Activate the virtual environment:
venv\Scripts\activate

#### On UNIX or macOS:

1. Open your terminal.
2. Create a virtual environment:

   python3 -m venv venv

3. Activate the virtual environment:
source venv/bin/activate

#### Install Requirements
Once the virtual environment is activated, install the required packages:

pip install -r requirements.txt

#### Create a Superuser (Optional)
If you want to access all features, you can create a superuser account:

python manage.py createsuperuser

Set Environment Variable
Make sure to set any necessary environment variables for your project.

Run the Project
Finally, run the development server:

python manage.py runserver
You can now access the site at http://127.0.0.1:8000/.

Enjoy exploring the world of fictional news!