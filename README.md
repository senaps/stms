# Execute:

    export FLASK_APP=app
    export FLASK_ENV=development
    flask shell
    >>> from project.extentions import db
    >>> db.create_all()
    >>> exit()
    flask run --host 0.0.0.0 --port 8000
    
and we are done! :)