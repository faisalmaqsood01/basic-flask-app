import json


def test_hello(client):
    res = client.get('/')
    assert res.status_code == 200
    expected = "Hello World"
    assert expected == res.get_data(as_text=True)


def test_opt_feature(client):
    res = client.get('/optimizely/feature')
    assert res.status_code == 200
    res1 = {
        'purchase': False
    }
    assert res1 == json.loads(res.get_data(as_text=True))


def test_opt_feature_with_params(client):
    res = client.get('/optimizely/feature?purchase=True&user_id=1')
    assert res.status_code == 200
    res1 = {
        'purchase': True,
        'discount_amount': 9
    }
    assert res1 == json.loads(res.get_data(as_text=True))


def test_opt_experiment(client):
    res = client.get('/optimizely/experiment?user_id=1')
    assert res.status_code == 200
    expected = "Order medium Pizza"
    assert expected == res.get_data(as_text=True)
