from flask import Flask
from instance.config import Config
from app.clients.routes import clients_bp
from app.projects.routes import projects_bp
from app.time_entries.routes import time_entries_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(clients_bp, url_prefix='/clients')
app.register_blueprint(projects_bp, url_prefix='/projects')
app.register_blueprint(time_entries_bp, url_prefix='/timeentries')

if __name__ == '__main__':
    app.run(debug=True)
