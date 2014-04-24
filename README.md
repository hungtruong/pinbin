#PinBin

By [Hung Truong](http://www.hung-truong.com/)

PinBin is a self-hosted service that makes it easier to debug
and visualize location-based data gathered from mobile devices.
You can send location coordinates and other optional properties
to PinBin and see that data on a map before building out a full
backend.

##Prerequisites
To run PinBin locally, you'll need to install a few requirements.
First, get [MongoDB](https://www.mongodb.org/) up and running on
your local development environment. You'll also need
[Python](https://www.python.org/) (2.x) on your system. You will want
to get set up with a [Heroku](https://www.heroku.com/) account
so you can eventually push the app to production.

Next, clone the repository:

```
$ git clone https://github.com/hungtruong/pinbin.git
```

It's probably a good idea to set up
[virtualenv](http://www.virtualenv.org/en/latest/) to work on
your project. Install the project dependencies:

```
$ pip install -r requirements.txt
```

You'll also need to obtain a [Mapbox](https://www.mapbox.com/)
key (free!) in order to visualize your location data on a map.
Add the key to a .env file that will make our variables available
to our app when we launch it via foreman.

```
$ echo "MAPBOX_KEY=mapboxuser.asdfasdf" > .env
```

If you have the [Heroku Toolbelt](https://toolbelt.heroku.com/)
installed, you should be able to run the app with the command:

```
$ foreman start
```

Point your browser to [localhost:5000](http://127.0.0.1:5000) and you
should see an empty map. Try posting some data to it to see
how location data is visualized.

```
$ curl -X POST -d "longitude=-83.748323&latitude=42.2646136&accuracy=5" http://127.0.0.1:5000
$ curl -X POST -d "longitude=-83.746730&latitude=42.2649831&accuracy=10" http://127.0.0.1:5000
$ curl -X POST -d "longitude=-83.734835&latitude=42.2748291&accuracy=30" http://127.0.0.1:5000
```

From here, you probably want to deploy PinBin to Heroku so you can start
sending it real location data from your mobile device.

##Deploying to Heroku
To deploy to Heroku, you'll first need to create an app.

```
$ heroku create
```
Set the Heroku environment config for your Mapbox key.

```
$ heroku config:set MAPBOX_KEY=mapboxuser.asdfasdf
```
You will also want to sign up for the MongoHQ addon.

```
$ heroku addons:add mongohq
```
Finally, push the repo to Heroku!

```
$ git push heroku master
```
If all goes well, you should be able to go to the Heroku app and see the same
blank map as before. Start pushing location data to your app to visualize and
debug it!

##Data format
PinBin accepts the following parameters when taking location data:
* latitude (required)
* longiude (required)
* timestamp (optional, defaults to creation time) In unix timestamp format
* accuracy (optional) Horizontal accuracy of location
* speed (optional) Speed in meters of device
