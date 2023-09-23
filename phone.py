import random
import time
import speechrecognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Function to simulate a phone call confirmation
def make_phone_call(otp):
    engine.say(f"Calling user to confirm transaction with OTP: {otp}")
    engine.runAndWait()
    time.sleep(2)  # Simulating a call delay

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        engine.say("Please say 'confirm' or 'cancel' to proceed.")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        user_response = recognizer.recognize_google(audio).lower()
        engine.say(f"User response: {user_response}")
        engine.runAndWait()
        if "confirm" in user_response:
            return True
    except sr.UnknownValueError:
        engine.say("Speech recognition could not understand audio.")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say(f"Could not request results from Google Speech Recognition service; {e}")
        engine.runAndWait()

    return False

def main():
    try:
        # Simulate user inserting a card and entering PIN
        engine.say("Welcome to the ATM.")
        engine.runAndWait()
        card_number = input("Please enter your card number: ")
        pin = input("Please enter your PIN: ")

        # Simulate OTP generation
        otp = generate_otp()
        engine.say(f"Generated OTP: {otp}")
        engine.runAndWait()

        # Simulate asking the user if they want to confirm via phone call
        engine.say("Do you want to confirm this transaction via phone call? (yes/no):")
        engine.runAndWait()
        confirm_call = input()
        if confirm_call.lower() == 'yes':
            # Simulate making a phone call
            if make_phone_call(otp):
                engine.say("Transaction confirmed. Dispensing cash...")
                engine.runAndWait()
            else:
                engine.say("Transaction canceled.")
                engine.runAndWait()
        else:
            engine.say("Transaction canceled.")
            engine.runAndWait()

    except KeyboardInterrupt:
        engine.say("Transaction canceled due to user interruption.")
        engine.runAndWait()

if _name_ == "_main_":
    main()