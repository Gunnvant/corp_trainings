import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import folium

def execute_query(engine,query):
    with engine.connect() as conn:
        result = conn.execute(query)
        result = [row for row in result]
        colnames = [row.keys() for row in result]
    result = pd.DataFrame(result,columns=list(colnames[0]))
    return result

def lat_long_in_neighbourhood(lat,long,coordinates):
    point=Point(long,lat)
    polygon=Polygon(coordinates[0][0])
    return polygon.contains(point)

def get_coordinate_lookup(json_data):
    coordinate_lookup = {}
    for feature in json_data['features']:
        coordinate_lookup[feature['properties']['neighbourhood']] = feature['geometry']['coordinates']
    return coordinate_lookup

def get_maps(json_data):
    m = folium.Map(
        location=[51.218575, 4.398631],
        tiles="cartodbpositron",
        zoom_start=11,
    )
    ttp = folium.GeoJsonTooltip(
       fields=['neighbourhood'],
         localize=True,
         style=('background-color: grey; color: white; font-family:'
                'courier new; font-size: 24px; padding: 10px;')
    )
    folium.GeoJson(json_data, name="geojson",tooltip = ttp).add_to(m)
    return m