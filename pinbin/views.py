from pinbin.models import Location
from pinbin import app, db
from flask import render_template, request, make_response
import json, datetime

@app.route('/', methods=['GET', 'POST'])
def show_locations():
  if request.method == 'GET':
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=50, type=int)
    #show list of locations
    locations = Location.objects.paginate(page=page, per_page=limit)
    #locations = Location.objects.limit(limit)
    return render_template('locations/list.html',
                            locations=locations,
                            page=page,
                            limit=limit)
  else:
    #handle location post
    longitude = float(request.values['longitude'])
    latitude = float(request.values['latitude'])
    speed = request.values.get('speed')
    accuracy = request.values.get('accuracy')
    timestamp = float(request.values.get('timestamp'))
    location = Location(coordinate=[longitude,latitude],
                        speed=speed,
                        accuracy=accuracy)
    if (timestamp):
      location.created_at = datetime.datetime.fromtimestamp(timestamp)
    if location.save():
      resp = make_response("ok\n")
      return resp
    else:
      return "Error saving", 401

@app.route('/geojson_circles/')
def get_geojson_circles():
  page = request.args.get('page', default=1, type=int)
  limit = request.args.get('limit', default=50, type=int)
  locations = Location.objects.paginate(page=page, per_page=limit)
  geojson_locations = []
  for location in locations.items:
    geojson_locations.append(location.geojson())
  return json.dumps(geojson_locations)

@app.route('/geojson_path/')
def get_geojson_path():
  page = request.args.get('page', default=1, type=int)
  limit = request.args.get('limit', default=50, type=int)
  locations = Location.objects.paginate(page=page, per_page=limit)
  geojson_path = {"type": "LineString"}
  coordinates = []
  for location in locations.items:
    coordinates.append(location.coordinate)
  geojson_path['coordinates'] = coordinates
  return json.dumps(geojson_path)
