# Gmail API Client

This Python script allows you to interact with the Gmail API for tasks such as authentication, reading the latest emails, sending emails, and deleting emails.

## Prerequisites

- Python 3.10.7 or later
- Google API Client Library for Python
- Google OAuth Client Library for Python

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/samsegomof/gmail_api_task.git
    cd gmail_api_task
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain Google API credentials:

    - Go to the [Google Developers Console](https://console.developers.google.com/).
    - Create a new project and enable the Gmail API.
    - Create OAuth 2.0 credentials and download the credentials JSON file.
    - Rename the JSON file to `credentials.json` and place it in the project directory.

## Usage

1. Run the script:

    ```bash
    python gmail_script.py
    ```

2. Follow the instructions to authorize the application to access your Gmail account.

3. Choose the action you want to perform (read emails, send email, delete email) by entering the corresponding number.

4. Follow the prompts to provide necessary information (e.g., email addresses, subject, message text).

## Features

- **Authentication**: Authenticate with Gmail API using OAuth 2.0.
- **Read Emails**: Get information about the latest emails in your inbox.
- **Send Email**: Send an email from your Gmail account.
- **Delete Email**: Delete an email from your Gmail account by providing its ID.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
