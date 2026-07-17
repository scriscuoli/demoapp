import sys

def get_min_max(num:int):
    snum = str(num)
    while len(snum) < 4:
        snum = f"0{snum}"

    #print(f"snum={snum}")
    da = (snum[0:1], snum[1:2], snum[2:3], snum[3:4 ])
    lowtohigh = sorted(da)
    hightolow = sorted(da, reverse=True)
    lth = int("".join(lowtohigh))
    htl = int("".join(hightolow))
    return (lth,htl)


def process_num(num):
    results = []
    while num != 6174:
        vmin,vmax =get_min_max(num)
        num = vmax - vmin
        results.append({"vmin":vmin,"vmax":vmax,"num":num})
    return results
