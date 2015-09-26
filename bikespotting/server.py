"""
    This module runs the back-end server to the bike spotting website
"""
# pyramid modules
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import os
cwd = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    config = Configurator()
    # add the routes and views
    config.add_route("index", "/")
    config.add_route("bikes", "/bikes")
    config.scan()
    config.add_static_view(name='static', path=os.path.join(cwd, 'static'))
    app = config.make_wsgi_app()

    # start the server
    server = make_server("0.0.0.0", 8080, app)
    print "[bike-spotting] server running on :%d" % 8080
    server.serve_forever()
