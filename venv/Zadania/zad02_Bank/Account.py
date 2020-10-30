class account:

    srodki=0
    maxDebet =0;
    imie="";
    nazwisko="";
    pesel="";

    def __init__(self, imie, nazwisko, pesel, srodki, maxDebet):
        self.imie = imie;
        self.nazwisko = nazwisko;
        self.pesel = pesel;
        self.srodki = srodki;
        self.maxDebet = maxDebet;


    def __str__(self):
        return f'Konto={self.imie}||{self.nazwisko}||{self.pesel}||suma:{self.srodki}||' \
               f'max.debet:{self.maxDebet}'


    def wyplac(self, wartosc):
        if(abs(self.srodki - wartosc)<self.maxDebet):
            self.srodki = self.srodki - wartosc;
        else:
            raise Exception("Przekroczony debet")


    def wplac(self, wartosc):
        self.srodki = self.srodki + wartosc;


