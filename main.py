from PyQt5.QtWidgets import QApplication, QTextBrowser, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
import sys
import openai

class Window(QWidget) :
    
    def __init__ (self):
        super().__init__()

        self.title="Chat GPT Memo"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 600
        
        self.setStyleSheet('border-top:black')
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon('D:/Solo Coding/Projects/ChatGPT/robot.png'))
        self.Ui()
    
    def Ui (self):
        
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.browser)
        vbox.addWidget(self.lineEdit)

        self.setLayout(vbox)
        self.lineEdit.returnPressed.connect(self.updateBrowser)
        
    
    def updateBrowser(self):
        openai.api_key ="YOUR API KEY"
              
        text = str(self.lineEdit.text ())
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user","content": text}
            ]
        )
        answer = completion.choices[0].message.content
        self.browser.append("<b>%s</b>"%(text))
        self.browser.append(answer)
        self.lineEdit.clear()
        
                    
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()