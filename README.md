# Local Setup Instructions

Follow these steps to set up the application locally:

## Prerequisites

- Ensure you have Python 3.13 installed on your machine. If not, download and install it from [python.org](https://www.python.org/).

## Steps to Set Up the Application

1. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Migrate the Database**

   ```bash
   python manage.py migrate
   ```

4. **Load Fixtures**

   ```bash
   python manage.py loaddata fixtures/*.yaml
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## Default Users

Use the following credentials to log in:

| Username | Password  |
| -------- | --------- |
| admin    | admin321! |

---

If you encounter any issues during the setup, feel free to reach out to the project maintainer.
