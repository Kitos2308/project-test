import csv
import os
import pandas as pd
import datetime as dt
file_name='logs.txt'

from analitic import find_ip


path=os.path.abspath(file_name)


def convert_datetime(val):
    length=len(val)
    return dt.datetime.strptime(val[1:length], "%Y-%m-%d %H:%M:%S,%f")

df = pd.read_csv(path,encoding='utf-8', sep=": " ,engine='python',
                 names=["date","level","ip_address","sid","method","api_route","none", "noned"],
                 usecols=["date","level","ip_address","sid","method","api_route"],
                 converters={'date':convert_datetime})



print(df['date'])



find_ip(df, "DEBUG")
