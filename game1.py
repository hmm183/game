import tkinter as tk
import random
from PIL import Image, ImageTk

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
ASTEROID_SIZE = 40
SPAWN_RATE = 1000  # milliseconds

# Asteroid class
class Asteroid:
    def __init__(self, canvas, image):
        self.image = ImageTk.PhotoImage(Image.open("asteroid3.png"))
        self.canvas = canvas
        self.x = random.randint(0, WINDOW_WIDTH - ASTEROID_SIZE)
        self.y = random.randint(0, WINDOW_HEIGHT - ASTEROID_SIZE)
        self.id = self.canvas.create_image(self.x, self.y, image=self.image)

# Main game class
class AsteroidDestroyerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Asteroid Destroyer Game")

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
        self.canvas.pack()

        self.score = 0
        self.score_label = self.canvas.create_text(20, 20, text=f"Score: {self.score}", fill="white")

        self.asteroids = []
        self.image = ImageTk.PhotoImage(Image.open("asteroid3.png"))
        
        self.create_asteroid()
        self.canvas.bind('<Button-1>', self.on_click)

        self.game_loop()

    def create_asteroid(self):
        if len(self.asteroids) < 10:
            asteroid = Asteroid(self.canvas, self.image)
            self.asteroids.append(asteroid)

    def on_click(self, event):
        # Check if the click hits any asteroid
        asteroid_id = self.canvas.find_closest(event.x, event.y)[0]
        for asteroid in self.asteroids:
            if asteroid.id == asteroid_id:
                # Check if the click is on top of the asteroid
                if self.canvas.coords(asteroid.id)[0] <= event.x <= self.canvas.coords(asteroid.id)[0] + ASTEROID_SIZE and \
                    self.canvas.coords(asteroid.id)[1] <= event.y <= self.canvas.coords(asteroid.id)[1] + ASTEROID_SIZE:
                    self.canvas.delete(asteroid.id)
                    self.asteroids.remove(asteroid)
                    self.score += 1
                    self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")
                    break

    def game_loop(self):
        # End the game if there are more than 10 asteroids on the screen
        if len(self.asteroids) >= 10:
            self.canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, text="Game Over", fill="white", font=("Helvetica", 30))
            self.canvas.unbind('<Button-1>')

        # Increase the spawn rate over time
        spawn_rate = SPAWN_RATE - self.score * 10
        if spawn_rate < 0:
            spawn_rate = 0

        # Schedule the next call to game_loop after 1000 milliseconds (1 second)
        self.root.after(spawn_rate, self.game_loop)

        # Create a new asteroid
        self.create_asteroid()

# Main function to start the game
def main():
    root = tk.Tk()
    game = AsteroidDestroyerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
