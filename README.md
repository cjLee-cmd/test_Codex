# test_Codex

## HTML Viewer

This repository contains `html_viewer.py`, a simple PyQt5 application that
allows you to sequentially browse HTML files located in the same directory.

### Features

- Displays `.html` files using an embedded browser (`QWebEngineView`).
- Navigation buttons and arrow keys (left/right) to switch between files.
- Horizontal scroll gestures also move to the next/previous file.
- `F11` toggles full-screen mode.
- `Esc` closes the viewer.

### Usage

1. Install dependencies (PyQt5 and PyQtWebEngine):

   ```bash
   pip install PyQt5==5.15.7 PyQtWebEngine==5.15.7
   ```

2. Place `html_viewer.py` in the folder containing your HTML files and run:

   ```bash
   python3 html_viewer.py
   ```

The application will start in full-screen mode, showing the first HTML file.
Use the buttons, arrow keys, or a horizontal scroll gesture to navigate through the files.
