from pinbin.models import Location
from pinbin import app, db
from flask import render_template, request, make_response

@app.route('/', methods=['GET', 'POST'])
def show_locations():
  if request.method == 'GET':
    #show list of locations
    locations = Location.objects.all()
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
