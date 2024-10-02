def time_to_sek(hh, mm, ss):
    total_s = 0
    total_s += ss 
    total_s += mm * 60
    total_s += hh * 3600
    return total_s

def sek_to_time(ss):
    hh = ss // 3600
    mm = (ss - (hh * 3600)) // 60
    ss -= (mm * 60 + hh * 3600)
    return hh, mm, ss