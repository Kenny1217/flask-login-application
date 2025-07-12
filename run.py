from app import flask_app

def main():
    app = flask_app()
    app.run(debug=True, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()