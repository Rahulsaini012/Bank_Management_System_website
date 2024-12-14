# Bank Management System

This is a simple Bank Management System developed using HTML, CSS, and Python (Flask). It allows users to create accounts and login with a secure 4-digit PIN.

## Features
- **Create Account**: Allows a user to create a bank account by entering basic details like username, contact number, city, state, and amount.
- **Login**: Users can log in using their username and 4-digit PIN.
- **Responsive Design**: The interface is designed to be responsive for all screen sizes, from desktops to mobile devices.

## Technologies Used
- **Frontend**: HTML, CSS (with Flexbox and animations for visual effects)
- **Backend**: Python (Flask framework)
- **Others**: JavaScript (for form toggling and basic client-side interaction)

## Prerequisites
To run this project, you need to have the following installed:
- Python 3.x
- Pip (Python package manager)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/bank-management-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd bank-management-system
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000` to access the Bank Management System.

## File Structure

- `app.py`: Flask application that handles the server-side logic for creating accounts and logging in.
- `templates/`: Contains HTML files for the frontend.
- `static/`: Contains static assets like images, CSS, and JavaScript files.

## Example Screenshots

### Create Account Form
![Create Account Form](static/images/create-account.png)

### Login Form
![Login Form](static/images/login-form.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
