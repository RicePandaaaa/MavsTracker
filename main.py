import stat_grabber as sg
import news_grabber as ng
import sys
import time

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QScrollArea, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the main window
        super(MainWindow, self).__init__()
        uic.loadUi("mainWindow.ui", self)
        self.setWindowTitle("Mavericks Stat Tracker")
        self.setFixedSize(self.size())

        # Information used by other functions and helper modules
        self.team_name = "Dallas Mavericks"
        self.last_news_update = 0

        # Initialize the layout for scrollAreaWidgetContents
        self.scroll_area_widget_contents = self.findChild(QWidget, "scrollAreaWidgetContents")
        layout = QVBoxLayout(self.scroll_area_widget_contents)
        layout.addWidget(self.news_label)
        self.scroll_area_widget_contents.setLayout(layout)

        # Initialize buttons and labels
        self.update_news_frame()
        
    def update_news_frame(self):
        # Only update if an hour has passed since last update
        if time.time() - self.last_news_update < 3600:
            return
        
        # Get team news
        team_news = ng.get_latest_news(self.team_name)
        
        # Format the news label
        new_string = ""

        for article in team_news:
            news_title = f'<b><a style="font-size:14pt; color:#ADD8E6;" href="{article["link"]}">{article["title"]}</a></b>'
            news_summary = f'<span style="font-size:13pt;">{article["summary"]}</span>'
            new_string += f"{news_title}<br>{news_summary}<br><br>"

        self.news_label.setText(new_string.strip())
        self.news_label.adjustSize()

        # Update time of last news update
        self.last_news_update = time.time()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the global stylesheet for all QPushButton widgets
    app.setStyleSheet("""
        QWidget {
            background-color: #3E5F7E;
            color: #D3DBDF;
        }
                      
        QPushButton {
            background-color: #002B5E;
            color: #FFFFFF;
            border: 2px solid #7B8A94;
        }
                      
        QPushButton:hover {
            background-color: #9BB6C4;
        }
                      
        QLabel {
            color: #D3DBDF;
        }
    """)


    window = MainWindow()
    window.show()
    sys.exit(app.exec())
