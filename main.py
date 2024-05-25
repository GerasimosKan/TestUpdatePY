import tkinter as tk
from tkinter import messagebox
import requests
import os

GITHUB_REPO = "https://api.github.com/repos/GerasimosKan/TestUpdatePY"
FILES_TO_UPDATE = ["module1.py", "module2.py"]

def check_for_updates():
    try:
        # Get the latest release information
        response = requests.get(f"{GITHUB_REPO}/releases/latest")
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release.get('tag_name', 'No version found')

        # Read the current version from the local version.txt
        with open("version.txt", "r") as f:
            current_version = f.read().strip()

        if latest_version != current_version:
            update_code_files()
            with open("version.txt", "w") as f:
                f.write(latest_version)
            messagebox.showinfo("Update Successful", "Code has been updated to the latest version.")
        else:
            messagebox.showinfo("No Update Available", "You already have the latest version.")

        # Update version label
        version_label.config(text=f"Version: {current_version}")

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to check for updates: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_code_files():
    for file in FILES_TO_UPDATE:
        file_url = f"https://raw.githubusercontent.com/GerasimosKan/TestUpdatePY/main/{file}"
        response = requests.get(file_url)
        response.raise_for_status()
        with open(file, "w") as f:
            f.write(response.text)

def create_ui():
    root = tk.Tk()
    root.title("Update Checker")
    root.geometry("400x250")  # Set window size

    # Add padding and background color to the window
    root.configure(bg="#f0f0f0")
    padding_frame = tk.Frame(root, bg="#f0f0f0")
    padding_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Welcome message label
    welcome_label = tk.Label(padding_frame, text="Welcome to the Update Checker!", font=("Arial", 14, "bold"), bg="#f0f0f0")
    welcome_label.pack(pady=10)

    # Check for Updates button
    update_button = tk.Button(padding_frame, text="Check for Updates", command=check_for_updates, bg="#4CAF50", fg="white", font=("Arial", 12))
    update_button.pack(pady=10)

    # Example usage of functions from module1 and module2
    from module1 import function1
    from module2 import function2

    # Labels for module functions
    module1_label = tk.Label(padding_frame, text=function1(), font=("Arial", 12), bg="#f0f0f0")
    module1_label.pack(pady=5)

    module2_label = tk.Label(padding_frame, text=function2(), font=("Arial", 12), bg="#f0f0f0")
    module2_label.pack(pady=5)

    # Version label
    version_label = tk.Label(padding_frame, text="Version: ", font=("Arial", 12), bg="#f0f0f0")
    version_label.pack(pady=5)

    # Update version label
    try:
        with open("version.txt", "r") as f:
            current_version = f.read().strip()
        version_label.config(text=f"Version: {current_version}")
    except FileNotFoundError:
        version_label.config(text="Version: Not available")

    root.mainloop()

if __name__ == "__main__":
    create_ui()
