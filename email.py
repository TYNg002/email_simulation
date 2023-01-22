# An Email Simulation

class Email:
    # construct Email class with some default property values 
    def __init__(self, title, email_contents, from_address):
        self.title = title
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    # function to mark email as read
    def mark_as_read(self):
        self.has_been_read = True

    # function to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True

# creates new Email object and adds it to the inbox
def add_email(title, email_contents, from_address):
    new_email = Email(title, email_contents, from_address)
    inbox.append(new_email)
    return new_email.title

# returns total emails in inbox
def get_count():
    email_count = len(inbox)
    return email_count

# prints email sender and content and marks email as read
def get_email(number):
    print(f"\nFrom:\n{inbox[number].from_address}\n")
    print(f"Contents:\n{inbox[number].email_contents}")
    inbox[number].has_been_read = True

# returns a list of unread emails
def get_unread_emails():
    unread_list = []
    # for each email in inbox, checks if email has been read
    # if not, that email gets added to unread_list
    for email in inbox:
        if not(email.has_been_read):
            unread_list.append(email.title)
    return unread_list

# returns a list of spam emails
def get_spam_emails():
    spam_list = []
    # for each email in inbox, checks if email has been marked as spam
    # if marked as spam, that email gets added to spam_list
    for email in inbox:
        if email.is_spam:
            spam_list.append(email.title)
    return spam_list

# deletes email from inbox
def delete():
    # present and ask user which email to delete
    print("Enter the number associated with the email you would like to delete:")
    show_emails()
    while True:
        # try loop catch runtime errors
        try:
            # print deletion confirmation directly before executing deleting line so the email 
            # title can be included in confirmation message
            email_index = int(input(": "))
            print(f"\n{inbox[email_index].title} has been deleted.")
            del inbox[email_index]
            break
        # guidance on multiple exception handling
        # https://www.geeksforgeeks.org/multiple-exception-handling-in-python/
        except (ValueError, IndexError):
            print("Input not associated with an email. Please try again.")

# prints titles of all emails in inbox with corresponding index number
def show_emails():
    for index, line in enumerate(inbox):
        print(f"{index}:\t{line.title}")

# initial empty inbox
inbox = []

# populate inbox
email1 = Email("Title 1", "Email content 1", "bob@domain.co")
inbox.append(email1)
email2 = Email("Title 2", "Email content 2", "doe@domain.co")
inbox.append(email2)

user_choice = ""

while user_choice != "quit":
    print(f"\nThere are a total of {get_count()} email(s).")
    user_choice = input("""What would you like to do:
Read
Mark spam
Send
Delete
Quit
: """)
    print("")
    # user chooses to read an email
    if user_choice.lower() == "read":
        # display unread emails
        if get_unread_emails() == []:
            print("There are no unread emails.")
        else:
            print(f"The following email(s) are currently unread:")
            for unread in get_unread_emails():
                print(unread)
        # display all emails to choose from
        print("\nEnter the number associated with the email you would like to view:")
        show_emails()
        # try/except to catch runtime errors
        while True:
            # display email information and mark email as read
            try:
                email_index = int(input(": "))
                get_email(email_index)
                inbox[email_index].mark_as_read()
                break
            except (ValueError, IndexError):
                print("Input not associated with an email. Please try again.")
    
    # user chooses to mark an email as spam
    elif user_choice.lower() == "mark spam":
    # display spam emails
        if get_spam_emails() == []:
            print("There are no emails marked as spam.")
        else:
            print("The following email(s) are currently marked as spam:")
            for spam in get_spam_emails():
                print(spam)
        # display all emails to choose from
        print("\nEnter the number associated with the email you would like to mark as spam:")
        show_emails()
        # try/except to catch runtime errors
        while True:
            # mark email as spam and display confirmation message
            try:
                email_index = int(input(": "))
                inbox[email_index].mark_as_spam()
                print(f"\n{inbox[email_index].title} has been marked as spam.")
                break
            except (ValueError, IndexError):
                print("Input not associated with an email. Please try again.")
    
    # user chooses to send an email to the inbox
    elif user_choice.lower() == "send":
        # request email information
        email_from = input("Enter the email address of the sender: ")
        email_title = input("\nEnter the title of the email: ")
        email_content = input("\nEnter the contents of the email: ")
        # use add email function and display confirmation message
        add_email(email_title, email_content, email_from)
        print(f"\n{email_title} has been sent to the inbox.")

    # user chooses to delete an email
    elif user_choice.lower() == "delete":
        delete()
    
    # user chooses to exit the program
    # loop will not run anymore as it does not fulfill the condition of the while loop
    elif user_choice.lower() == "quit":
        print("Program terminated.")
    
    # if user input is not valid
    else:
        print("Input not recognised. Please try again.")