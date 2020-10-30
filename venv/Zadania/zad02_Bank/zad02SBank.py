import Zadania.zad02_Bank.Account as Account

if __name__ == '__main__':
    a1 = Account.account("Jan", "Kowalski", "77777788888", 1000, 2000);
    a2 = Account.account("Piotr", "Nowak", "2231231412", 22000, 1000);
    a3 = Account.account("Marta", "Zielinska", "7772123122", 500000, 100000);
    a4 = Account.account("Jacek", "Sasin", "111111111", 20, 7000000);
    print(a1);
    a1.wplac(10000);
    print(a1.srodki);

    try:
        a1.wyplac(13001);
    except Exception as e:
        print(e);

    print(a1.srodki);


    listaKont = []
    listaKont.append(a1);
    listaKont.append(a2);
    listaKont.append(a3);
    listaKont.append(a4);

    for x in listaKont:
        print(x);


