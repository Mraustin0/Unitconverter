from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QTabWidget, QLabel, QLineEdit, QComboBox, 
                            QPushButton, QFrame, QListWidget, QMessageBox, QApplication)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QFont, QPalette, QLinearGradient, QBrush, QColor
from src.core.converter import convert_length, convert_weight, convert_temperature
from src.gui.styles import MAIN_STYLE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("เครื่องแปลงหน่วย")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet(MAIN_STYLE)
        
        # History storage
        self.conversion_history = []
        
        self.setup_ui()
        self.connect_signals()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        self.create_header(layout)
        
        # Tabs
        self.create_tabs(layout)
        
        # Input section
        self.create_input_section(layout)
        
        # Error message (เพิ่มใหม่)
        self.create_error_section(layout)
        
        # Result section
        self.create_result_section(layout)
        
        # History section
        self.create_history_section(layout)
        
    def create_header(self, layout):
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout(header_frame)
        
        title = QLabel("เครื่องแปลงหน่วย")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        header_layout.addWidget(title)
        layout.addWidget(header_frame)
        
    def create_tabs(self, layout):
        self.tabs = QTabWidget()
        self.tabs.setObjectName("mainTabs")
        
        # Length tab
        length_tab = QWidget()
        self.tabs.addTab(length_tab, "ความยาว")
        
        # Weight tab  
        weight_tab = QWidget()
        self.tabs.addTab(weight_tab, "น้ำหนัก")
        
        # Temperature tab
        temp_tab = QWidget()
        self.tabs.addTab(temp_tab, "อุณหภูมิ")
        
        self.tabs.currentChanged.connect(self.on_tab_changed)
        layout.addWidget(self.tabs)
        
    def create_input_section(self, layout):
        input_frame = QFrame()
        input_frame.setObjectName("inputFrame")
        input_layout = QVBoxLayout(input_frame)
        
        # Value input
        value_layout = QHBoxLayout()
        value_label = QLabel("ค่าเดิม:")
        value_label.setObjectName("fieldLabel")
        
        self.value_input = QLineEdit()
        self.value_input.setObjectName("valueInput")
        self.value_input.setPlaceholderText("กรุณาใส่ตัวเลข เช่น 100")
        
        self.from_unit = QComboBox()
        self.from_unit.setObjectName("unitCombo")
        
        value_layout.addWidget(value_label, 1)
        value_layout.addWidget(self.value_input, 2)
        value_layout.addWidget(self.from_unit, 2)
        
        # Target unit
        target_layout = QHBoxLayout()
        target_label = QLabel("หน่วยเป้าหมาย:")
        target_label.setObjectName("fieldLabel")
        
        self.to_unit = QComboBox()
        self.to_unit.setObjectName("unitCombo")
        
        target_layout.addWidget(target_label, 1)
        target_layout.addWidget(self.to_unit, 4)
        
        input_layout.addLayout(value_layout)
        input_layout.addLayout(target_layout)
        layout.addWidget(input_frame)
        
        # Initialize with length units
        self.update_unit_options("length")
        
    def create_error_section(self, layout):
        """สร้างส่วนแสดงข้อความ error"""
        self.error_label = QLabel()
        self.error_label.setObjectName("errorLabel")
        self.error_label.setStyleSheet("""
            #errorLabel {
                background: #fef2f2;
                border: 2px solid #fecaca;
                border-radius: 8px;
                color: #dc2626;
                padding: 10px 15px;
                font-size: 13px;
                font-weight: 500;
                margin: 5px 0;
            }
        """)
        self.error_label.setWordWrap(True)
        self.error_label.hide()  # เริ่มต้นซ่อนไว้
        layout.addWidget(self.error_label)
        
    def create_result_section(self, layout):
        self.result_frame = QFrame()
        self.result_frame.setObjectName("resultFrame")
        result_layout = QVBoxLayout(self.result_frame)
        
        self.result_from = QLabel("0")
        self.result_from.setObjectName("resultValue")
        self.result_from.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.result_from_unit = QLabel("[cm]")
        self.result_from_unit.setObjectName("resultUnit")
        self.result_from_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        equals_label = QLabel("=")
        equals_label.setObjectName("equalsLabel")
        equals_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.result_to = QLabel("0")
        self.result_to.setObjectName("resultValue")
        self.result_to.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.result_to_unit = QLabel("[m]")
        self.result_to_unit.setObjectName("resultUnit")
        self.result_to_unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ปุ่มปิดโปรแกรม (แก้ไขจากเดิม)
        self.close_btn = QPushButton("ปิดโปรแกรม")
        self.close_btn.setObjectName("copyButton")
        self.close_btn.clicked.connect(self.close_application)
        
        result_layout.addWidget(self.result_from)
        result_layout.addWidget(self.result_from_unit)
        result_layout.addWidget(equals_label)
        result_layout.addWidget(self.result_to)
        result_layout.addWidget(self.result_to_unit)
        result_layout.addWidget(self.close_btn)
        
        layout.addWidget(self.result_frame)
        
    def create_history_section(self, layout):
        history_frame = QFrame()
        history_frame.setObjectName("historyFrame")
        history_layout = QVBoxLayout(history_frame)
        
        history_label = QLabel("ประวัติการแปลง")
        history_label.setObjectName("historyLabel")
        
        self.history_list = QListWidget()
        self.history_list.setObjectName("historyList")
        self.history_list.setMaximumHeight(120)
        
        history_layout.addWidget(history_label)
        history_layout.addWidget(self.history_list)
        layout.addWidget(history_frame)
        
    def connect_signals(self):
        self.value_input.textChanged.connect(self.on_input_changed)
        self.from_unit.currentTextChanged.connect(self.on_input_changed)
        self.to_unit.currentTextChanged.connect(self.on_input_changed)
        
    def on_tab_changed(self, index):
        # รีเซ็ทสีและข้อความ error เมื่อเปลี่ยนแท็บ
        self.reset_input_style()
        self.clear_error_message()
        
        tab_types = ["length", "weight", "temperature"]
        if index < len(tab_types):
            self.update_unit_options(tab_types[index])
            self.convert_units()
            
    def reset_input_style(self):
        """รีเซ็ทสี input field ให้เป็นปกติ"""
        # กำหนด style ปกติโดยตรง
        self.value_input.setStyleSheet("""
            QLineEdit#valueInput {
                background: #ffffff;
                border: 2px solid #e5e7eb;
                border-radius: 10px;
                padding: 12px 16px;
                color: #374151;
                font-size: 16px;
            }
            QLineEdit#valueInput:focus {
                border-color: #3b82f6;
                outline: none;
            }
        """)
        
    def update_unit_options(self, conversion_type):
        self.from_unit.clear()
        self.to_unit.clear()
        
        if conversion_type == "length":
            units = [
                ("cm", "เซนติเมตร [cm]"),
                ("m", "เมตร [m]"), 
                ("km", "กิโลเมตร [km]"),
                ("inch", "นิ้ว [inch]"),
                ("foot", "ฟุต [foot]"),
                ("yard", "หลา [yard]"),
                ("mile", "ไมล์ [mile]")
            ]
        elif conversion_type == "weight":
            units = [
                ("g", "กรัม [g]"),
                ("kg", "กิโลกรัม [kg]"),
                ("lb", "ปอนด์ [lb]"),
                ("oz", "ออนซ์ [oz]")
            ]
        else:  # temperature
            units = [
                ("C", "เซลเซียส [°C]"),
                ("F", "ฟาเรนไฮต์ [°F]"),
                ("K", "เคลวิน [K]")
            ]
            
        for value, display in units:
            self.from_unit.addItem(display, value)
            self.to_unit.addItem(display, value)
            
        # Set different default selections
        if len(units) > 1:
            self.to_unit.setCurrentIndex(1)
            
    def on_input_changed(self):
        self.convert_units()
        
    def convert_units(self):
        """แปลงหน่วยพร้อม validation"""
        try:
            # ตรวจสอบ input string ก่อนแปลงเป็น float
            input_text = self.value_input.text().strip()
            if not input_text:
                return
                
            # ตรวจสอบ -0 สำหรับความยาวและน้ำหนัก
            current_tab = self.tabs.currentIndex()
            if current_tab in [0, 1] and input_text.startswith('-0'):  # Length หรือ Weight
                if current_tab == 0:
                    raise ValueError("ความยาวไม่สามารถเป็นค่าติดลบได้")
                else:
                    raise ValueError("น้ำหนักไม่สามารถเป็นค่าติดลบได้")
            
            value = float(input_text)
            from_unit = self.from_unit.currentData()
            to_unit = self.to_unit.currentData()
            
            if not from_unit or not to_unit:
                return
            
            # ล้างข้อความ error ก่อน
            self.clear_error_message()
            
            if current_tab == 0:  # Length
                conversions = convert_length(value, from_unit)
            elif current_tab == 1:  # Weight
                conversions = convert_weight(value, from_unit)
            else:  # Temperature
                conversions = convert_temperature(value, from_unit)
                
            result = conversions.get(to_unit, 0)
            
            # Update result display
            self.result_from.setText(f"{value:,.2f}".rstrip('0').rstrip('.'))
            self.result_from_unit.setText(f"[{from_unit}]")
            self.result_to.setText(f"{result:,.4f}".rstrip('0').rstrip('.'))
            self.result_to_unit.setText(f"[{to_unit}]")
            
            # เปลี่ยนสีกลับเป็นปกติ
            self.reset_input_style()
            
            # Add to history
            history_text = f"{value} {from_unit} → {result:.4f} {to_unit}"
            if history_text not in self.conversion_history:
                self.conversion_history.insert(0, history_text)
                if len(self.conversion_history) > 10:
                    self.conversion_history.pop()
                self.update_history_display()
                
        except ValueError as e:
            # แสดง error message
            self.show_error_message(str(e))
            self.result_from.setText("Error")
            self.result_to.setText("Error")
            
            # เปลี่ยนสี input field เป็นสีแดง
            self.value_input.setStyleSheet("""
                background: #ffffff;
                border: 2px solid #dc2626;
                border-radius: 10px;
                padding: 12px 16px;
                color: #dc2626;
                font-size: 16px;
            """)
        except Exception as e:
            self.show_error_message(f"เกิดข้อผิดพลาด: {str(e)}")
            self.result_from.setText("Error")
            self.result_to.setText("Error")
            
    def show_error_message(self, message):
        """แสดงข้อความ error"""
        self.error_label.setText(f"⚠️ {message}")
        self.error_label.show()
        
    def clear_error_message(self):
        """ล้างข้อความ error"""
        self.error_label.hide()
        
    def update_history_display(self):
        self.history_list.clear()
        for item in self.conversion_history[:5]:  # Show last 5
            self.history_list.addItem(item)
            
    def close_application(self):
        """ปิดโปรแกรม"""
        reply = QMessageBox.question(self, 'ปิดโปรแกรม', 
                                   'คุณต้องการปิดโปรแกรมหรือไม่?',
                                   QMessageBox.StandardButton.Yes | 
                                   QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()