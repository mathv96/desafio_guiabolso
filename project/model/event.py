from datetime import datetime

class Event():
    def __init__(self, component=None, version=None, responsible=None, status=None):
        self.component = component
        self.version = version
        self.responsible = responsible
        self.status = status
        self.date=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')