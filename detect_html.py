from HTMLParser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr, value in attrs:
            print '-> %s > %s' % (attr, value)

parser = SimpleHTMLParser()
lines = int(raw_input())
feed_text = '\n'.join([raw_input() for x in xrange(lines)])
parser.feed(feed_text)