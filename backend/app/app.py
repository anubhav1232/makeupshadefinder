from flask import Flask
from app.routes.skin_analysis import skin_analysis_bp

app = Flask(__name__)
app.register_blueprint(skin_analysis_bp)

if __name__ == '__main__':
    app.run(debug=True)
