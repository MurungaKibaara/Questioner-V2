'''Application entrypoint'''
from app import create_app
APP = create_app('testing')

if __name__ == "__main__":
    APP.run()
