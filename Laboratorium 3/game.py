import random
from typing import Tuple, List, Set, Optional

class Board:
    def __init__(self, width: int = 5, height: int = 5):
        if width < 5 or height < 5:
            raise ValueError("Plansza musi mieć wymiary minimum 5x5")
        
        self.width = width
        self.height = height
        self.start: Optional[Tuple[int, int]] = None
        self.stop: Optional[Tuple[int, int]] = None
        self.obstacles: Set[Tuple[int, int]] = set()
        self.current_position: Optional[Tuple[int, int]] = None
        
        self.generate_board()

    def generate_board(self, obstacle_count: int = 5):
        """Generuje start, stop i przeszkody."""
        edges = set()
        for x in range(self.width):
            edges.add((x, 0))              
            edges.add((x, self.height - 1)) 
        for y in range(self.height):
            edges.add((0, y))              
            edges.add((self.width - 1, y)) 

        edges_list = list(edges)
        
        while True:
            self.start = random.choice(edges_list)
            self.stop = random.choice(edges_list)
            
            if self.start == self.stop:
                continue
                
            dist = abs(self.start[0] - self.stop[0]) + abs(self.start[1] - self.stop[1])
            if dist > 1:
                break
        
        self.current_position = self.start

        all_positions = set((x, y) for x in range(self.width) for y in range(self.height))
        available_for_obstacles = list(all_positions - {self.start, self.stop})
        
        count = min(obstacle_count, len(available_for_obstacles))
        self.obstacles = set(random.sample(available_for_obstacles, count))

    def validate_move(self, new_x: int, new_y: int) -> tuple[bool, str]:
        """Sprawdza, czy ruch na podane pole jest legalny."""
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            return False, "Out of bounds"
        
        if (new_x, new_y) in self.obstacles:
            return False, "Obstacle hit"
            
        return True, "OK"

    def move(self, direction: str) -> str:
        """Wykonuje ruch: UP, DOWN, LEFT, RIGHT."""
        if not self.current_position:
            return "Game not initialized"

        x, y = self.current_position
        new_x, new_y = x, y

        direction = direction.upper()
        if direction == "UP":
            new_y -= 1
        elif direction == "DOWN":
            new_y += 1
        elif direction == "LEFT":
            new_x -= 1
        elif direction == "RIGHT":
            new_x += 1
        else:
            return "Invalid direction"

        is_valid, message = self.validate_move(new_x, new_y)

        if is_valid:
            self.current_position = (new_x, new_y)
            if self.current_position == self.stop:
                return "STOP REACHED"
            return "MOVED"
        else:
            return f"ERROR: {message}"

    def display(self):
        """Wyświetla planszę w terminalu."""
        print(f"Start: {self.start}, Stop: {self.stop}, Current: {self.current_position}")
        output = ""
        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                pos = (x, y)
                if pos == self.current_position:
                    row_str += "[O]" 
                elif pos == self.start:
                    row_str += " A "
                elif pos == self.stop:
                    row_str += " B "
                elif pos in self.obstacles:
                    row_str += " X "
                else:
                    row_str += " . "
            output += row_str + "\n"
        print(output)
        return output

# przykład użycia metod
if __name__ == "__main__":
    game = Board(6, 6)
    game.display()
    print(game.move("RIGHT"))
    game.display()