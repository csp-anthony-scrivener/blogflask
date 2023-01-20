from app import app_factory
import os
import dotenv


basedir = os.path.abspath(__file__)

env_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_path):
    dotenv.load_dotenv(env_path)

app = app_factory(os.getenv('FLASK_ENVIRONMENT') or 'default')



if __name__ == '__main__':
    app.run()