from pyramid.view import view_config
from pyramid.response import Response, FileResponse

import os
import requests as rq
import station
cwd = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='index')
def index(request):
    return FileResponse(os.path.join(cwd, 'templates/index.html'))

@view_config(route_name='bikes')
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

