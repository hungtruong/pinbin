import datetime
from flask import url_for
from pinbin import db
import json

class Location(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    coordinate = db.GeoPointField(required=True)
    speed = db.FloatField()
    accuracy = db.FloatField()

    def get_absolute_url(self):
      return url_for('location', kwargs={"slug": self.slug})

    def geojson(self):
      return {"type":"Feature",
              "geometry":
                {
                  "type":"Point",
                  "coordinates": [self.coordinate[0], self.coordinate[1]]
                },
              "properties":
                {
                  "radius":self.accuracy
                }
              }

    def __unicode__(self):
      return "%s @ %s %s" % (self.created_at, self.coordinate[0], self.coordinate[1])

    meta = {
      'allow_inheritance': True,
      'indexes': ['-created_at'],
      'ordering': ['-created_at']
    }
