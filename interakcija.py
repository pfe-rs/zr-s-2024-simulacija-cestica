import math
from sympy import symbols, diff
k = 9 * 10**9
class Interakcija():
    def rastojanje(cestica1, cestica2):
        x1, y1 = cestica1._pozicija
        x2, y2 = cestica2._pozicija
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def Kulonov_zakon(cestica1, cestica2):
        r = Interakcija.rastojanje(cestica1, cestica2)
        x1, y1 = cestica1._pozicija
        x2, y2 = cestica2._pozicija
        f = k * abs(cestica1._naelektrisanje * cestica2._naelektrisanje) / (r**3)
        fx = f * abs(x2 - x1)
        fy = f * abs(y2 - y1)
        return (fx, fy)


    def sila(cestica1, cestica2):
        return Interakcija.Kulonov_zakon(cestica1, cestica2)

    def ubrzanje(cestica, sila):
        fx, fy = sila
        ax = fx / cestica._masa
        ay = fy / cestica._masa
        return (ax, ay)
    
    def ukupna_sila(sile):
        x = 0
        y = 0
        for fx, fy in sile:
            x += fx
            y += fy

        return (x, y) 

    def Ojlerov_algoritam(cestica, t):
        x, y = cestica._pozicija
        vx, vy = cestica._brzina

        x += vx * t
        y += vy * t

        return (x, y)
    
