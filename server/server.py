"""
    This module runs the back-end server to the bike spotting website
"""
# pyramid modules
from wsgiref.simple_server import make_server
import os
from pyramid.response import Response, FileResponse
from pyramid.config import Configurator

# http modules and station/serialization
import requests as rq
import station

def bikes(request):
    """
    defines the response when directing to the "bikes" route.
    """
    # pick up the latest bike statuses
    api_uri = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"
    r = rq.get(api_uri)
    
    # build a dictionary of stations from the API response
    stations = station.StationCollection()
    stations.from_xml_string(r.text)

    return Response(stations.to_json())

def index(request):
    return FileResponse(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views/index.html'))

if __name__ == "__main__":
    config = Configurator()
    config.add_route("index", "/")
    config.add_view(index, route_name="index")
    # add the routes and views
    config.add_route("bikes", "/bikes")
    config.add_view(bikes, route_name="bikes")
    app = config.make_wsgi_app()

    # start the server
    server = make_server("0.0.0.0", 8080, app)
    server.serve_forever()
