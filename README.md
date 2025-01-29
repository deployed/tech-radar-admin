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
   uv sync
   ```

3. **Install pre-commis hooks**

   ```bash
      pre-commit install
   ```

4. **(Optional) Execute hooks on all files:**

   ```bash
      pre-commit run --all-files
   ```

5. **Migrate the Database**

   ```bash
   python manage.py migrate
   ```

6. **Load Fixtures**

   ```bash
   python manage.py loaddata fixtures/*.yaml
   ```

7. **Run the Development Server**

   ```bash
   uv run manage.py runserver
   ```

## Default Users

Use the following credentials to log in:

| Username | Password  |
| -------- | --------- |
| admin    | admin321! |

---

If you encounter any issues during the setup, feel free to reach out to the project maintainer.
