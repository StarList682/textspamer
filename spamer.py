import pyautogui
import time

def send_message(message, interval, repetitions):
    """
    Function to send a message at a specified interval.

    :param message: The text of the message to be sent.
    :param interval: The interval between messages in seconds.
    :param repetitions: The number of times the message will be sent.
    """
    for _ in range(repetitions):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(interval)

if __name__ == "__main__":
    message = input("Enter the message to send: ")
    interval = float(input("Enter the interval between messages (in seconds): "))
    repetitions = int(input("Enter the number of repetitions: "))

    print("You have 5 seconds to switch to the chat window.")
    time.sleep(5)

    send_message(message, interval, repetitions)
