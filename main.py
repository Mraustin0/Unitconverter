import sys
from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Unit Converter")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("yoyo")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()