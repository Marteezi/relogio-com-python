import time

s = 0
m = 0
h = 0

while True:
    if s != 60:
            s += 1
            time.sleep(1.0)
    else:
        m += 1
        s = 0
        if m == 60:
             m = 0
             s = 0
             h += 1
        if h == 24:
                s = 0
                m = 0
                h = 0

    segundos = "{:02}".format(s)
    minutos = "{:02}".format(m)
    horas = "{:02}".format(h)

    print("\r{}:{}:{}".format(horas, minutos, segundos), end="")
