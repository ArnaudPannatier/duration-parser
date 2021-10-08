def str2secs(duration_str):
    h, m, s = duration_str.split(":")
    return h * 3600 + m * 60 + s 

def secs2str(s):
    h = s // 3600
    s -= h
    m = s // 60
    s -= m
    return "{}:{}:{}".format(h, m, s)
    