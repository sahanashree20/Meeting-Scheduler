from flask import Blueprint, render_template, request
from app.scheduler import parse_csv, suggest_meeting_time

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        df = parse_csv(file)
        best_time = suggest_meeting_time(df)
        return render_template("result.html", best_time=best_time)
    return render_template("upload.html")
