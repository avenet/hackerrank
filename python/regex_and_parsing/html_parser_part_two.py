from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data == '\n':
            return
        
        print('>>> Data')
        self.print_data(data)
    
    def print_data(self, data):
        print(data)
    
    def handle_comment(self, data):
        if data == '\n':
            return
        
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        
        self.print_data(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
