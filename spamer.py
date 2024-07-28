import pyautogui
import time
import emoji
import pyperclip

def send_message(message, interval, repetitions):
    """
    Function to send a message at a specified interval.

    :param message: The text of the message to be sent.
    :param interval: The interval between messages in seconds.
    :param repetitions: The number of times the message will be sent.
    """
    message = emoji.emojize(message, language='alias')  # Convert emoji aliases to actual emojis
    for _ in range(repetitions):
        pyperclip.copy(message)  # Copy the message to the clipboard
        pyautogui.hotkey("ctrl", "v")  # Paste the message from the clipboard
        pyautogui.press("enter")
        time.sleep(interval)

if __name__ == "__main__":
    message = input("Enter the message to send (you can use emoji aliases, e.g., :smile:): ")
    interval = float(input("Enter the interval between messages (in seconds): "))
    repetitions = int(input("Enter the number of repetitions: "))

    print("You have 5 seconds to switch to the chat window.")
    time.sleep(5)

    send_message(message, interval, repetitions)
