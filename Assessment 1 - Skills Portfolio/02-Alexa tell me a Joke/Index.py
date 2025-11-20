import tkinter as tk
from tkinter import font
import random
from pathlib import Path

# Main class for the Alexa Joke Teller application
class AlexaJokeApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Alexa Joke Teller")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load all jokes from the text file
        self.jokes = self.load_jokes()
        
        # Variables to store current joke details
        self.current_joke = None
        self.setup_text = ""
        self.punchline_text = ""
        
        # Create the user interface
        self.setup_ui()
        
    def load_jokes(self):
        """Load jokes from the randomJokes.txt file"""
        jokes = []
        try:
            # Import os module to work with file paths
            import os
            
            # Get the folder where this script is running from
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Build the path to randomJokes.txt in the same folder
            jokes_path = os.path.join(script_dir, "randomJokes.txt")
            
            # Print debug info to help with troubleshooting
            print(f"Looking for jokes file at: {jokes_path}")
            print(f"File exists: {os.path.exists(jokes_path)}")
            
            # Open and read the jokes file
            with open(jokes_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
            
            # Split the file into individual lines (each line is one joke)
            lines = file_content.strip().split('\n')
            
            # Parse each joke - setup and punchline are separated by '?'
            for line in lines:
                if '?' in line:
                    parts = line.split('?', 1)  # Split only at first '?'
                    setup = parts[0].strip() + '?'  # The question part
                    punchline = parts[1].strip()  # The answer part
                    jokes.append((setup, punchline))  # Add to jokes list
            
            print(f"Successfully loaded {len(jokes)} jokes!")
                    
        except Exception as e:
            # If file not found or error occurs, use backup jokes
            print(f"Error loading jokes: {e}")
            jokes = [
                ("Why did the chicken cross the road?", "To get to the other side."),
                ("What happens if you boil a clown?", "You get a laughing stock."),
                ("Why did the car get a flat tire?", "Because there was a fork in the road!")
            ]
        
        return jokes
    
    def setup_ui(self):
        """Set up all the visual elements of the GUI"""
        
        # Try to load and display the background image
        try:
            from PIL import Image, ImageTk
            import os
            
            # Get the current script directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            bg_path = os.path.join(script_dir, "bgimage.png")
            
            print(f"Looking for background image at: {bg_path}")
            print(f"File exists: {os.path.exists(bg_path)}")
            
            # If background image exists, load and resize it
            if os.path.exists(bg_path):
                bg_image = Image.open(bg_path)
                bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(bg_image)
                
                # Create label to hold the background image
                bg_label = tk.Label(self.root, image=self.bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                print("Background image loaded successfully!")
            else:
                # If no image found, use solid dark blue background
                print("Background image not found, using solid color")
                self.root.configure(bg='#1a1a2e')
                
        except ImportError as e:
            # If Pillow library not installed, use solid color
            print(f"PIL/Pillow not installed: {e}")
            print("Install with: pip install Pillow")
            self.root.configure(bg='#1a1a2e')
        except Exception as e:
            print(f"Error loading background: {e}")
            self.root.configure(bg='#1a1a2e')
        
        # Create custom fonts for different text elements
        title_font = font.Font(family="Arial", size=24, weight="bold")
        joke_font = font.Font(family="Arial", size=14)
        button_font = font.Font(family="Arial", size=11, weight="bold")
        
        # Main container frame - holds all elements with dark background
        main_frame = tk.Frame(self.root, bg='#0f0f1e', bd=2, relief=tk.RAISED)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=700, height=500)
        
        # Title at the top of the window
        title_label = tk.Label(
            main_frame, 
            text="🎤 Alexa Joke Teller", 
            font=title_font,
            bg='#0f0f1e',
            fg='#6c63ff',
            pady=20
        )
        title_label.pack()
        
        # Frame to display the jokes
        joke_frame = tk.Frame(main_frame, bg='#1a1a2e', bd=2, relief=tk.SUNKEN)
        joke_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        # Label to show the joke setup (question)
        self.setup_label = tk.Label(
            joke_frame,
            text="Click 'Alexa tell me a Joke' to start!",
            font=joke_font,
            bg='#1a1a2e',
            fg='#ffffff',
            wraplength=600,
            justify=tk.CENTER,
            pady=20
        )
        self.setup_label.pack(pady=(30, 10))
        
        # Label to show the punchline (answer)
        self.punchline_label = tk.Label(
            joke_frame,
            text="",
            font=joke_font,
            bg='#1a1a2e',
            fg='#00ff88',
            wraplength=600,
            justify=tk.CENTER,
            pady=10
        )
        self.punchline_label.pack(pady=(10, 30))
        
        # Frame to hold all the buttons
        button_frame = tk.Frame(main_frame, bg='#0f0f1e')
        button_frame.pack(pady=20)
        
        # Common settings for all buttons
        button_config = {
            'font': button_font,
            'width': 20,  # Made wider to fit text better
            'height': 2,
            'bd': 0,
            'relief': tk.FLAT,
            'cursor': 'hand2'
        }
        
        # Button 1: Tell me a joke - displays random joke setup
        self.joke_button = tk.Button(
            button_frame,
            text="🎙️ Alexa tell me a Joke",
            command=self.tell_joke,
            bg='#6c63ff',
            fg='white',
            activebackground='#5848cc',
            activeforeground='white',
            **button_config
        )
        self.joke_button.grid(row=0, column=0, padx=5, pady=5)
        
        # Button 2: Show punchline - reveals the answer to the joke
        self.punchline_button = tk.Button(
            button_frame,
            text="😄 Show Punchline",
            command=self.show_punchline,
            bg='#00d4ff',
            fg='white',
            activebackground='#00a8cc',
            activeforeground='white',
            state=tk.DISABLED,  # Disabled until a joke is shown
            **button_config
        )
        self.punchline_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Button 3: Next joke - resets to get another joke
        self.next_button = tk.Button(
            button_frame,
            text="➡️ Next Joke",
            command=self.next_joke,
            bg='#ff6b9d',
            fg='white',
            activebackground='#cc4d73',
            activeforeground='white',
            state=tk.DISABLED,  # Disabled until punchline is shown
            **button_config
        )
        self.next_button.grid(row=1, column=0, padx=5, pady=5)
        
        # Button 4: Quit - closes the application
        self.quit_button = tk.Button(
            button_frame,
            text="❌ Quit",
            command=self.root.quit,
            bg='#ff4757',
            fg='white',
            activebackground='#cc3644',
            activeforeground='white',
            **button_config
        )
        self.quit_button.grid(row=1, column=1, padx=5, pady=5)
        
    def tell_joke(self):
        """Display a random joke setup when button is clicked"""
        
        # Check if jokes list is empty
        if not self.jokes:
            self.setup_label.config(text="No jokes available!")
            return
        
        # Pick a random joke from the list
        self.current_joke = random.choice(self.jokes)
        self.setup_text = self.current_joke[0]  # The setup (question)
        self.punchline_text = self.current_joke[1]  # The punchline (answer)
        
        # Display the setup in the label
        self.setup_label.config(text=self.setup_text)
        self.punchline_label.config(text="")  # Clear punchline
        
        # Update button states
        self.punchline_button.config(state=tk.NORMAL)  # Enable show punchline
        self.joke_button.config(state=tk.DISABLED)  # Disable tell joke
        self.next_button.config(state=tk.DISABLED)  # Disable next joke
        
    def show_punchline(self):
        """Display the punchline when button is clicked"""
        
        # Show the answer to the joke
        self.punchline_label.config(text=self.punchline_text)
        
        # Update button states
        self.punchline_button.config(state=tk.DISABLED)  # Disable punchline
        self.next_button.config(state=tk.NORMAL)  # Enable next joke
        
    def next_joke(self):
        """Reset the display to get ready for next joke"""
        
        # Clear the joke display
        self.setup_label.config(text="Ready for another joke!")
        self.punchline_label.config(text="")
        
        # Reset button states
        self.joke_button.config(state=tk.NORMAL)  # Enable tell joke
        self.punchline_button.config(state=tk.DISABLED)  # Disable punchline
        self.next_button.config(state=tk.DISABLED)  # Disable next joke

# Main function to run the program
def main():
    root = tk.Tk()  # Create main window
    app = AlexaJokeApp(root)  # Create application instance
    root.mainloop()  # Start the GUI event loop

# Run the program when script is executed
if __name__ == "__main__":
    main()