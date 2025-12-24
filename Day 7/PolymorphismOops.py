# Parent class
class Notification:
    def send(self, message):
        # This method is meant to be overridden
        # Parent gives a common method name
        pass

# Child class 1
class EmailNotification(Notification):
    def send(self, message):
        # Same method name 'send'
        # Different behavior
        print(f"Sending Email: {message}")

# Child class 2
class SMSNotification(Notification):
    def send(self, message):
        # Same method name 'send'
        # Different behavior
        print(f"Sending SMS: {message}")

# This function does NOT care about notification type
def notify_user(notification):
    # Polymorphism happens here
    # Python decides which send() to call at runtime
    notification.send("Hello User")

# Using different objects
notify_user(EmailNotification())
notify_user(SMSNotification())
