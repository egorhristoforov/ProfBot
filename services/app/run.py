import os
from server import app

if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG', False), port=5001)
