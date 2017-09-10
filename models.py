from sqlalchemy import Column, Integer, String, Boolean
from geoalchemy2.types import Geography
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    online = Column(Boolean)
    location = Column(Geography(geometry_type='POINT', srid=420))
    marker = Column(Geography(geometry_type='POINT', srid=699))

    def __init__(self, json=None):
        if json is not None:
            self.from_json(json)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def to_json(self):
        return {
            'name': self.name,
            'online': self.online,
            'location': {
                'lat': self.location.geom.y,
                'long': self.location.geom.x
            },
            'marker': {
                'lat': self.marker.geom.y,
                'long': self.marker.geom.x
            }
        }
    
    def from_json(self, json):
        self.name = json['name']
        self.online = json['online']
        self.location.geom.y = json['location']['lat']
        self.location.geom.x = json['location']['long']
        self.marker.geom.y = json['marker']['lat']
        self.marker.geom.x = json['marker']['long']



def get_user(name):
    return User.query.filter(User.name == name).first()