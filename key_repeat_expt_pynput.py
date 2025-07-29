from pynput.keyboard import Listener, Key
import matplotlib.pyplot as plt
import time

class KeyPressApp:
    def __init__(self):

        self.time_data = []

        with Listener(on_press=self.on_key_press, on_release=self.on_key_release, suppress=True) as l:
            l.join()
        self.plot_time_data()

    def on_key_press(self, key):
        timestamp = time.time()

        # Prevent Esc from recording before plot
        if key == Key.esc:
            return False

        self.time_data.append((timestamp, 1))
        print(f"[PRESS] Key: {key.char} at {timestamp}")

    def on_key_release(self, key):
        timestamp = time.time()
        self.time_data.append((timestamp, -1))
        print(f"[RELEASE] Key: {key.char} at {timestamp}")

    def plot_time_data(self):
        if not self.time_data:
            print("No key events recorded.")
            return

        # Normalize time to start from zero
        t0 = self.time_data[0][0]
        times = [t - t0 for t, _ in self.time_data]
        states = [s for _, s in self.time_data]

        plt.figure(figsize=(8, 2))
        plt.step(times, states, where='post', marker='o')
        plt.title("MacOS pynput")
        plt.xlabel("Time since first event (s)")
        plt.ylabel("State")
        plt.ylim((-2, 2))
        plt.yticks([-1, 1], labels=["Released", "Pressed"])
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = KeyPressApp()
