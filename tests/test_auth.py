import pytest
from app import create_app, db
from app.models.user import User


@pytest.fixture
def app():
    application = create_app('testing')
    with application.app_context():
        db.create_all()
        yield application
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_password_hashing(app):
    with app.app_context():
        user = User(username='hashtest', role='owner')
        user.set_password('securepass')
        assert user.check_password('securepass')
        assert not user.check_password('wrongpass')


def test_login_success(app, client):
    with app.app_context():
        user = User(username='loginuser', role='employee')
        user.set_password('mypass')
        db.session.add(user)
        db.session.commit()

    resp = client.post('/login', data={'username': 'loginuser', 'password': 'mypass'},
                       follow_redirects=True)
    assert resp.status_code == 200


def test_login_wrong_password(client):
    resp = client.post('/login', data={'username': 'nobody', 'password': 'bad'},
                       follow_redirects=True)
    assert b'Invalid' in resp.data
