from api.models import db, User, Device, Sensor


def create_user(user_data):
    email = user_data.get("email")
    if User.query.filter_by(email=email).first():
        raise AlreadyExists("User %s already exists" % email)
    user = User(user_data)
    db.session.add(user)
    db.session.commit()
    return user.as_dict()


def get_user(email):
    users = User.query.filter_by()
    if email:
        users = users.filter_by(email=email)
    if not users:
        raise NotFound("User %s has not been found" % email)
    return [c.as_dict() for c in users]


def create_divice(divice_data):
    user_id = divice_data.get("user_id")
    if not User.query.filter_by(id=user_id).first():
        raise AlreadyExists("User %s already exists" % user_id)
    device = Device(divice_data)
    db.session.add(device)
    db.session.commit()
    return device.as_dict()


def get_divice(id_):
    device = Device.query.filter_by()
    if id_:
        device = device.filter_by(id=id_)
    if not device:
        raise NotFound("Device %s has not been found" % id_)
    return [c.as_dict() for c in device]


def create_sensor(sensor_data):
    sensor = Sensor(sensor_data)
    db.session.add(sensor)
    db.session.commit()
    return sensor.as_dict()


def get_sensor(id_):
    sensor = Sensor.query.filter_by()
    if id_:
        sensor = sensor.filter_by(id=id_)
    if not sensor:
        raise NotFound("Sensor %s has not been found" % id_)
    return [c.as_dict() for c in sensor]

# Exceptions


class NotFound(Exception):
    pass


class AlreadyExists(Exception):
    pass
