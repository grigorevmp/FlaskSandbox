from app import appName, db
from app.models import User, Post


@appName.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
