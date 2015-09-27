"""
    This module runs the back-end server to the bike spotting website
"""
# pyramid modules
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import views
import os
from crawler import Crawler

cwd = os.path.dirname(os.path.abspath(__file__))
print cwd

def foo(request):
    return Response("heoihwe")

if __name__ == "__main__":
    config = Configurator()
    # add the routes and views
    config.add_route("index", "/")
    config.add_route("bikes", "/bikes")
    config.add_static_view(name='static', path='static')
    config.scan(views)
    app = config.make_wsgi_app()

    # start the server and the crawler
    server = make_server("0.0.0.0", 8080, app)
    crawler = Crawler()
    crawler.setup("https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml", 30)
    crawler.start()

    print "[bike-spotting] server running on :%d" % 8080
    server.serve_forever()
