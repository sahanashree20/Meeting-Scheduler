from flask import Blueprint, request, jsonify
from app import db
from app.models import Meeting
from app.scheduler import parse_csv, suggest_meeting_time
from app.utils import send_email, create_ics_event

bp = Blueprint('api', __name__)

@bp.route('/schedule', methods=['POST'])
def schedule_meeting():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    df = parse_csv(file)
    best_time = suggest_meeting_time(df)

    # Example: send email and save to DB
    recipients = ['recipient@example.com']
    send_email("Meeting Scheduled", recipients, f"Meeting at: {best_time}")
    
    meeting = Meeting(title="Team Meeting", start_time=best_time, participants=",".join(df.columns))
    db.session.add(meeting)
    db.session.commit()

    return jsonify({"message": "Meeting scheduled", "time": best_time})
