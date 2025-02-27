import datetime as dt
current_date=dt.date.today()
print("Dia: "+str(current_date.day))
print("Mes: "+str(current_date.month))
print("Ano: "+str(current_date.year))
anoact=int(current_date.year)
mesact=int(current_date.month)
diaact=int(current_date.day)

anonac=int(input("¿En que año naciste? "))
mesnac=int(input("Inserta el numero del mes nacimiento? "))
dianac=int(input("Inserta el numero del dia de nacimiento? "))
if (anoact>=anonac and mesact<mesnac and diaact<dianac):
    ano=(anoact-anonac)-1
    mes=(13-mesnac)
    if mesnac==1:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==2:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==3:
        dias=28-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==4:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==5:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==6:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==7:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==8:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==9:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==10:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==11:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==12:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
if(anoact==anonac and mesact==mesnac and diaact>dianac):
    dias=diaact-dianac
    print(f"años:cero mai meses: nading dias: {dias}")
if(anoact>anonac and mesact>mesnac and diaact==dianac):
    ano=(anoact-anonac)
    mes=(mesact-mesnac)
    print(f"año: {ano} mes: {mes} dias: mañana haces un dia papirrin")
if(anoact==anonac and mesact==mesnac and diaact==dianac):
    print("Happy ferti chiquilin")
if(anoact<anonac):
    print("tus papis tendran acción muy pronto...")
if(anoact>anonac and mesact==mesnac and diaact>dianac):
    ano=(anoact-anonac)
    dias=diaact-dianac
    print(f"tienes: {ano}  meses: aun no chiquitin dias: {dias}")
if(anoact>anonac and mesact==mesnac and diaact<dianac):
    ano=(anoact-anonac)-1
    mes=(13-mesnac)
    if mesnac==1:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    if mesnac==2:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==3:
        dias=28-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==4:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==5:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==6:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==7:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==8:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==9:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==10:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==11:
        dias=31-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    elif mesnac==12:
        dias=30-(dianac-diaact)
        print(f"año: {ano} mes: {mes} dias: {dias}")
    

