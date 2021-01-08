from flask import Flask, request

from helpers import *

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('user', None)
    if name:
        return "Hello {}".format(name)
    else:
        return "Hello World"


@app.route('/optimizely/experiment')
def opt_experiment():
    optimizely_client = setup_optimizely()
    user_id = request.args.get('user_id', None)
    explore_experiment = optimizely_experiment(optimizely_client, user_id)
    return "Order {} Pizza".format(explore_experiment)


@app.route('/optimizely/feature')
def opt_feature():
    is_purchase = request.args.get('purchase', None)
    user_id = request.args.get('user_id', None)
    optimizely_client = setup_optimizely()
    explore_opt = optimizely_feature(optimizely_client, user_id, is_purchase)
    optimizely_client.track('purchase', user_id)
    return explore_opt


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, use_debugger=True, use_reloader=False)
