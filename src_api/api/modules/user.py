from api.models import db, User, Device, Sensor


def create_user(user_data):
    email = user_data.get("email")
    if User.query.filter_by(email=email).first():
        raise AlreadyExists("User %s already exists" % email)
    user = User(user_data)
    db.session.add(user)
    db.session.commit()
    return user.as_dict()


def get_user(args):
    users = User.query.filter_by()
    if args.get('email'):
        users = users.filter_by(email=args.get('email'))
    if args.get('name'):
        users = users.filter_by(name=args.get('name'))
    if args.get('id'):
        users = users.filter_by(id=args.get('id'))
    if not users:
        raise NotFound("User has not been found")
    return [c.as_dict() for c in users]


def create_divice(divice_data):
    user_id = divice_data.get("user_id")
    if not User.query.filter_by(id=user_id).first():
        raise AlreadyExists("User %s already exists" % user_id)
    device = Device(divice_data)
    db.session.add(device)
    db.session.commit()
    return device.as_dict()


def get_divice(args):
    device = Device.query.filter_by()
    if args.get('id'):
        device = device.filter_by(id=args.get('id'))
    if args.get('geolocation'):
        device = device.filter_by(geolocation=args.get('geolocation'))
    if args.get('user_id'):
        device = device.filter_by(user_id=args.get('user_id'))
    if not device:
        raise NotFound("Device has not been found")
    return [c.as_dict() for c in device]


def create_sensor(sensor_data):
    sensor = Sensor(sensor_data)
    db.session.add(sensor)
    db.session.commit()
    return sensor.as_dict()


def get_sensor(args):
    sensor = Sensor.query.filter_by()
    if args.get('id'):
        sensor = sensor.filter_by(id=args.get('id'))
    if args.get('name'):
        sensor = sensor.filter_by(name=args.get('name'))
    if args.get('variable'):
        sensor = sensor.filter_by(variable=args.get('variable'))
    if not sensor:
        raise NotFound("Sensor has not been found")
    return [c.as_dict() for c in sensor]

# Exceptions


class NotFound(Exception):
    pass


class AlreadyExists(Exception):
    pass
