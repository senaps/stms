# Execute:

    export FLASK_APP=app
    export FLASK_ENV=development
    flask shell
    >>> from project.extentions import db
    >>> db.create_all()
    >>> exit()
    flask run --host 0.0.0.0 --port 8000

or if you've got error's with above commands, you could go on with docker

    sudo docker build -t stms .
    sudo docker run -d -p 8000:8000 --name stms_worker stms

    
and we are done! :)
