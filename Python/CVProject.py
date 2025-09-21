# Reid Sanders
# Display OpenCV Version using Tkinter
# 09/21/2025

# WORK IN PROGRESS

import cv2
import tkinter as tk

# Create the Tkinter root window
root = tk.Tk()
root.title("OpenCV Version Display")
root.geometry("300x100")

# Get OpenCV version
opencv_version = cv2.__version__

# Create a label and display the version
label = tk.Label(root, text=f"OpenCV Version: {opencv_version}", font=("Arial", 14))
label.pack(expand=True, padx=20, pady=20)


# Run the Tkinter main loop
root.mainloop()
