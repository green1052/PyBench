import datetime
import decimal


def get_pi():
    startDateTime = datetime.datetime.now()

    decimal.getcontext().prec += 2
    three = decimal.Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24

    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t

    decimal.getcontext().prec -= 2

    endDateTime = datetime.datetime.now()

    return {"pi": +s, "start": startDateTime, "end": endDateTime}


print("원주율을 구하고 있습니다...")

decimal.getcontext().prec = 50000
pi = get_pi()

millisecondCalculation = (pi["end"] - pi["start"]).total_seconds() * 1000

print(f"50000자리의 원주율을 구하는데 약 {round(millisecondCalculation)}ms가 걸렸습니다.")
