# How to Run the Slot Machine Game

Follow these instructions to set up and run the Slot Machine Game on your local machine.

## Prerequisites

- Python 3.7 or higher
- Git (optional, for cloning the repository)

## Setup and Running

### For Unix-based Systems (macOS, Linux)

1. Open a terminal.

2. Navigate to the project directory:
   ```
   cd path/to/slot-machine-game
   ```

3. Run the setup script:
   ```
   ./run_game.sh
   ```

4. Open `http://127.0.0.1:5000/` in your web browser.

### For Windows

1. Open Command Prompt or PowerShell.

2. Navigate to the project directory:
   ```
   cd path\to\slot-machine-game
   ```

3. Run the setup script:
   ```
   run_game.bat
   ```

4. Open `http://127.0.0.1:5000/` in your web browser.

### Using Docker

1. Ensure Docker is installed and running on your system.

2. Open a terminal or command prompt and navigate to the project directory:
   ```
   cd path\to\slot-machine-game
   ```

3. Build the Docker image:
   ```
   docker build -t slot-machine-game .
   ```

4. Run the Docker container:
    ```
    docker run -p 5000:5000 slot-machine-game
    ```

4. Open `http://127.0.0.1:5000/` in your web browser.




## Playing the Game

1. Enter a username and click "Start Game".
2. Click "Roll" to spin the slots.
3. Match symbols to win credits.
4. Click "Cash Out" to end the game (be careful, the button might move!).

## Troubleshooting

- If you encounter a "Permission denied" error when running the .sh file on Unix-based systems, make it executable with:
  ```
  chmod +x run_game.sh
  ```

- Ensure your backend is running on `http://localhost:5000`. If it's running on a different port, update the `API_URL` in `index.html`.

- If you see CORS errors, make sure your backend is running and CORS is properly configured.

Enjoy the game!