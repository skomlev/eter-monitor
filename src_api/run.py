from api.app import create_app


application = create_app()

if __name__ == '__main__':
    host = application.config["APP_HOST"]
    port = application.config["APP_PORT"]
    application.run(host=host, port=port)
