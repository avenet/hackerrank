from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("{}".format(tag))
        self.print_attrs(attrs)

    def print_attrs(self, attrs):
        for attr_name, attr_value in attrs:
            print(
                '-> {0} > {1}'.format(
                    attr_name,
                    attr_value
                )
            )


parser = MyHTMLParser()

line_count = int(input())
lines = []

for line_read_attempt in range(line_count):
    lines.append(input())

html_content = '\n'.join(lines)

parser.feed(html_content)
