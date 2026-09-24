import pyspark
import pandas as pd
from pyspark.sql import SparkSession

def start_session:
    return SparkSession.builder.appName('y_footy_analytics_tho_v1').getOrCreate()

