import sys
import datetime
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class PublisherWindow(QWidget):
	def __init__(self):
		super().__init__()
		
		self.resize(480, 640)
		self.move(800, 200)
		self.setWindowTitle('alsamixer')
		
		self.initUI()
	
	def initUI(self):
		self.summaryInput = QLineEdit()
		self.tagInput = QLineEdit()
		self.titleInput = QLineEdit()
			
		self.citationInput = QPlainTextEdit()
		self.notesInput = QPlainTextEdit()
		
		self.publishButton = QPushButton('Publish')
		self.publishButton.clicked.connect(self.publishInput)
		
		windowLabel = QLabel('Publish New Research Notes')
		windowLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
		
		summaryLabel = QLabel('Summary')
		tagLabel = QLabel('Tags')
		titleLabel = QLabel('Title')
		citationLabel = QLabel('Citation')
		notesLabel = QLabel('Notes')
				
		singleTextGrid = QGridLayout()
		
		singleTextGrid.addWidget(titleLabel, 0,0)
		singleTextGrid.addWidget(self.titleInput, 0,1)
		singleTextGrid.addWidget(tagLabel, 1,0)
		singleTextGrid.addWidget(self.tagInput, 1, 1)
		singleTextGrid.addWidget(summaryLabel, 2,0)
		singleTextGrid.addWidget(self.summaryInput, 2,1)
		
		multiTextVBox = QVBoxLayout()
		multiTextVBox.addWidget(citationLabel)
		multiTextVBox.addWidget(self.citationInput)
		multiTextVBox.addWidget(notesLabel)
		multiTextVBox.addWidget(self.notesInput)
		multiTextVBox.addWidget(self.publishButton)
		
		parentVBox = QVBoxLayout()
		parentVBox.addWidget(windowLabel)
		parentVBox.addLayout(singleTextGrid)
		parentVBox.addLayout(multiTextVBox)
		
		self.setLayout(parentVBox)
		
	def publishInput(self):
		summary = self.summaryInput.text()
		tags = self.tagInput.text()
		title = self.titleInput.text()
		citation = self.citationInput.document().toPlainText()
		notes = self.notesInput.document().toPlainText()
		date = datetime.date.today().strftime("%Y-%m-%d")
		modifiedDate = date
		slug = re.sub('[^0-9a-zA-Z_]+', '', title.lower().replace(' ', '_'))
		
		document = ""
		document += ''.join(["title:", title, "\n"])
		document += ''.join(["slug:", slug, "\n"])
		document += ''.join(["category:", 'research notes', "\n"])
		document += ''.join(["date:", date, "\n"])
		document += ''.join(["modified:", modifiedDate, "\n"])
		document += ''.join(["summary:", summary, "\n"])
		document += ''.join(["tags:", tags, "\n"])
		document += ''.join(["\n", "## Citation", "\n"])
		document += ''.join(["\n", citation, "\n"])
		document += ''.join(["\n", "## Notes", "\n"])
		document += ''.join(["\n", notes, "\n"])
		
		with open('content/researchNotes/' + slug + '.md', 'w+') as notesFile:
			notesFile.write(document)
		
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText("Successfully wrote new notes file")
		msgBox.exec_()
		
		self.resetInput()
		
	def resetInput(self):
		self.summaryInput.setText('')
		self.tagInput.setText('')
		self.titleInput.setText('')
		
		self.citationInput.document().setPlainText('')
		self.notesInput.document().setPlainText('')
				
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PublisherWindow()
    window.show()
    
    sys.exit(app.exec_())