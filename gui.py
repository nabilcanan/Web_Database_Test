import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# This will start the Flask server
import threading
from app import app


def start_flask_app():
    app.run(port=5000)


if __name__ == '__main__':
    # Start Flask in a background thread
    threading.Thread(target=start_flask_app).start()

    # Create a PyQt application
    app_qt = QApplication(sys.argv)

    web = QWebEngineView()
    web.load(QUrl("http://127.0.0.1:5000/"))
    web.show()

    sys.exit(app_qt.exec_())
