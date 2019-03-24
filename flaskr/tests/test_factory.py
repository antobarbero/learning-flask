from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


# this `client` argument matches with the `client` fixture function.
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello world!'
