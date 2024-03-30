import math
import random
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols,diff

k = 9 * 10**9




class Cestica:
    def __init__(self, pozicija, brzina, masa, naelektrisanje):
        self._pozicija = pozicija
        self._brzina = brzina
        self._masa = masa
        self._naelektrisanje = naelektrisanje

    @property
    def pozicija(self):
        return self._pozicija

    @pozicija.setter
    def pozicija(self, nova_pozicija):
        self._pozicija = nova_pozicija

    @property
    def brzina(self):
        return self._brzina

    @brzina.setter
    def brzina(self, nova_brzina):
        self._brzina = nova_brzina


    def __str__(self):
        return f"Čestica na poziciji {self._pozicija}, brzina {self._brzina}, masa {self._masa}, naelektrisanje {self._naelektrisanje}"

    def azuriranje_pozicije(self, t):
        self.pozicija = Interakcija.Ojlerov_algoritam(self, t)


class Interakcija:
    def rastojanje(cestica1, cestica2):
        x1, y1 = cestica1._pozicija
        x2, y2 = cestica2._pozicija
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def Lennard_Jonesov_potencijal(cestica1, cestica2, epsilon, sigma):
        r = Interakcija.rastojanje(cestica1, cestica2)
        V = 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6)
        return diff(V, r)

    def Kulonov_zakon(cestica1, cestica2):
        r = Interakcija.rastojanje(cestica1, cestica2)
        x1, y1 = cestica1._pozicija
        x2, y2 = cestica2._pozicija
        f = k * abs(cestica1._naelektrisanje * cestica2._naelektrisanje) / (r**3)
       
        fx = f * abs(x2 - x1)
        fy = f * abs(y2 - y1)
        return(fx,fy)
       

    def sila(cestica1, cestica2):
        if cestica1._naelektrisanje == 0 and cestica2._naelektrisanje == 0:
            return Interakcija.Lennard_Jonesov_potencijal(cestica1, cestica2)
        else:
            return Interakcija.Kulonov_zakon(cestica1, cestica2)

    @staticmethod
    def ubrzanje(cestica,cestice):
        ukupna_sila_x, ukupna_sila_y = Interakcija.ukupna_sila(cestica, cestice)
        ax = ukupna_sila_x / cestica._masa
        ay = ukupna_sila_y / cestica._masa
        return (ax, ay)
    
    @staticmethod
    def ukupna_sila(cestica, ostale_cestice):
        ukupna_sila_x = 0
        ukupna_sila_y = 0

        for druga_cestica in ostale_cestice:
            if cestica != druga_cestica:
                sila_između_x, sila_između_y = Interakcija.sila(cestica, druga_cestica)
                pravac = np.array(druga_cestica._pozicija) - np.array(cestica._pozicija)
                normiran_pravac = pravac / np.linalg.norm(pravac)

                sila_x = sila_između_x * normiran_pravac[0]
                sila_y = sila_između_y * normiran_pravac[1]

                ukupna_sila_x += sila_x
                ukupna_sila_y += sila_y

        return ukupna_sila_x, ukupna_sila_y
    @staticmethod
    def Ojlerov_algoritam(cestica, t):
        x, y = cestica._pozicija
        vx, vy = cestica._brzina

        x += vx * t
        y += vy * t

        return (x, y)


class Simulacija:
    def __init__(self, broj_cestica, sirina_okvira, visina_okvira, trajanje):
        self.broj_cestica = broj_cestica
        self.sirina_okvira = sirina_okvira
        self.visina_okvira = visina_okvira
        self.trajanje_animacije = trajanje
        self.cestice = self.inicijalizacija_cestica()

    def inicijalizacija_cestica(self):
        cestice = []
        for _ in range(self.broj_cestica):
          pozicija = [random.uniform(0, self.sirina_okvira), random.uniform(0, self.visina_okvira)]
          brzina = (random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9))  
          masa = random.uniform(0.1, 10)
          naelektrisanje = 150 * 10 ** -6#10**-6
          cestica = Cestica(pozicija, brzina, masa, naelektrisanje)
          cestice.append(cestica)
        return cestice
    
    def check_wall_collisions(self):
      for cestica in self.cestice:
        if cestica.pozicija[0] <= 0 or cestica.pozicija[0] >= self.sirina_okvira:
            cestica.brzina = (-cestica.brzina[0], cestica.brzina[1])  
        if cestica.pozicija[1] <= 0 or cestica.pozicija[1] >= self.visina_okvira:
            cestica.brzina = (cestica.brzina[0], -cestica.brzina[1])



    def azuriraj_interakcije(self, dt):
        for i in range(len(self.cestice)):
            #for j in range(i+1, len(self.cestice)):
            for j in range(len(self.cestice)):
                cestica1 = self.cestice[i]
                cestica2 = self.cestice[j]

                if cestica1._naelektrisanje != 0 and cestica2._naelektrisanje != 0:
                    r = Interakcija.rastojanje(cestica1, cestica2)
                    Fx, Fy = Interakcija.Kulonov_zakon(cestica1, cestica2)
                    a1 = Fx / cestica1._masa
                    a2 = Fy / cestica1._masa
                    vx, vy = cestica1._brzina
                    vx += a1* dt
                    vy += a2 * dt
                    cestica1._brzina = (vx, vy)
                    a12 = Fx / cestica2._masa
                    a22 = Fy / cestica2._masa
                    vx2, vy2 = cestica2._brzina
                    vx2 += a12* dt
                    vy2 += a22 * dt
                    cestica2._brzina = (vx2, vy2)


    def azuriraj_pozicije(self, dt):
        self.azuriraj_interakcije(dt)
        self.check_wall_collisions()
        for cestica in self.cestice:
            nova_pozicija = Interakcija.Ojlerov_algoritam(cestica, dt)
            cestica._pozicija = nova_pozicija 



    def pokreni_simulaciju(self):
        dt = 0.1
        broj_koraka = int(self.trajanje_animacije / dt) 
        izabrana_cestica = self.cestice[0]

        plt.figure()  

        for korak in range(broj_koraka):
            self.azuriraj_pozicije(dt)
            self.vizualizuj()

            
            print(f'Korak {korak+1}: Pozicija: {izabrana_cestica.pozicija}, Brzina: {izabrana_cestica.brzina}')
            plt.pause(0.01)  
            plt.draw() 

        plt.show()


      
      
    def vizualizuj(self):
      plt.clf()
      x_positions = [cestica._pozicija[0] for cestica in self.cestice]
      y_positions = [cestica._pozicija[1] for cestica in self.cestice]

      plt.scatter(x_positions, y_positions, marker='o', color='blue')

      plt.title('Simulacija dinamike čestica')
      plt.xlabel('X koordinata')
      plt.ylabel('Y koordinata')

    
      plt.xlim(0, self.sirina_okvira)
      plt.ylim(0, self.visina_okvira)

      plt.grid(True)
      plt.draw()
      



simulacija = Simulacija(30, 30, 30, 10)
simulacija.pokreni_simulaciju()

