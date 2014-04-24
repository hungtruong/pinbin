from pinbin.models import Location
from pinbin import app, db
from flask import render_template, request, make_response
import json

@app.route('/', methods=['GET', 'POST'])
def show_locations():
  if request.method == 'GET':
    #show list of locations
    locations = Location.objects.limit(50)
    return render_template('locations/list.html', locations=locations)
  else:
    #handle location post
    longitude = float(request.values['longitude'])
    latitude = float(request.values['latitude'])
    speed = request.values.get('speed')
    accuracy = request.values.get('accuracy')
    location = Location(coordinate=[longitude,latitude],
                        speed=speed,
                        accuracy=accuracy)
    if location.save():
      resp = make_response("ok\n")
      return resp
    else:
      return "Error saving", 401

@app.route('/geojson_circles/')
def get_geojson_circles():
  locations = Location.objects.limit(50)
  geojson_locations = []
  for location in locations:
    geojson_locations.append(location.geojson())
  return json.dumps(geojson_locations)

@app.route('/geojson_path/')
def get_geojson_path():
  locations = Location.objects.limit(50)
  geojson_path = {"type": "LineString"}
  coordinates = []
  for location in locations:
    coordinates.append(location.coordinate)
  geojson_path['coordinates'] = coordinates
  return json.dumps(geojson_path)
