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

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)

    def to_json(self):
        return {
            'name': self.name,
            'online': self.online,
            'location': {
                'lat': self.location.geom.x,
                'long': self.location.geom.y
            },
            'marker': {
                'lat': self.marker.geom.x,
                'long': self.marker.geom.y
            }
        }


def get_user(name):
    return User.query.filter(User.name == name).first()