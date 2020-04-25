from app import app, db
from app.models import Poem


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Poem': Poem}


if __name__ == "__main__":
    db.create_all()
    app.run()
