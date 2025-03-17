import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.contacts = {}  # 주소록 데이터를 저장할 딕셔너리
        
        self.initUI()
    
    def initUI(self):
        # 아이콘 추가
        self.name_icon = QLabel()
        self.name_icon.setPixmap(QPixmap("user_icon.png").scaled(20, 20))
        
        self.phone_icon = QLabel()
        self.phone_icon.setPixmap(QPixmap("phone_icon.png").scaled(20, 20))
        
        # 라벨 및 입력 필드 (연락처 추가)
        self.name_label = QLabel('이름:')
        self.name_input = QLineEdit()
        self.phone_label = QLabel('전화번호:')
        self.phone_input = QLineEdit()
        
        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_icon)
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)
        
        phone_layout = QHBoxLayout()
        phone_layout.addWidget(self.phone_icon)
        phone_layout.addWidget(self.phone_label)
        phone_layout.addWidget(self.phone_input)
        
        self.add_button = QPushButton('추가')
        
        # 검색 기능
        self.search_label = QLabel('검색:')
        self.search_input = QLineEdit()
        self.search_button = QPushButton('검색')
        
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        
        # 결과 표시
        self.result_browser = QTextBrowser()
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addLayout(name_layout)
        layout.addLayout(phone_layout)
        layout.addWidget(self.add_button)
        layout.addLayout(search_layout)
        layout.addWidget(self.result_browser)
        
        self.setLayout(layout)
        
        # 이벤트 연결
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)
        
        self.setWindowTitle('주소록 프로그램')
        self.setGeometry(100, 100, 350, 300)
    
    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        
        if name and phone:
            self.contacts[name] = phone
            self.result_browser.append(f'추가됨: {name} - {phone}')
        else:
            self.result_browser.append('이름과 전화번호를 입력하세요!')
        
    def search_contact(self):
        query = self.search_input.text().strip()
        
        results = [f'{name}: {phone}' for name, phone in self.contacts.items() if query in name or query in phone]
        
        if results:
            self.result_browser.append("검색 결과:")
            self.result_browser.append("\n".join(results))
        else:
            self.result_browser.append(f'검색 결과 없음: {query}')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())
