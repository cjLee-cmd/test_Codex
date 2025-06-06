import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt, QEvent

class HtmlBrowser(QMainWindow):
    def __init__(self, html_files):
        super().__init__()
        self.html_files = html_files
        self.index = 0

        self.view = QWebEngineView()
        self.setCentralWidget(self.view)
        self.view.installEventFilter(self)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        prev_action = QAction('Prev', self)
        prev_action.triggered.connect(self.prev_page)
        toolbar.addAction(prev_action)
        next_action = QAction('Next', self)
        next_action.triggered.connect(self.next_page)
        toolbar.addAction(next_action)

        self.load_page()
        self.showFullScreen()

    def load_page(self):
        if not self.html_files:
            return
        file_url = QUrl.fromLocalFile(self.html_files[self.index])
        self.view.load(file_url)
        self.setWindowTitle(os.path.basename(self.html_files[self.index]))

    def next_page(self):
        if not self.html_files:
            return
        self.index = (self.index + 1) % len(self.html_files)
        self.load_page()

    def prev_page(self):
        if not self.html_files:
            return
        self.index = (self.index - 1) % len(self.html_files)
        self.load_page()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.next_page()
        elif event.key() == Qt.Key_Left:
            self.prev_page()
        elif event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        elif event.key() == Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

    def eventFilter(self, source, event):
        if source is self.view and event.type() == QEvent.Wheel:
            delta = event.angleDelta().x()
            if delta < 0:
                self.next_page()
                return True
            elif delta > 0:
                self.prev_page()
                return True
        return super().eventFilter(source, event)


def main():
    app = QApplication(sys.argv)
    html_files = sorted(
        os.path.abspath(f)
        for f in os.listdir('.')
        if f.lower().endswith('.html')
    )
    browser = HtmlBrowser(html_files)
    browser.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
