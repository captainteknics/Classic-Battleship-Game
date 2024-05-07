class BattleshipGame:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.player_grid = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ship_sizes = [5, 4, 3, 3, 2]  # Example ship sizes

    def print_grid(self, grid):
        """Prints the given grid"""
        for row in grid:
            print(' '.join(row))
        print()

    def place_ships_randomly(self, grid):
        """Randomly places ships on the given grid"""
        import random
        for ship_size in self.ship_sizes:
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    row = random.randint(0, self.grid_size - 1)
                    col = random.randint(0, self.grid_size - ship_size)
                else:
                    row = random.randint(0, self.grid_size - ship_size)
                    col = random.randint(0, self.grid_size - 1)

                if self.check_free_space(grid, row, col, ship_size, orientation):
                    self.place_ship(grid, row, col, ship_size, orientation)
                    placed = True

    def check_free_space(self, grid, row, col, ship_size, orientation):
        """Checks if there is free space to place a ship"""
        if orientation == 'H':
            return all(grid[row][col+i] == '-' for i in range(ship_size))
        else:
            return all(grid[row+i][col] == '-' for i in range(ship_size))

    def place_ship(self, grid, row, col, ship_size, orientation):
        """Places a ship on the given grid"""
        if orientation == 'H':
            for i in range(ship_size):
                grid[row][col+i] = 'S'
        else:
            for i in range(ship_size):
                grid[row+i][col] = 'S'

    def start_game(self):
        """Starts the game"""
        print("Welcome to Battleship!")
        self.place_ships_randomly(self.computer_grid)
        # For simplicity, we'll also randomly place player's ships
        self.place_ships_randomly(self.player_grid)

        # Print player's grid
        print("Your grid:")
        self.print_grid(self.player_grid)

        # Game loop would go here, but for now, we just end the game
        print("Game setup complete. Prototype ready for gameplay implementation.")

# Create and start the game
game = BattleshipGame()
game.start_game()
