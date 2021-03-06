import json
import time
import gzip
import logging
import urllib
import urllib2
import HTMLParser

from StringIO import StringIO

from supybot.commands import *
import supybot.callbacks as callbacks

logger = logging.getLogger('supybot')
html_parser = HTMLParser.HTMLParser()

class StackEx(callbacks.Plugin):
    """silly stuff to do with http://libraries.stackexchange.com/
    """
    threaded = True

    def __init__(self, irc):
        self.__parent = super(StackEx, self)
        self.__parent.__init__(irc)
        # when starting up fetch any questions in the last two hours
        self.last_request = int(time.time()) - (2 * 60 * 60)

    def __call__(self, irc, msg):
        self.__parent.__call__(irc, msg)
        now = int(time.time())
        wait = self.registryValue('waitPeriod')
        if now - self.last_request > wait:
            logger.info("looking for new questions since %s" % now)
            irc = callbacks.SimpleProxy(irc, msg)
            questions = get_questions(self.last_request)
            self.last_request = now
            if len(questions) > 0:
                n = ["%s - %s" % (q['title'], q['url']) for q in questions]
                logger.info("found questions: %s" % n)
                irc.reply('[library stackexchange] ' + ' ; '.join(n), to='#code4lib', prefixNick=False)

    def lastq(self, irc, msg, args):
        """returns the last libraries stack exchange question
        """
        t = int(time.time())
        q = get_questions(0)[0]
        irc.reply("%s <%s>" % (q['title'], q['url']))

    lastq = wrap(lastq)

def get_questions(from_date):
    new_questions = []
    # all stack exchange api calls return gzipped content
    # kinda sucky that urllib2 doesn't hande gzip :(
    url = "http://api.stackexchange.com/2.0/questions?order=desc&sort=creation&site=libraries.stackexchange.com&fromdate=%s" % from_date
    logger.info("calling stackex api: %s" % url)
    response = urllib2.urlopen(url)
    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    questions = json.loads(data)
    logger.info("got stackex response: %s" % questions)
    for question in questions['items']:
        new_questions.append({
            'title': textify(question['title']),
            'url': shorten(textify(question['link']))})

    return new_questions

def textify(html):
    return html_parser.unescape(html)

def shorten(long_url):
    params = {'longUrl' : long_url, 'login' : 'zoia', 'apiKey' : 'R_e0079bf72e9c5f53bb48ef0fe706a57c', 'version' : '2.0.1', 'format' : 'json'}
    url = 'http://api.bit.ly/shorten?' + urllib.urlencode(params)
    response = urllib2.urlopen(url).read()
    data = json.loads(response)
    return data['results'][long_url]['shortUrl']

Class = StackEx
