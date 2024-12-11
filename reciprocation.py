import random
import logging
import tkinter as tk
from tkinter import messagebox

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class ReciprocalGiftRandomizer:
    def __init__(self, names):
        if len(names) % 2 != 0:
            raise ValueError("An even number of names is required for reciprocal matching.")
        self.names = names

    def generate_reciprocal_pairs(self):
        # Shuffle names for randomness
        shuffled_names = self.names[:]
        random.shuffle(shuffled_names)

        # Pair names reciprocally
        pairs = [(shuffled_names[i], shuffled_names[i + 1]) for i in range(0, len(shuffled_names), 2)]

        # Log the pairs
        self.log_pairs(pairs)

        return pairs

    @staticmethod
    def log_pairs(pairs):
        logging.info("Reciprocal Gift Pairs:")
        for giver, receiver in pairs:
            logging.info(f"{giver} will give a gift to {receiver}, and {receiver} will give a gift to {giver}")

    @staticmethod
    def display_pairs(pairs):
        # Create a simple Tkinter pop-up dialog
        pair_strings = "\n".join(
            [f"{giver} will give a gift to {receiver}, and {receiver} will give a gift to {giver}" for giver, receiver
             in pairs])
        messagebox.showinfo("Reciprocal Gift Pairs", pair_strings)

    def create_gui(self):
        # Create the main Tkinter window
        root = tk.Tk()
        root.title("Reciprocal Gift Randomizer")
        root.geometry("400x200")

        # Label for instruction
        instruction_label = tk.Label(root, text="Click the button to generate reciprocal gift pairs.", font=("Arial", 12))
        instruction_label.pack(pady=20)

        # Button to randomize and show the gift pairs
        def randomize_and_show():
            pairs = self.generate_reciprocal_pairs()
            self.display_pairs(pairs)

        randomize_button = tk.Button(root, text="Randomize", command=randomize_and_show, font=("Arial", 14))
        randomize_button.pack(pady=10)

        # Start the Tkinter event loop
        root.mainloop()


def main_reciprocal():
    # List of names
    names = ["John", "Nancy", "Wanjahi", "Njuguna", "Stephani", "Jamila"]

    # Create an instance of ReciprocalGiftRandomizer
    reciprocal_randomizer = ReciprocalGiftRandomizer(names)

    # Create and run the GUI
    reciprocal_randomizer.create_gui()


if __name__ == "__main__":
    main_reciprocal()
