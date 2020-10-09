import pandas as pd
import re
import graphic


def time_converter(time):
    time = '0' + time if time[1] == ':' else time

    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif (time[-2:] == "PM" and time[:2] == "12")or(time[-2:] == "AM"):
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:-2]


def parseDataFrame(frame):
    month = "|".join(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    for column in frame.columns:
        frame[column] = frame[column].apply(
            lambda x: (str(x) + '.2019' if bool(re.match("^\d{1,2}\.(" + month + ")$", str(x))) else x))
        frame[column] = frame[column].apply(
            lambda x: (
                time_converter(x) if bool(re.match('^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$', str(x))) else x))
        frame[column] = frame[column].apply(
            lambda x: (
                int(x[:-1]) if bool(re.match("^\d{1,2}\%$", str(x))) else x))
        frame[column] = frame[column].apply(
            lambda x: (
                float(x.replace(",", '.')) if bool(re.match("^\d+(,)\d+$", str(x))) else x))
        frame[column] = frame[column].apply(
            lambda x: (
                int(x.replace("mph", '').strip()) if bool(re.match("\d+\s(mph)", str(x))) else x))
    return frame


if __name__ == '__main__':
    frame = pd.read_csv("DATABASE.csv", sep=";")
    frame = parseDataFrame(frame)
    frame.set_index('day/month', inplace=True)
    graphic.graphics(frame)
