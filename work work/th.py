import thinker as tk
# Handling button click event

def button_click():
    #print("Button Clicked")

    # Show an information message box
    msgbox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

    # Ask for user Confirmation
    result = msgbox.askyesno("Confirmation", "Do you want to continue?")

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

# Add a label widget
label = tk.label(root, text="Hello Friend \n")
label.pack()

# Add a button widget
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

# Styling the button widget
button.config(fg="red", bg="yellow")

# Start the event log
root.mainloop()

