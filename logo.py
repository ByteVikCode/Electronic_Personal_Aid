import tkinter as tk
import os
import subprocess
import pyautogui

def run_program():
    print("Run button clicked!")
    # Directly execute the code from main.py here
    try:
        import main  # Import the contents of main.py
        # Call the main function or any other code you want to execute
        main.main_function()
    except Exception as e:
        print(f"Error executing main.py: {e}")

def exit_program():
    print("Exit button clicked!")
    root.destroy()


root = tk.Tk()
root.title("Electronic Personal Aid")
root.geometry("400x300")

# Styling
root.configure(bg="white")
root.resizable(True, True)

# Logo
logo_image = tk.PhotoImage(file="C:\\Users\\HP\\PycharmProjects\\Personal_Aid\\logo.png")
logo_label = tk.Label(root, image=logo_image, bg="white")  # Ensure the background matches the window
logo_label.pack(pady=20)

# Title
title_label = tk.Label(root, text="Electronic Personal Aid", font=("Arial", 18), bg="white")
title_label.pack()

# Buttons Frame
buttons_frame = tk.Frame(root, bg="white")  # Ensure the background matches the window
buttons_frame.pack(pady=20)

# Run Button
run_button = tk.Button(buttons_frame, text="Run", command=run_program, padx=10, pady=5, font=("Arial", 14))
run_button.grid(row=0, column=0, padx=10)

# Exit Button
exit_button = tk.Button(buttons_frame, text="Exit", command=exit_program, padx=10, pady=5, font=("Arial", 14))
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()
