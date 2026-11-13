import tkinter as tk
from datetime import datetime

class WorkshopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workshop Participant Greeting")
        self.root.geometry("450x400")
        self.root.config(padx=20, pady=20)

        # 1. Title / Instruction Label
        self.title_label = tk.Label(
            root, 
            text="Workshop Participant Greeting", 
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=(0, 5))

        self.subtitle_label = tk.Label(
            root, 
            text="Please enter your name below and click Check In.", 
            font=("Arial", 10), 
            fg="gray"
        )
        self.subtitle_label.pack(pady=(0, 15))

        # 2. Input Frame for Name Entry
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill="x", pady=5)

        self.name_label = tk.Label(self.input_frame, text="Participant Name:", font=("Arial", 11))
        self.name_label.pack(side="left", padx=(0, 10))

        self.name_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=20)
        self.name_entry.pack(side="left", expand=True, fill="x")

        # 3. Check In Button
        self.checkin_button = tk.Button(
            root, 
            text="Check In", 
            font=("Arial", 11, "bold"), 
            bg="#4CAF50", 
            fg="white", 
            padx=10, 
            pady=5, 
            command=self.handle_checkin
        )
        self.checkin_button.pack(pady=15)

        # 4. Multi-line Text Widget for Welcome Message & Date
        self.output_text = tk.Text(
            root, 
            height=6, 
            width=40, 
            font=("Arial", 11), 
            state="disabled", 
            bg="#f4f4f4"
        )
        self.output_text.pack(pady=5)

    def handle_checkin(self):
        # Read the typed name from the Entry widget
        participant_name = self.name_entry.get().strip()
        
        # Get current workshop date
        current_date = datetime.now().strftime("%B %d, %Y")

        # Enable text box temporarily to insert output
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)

        if participant_name:
            message = (
                f"Hello, {participant_name}!\n\n"
                f"Welcome to the workshop.\n"
                f"Workshop Date: {current_date}\n"
                f"Status: Checked In Successfully!"
            )
        else:
            message = (
                "Error: Please enter a valid name\n"
                "before clicking Check In."
            )

        self.output_text.insert(tk.END, message)
        # Disable text box again to make it read-only for the user
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkshopApp(root)
    root.mainloop()