import postalsend
import json

def main():
    server = input("Enter postal sever domain: ")
    api_key = input("Enter API key: ")
    sender = input("From: ")
    recipient = input ("To: ")
    subject = input("Subject: ")
    text = input("Text: ")


    print("Sending...")
    postalsend.login(server, api_key)
    response = postalsend.send(from_address=sender, to_address=recipient, subject=subject, plain_body=text)

    # Pretty print the response
    print(json.dumps(response, indent=2))

    print("Setting up push...")
    postalsend.push_setup(recipient, sender)

    print("Sending push...")
    while True:
        postalsend.push_send(subject, tag="test", plain_body="this is a test push notification")
        input("Press Enter to send again...")


if __name__ == "__main__":
    main()