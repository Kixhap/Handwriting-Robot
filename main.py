import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk  # Import ttk for themed widgets

from Translate import svg_to_gcode
from handwriting_synthesis import Hand
from Request import get_openai_response
from Translate import start

def handler():
    response = get_openai_response(lines_entry.get("1.0", tk.END))
    generate_handwriting(response)

def translate():
    start()

# Function to format into 60 char per line
def format_lines(text):
    formatted_lines = []
    words = text.split()

    current_line = ""
    for word in words:
        # Check length
        if len(current_line) + len(word) + 1 > 50:
            if current_line:
                formatted_lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " "
            current_line += word

    # Append any remaining line
    if current_line:
        formatted_lines.append(current_line)

    return formatted_lines


# Function to generate handwriting based on user input
def generate_handwriting(response):
    try:
        # Get user input from the multi-line text box
        user_input = response.strip()

        # Format the lines to ensure a max of 65 characters each
        formatted_lines = format_lines(user_input)

        # This step ensures we're only passing formatted lines to handwriting
        lines = [line.strip() for line in formatted_lines if line.strip()]  # Remove any empty lines

        # Get styles input and ensure valid style input
        styles_input = styles_entry.get()
        styles = [styles_input for _ in lines]

        # Set default values for stroke widths and colors
        stroke_widths = [1 for _ in lines]
        stroke_colors = ['black' for _ in lines]
        biases = [.7 for _ in lines]

        # Create handwriting object
        hand = Hand()

        # Write the image with user-specified parameters
        hand.write(
            filename='img/output.svg',
            lines=lines,
            biases=biases,
            styles=styles,
            stroke_colors=stroke_colors,
            stroke_widths=stroke_widths
        )

        # Show success message
        messagebox.showinfo("Success", "Handwriting image generated successfully!")

    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"An error occurred: {e}")  # Simplified error handling


# Create the main application window
root = tk.Tk()
root.title("Handwriting Robot")

# Set the size of the main window
root.geometry("960x500")

# Create a style object
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TScrolledText", font=("Helvetica", 12))

# Create labels and a multi-line text box for inputting lines
ttk.Label(root, text="Ask away:").pack(pady=10)
lines_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=5)  # Multi-line text box for lines
lines_entry.pack(pady=10)

# Create labels and entry fields for user inputs
ttk.Label(root, text="Enter Style (one number 1-9):").pack(pady=10)
styles_entry = ttk.Entry(root, width=100)
styles_entry.pack(pady=5)

# Create a button to trigger the handwriting generation
generate_button = ttk.Button(root, text="Generate Handwriting", command=handler)
generate_button.pack(pady=20)

generate_button = ttk.Button(root, text="Translate svg to gcode", command=translate)
generate_button.pack(pady=20)

# Run the application
root.mainloop()
