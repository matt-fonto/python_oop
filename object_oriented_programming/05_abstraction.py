# Abstraction: expose only essential features and hide internal details of implementation
class EmailSender:
    def __init__(self, heading, body):
        self.heading = heading
        self.body = body
    
    # connect and prepare body will be called from the send_email
    # abstraction: we should hide unnecessary information from the instances
    # double underscore: name mangling, making the methods private
    # private method
    def __connect(self, smtp_server):
        print(f"Connecting to SMTP server: {smtp_server}")

    def __prepare_body(self):
        print(f"Preparing email with heading: {self.heading} and body: {self.body}")

    def __send(self):
        print("Sending email...")
    
    @staticmethod
    def get_smtp_server():
        return 3000

    # public, exposed method
    def send_email(self):
        # private methods: handle underlying complexities
        self.__connect(self.get_smtp_server()) # internal connection logic 
        self.__prepare_body() # internal body prep
        self.__send() # internal sending logic
        print("Email sent successfully")

email = EmailSender("meeting reminder", "Meeting today at 3 pm.")
email.send_email()