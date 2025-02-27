p=int(input("Ingrese el costo del producto: "))
d=int(input("Ingrese la cantidad de dinero con la que paga: "))
c=d-p
mil=c//1000
if mil==0:
    quinientos=c//500
    if quinientos==0:
        docientos=c//200
        if docientos==0:
            cien=c//100
            if cien==0:
                cincuenta=c//50
                if cincuenta==0:
                    veinte=c//20
                    if veinte==0:
                        diez=c//10
                        if diez==0:
                            cinco=c//5
                            if cinco==0:
                                dos=c//2
                                if dos==0:
                                    uno=c//1
                                    r=r%1
                                else:
                                    r=c%2
                                    uno=r//1
                                    r=r%1
                            else:
                                r=c%5
                                dos=r//2
                                r=r%2
                                uno=r//1
                                r=r%1
                        else:
                            r=c%10
                            cinco=r//5
                            r=r%5
                            dos=r//2
                            r=r%2
                            uno=r//1
                            r=r%1
                    else:
                        r=c%20
                        diez=r//10
                        r=r%10
                        cinco=r//5
                        r=r%5
                        dos=r//2
                        r=r%2
                        uno=r//1
                        r=r%1
                else:
                    r=c%50
                    veinte=r//20
                    r=r%20
                    diez=r//10
                    r=r%10
                    cinco=r//5
                    r=r%5
                    dos=r//2
                    r=r%2
                    uno=r//1
                    r=r%1
            else:
                r=c%100
                cincuenta=r//50
                r=r%50
                veinte=r//20
                r=r%20
                diez=r//10
                r=r%10
                cinco=r//5
                r=r%5
                dos=r//2
                r=r%2
                uno=r//1
                r=r%1
        else:
            r=c%200
            cien=r//100
            r=r%100
            cincuenta=r//50
            r=r%50
            veinte=r//20
            r=r%20
            diez=r//10
            r=r%10
            cinco=r//5
            r=r%5
            dos=r//2
            r=r%2
            uno=r//1
            r=r%1
    else:
        r=c%500
        docientos=r//200
        r=r%200
        cien=r//100
        r=r%100
        cincuenta=r//50
        r=r%50
        veinte=r//20
        r=r%20
        diez=r//10
        r=r%10
        cinco=r//5
        r=r%5
        dos=r//2
        r=r%2
        uno=r//1
        r=r%1
else:
    r=c%1000
    quinientos=r//200
    r=r%200
    cien=r//100
    r=r%100
    cincuenta=r//50
    r=r%50
    veinte=r//20
    r=r%20
    diez=r//10
    r=r%10
    cinco=r//5
    r=r%5
    dos=r//2
    r=r%2
    uno=r//1
    r=r%1
        
print("Entregue:\n"+str(mil)+"mil\n"+str(quinientos)+" quinientos\n"+str(docientos)+" docientos\n"+str(cien)+" cien\n"+str(cincuenta)+" cincuenta\n"+str(veinte)+" veinte\n"+str(diez)+" diez\n"+str(cinco)+" cinco\n"+str(dos)+" dos\n"+str(uno)+" uno")
        
