from flask_mail import Message
from app import mail
from ics import Calendar, Event

def send_email(subject, recipients, body):
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)

def create_ics_event(title, start_time):
    c = Calendar()
    e = Event()
    e.name = title
    e.begin = start_time
    e.duration = {"minutes": 30}
    c.events.add(e)
    return str(c)
