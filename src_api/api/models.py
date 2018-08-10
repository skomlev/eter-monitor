from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


class User(Base):

    __tablename__ = 'user'

    name = db.Column(db.Unicode(128))
    email = db.Column(db.Unicode(128), nullable=False)
    password = db.Column(db.Unicode(128))

    def __init__(self, user_data):
        for k, v in user_data.items():
            self.__setattr__(k, v)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if not (c.name == 'date_created')
        }


class Sensor(Base):

    __tablename__ = 'sensor'

    name = db.Column(db.Unicode(30), nullable=False)
    variable = db.Column(db.Unicode(30), nullable=False)
    description = db.Column(db.Unicode(128))

    def __init__(self, user_data):
        for k, v in user_data.items():
            self.__setattr__(k, v)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if not (c.name == 'date_created')
        }


class Measure(Base):

    __tablename__ = 'measure'

    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    sensor = relationship('Sensor')
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = relationship('Device')
    value = db.Column(db.Unicode(10), nullable=False)

    def __init__(self, user_data):
        for k, v in user_data.items():
            self.__setattr__(k, v)

    def __str__(self):
        return self.sensor

    def __repr__(self):
        return '<sensor %r>' % self.sensor

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if not (c.name == 'date_created')
        }


class Device(Base):

    __tablename__ = 'device'

    state = db.Column(db.Boolean, default=False)
    geolocation = db.Column(db.Unicode(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('User')

    def __init__(self, user_data):
        for k, v in user_data.items():
            self.__setattr__(k, v)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if not (c.name == 'date_created')
        }
