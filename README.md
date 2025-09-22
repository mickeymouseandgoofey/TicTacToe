🕹️ Tic Tac Go — Flask Edition

A simple web-based Tic Tac Toe game built with Python and Flask. Two players take turns placing Xs and Os on a 3×3 grid until one wins or the game ends in a draw.
📁 Project Structure
tic-tac-go/
├── app.py               # Main Flask app
├── static/
│   └── styles.css       # CSS styling for the game
├── templates/
│   ├── game.html        # Main game interface
│   └── index.html       # Optional landing page
└── README.md            # Setup instructions (this file)


🚀 Getting Started
1. Clone the repository
   git clone https://github.com/your-username/tic-tac-go.git
   cd tic-tac-go

2. Set up a virtual environment (recommended)
   python -m venv venv
   venv\Scripts\activate  # On Windows

3. Install Flask
   pip install flask

4. Run the app
   python app.py

5. http://localhost:5000

🧠 How It Works

  The board is a 3×3 grid rendered in HTML.

  Players take turns clicking empty cells to submit moves.

  Flask handles game logic, win/draw detection, and board updates.

  No JavaScript required — everything is server-rendered.

🎨 Styling

The game uses static/styles.css for a clean, centered layout with hover effects and winner announcements.
🧪 Debugging Tips

  Console prints show board state and move details.

  Invalid moves (e.g., clicking an occupied cell) are ignored.

  Errors in form submission return a 400 response.

📦 Deployment Notes

If you're hosting with IIS on Windows:

  Place files in C:\inetpub\wwwroot

  Use a WSGI handler like wfastcgi or reverse proxy to localhost:5000

  Ensure Python and Flask are installed on the host machine

🙌 Contributing

Ideas welcome:

  Add player names or score tracking

  Add AI opponent (Minimax or random)

  Style enhancements or animations

📄 License

MIT — free to use, modify, and share.
