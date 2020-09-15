from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from main import create_app, db
from main.controller.user_controller import api as user_api
from main.controller.hotel_controller import api as hotel_api
from main.model.revoked_token import RevokedTokenModel
from main.cache import cache
import os


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
jwt = JWTManager(app)
CORS(app)
app.register_blueprint(user_api)
app.register_blueprint(hotel_api)
cache.init_app(app)
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.before_first_request
def create_tables():
    db.create_all()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


@manager.command
def run():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    manager.run()
