from app import create_app
from app.db import db
from flask_swagger_ui import get_swaggerui_blueprint
from app.models import Pokemon

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swagger_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Pokemon Scouting API"}
)

app = create_app()
app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
