# arquivo: test_users.py

from app.models import User, db

def test_create_user(app):
    with app.app_context():
        user = User(username="teste", email="teste@example.com")
        db.session.add(user)
        db.session.commit()

        saved_user = User.query.filter_by(username="teste").first()
        assert saved_user is not None
        assert saved_user.email == "teste@example.com"