import logging

from optimizely import optimizely


def setup_optimizely():
    logging.basicConfig(level=logging.INFO)
    optimizely_client = optimizely.Optimizely(
        sdk_key='WaasWMjNh3oKoVMP759hX'
    )
    logging.info('Is optimizely_client valid: {}'.format(optimizely_client.is_valid))
    return optimizely_client


def optimizely_experiment(optimizely_client, user_id):
    variation = optimizely_client.activate('explore_python_test', user_id)

    if variation == 'small':
        logging.info('Small Variation: {}'.format(variation))
    elif variation == 'medium':
        logging.info('medium Variation: {}'.format(variation))
    elif variation == 'large':
        logging.info('large Variation: {}'.format(variation))
    else:
        logging.info('No Variation: {}'.format(variation))

    return variation


def optimizely_feature(optimizely_client, user_id, is_purchase):
    discount_enabled = optimizely_client.is_feature_enabled('discount', user_id)
    response = {
        'purchase': False,
    }
    if discount_enabled:
        discount_amount = optimizely_client.get_feature_variable_integer('discount', 'discount', user_id)
        logging.info('{} got a discount of {}'.format(user_id, str(discount_amount)))
        if bool(is_purchase) is True:
            optimizely_client.track('purchase', user_id)
            logging.info('{} purchase successfully discount {}'.format(user_id, str(discount_amount)))
            response = {
                'purchase': True,
                'discount_amount': discount_amount
            }
            return response
    else:
        logging.info('{} did not get the discount feature'.format(user_id))

    return response
