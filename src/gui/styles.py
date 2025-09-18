MAIN_STYLE = """
QMainWindow {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0 #1e3a8a, stop:1 #3b82f6);
}

#titleLabel {
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin: 10px;
}

#subtitleLabel {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 20px;
}

#headerFrame {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #1e3a8a, stop:1 #3b82f6);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 20px;
}

QTabWidget::pane {
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    background: #ffffff;
    padding: 8px;
}

QTabWidget::tab-bar {
    alignment: center;
}

QTabBar::tab {
    background: #f8fafc;
    color: #64748b;
    padding: 12px 25px;
    margin: 2px;
    border-radius: 8px;
    font-weight: 500;
    border: 2px solid #e2e8f0;
    min-width: 60px;
}

QTabBar::tab:selected {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #1e3a8a, stop:1 #3b82f6);
    color: white;
    border: 2px solid #3b82f6;
}

QTabBar::tab:hover {
    background: #e2e8f0;
    color: #1e3a8a;
    border: 2px solid #cbd5e1;
}

#inputFrame {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 15px;
    padding: 20px;
}

#fieldLabel {
    color: #1e3a8a;
    font-weight: 600;
    font-size: 14px;
    min-width: 120px;
}

#valueInput {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px 16px;
    color: #1e293b;
    font-size: 16px;
}

#valueInput:focus {
    border: 2px solid #3b82f6;
    background: #ffffff;
    outline: 0px solid #3b82f6;
}

#unitCombo {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px 16px;
    color: #1e293b;
    font-size: 14px;
}

#unitCombo::drop-down {
    border: none;
    width: 20px;
}

#unitCombo::down-arrow {
    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDFMNiA2TDExIDEiIHN0cm9rZT0iIzY0NzQ4YiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+Cg==);
}

#unitCombo:focus {
    border: 2px solid #3b82f6;
    background: #ffffff;
}

#unitCombo QAbstractItemView {
    background: #ffffff;
    color: #1e293b;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    selection-background-color: #f1f5f9;
    outline: none;
}

#unitCombo QAbstractItemView::item {
    padding: 8px 12px;
    color: #1e293b;
}

#unitCombo QAbstractItemView::item:selected {
    background: #3b82f6;
    color: white;
}

#convertButton {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #1e3a8a, stop:1 #3b82f6);
    border: none;
    border-radius: 12px;
    padding: 16px;
    color: white;
    font-size: 16px;
    font-weight: bold;
}

#convertButton:hover {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #1d4ed8, stop:1 #2563eb);
}

#convertButton:pressed {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #1e40af, stop:1 #1d4ed8);
}

#resultFrame {
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 15px;
    padding: 25px;
}

#resultValue {
    font-size: 28px;
    font-weight: bold;
    color: #1e3a8a;
    margin: 8px;
}

#resultUnit {
    font-size: 16px;
    color: #64748b;
    margin: 8px;
}

#equalsLabel {
    font-size: 20px;
    color: #64748b;
    margin: 15px;
    font-weight: 500;
}

#copyButton {
    background: #ffffff;
    border: 2px solid #1e3a8a;
    border-radius: 8px;
    color: #1e3a8a;
    padding: 8px 16px;
    margin-top: 15px;
    font-weight: 500;
}

#copyButton:hover {
    background: #1e3a8a;
    color: white;
    border: 2px solid #1e3a8a;
}

#copyButton:pressed {
    background: #1e40af;
    color: white;
    border: 2px solid #1e40af;
}

#historyFrame {
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 15px;
    padding: 20px;
}

#historyLabel {
    color: #1e3a8a;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 15px;
}

#historyList {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    color: #475569;
    font-size: 13px;
    padding: 5px;
    outline: none;
}

#historyList::item {
    padding: 10px 15px;
    border-bottom: 1px solid #f1f5f9;
    border-radius: 6px;
    margin: 2px;
}

#historyList::item:selected {
    background: #f1f5f9;
    color: #1e3a8a;
    border: 1px solid #cbd5e1;
}

#historyList::item:hover {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}

#historyList::item:last-child {
    border-bottom: none;
}
"""