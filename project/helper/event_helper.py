from model.event import Event

def return_event(event):
    ev = Event(event['component'], event['version'], event['responsible'], event['status'])
    return ev