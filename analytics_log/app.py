import csv
import os
import pandas as pd
import datetime as dt
file_name='logs.txt'

from analytic import Analytic


path=os.path.abspath(file_name)


def convert_datetime(val):
    length=len(val)
    return dt.datetime.strptime(val[1:length], "%Y-%m-%d %H:%M:%S,%f")

df = pd.read_csv(path,encoding='utf-8', sep=": " ,engine='python',
                 names=["date","level","ip_address","sid","method","api_route","none", "noned"],
                 usecols=["date","level","ip_address","sid","method","api_route"],
                 converters={'date':convert_datetime})




if __name__ == '__main__':


    first=Analytic(df,"INFO")

    first.find_ip(df, "INFO")

    first.prohibit_route(df)
