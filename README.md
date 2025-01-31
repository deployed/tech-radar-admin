# Local Setup Instructions

Follow these steps to set up the application locally:

## Prerequisites

- To use this project, you need to have `uv` installed. You can install it using the following command:
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## Steps to Set Up the Application

1. **Install Required Packages**

   ```bash
   uv sync --locked
   ```

2. **Install pre-commis hooks**

   ```bash
      pre-commit install
   ```

3. **(Optional) Execute hooks on all files:**

   ```bash
      pre-commit run --all-files
   ```

4. **Migrate the Database**

   ```bash
   python manage.py migrate
   ```

5. **Load Fixtures**

   ```bash
   python manage.py loaddata fixtures/*.yaml
   ```

6. **Run the Development Server**

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
