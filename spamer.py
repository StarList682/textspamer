import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import emoji
import pyperclip

def send_message():
    try:
        message = message_entry.get()
        interval = float(interval_entry.get())
        repetitions = int(repetitions_entry.get())

        message = emoji.emojize(message, language='alias') 
        
        print("You have 5 seconds to switch to the chat window.")
        time.sleep(5)

        for _ in range(repetitions):
            pyperclip.copy(message)
            pyautogui.hotkey("ctrl", "v") 
            pyautogui.press("enter")
            time.sleep(interval)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values for interval and repetitions.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Auto Message Sender")
root.geometry("400x300")
root.configure(bg="#2e2e2e")
title_label = tk.Label(root, text="Auto Message Sender", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)
frame = tk.Frame(root, bg="#2e2e2e")
frame.pack(pady=10)
tk.Label(frame, text="Message:", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
message_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
message_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Interval (seconds):", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
interval_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
interval_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Repetitions:", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
repetitions_entry = tk.Entry(frame, width=30, font=("Helvetica", 12))
repetitions_entry.grid(row=2, column=1, padx=10, pady=10)
send_button = tk.Button(root, text="Send Message", command=send_message, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12, "bold"))
send_button.pack(pady=20)
root.mainloop()
