import customtkinter as ctk
import matplotlib.pyplot as plt
import time

# Setup appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class KeyPressApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Keypress Logger")
        self.geometry("400x200")
        self.time_data = []

        self.label = ctk.CTkLabel(self, text="Press any key... (Esc to plot)", font=("Arial", 16))
        self.label.pack(pady=60)

        self.bind_all("<KeyPress>", self.on_key_press)
        self.bind_all("<KeyRelease>", self.on_key_release)

    def on_key_press(self, event):
        timestamp = time.time()

        # Prevent Esc from recording before plot
        if event.keysym == "Escape":
            self.plot_time_data()
            return

        self.time_data.append((timestamp, 1))
        print(f"[PRESS] Key: {event.keysym} at {timestamp}")

    def on_key_release(self, event):
        timestamp = time.time()
        self.time_data.append((timestamp, -1))
        print(f"[RELEASE] Key: {event.keysym} at {timestamp}")

    def plot_time_data(self):
        if not self.time_data:
            print("No key events recorded.")
            return

        # Normalize time to start from zero
        t0 = self.time_data[0][0]
        times = [t - t0 for t, _ in self.time_data]
        states = [s for _, s in self.time_data]

        plt.figure(figsize=(8, 4))
        plt.step(times, states, where='post', marker='o')
        plt.title("Key Press (+1) / Release (-1) Timeline")
        plt.xlabel("Time since first event (s)")
        plt.ylabel("State")
        plt.yticks([-1, 1], labels=["Released", "Pressed"])
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = KeyPressApp()
    app.mainloop()
