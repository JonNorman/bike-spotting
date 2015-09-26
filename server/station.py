import xml.etree.ElementTree as et
import json

class StationCollection(object):

    def __init__(self):
        self.stations = None

    def from_xml_string(self, xml_tree_string):
        xml_tree = et.fromstring(xml_tree_string)
        stations = {}
        for elem in xml_tree.getchildren():
            props = elem.getchildren()
            station = Station({prop.tag: prop.text for prop in props})
            stations[station.props['id']] = station
        
        self.stations = stations

    def to_json(self):
        return json.dumps(self.stations, default=Station.serialize)

class Station(object):

    def __init__(self, attributes):
        self.props = attributes

    def serialize(self):
        return self.props

    def __str__(self):
        return "ID: {id} Name: {name}".format(**self.props)
