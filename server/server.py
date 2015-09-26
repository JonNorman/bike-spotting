from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import requests as rq
import xml.etree.ElementTree as et
import json

class Station(object):

    def __init__(self, attributes):
        self.props = attributes

    def serialize(self):
        return self.props

    def __str__(self):
        return "ID: {id} Name: {name}".format(**self.props)

def parse_xml(tree):
    stations = {}
    for elem in tree.getchildren():
        props = elem.getchildren()
        station = Station({prop.tag: prop.text for prop in props})
        stations[station.props['id']] = station

    return stations

def home(request):
    r = rq.get("https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml")
    tree = et.fromstring(r.text)
    stations = parse_xml(tree)
    return Response("{:s}".format(json.dumps(stations, default=Station.serialize)))

if __name__ == "__main__":
    config = Configurator()
    config.add_route("home", "/")
    config.add_view(home, route_name="home")
    app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 8080, app)
    server.serve_forever()