from model.event import Event

class EventHelper():

    def return_event(self, event):
        ev = Event(event['component'], event['version'], event['responsible'], event['status'])
        return ev