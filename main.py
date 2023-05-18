from docx import Document
class main():
    def __init__(self ,headSize = 29 , headFont = "monospace" , normalSize = 15 , normalFont = "sans serif" , inFile = "in.txt" , outFile = "out.docx"):
        self.headSize = headSize
        self.headFont = headFont
        self.normalSize = normalSize
        self.normalFont = normalFont
        self.document = Document()
        self.document.add_page()
        self.points = []
        self.headers = []
    def readfile(self):
        file = open(self.inFile , "rt")
        self.fileContents = file.read()
        file.close()
