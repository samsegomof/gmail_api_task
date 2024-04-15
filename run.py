from gmail_script import GmailClient


class GmailCLI:
    """A simple command-line interface for interacting with the Gmail API."""
    def __init__(self):
        self.gmail_client = GmailClient()

    def run(self):
        print("Welcome to Gmail Client!")

        while True:
            print("\nChoose an action:")
            print("1. Read emails")
            print("2. Send email")
            print("3. Delete email")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.read_emails()
            elif choice == '2':
                self.send_email()
            elif choice == '3':
                self.delete_email()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

    def read_emails(self):
        print("\nFetching the latest emails...\n")
        self.gmail_client.get_last_emails()

    def send_email(self):
        sender = input("Enter your email address: ")
        recipient = input("Enter recipient's email address: ")
        subject = input("Enter email subject: ")
        message_text = input("Enter email message: ")
        self.gmail_client.send_email(sender, recipient, subject, message_text)

    def delete_email(self):
        message_id = input("Enter the ID of the email you want to delete: ")
        self.gmail_client.delete_email(message_id)


if __name__ == "__main__":
    gmail_cli = GmailCLI()
    gmail_cli.run()
