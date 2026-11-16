
from speech_to_text import listen
from ai_brain import get_ai_response
from text_to_speech import speak


def main():

    print("\n================================")
    print("       AI VOICE ASSISTANT")
    print("================================")

    while True:

        print("\nChoose your input method:")
        print("1. Speak using Microphone")
        print("2. Type your Message")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        # Voice input
        if choice == "1":

            user_text = listen()

        # Text input
        elif choice == "2":

            user_text = input("\nYou: ").strip()

        # Exit application
        elif choice == "3":

            print("\nThank you for using AI Assistant!")
            break

        else:

            print("\nInvalid choice! Please select 1, 2 or 3.")
            continue

        # Check user input
        if not user_text:
            print("No message received. Try again.")
            continue

        # Get response from AI
        ai_response = get_ai_response(user_text)

        # Convert AI response into speech
        if ai_response:
            speak(ai_response)


if __name__ == "__main__":
    main()
