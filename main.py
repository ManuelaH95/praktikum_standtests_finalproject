import requests
import configuration as conf
import data as d


def create_new_order():
    order = requests.post(conf.URL_SERVICE + conf.CREATE_ORDER_PATH, json=d.order_details, headers=d.headers)

    assert order.status_code == 201
    order_num = order.json()["track"]
    return order_num


def get_order_by_track(order_num: int):
    # /api/v1/orders/track?t=908034
    params = dict()
    params["t"] = order_num
    order = requests.get(conf.URL_SERVICE + conf.GET_ORDER_BY_TRACK_PATH, params=params, headers=d.headers)
    assert order.status_code == 200


def test_run_checks():
    order_num = create_new_order()
    get_order_by_track(order_num)
