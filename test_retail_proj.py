from lib.DataReader import *
from lib.DataManipulation import *
from lib.ConfigReader import *


def test_read_customers_df(spark):
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

def test_read_orders_df(spark):
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68884

def test_filter_close_orders(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_closed_orders(orders_df).count()
    assert filtered_count == 7556 

def test_read_app_config():
    config = get_app_config("LOCAL")
    assert config["orders.file.path"]=="data/orders.csv"