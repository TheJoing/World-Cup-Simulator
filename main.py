import random
from time import sleep


class Sele:
    def __init__(self, nome, nome_sigla, forca):
        self.nome = nome
        self.nome_sigla = nome_sigla
        self.forca = forca
        self.gol = 0
        self.pontos = 0
        self.pontos1 = 0
        self.pontos2 = 0
        self.pontos3 = 0
        self.pontos_12 = 0
        self.pontos_23 = 0
        self.pontos_13 = 0
        self.saldo = 0
        self.saldo_12 = 0
        self.saldo_13 = 0
        self.saldo_23 = 0
        self.gols_feitos = 0
        self.gols_feitos_12 = 0
        self.gols_feitos_13 = 0
        self.gols_feitos_23 = 0
        self.primeiro = False
        self.segundo = False
        self.terceiro = False
        self.quarto = False
        self.pla1 = 0
        self.pla2 = 0
        self.pla3 = 0
        self.pla4 = 0
        self.pen4 = 0
        self.pla5 = 0
        self.pen5 = 0
        self.pla6 = 0
        self.pen6 = 0


def aleatorizador(z):
    if z[0] == 1:
        return [n1, s1, f1]
    elif z[0] == 2:
        return [n2222, s2, f2]
    elif z[0] == 3:
        return [n3, s3, f3]
    elif z[0] == 4:
        return [n4, s4, f4]
    elif z[0] == 5:
        return [n5, s5, f5]
    elif z[0] == 6:
        return [n6, s6, f6]
    elif z[0] == 7:
        return [n7, s7, f7]
    elif z[0] == 8:
        return [n8, s8, f8]
    elif z[0] == 9:
        return [n9, s9, f9]
    elif z[0] == 10:
        return [n10, s10, f10]
    elif z[0] == 11:
        return [n11, s11, f11]
    elif z[0] == 12:
        return [n12, s12, f12]
    elif z[0] == 13:
        return [n13, s13, f13]
    elif z[0] == 14:
        return [n14, s14, f14]
    elif z[0] == 15:
        return [n15, s15, f15]
    elif z[0] == 16:
        return [n16, s16, f16]
    elif z[0] == 17:
        return [n17, s17, f17]
    elif z[0] == 18:
        return [n18, s18, f18]
    elif z[0] == 19:
        return [n19, s19, f19]
    elif z[0] == 20:
        return [n20, s20, f20]
    elif z[0] == 21:
        return [n21, s21, f21]
    elif z[0] == 22:
        return [n22, s22, f22]
    elif z[0] == 23:
        return [n23, s23, f23]
    elif z[0] == 24:
        return [n24, s24, f24]
    elif z[0] == 25:
        return [n25, s25, f25]
    elif z[0] == 26:
        return [n26, s26, f26]
    elif z[0] == 27:
        return [n27, s27, f27]
    elif z[0] == 28:
        return [n28, s28, f28]
    elif z[0] == 29:
        return [n29, s29, f29]
    elif z[0] == 30:
        return [n30, s30, f30]
    elif z[0] == 31:
        return [n31, s31, f31]
    elif z[0] == 32:
        return [n32, s32, f32]


def removedor():
    aleatoto = random.choices(listaa23)
    listaa23.remove(aleatoto[0])
    return aleatorizador(aleatoto)


quertempo = int(input("Digite quantos segundo quer que dure o jogo (digite somente o número) \n"))
x = quertempo/90
querforca = input("Se quiser a força padrão digite: p / Se quiser grupos aleatórios digite a."
                  "\nCaso queira grupos normais e escolher a força pressione enter \n")


if querforca.lower() == "p":
    sel1 = Sele("Catar", "CAT", 12)
    sel2 = Sele("Holanda", "HOL", 38)
    sel3 = Sele("Senegal", "SEN", 29)
    sel4 = Sele("Equador", "EQU", 26)
    sel5 = Sele("Inglaterra", "ING", 37)
    sel6 = Sele("País de Gales", "GAL", 25)
    sel7 = Sele("Estados Unidos", "EUA", 24)
    sel8 = Sele("Irã", "IRA", 20)
    sel9 = Sele("Argentina", "ARG", 43)
    sel10 = Sele("Polônia", "POL", 27)
    sel11 = Sele("México", "MEX", 29)
    sel12 = Sele("Arábia Saudita", "SAU", 15)
    sel13 = Sele("Dinamarca", "DIN", 37)
    sel14 = Sele("Australia", "AUS", 20)
    sel15 = Sele("França", "FRA", 42)
    sel16 = Sele("Tunísia", "TUN", 15)
    sel17 = Sele("Alemanha", "ALE", 40)
    sel18 = Sele("Costa Rica", "COS", 22)
    sel19 = Sele("Espanha", "ESP", 35)
    sel20 = Sele("Japão", "JAP", 26)
    sel21 = Sele("Marrocos", "MAR", 23)
    sel22 = Sele("Canada", "CAN", 25)
    sel23 = Sele("Bélgica", "BEL", 39)
    sel24 = Sele("Croacia", "CRO", 34)
    sel25 = Sele("Suiça", "SUI", 32)
    sel26 = Sele("Sérvia", "SER", 30)
    sel27 = Sele("Brasil", "BRA", 44)
    sel28 = Sele("Camarões", "CAM", 18)
    sel29 = Sele("Uruguai", "URU", 31)
    sel30 = Sele("Gana", "GAN", 17)
    sel31 = Sele("Portugal", "POR", 34)
    sel32 = Sele("Coreia do Sul", "COR", 21)
else:
    f1 = int(input("Digite a força do Catar: {um número de 1 a 50} \n"))
    if f1 == 0:
        n1 = input("Digite o nome do time/seleção: \n")
        s1 = input("Digite o nome da sigla do time/seleção: \n")
        f1 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n1 = "Catar"
        s1 = "CAT"
    f2 = int(input("Digite a força do Holanda: {um número de 1 a 50} \n"))
    if f2 == 0:
        n2222 = input("Digite o nome do time/seleção: \n")
        s2 = input("Digite o nome da sigla do time/seleção: \n")
        f2 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n2222 = "Holanda"
        s2 = "HOL"
    f3 = int(input("Digite a força do Senegal: {um número de 1 a 50} \n"))
    if f3 == 0:
        n3 = input("Digite o nome do time/seleção: \n")
        s3 = input("Digite o nome da sigla do time/seleção: \n")
        f3 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n3 = "Senegal"
        s3 = "SEN"
    f4 = int(input("Digite a força do Equador: {um número de 1 a 50} \n"))
    if f4 == 0:
        n4 = input("Digite o nome do time/seleção: \n")
        s4 = input("Digite o nome da sigla do time/seleção: \n")
        f4 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n4 = "Equador"
        s4 = "EQU"
    f5 = int(input("Digite a força do Inglaterra: {um número de 1 a 50} \n"))
    if f5 == 0:
        n5 = input("Digite o nome do time/seleção: \n")
        s5 = input("Digite o nome da sigla do time/seleção: \n")
        f5 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n5 = "Inglaterra"
        s5 = "ING"
    f6 = int(input("Digite a força do País de Gales: {um número de 1 a 50} \n"))
    if f6 == 0:
        n6 = input("Digite o nome do time/seleção: \n")
        s6 = input("Digite o nome da sigla do time/seleção: \n")
        f6 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n6 = "País de Gales"
        s6 = "GAL"
    f7 = int(input("Digite a força do Estados Unidos: {um número de 1 a 50} \n"))
    if f7 == 0:
        n7 = input("Digite o nome do time/seleção: \n")
        s7 = input("Digite o nome da sigla do time/seleção: \n")
        f7 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n7 = "Estados Unidos"
        s7 = "EUA"
    f8 = int(input("Digite a força do Irã: {um número de 1 a 50} \n"))
    if f8 == 0:
        n8 = input("Digite o nome do time/seleção: \n")
        s8 = input("Digite o nome da sigla do time/seleção: \n")
        f8 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n8 = "Irã"
        s8 = "IRA"
    f9 = int(input("Digite a força do Argentina: {um número de 1 a 50} \n"))
    if f9 == 0:
        n9 = input("Digite o nome do time/seleção: \n")
        s9 = input("Digite o nome da sigla do time/seleção: \n")
        f9 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n9 = "Argentina"
        s9 = "ARG"
    f10 = int(input("Digite a força do Polônia: {um número de 1 a 50} \n"))
    if f10 == 0:
        n10 = input("Digite o nome do time/seleção: \n")
        s10 = input("Digite o nome da sigla do time/seleção: \n")
        f10 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n10 = "Polônia"
        s10 = "POL"
    f11 = int(input("Digite a força do México: {um número de 1 a 50} \n"))
    if f11 == 0:
        n11 = input("Digite o nome do time/seleção: \n")
        s11 = input("Digite o nome da sigla do time/seleção: \n")
        f11 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n11 = "México"
        s11 = "MEX"
    f12 = int(input("Digite a força do Arábia Saudita: {um número de 1 a 50} \n"))
    if f12 == 0:
        n12 = input("Digite o nome do time/seleção: \n")
        s12 = input("Digite o nome da sigla do time/seleção: \n")
        f12 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n12 = "Arábia Saudita"
        s12 = "SAU"
    f13 = int(input("Digite a força do Dinamarca: {um número de 1 a 50} \n"))
    if f13 == 0:
        n13 = input("Digite o nome do time/seleção: \n")
        s13 = input("Digite o nome da sigla do time/seleção: \n")
        f13 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n13 = "Dinamarca"
        s13 = "DIN"
    f14 = int(input("Digite a força do Australia: {um número de 1 a 50} \n"))
    if f14 == 0:
        n14 = input("Digite o nome do time/seleção: \n")
        s14 = input("Digite o nome da sigla do time/seleção: \n")
        f14 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n14 = "Australia"
        s14 = "AUS"
    f15 = int(input("Digite a força do França: {um número de 1 a 50} \n"))
    if f15 == 0:
        n15 = input("Digite o nome do time/seleção: \n")
        s15 = input("Digite o nome da sigla do time/seleção: \n")
        f15 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n15 = "França"
        s15 = "FRA"
    f16 = int(input("Digite a força do Tunísia: {um número de 1 a 50} \n"))
    if f16 == 0:
        n16 = input("Digite o nome do time/seleção: \n")
        s16 = input("Digite o nome da sigla do time/seleção: \n")
        f16 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n16 = "Tunísia"
        s16 = "TUN"
    f17 = int(input("Digite a força do Alemanha: {um número de 1 a 50} \n"))
    if f17 == 0:
        n17 = input("Digite o nome do time/seleção: \n")
        s17 = input("Digite o nome da sigla do time/seleção: \n")
        f17 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n17 = "Alemanha"
        s17 = "ALE"
    f18 = int(input("Digite a força do Costa Rica: {um número de 1 a 50} \n"))
    if f18 == 0:
        n18 = input("Digite o nome do time/seleção: \n")
        s18 = input("Digite o nome da sigla do time/seleção: \n")
        f18 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n18 = "Costa Rica"
        s18 = "COS"
    f19 = int(input("Digite a força do Espanha: {um número de 1 a 50} \n"))
    if f19 == 0:
        n19 = input("Digite o nome do time/seleção: \n")
        s19 = input("Digite o nome da sigla do time/seleção: \n")
        f19 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n19 = "Espanha"
        s19 = "ESP"
    f20 = int(input("Digite a força do Japão: {um número de 1 a 50} \n"))
    if f20 == 0:
        n20 = input("Digite o nome do time/seleção: \n")
        s20 = input("Digite o nome da sigla do time/seleção: \n")
        f20 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n20 = "Japão"
        s20 = "JAP"
    f21 = int(input("Digite a força do Marrocos: {um número de 1 a 50} \n"))
    if f21 == 0:
        n21 = input("Digite o nome do time/seleção: \n")
        s21 = input("Digite o nome da sigla do time/seleção: \n")
        f21 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n21 = "Marrocos"
        s21 = "MAR"
    f22 = int(input("Digite a força do Canada: {um número de 1 a 50} \n"))
    if f22 == 0:
        n22 = input("Digite o nome do time/seleção: \n")
        s22 = input("Digite o nome da sigla do time/seleção: \n")
        f22 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n22 = "Canada"
        s22 = "CAN"
    f23 = int(input("Digite a força do Bélgica: {um número de 1 a 50} \n"))
    if f23 == 0:
        n23 = input("Digite o nome do time/seleção: \n")
        s23 = input("Digite o nome da sigla do time/seleção: \n")
        f23 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n23 = "Bélgica"
        s23 = "BEL"
    f24 = int(input("Digite a força do Croacia: {um número de 1 a 50} \n"))
    if f24 == 0:
        n24 = input("Digite o nome do time/seleção: \n")
        s24 = input("Digite o nome da sigla do time/seleção: \n")
        f24 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n24 = "Croacia"
        s24 = "CRO"
    f25 = int(input("Digite a força do Suiça: {um número de 1 a 50} \n"))
    if f25 == 0:
        n25 = input("Digite o nome do time/seleção: \n")
        s25 = input("Digite o nome da sigla do time/seleção: \n")
        f25 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n25 = "Suiça"
        s25 = "SUI"
    f26 = int(input("Digite a força do Sérvia: {um número de 1 a 50} \n"))
    if f26 == 0:
        n26 = input("Digite o nome do time/seleção: \n")
        s26 = input("Digite o nome da sigla do time/seleção: \n")
        f26 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n26 = "Sérvia"
        s26 = "SER"
    f27 = int(input("Digite a força do Brasil: {um número de 1 a 50} \n"))
    if f27 == 0:
        n27 = input("Digite o nome do time/seleção: \n")
        s27 = input("Digite o nome da sigla do time/seleção: \n")
        f27 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n27 = "Brasil"
        s27 = "BRA"
    f28 = int(input("Digite a força do Camarões: {um número de 1 a 50} \n"))
    if f28 == 0:
        n28 = input("Digite o nome do time/seleção: \n")
        s28 = input("Digite o nome da sigla do time/seleção: \n")
        f28 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n28 = "Camarões"
        s28 = "CAM"
    f29 = int(input("Digite a força do Uruguai: {um número de 1 a 50} \n"))
    if f29 == 0:
        n29 = input("Digite o nome do time/seleção: \n")
        s29 = input("Digite o nome da sigla do time/seleção: \n")
        f29 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n29 = "Uruguai"
        s29 = "URU"
    f30 = int(input("Digite a força do Gana: {um número de 1 a 50} \n"))
    if f30 == 0:
        n30 = input("Digite o nome do time/seleção: \n")
        s30 = input("Digite o nome da sigla do time/seleção: \n")
        f30 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n30 = "Gana"
        s30 = "GAN"
    f31 = int(input("Digite a força do Portugal: {um número de 1 a 50} \n"))
    if f31 == 0:
        n31 = input("Digite o nome do time/seleção: \n")
        s31 = input("Digite o nome da sigla do time/seleção: \n")
        f31 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n31 = "Portugal"
        s31 = "POR"
    f32 = int(input("Digite a força do Coreia do Sul: {um número de 1 a 50} \n"))
    if f32 == 0:
        n32 = input("Digite o nome do time/seleção: \n")
        s32 = input("Digite o nome da sigla do time/seleção: \n")
        f32 = int(input("Digite a força do do time/seleção: {um número de 1 a 50} \n"))
    else:
        n32 = "Coreia do Sul"
        s32 = "COR"
    if querforca.lower() == "a":
        listaa23 = []
        for paq in range(1, 33):
            listaa23.append(paq)
        aa = removedor()
        sel1 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel2 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel3 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel4 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel5 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel6 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel7 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel8 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel9 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel10 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel11 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel12 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel13 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel14 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel15 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel16 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel17 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel18 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel19 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel20 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel21 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel22 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel23 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel24 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel25 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel26 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel27 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel28 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel29 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel30 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel31 = Sele(aa[0], aa[1], aa[2])
        aa = removedor()
        sel32 = Sele(aa[0], aa[1], aa[2])
    else:
        sel1 = Sele(n1, s1, f1)
        sel2 = Sele(n2222, s2, f2)
        sel3 = Sele(n3, s3, f3)
        sel4 = Sele(n4, s4, f4)
        sel5 = Sele(n5, s5, f5)
        sel6 = Sele(n6, s6, f6)
        sel7 = Sele(n7, s7, f7)
        sel8 = Sele(n8, s8, f8)
        sel9 = Sele(n9, s9, f9)
        sel10 = Sele(n10, s10, f10)
        sel11 = Sele(n11, s11, f11)
        sel12 = Sele(n12, s12, f12)
        sel13 = Sele(n13, s13, f13)
        sel14 = Sele(n14, s14, f14)
        sel15 = Sele(n15, s15, f15)
        sel16 = Sele(n16, s16, f16)
        sel17 = Sele(n17, s17, f17)
        sel18 = Sele(n18, s18, f18)
        sel19 = Sele(n19, s19, f19)
        sel20 = Sele(n20, s20, f20)
        sel21 = Sele(n21, s21, f21)
        sel22 = Sele(n22, s22, f22)
        sel23 = Sele(n23, s23, f23)
        sel24 = Sele(n24, s24, f24)
        sel25 = Sele(n25, s25, f25)
        sel26 = Sele(n26, s26, f26)
        sel27 = Sele(n27, s27, f27)
        sel28 = Sele(n28, s28, f28)
        sel29 = Sele(n29, s29, f29)
        sel30 = Sele(n30, s30, f30)
        sel31 = Sele(n31, s31, f31)
        sel32 = Sele(n32, s32, f32)


def jogo(time1, time2, pro, num):
    time1.gol = 0
    time2.gol = 0
    golo = [1, 0]
    prob = time1.forca
    prob2 = time2.forca
    cont = 100-prob
    cont2 = 100-prob2
    gol11 = random.randint(1, 90)
    gol12 = random.randint(1, 90)
    while gol12 == gol11:
        gol12 = random.randint(1, 90)
    gol13 = random.randint(1, 90)
    while gol13 == gol11 and gol12:
        gol13 = random.randint(1, 90)
    gol14 = random.randint(1, 90)
    while gol13 == gol11 and gol12 and gol13:
        gol13 = random.randint(1, 90)
    gol15 = random.randint(1, 95)
    while gol15 == gol11 and gol12 and gol13 and gol14:
        gol15 = random.randint(1, 95)
    gol21 = random.randint(1, 90)
    gol22 = random.randint(1, 90)
    while gol22 == gol21:
        gol22 = random.randint(1, 90)
    gol23 = random.randint(1, 90)
    while gol23 == gol21 and gol22:
        gol23 = random.randint(1, 90)
    gol24 = random.randint(1, 90)
    while gol23 == gol21 and gol22 and gol23:
        gol23 = random.randint(1, 90)
    gol25 = random.randint(1, 95)
    while gol25 == gol21 and gol22 and gol23 and gol24:
        gol25 = random.randint(1, 95)
    print(f'Jogo entre {time1.nome} e {time2.nome}')
    for z in range(1, 6):
        if z == 5:
            prob += 7
            prob2 += 7
        n = random.choices(golo, weights=[prob, cont])
        n2 = random.choices(golo, weights=[prob2, cont2])
        if n == [1]:
            time1.gol += 1
        else:
            if z == 1:
                gol11 = 0
            elif z == 2:
                gol12 = 0
            elif z == 3:
                gol13 = 0
            elif z == 4:
                gol14 = 0
            elif z == 5:
                gol15 = 0
        if n2 == [1]:
            time2.gol += 1
        else:
            if z == 1:
                gol21 = 0
            elif z == 2:
                gol22 = 0
            elif z == 3:
                gol23 = 0
            elif z == 4:
                gol24 = 0
            elif z == 5:
                gol25 = 0
    sleep(1)
    extra = 90
    if gol25 > 90 or gol15 > 90:
        if gol25 > gol15:
            extra = gol25
        else:
            extra = gol15
    gols_1 = 0
    gols_2 = 0
    for tempo in range(1, extra+1):
        tem = 0
        if gol11 == tempo:
            print(f'{tempo}\' {time1.nome} fez um Gol!')
            gols_1 += 1
        elif gol12 == tempo:
            print(f'{tempo}\' {time1.nome} fez um Gol!')
            gols_1 += 1
        elif gol13 == tempo:
            print(f'{tempo}\' {time1.nome} fez um Gol!')
            gols_1 += 1
        elif gol14 == tempo:
            print(f'{tempo}\' {time1.nome} fez um Gol!')
            gols_1 += 1
        elif gol15 == tempo:
            print(f'{tempo}\' {time1.nome} fez um Gol!')
            gols_1 += 1
        else:
            tem += 1
        if gol21 == tempo:
            print(f'{tempo}\' {time2.nome} fez um Gol!')
            gols_2 += 1
        elif gol22 == tempo:
            print(f'{tempo}\' {time2.nome} fez um Gol!')
            gols_2 += 1
        elif gol23 == tempo:
            print(f'{tempo}\' {time2.nome} fez um Gol!')
            gols_2 += 1
        elif gol24 == tempo:
            print(f'{tempo}\' {time2.nome} fez um Gol!')
            gols_2 += 1
        elif gol25 == tempo:
            print(f'{tempo}\' {time2.nome} fez um Gol!')
            gols_2 += 1
        else:
            tem += 1
        if num > 5:
            sleep(2*x)
        else:
            sleep(x)
        if tem == 2:
            print(f'{tempo}\' {time1.nome_sigla} {gols_1} X {gols_2} {time2.nome_sigla}')
    print(f'{time1.nome} {time1.gol} X {time2.gol} {time2.nome}')
    sleep(3)
    if time1.gol > time2.gol:
        if num == 1:
            time1.pla1 = time1.gol
            time2.pla1 = time2.gol
        elif num == 2:
            time1.pla2 = time1.gol
            time2.pla2 = time2.gol
        elif num == 3:
            time1.pla3 = time1.gol
            time2.pla3 = time2.gol
        elif num == 4:
            quartas.append(time1)
            time1.pla4 = time1.gol
            time2.pla4 = time2.gol
        elif num == 5:
            semis.append(time1)
            time1.pla5 = time1.gol
            time2.pla5 = time2.gol
        elif num == 6:
            final.append(time1)
            time1.pla6 = time1.gol
            time2.pla6 = time2.gol
        return 3
    elif time2.gol > time1.gol:
        if num == 1:
            time1.pla1 = time1.gol
            time2.pla1 = time2.gol
        elif num == 2:
            time1.pla2 = time1.gol
            time2.pla2 = time2.gol
        elif num == 3:
            time1.pla3 = time1.gol
            time2.pla3 = time2.gol
        elif num == 4:
            quartas.append(time2)
            time1.pla4 = time1.gol
            time2.pla4 = time2.gol
        elif num == 5:
            semis.append(time2)
            time1.pla5 = time1.gol
            time2.pla5 = time2.gol
        elif num == 6:
            final.append(time2)
            time1.pla6 = time1.gol
            time2.pla6 = time2.gol
        return 0
    else:
        if pro is False:
            if num == 1:
                time1.pla1 = time1.gol
                time2.pla1 = time2.gol
            elif num == 2:
                time1.pla2 = time1.gol
                time2.pla2 = time2.gol
            elif num == 3:
                time1.pla3 = time1.gol
                time2.pla3 = time2.gol
            return 1
        else:
            prob -= 2
            prob2 -= 2
            gol16 = random.randint(91, 120)
            gol17 = random.randint(91, 125)
            while gol17 == gol16:
                gol17 = random.randint(91, 125)
            gol26 = random.randint(91, 120)
            gol27 = random.randint(91, 125)
            while gol27 == gol26:
                gol27 = random.randint(91, 125)
            print("Prorrogação:")
            sleep(3)
            for v in range(1, 3):
                if v == 2:
                    prob += 5
                    prob2 += 5
                n = random.choices(golo, weights=[prob, cont])
                n2 = random.choices(golo, weights=[prob2, cont2])
                if n == [1]:
                    time1.gol += 1
                else:
                    if v == 1:
                        gol16 = 0
                    elif v == 2:
                        gol17 = 0
                if n2 == [1]:
                    time2.gol += 1
                else:
                    if v == 1:
                        gol26 = 0
                    elif v == 2:
                        gol27 = 0
            extra = 120
            if gol26 > 120 or gol27 > 120:
                if gol26 > gol27:
                    extra = gol26
                else:
                    extra = gol27
            for tempo in range(91, extra+1):
                tem = 0
                if gol16 == tempo:
                    print(f'{tempo}\' {time1.nome} fez um Gol!')
                    gols_1 += 1
                elif gol17 == tempo:
                    print(f'{tempo}\' {time1.nome} fez um Gol!')
                    gols_1 += 1
                else:
                    tem += 1
                if gol26 == tempo:
                    print(f'{tempo}\' {time2.nome} fez um Gol!')
                    gols_2 += 1
                elif gol27 == tempo:
                    print(f'{tempo}\' {time2.nome} fez um Gol!')
                    gols_2 += 1
                else:
                    tem += 1
                if num > 5:
                    sleep(2*x)
                else:
                    sleep(x)
                if tem == 2:
                    print(f'{tempo}\' {time1.nome_sigla} {gols_1} X {gols_2} {time2.nome_sigla}')
            print(f'Pr: {time1.nome} {time1.gol} X {time2.gol} {time2.nome}')
            sleep(3)
            if time1.gol > time2.gol:
                if num == 4:
                    quartas.append(time1)
                    time1.pla4 = time1.gol
                    time2.pla4 = time2.gol
                elif num == 5:
                    semis.append(time1)
                    time1.pla5 = time1.gol
                    time2.pla5 = time2.gol
                elif num == 6:
                    final.append(time1)
                    time1.pla6 = time1.gol
                    time2.pla6 = time2.gol
                return 3
            elif time2.gol > time1.gol:
                if num == 4:
                    quartas.append(time2)
                    time1.pla4 = time1.gol
                    time2.pla4 = time2.gol
                elif num == 5:
                    semis.append(time2)
                    time1.pla5 = time1.gol
                    time2.pla5 = time2.gol
                elif num == 6:
                    final.append(time2)
                    time1.pla6 = time1.gol
                    time2.pla6 = time2.gol
                return 0
            else:
                prob += 10
                prob += 10
                penaltis = True
                cinco = True
                if num == 4:
                    time1.pla4 = time1.gol
                    time2.pla4 = time2.gol
                elif num == 5:
                    time1.pla5 = time1.gol
                    time2.pla5 = time2.gol
                elif num == 6:
                    time1.pla6 = time1.gol
                    time2.pla6 = time2.gol
                time1.gol = 0
                time2.gol = 0
                prob += 15
                prob2 += 15
                print("Penaltis:")
                sleep(3)
                while penaltis is True:
                    if cinco is True:
                        for v in range(1, 6):
                            n = random.choices(golo, weights=[prob, cont])
                            n2 = random.choices(golo, weights=[prob2, cont2])
                            if n == [1]:
                                time1.gol += 1
                                print(f'{time1.nome} marcou')
                            else:
                                print(f'{time1.nome} errou')
                            sleep(3)
                            if n2 == [1]:
                                time2.gol += 1
                                print(f'{time2.nome} marcou')
                            else:
                                print(f'{time2.nome} errou')
                            sleep(3)
                            print(f'Rodada {v}: {time1.nome} {time1.gol} X {time2.gol} {time2.nome}')
                            sleep(3)
                            if v == 3:
                                if time1.gol-time2.gol >= 3:
                                    break
                                elif time2.gol-time1.gol >= 3:
                                    break
                            elif v == 4:
                                if time1.gol-time2.gol >= 2:
                                    break
                                elif time2.gol-time1.gol >= 2:
                                    break
                            cinco = False
                    elif cinco is False:
                        for q in range(1, 2):
                            n = random.choices(golo, weights=[prob, cont])
                            n2 = random.choices(golo, weights=[prob2, cont2])
                            if n == [1]:
                                time1.gol += 1
                                print(f'{time1.nome} marcou')
                            else:
                                print(f'{time1.nome} errou')
                            sleep(3)
                            if n2 == [1]:
                                time2.gol += 1
                                print(f'{time2.nome} marcou')
                            else:
                                print(f'{time2.nome} errou')
                            sleep(3)
                    if time1.gol > time2.gol:
                        if num == 4:
                            quartas.append(time1)
                            time1.pen4 = time1.gol
                            time2.pen4 = time2.gol
                        elif num == 5:
                            semis.append(time1)
                            time1.pen5 = time1.gol
                            time2.pen5 = time2.gol
                        elif num == 6:
                            final.append(time1)
                            time1.pen6 = time1.gol
                            time2.pen6 = time2.gol
                        print(f'Pen: {time1.nome} {time1.gol} X {time2.gol} {time2.nome}')
                        return 3
                    elif time2.gol > time1.gol:
                        if num == 4:
                            quartas.append(time2)
                            time1.pen4 = time1.gol
                            time2.pen4 = time2.gol
                        elif num == 5:
                            semis.append(time2)
                            time1.pen5 = time1.gol
                            time2.pen5 = time2.gol
                        elif num == 6:
                            final.append(time2)
                            time1.pen6 = time1.gol
                            time2.pen6 = time2.gol
                        print(f'Pen: {time1.nome} {time1.gol} X {time2.gol} {time2.nome}')
                        return 0


def pontuacao(res, time3, time4, nu):
    time3.gols_feitos += time3.gol
    time4.gols_feitos += time4.gol
    time3.saldo += time3.gol - time4.gol
    time4.saldo += time4.gol - time3.gol
    if nu == 1:
        time3.saldo_12 += time3.gol - time4.gol
        time3.saldo_13 += time3.gol - time4.gol
        time4.saldo_12 += time4.gol - time3.gol
        time4.saldo_13 += time3.gol - time4.gol
        time3.gols_feitos_12 += time3.gol
        time3.gols_feitos_13 += time3.gol
        time4.gols_feitos_12 += time4.gol
        time4.gols_feitos_13 += time4.gol
    elif nu == 2:
        time3.saldo_12 += time3.gol - time4.gol
        time3.saldo_23 += time3.gol - time4.gol
        time4.saldo_12 += time4.gol - time3.gol
        time4.saldo_23 += time3.gol - time4.gol
        time3.gols_feitos_12 += time3.gol
        time3.gols_feitos_23 += time3.gol
        time4.gols_feitos_12 += time4.gol
        time4.gols_feitos_23 += time4.gol
    elif nu == 3:
        time3.saldo_23 += time3.gol - time4.gol
        time3.saldo_13 += time3.gol - time4.gol
        time4.saldo_23 += time4.gol - time3.gol
        time4.saldo_13 += time3.gol - time4.gol
        time3.gols_feitos_13 += time3.gol
        time3.gols_feitos_23 += time3.gol
        time4.gols_feitos_13 += time4.gol
        time4.gols_feitos_23 += time4.gol
    if res == 3:
        time3.pontos += 3
        if nu == 1:
            time3.pontos1 = 3
            time3.pontos_12 += 3
            time3.pontos_13 += 3
        elif nu == 2:
            time3.pontos2 = 3
            time3.pontos_12 += 3
            time3.pontos_23 += 3
        elif nu == 3:
            time3.pontos3 = 3
            time3.pontos_23 += 3
            time3.pontos_13 += 3
    elif res == 1:
        time3.pontos += 1
        time4.pontos += 1
        if nu == 1:
            time3.pontos1 = 1
            time4.pontos1 = 1
            time3.pontos_12 += 1
            time3.pontos_13 += 1
            time4.pontos_12 += 1
            time4.pontos_13 += 1
        elif nu == 2:
            time3.pontos2 = 1
            time4.pontos2 = 1
            time3.pontos_12 += 1
            time3.pontos_23 += 1
            time4.pontos_12 += 1
            time4.pontos_23 += 1
        elif nu == 3:
            time3.pontos3 = 1
            time4.pontos3 = 1
            time3.pontos_13 += 1
            time3.pontos_23 += 1
            time4.pontos_13 += 1
            time4.pontos_23 += 1
    else:
        time4.pontos += 3
        if nu == 1:
            time4.pontos1 = 3
            time4.pontos_12 += 3
            time4.pontos_13 += 3
        elif nu == 2:
            time4.pontos2 = 3
            time4.pontos_12 += 3
            time4.pontos_23 += 3
        elif nu == 3:
            time4.pontos3 = 3
            time4.pontos_13 += 3
            time4.pontos_23 += 3


def jogo_real(primeiro, segundo, num, mate):
    pq = jogo(primeiro, segundo, mate, num)
    if mate is False:
        pontuacao(pq, primeiro, segundo, num)


def desempate(tt1, tt2, tt3, tt4):
    n = 1
    if n == 1:
        if type(tt1) == int:
            arruma.append(0)
            if type(tt2) == int:
                arruma.append(0)
                if tt3.saldo > tt4.saldo:
                    arruma.append(1)
                    arruma.append(2)
                elif tt4.saldo > tt3.saldo:
                    arruma.append(2)
                    arruma.append(1)
                else:
                    n = 2
            elif type(tt3) == int:
                if tt2.saldo > tt4.saldo:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.saldo > tt2.saldo:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    n = 2
            elif type(tt4) == int:
                if tt2.saldo > tt3.saldo:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.saldo > tt2.saldo:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    n = 2
            else:
                if tt2.saldo > tt3.saldo:
                    if tt2.saldo > tt4.saldo:
                        arruma.append(1)
                        if tt3.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.saldo > tt3.saldo:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, 2, tt3, tt4)
                            elif tt1 == 4:
                                desempate(4, 1, tt3, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt2.saldo:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, 4, tt4)
                        elif tt1 == 4:
                            desempate(4, tt2, 3, tt4)
                        arruma[2] += 3
                elif tt3.saldo > tt2.saldo:
                    if tt3.saldo > tt4.saldo:
                        if tt2.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.saldo > tt2.saldo:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, tt2, 2, tt4)
                            elif tt1 == 4:
                                desempate(4, tt2, 1, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt3.saldo:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, 4, tt3, tt4)
                        elif tt1 == 4:
                            desempate(4, 3, tt3, tt4)
                        arruma[1] += 3
                else:
                    if tt2.saldo > tt4.saldo:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 4)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 3)
                        arruma[3] += 3
                    elif tt4.saldo > tt2.saldo:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 2)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 1)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 2
        elif type(tt2) == int:
            if type(tt3) == int:
                if tt1.saldo > tt4.saldo:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.saldo > tt1.saldo:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    n = 2
            elif type(tt4) == int:
                if tt1.saldo > tt3.saldo:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.saldo > tt1.saldo:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    n = 2
            else:
                if tt1.saldo > tt3.saldo:
                    if tt1.saldo > tt4.saldo:
                        arruma.append(1)
                        arruma.append(0)
                        if tt3.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.saldo > tt3.saldo:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(2, 1, tt3, tt4)
                            elif tt2 == 4:
                                desempate(1, 4, tt3, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt1.saldo:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, 4, tt4)
                        elif tt2 == 4:
                            desempate(tt1, 4, 3, tt4)
                        arruma[2] += 3
                elif tt3.saldo > tt1.saldo:
                    if tt3.saldo > tt4.saldo:
                        if tt1.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.saldo > tt1.saldo:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(tt1, 1, 2, tt4)
                            elif tt2 == 4:
                                desempate(tt1, 4, 1, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt3.saldo:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(2, 1, tt3, tt4)
                        elif tt2 == 4:
                            desempate(1, 4, tt3, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                else:
                    if tt1.saldo > tt4.saldo:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 4)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 3)
                        arruma[3] += 3
                    elif tt4.saldo > tt1.saldo:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 2)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 1)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 2
        elif type(tt3) == int:
            if type(tt4) == int:
                if tt1.saldo > tt2.saldo:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                elif tt2.saldo > tt1.saldo:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                else:
                    n = 2
            else:
                if tt1.saldo > tt2.saldo:
                    if tt1.saldo > tt4.saldo:
                        arruma.append(1)
                        if tt2.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.saldo > tt2.saldo:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(2, tt2, 1, tt4)
                            elif tt3 == 4:
                                desempate(1, tt2, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt1.saldo:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, 4, 1, tt4)
                        elif tt3 == 4:
                            desempate(tt1, 3, 4, tt4)
                        arruma[1] += 3
                elif tt2.saldo > tt1.saldo:
                    if tt2.saldo > tt4.saldo:
                        if tt1.saldo > tt4.saldo:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.saldo > tt1.saldo:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(tt1, 2, 1, tt4)
                            elif tt3 == 4:
                                desempate(tt1, 1, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.saldo > tt2.saldo:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(2, tt2, 1, tt4)
                        elif tt3 == 4:
                            desempate(1, tt2, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                else:
                    if tt1.saldo > tt4.saldo:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 4)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 3)
                        arruma[3] += 3
                    elif tt4.saldo > tt1.saldo:
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 2)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 1)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                    else:
                        n = 2
        elif type(tt4) == int:
            if tt1.saldo > tt2.saldo:
                if tt1.saldo > tt3.saldo:
                    arruma.append(1)
                    if tt2.saldo > tt3.saldo:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.saldo > tt2.saldo:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(2, tt2, tt3, 1)
                        elif tt4 == 4:
                            desempate(1, tt2, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.saldo > tt1.saldo:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, 4, tt3, 1)
                    elif tt4 == 4:
                        desempate(tt1, 3, tt3, 4)
                    arruma[1] += 3
            elif tt2.saldo > tt1.saldo:
                if tt2.saldo > tt3.saldo:
                    if tt1.saldo > tt3.saldo:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.saldo > tt1.saldo:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(tt1, 2, tt3, 1)
                        elif tt4 == 4:
                            desempate(tt1, 1, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.saldo > tt2.saldo:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(2, tt2, tt3, 1)
                    elif tt4 == 4:
                        desempate(1, tt2, tt3, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
            else:
                if tt1.saldo > tt3.saldo:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 4, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 3, 4)
                    arruma[2] += 3
                elif tt3.saldo > tt1.saldo:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 2, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 1, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
                else:
                    n = 2
    if n == 2:
        if type(tt1) == int:
            if type(tt2) == int:
                if tt3.gols_feitos > tt4.gols_feitos:
                    arruma.append(1)
                    arruma.append(2)
                elif tt4.gols_feitos > tt3.gols_feitos:
                    arruma.append(2)
                    arruma.append(1)
                else:
                    n = 3
            elif type(tt3) == int:
                if tt2.gols_feitos > tt4.gols_feitos:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.gols_feitos > tt2.gols_feitos:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    n = 3
            elif type(tt4) == int:
                if tt2.gols_feitos > tt3.gols_feitos:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.gols_feitos > tt2.gols_feitos:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    n = 3
            else:
                if tt2.gols_feitos > tt3.gols_feitos:
                    if tt2.gols_feitos > tt4.gols_feitos:
                        arruma.append(1)
                        if tt3.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt3.gols_feitos:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, 2, tt3, tt4)
                            elif tt1 == 4:
                                desempate(4, 1, tt3, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt2.gols_feitos:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, 4, tt4)
                        elif tt1 == 4:
                            desempate(4, tt2, 3, tt4)
                        arruma[2] += 3
                elif tt3.gols_feitos > tt2.gols_feitos:
                    if tt3.gols_feitos > tt4.gols_feitos:
                        if tt2.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt2.gols_feitos:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, tt2, 2, tt4)
                            elif tt1 == 4:
                                desempate(4, tt2, 1, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt3.gols_feitos:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, 4, tt3, tt4)
                        elif tt1 == 4:
                            desempate(4, 3, tt3, tt4)
                        arruma[1] += 3
                else:
                    if tt2.gols_feitos > tt4.gols_feitos:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 4)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 3)
                        arruma[3] += 3
                    elif tt4.gols_feitos > tt2.gols_feitos:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 2)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 1)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 3
        elif type(tt2) == int:
            if type(tt3) == int:
                if tt1.gols_feitos > tt4.gols_feitos:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.gols_feitos > tt1.gols_feitos:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    n = 3
            elif type(tt4) == int:
                if tt1.gols_feitos > tt3.gols_feitos:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.gols_feitos > tt1.gols_feitos:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    n = 3
            else:
                if tt1.gols_feitos > tt3.gols_feitos:
                    if tt1.gols_feitos > tt4.gols_feitos:
                        arruma.append(1)
                        arruma.append(0)
                        if tt3.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt3.gols_feitos:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(2, 1, tt3, tt4)
                            elif tt2 == 4:
                                desempate(1, 4, tt3, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt1.gols_feitos:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, 4, tt4)
                        elif tt2 == 4:
                            desempate(tt1, 4, 3, tt4)
                        arruma[2] += 3
                elif tt3.gols_feitos > tt1.gols_feitos:
                    if tt3.gols_feitos > tt4.gols_feitos:
                        if tt1.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt1.gols_feitos:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(tt1, 1, 2, tt4)
                            elif tt2 == 4:
                                desempate(tt1, 4, 1, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt3.gols_feitos:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(2, 1, tt3, tt4)
                        elif tt2 == 4:
                            desempate(1, 4, tt3, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                else:
                    if tt1.gols_feitos > tt4.gols_feitos:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 4)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 3)
                        arruma[3] += 3
                    elif tt4.gols_feitos > tt1.gols_feitos:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 2)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 1)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 3
        elif type(tt3) == int:
            if type(tt4) == int:
                if tt1.gols_feitos > tt2.gols_feitos:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                elif tt2.gols_feitos > tt1.gols_feitos:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                else:
                    n = 3
            else:
                if tt1.gols_feitos > tt2.gols_feitos:
                    if tt1.gols_feitos > tt4.gols_feitos:
                        arruma.append(1)
                        if tt2.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt2.gols_feitos:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(2, tt2, 1, tt4)
                            elif tt3 == 4:
                                desempate(1, tt2, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt1.gols_feitos:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, 4, 1, tt4)
                        elif tt3 == 4:
                            desempate(tt1, 3, 4, tt4)
                        arruma[1] += 3
                elif tt2.gols_feitos > tt1.gols_feitos:
                    if tt2.gols_feitos > tt4.gols_feitos:
                        if tt1.gols_feitos > tt4.gols_feitos:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.gols_feitos > tt1.gols_feitos:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(tt1, 2, 1, tt4)
                            elif tt3 == 4:
                                desempate(tt1, 1, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.gols_feitos > tt2.gols_feitos:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(2, tt2, 1, tt4)
                        elif tt3 == 4:
                            desempate(1, tt2, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                else:
                    if tt1.gols_feitos > tt4.gols_feitos:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 4)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 3)
                        arruma[3] += 3
                    elif tt4.gols_feitos > tt1.gols_feitos:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 2)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 1)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                    else:
                        n = 3
        elif type(tt4) == int:
            if tt1.gols_feitos > tt2.gols_feitos:
                if tt1.gols_feitos > tt3.gols_feitos:
                    arruma.append(1)
                    if tt2.gols_feitos > tt3.gols_feitos:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.gols_feitos > tt2.gols_feitos:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(2, tt2, tt3, 1)
                        elif tt4 == 4:
                            desempate(1, tt2, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.gols_feitos > tt1.gols_feitos:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, 4, tt3, 1)
                    elif tt4 == 4:
                        desempate(tt1, 3, tt3, 4)
                    arruma[1] += 3
            elif tt2.gols_feitos > tt1.gols_feitos:
                if tt2.gols_feitos > tt3.gols_feitos:
                    if tt1.gols_feitos > tt3.gols_feitos:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.gols_feitos > tt1.gols_feitos:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(tt1, 2, tt3, 1)
                        elif tt4 == 4:
                            desempate(tt1, 1, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.gols_feitos > tt2.gols_feitos:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(2, tt2, tt3, 1)
                    elif tt4 == 4:
                        desempate(1, tt2, tt3, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
            else:
                if tt1.gols_feitos > tt3.gols_feitos:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 4, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 3, 4)
                    arruma[2] += 3
                elif tt3.gols_feitos > tt1.gols_feitos:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 2, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 1, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
                else:
                    n = 3
    if n == 3:
        if type(tt1) == int:
            if type(tt2) == int:
                if tt3.pontos3 > tt4.pontos3:
                    arruma.append(1)
                    arruma.append(2)
                elif tt4.pontos3 > tt3.pontos3:
                    arruma.append(2)
                    arruma.append(1)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(2)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(1)
            elif type(tt3) == int:
                if tt2.pontos2 > tt4.pontos2:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.pontos2 > tt2.pontos2:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(2)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
            elif type(tt4) == int:
                if tt2.pontos1 > tt3.pontos1:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.pontos1 > tt2.pontos1:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(0)
            else:
                if tt2.pontos_12 > tt3.pontos_13:
                    if tt2.pontos_12 > tt4.pontos_23:
                        arruma.append(1)
                        if tt3.pontos_13 > tt4.pontos_23:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.pontos_23 > tt3.pontos_13:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, 2, tt3, tt4)
                            elif tt1 == 4:
                                desempate(4, 1, tt3, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.pontos_23 > tt2.pontos_12:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, 4, tt4)
                        elif tt1 == 4:
                            desempate(4, tt2, 3, tt4)
                        arruma[2] += 3
                elif tt3.pontos_13 > tt2.pontos_12:
                    if tt3.pontos_13 > tt4.pontos_23:
                        if tt2.pontos_12 > tt4.pontos_23:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.pontos_23 > tt2.pontos_12:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt1 == 1:
                                desempate(1, tt2, 2, tt4)
                            elif tt1 == 4:
                                desempate(4, tt2, 1, tt4)
                            arruma[1] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.pontos_23 > tt3.pontos_13:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, 4, tt3, tt4)
                        elif tt1 == 4:
                            desempate(4, 3, tt3, tt4)
                        arruma[1] += 3
                else:
                    if tt2.pontos_12 > tt4.pontos_23:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 4)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 3)
                        arruma[3] += 3
                    elif tt4.pontos_23 > tt2.pontos_12:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, tt3, 2)
                        elif tt1 == 4:
                            desempate(4, tt2, tt3, 1)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 4
        elif type(tt2) == int:
            if type(tt3) == int:
                if tt1.pontos1 > tt4.pontos1:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(2)
                elif tt4.pontos1 > tt1.pontos1:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(0)
                        arruma.append(2)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(0)
                        arruma.append(1)
            elif type(tt4) == int:
                if tt1.pontos2 > tt3.pontos2:
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(2)
                    arruma.append(0)
                elif tt3.pontos2 > tt1.pontos2:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(2)
                        arruma.append(0)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                        arruma.append(0)
            else:
                if tt1.pontos_12 > tt3.pontos_23:
                    if tt1.pontos_12 > tt4.pontos_13:
                        arruma.append(1)
                        arruma.append(0)
                        if tt3.pontos_23 > tt4.pontos_13:
                            arruma.append(2)
                            arruma.append(3)
                        elif tt4.pontos_13 > tt3.pontos_23:
                            arruma.append(3)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(2, 1, tt3, tt4)
                            elif tt2 == 4:
                                desempate(1, 4, tt3, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.pontos_13 > tt1.pontos_12:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(3)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, 4, tt4)
                        elif tt2 == 4:
                            desempate(tt1, 4, 3, tt4)
                        arruma[2] += 3
                elif tt3.pontos_23 > tt1.pontos_12:
                    if tt3.pontos_23 > tt4.pontos_13:
                        if tt1.pontos_12 > tt4.pontos_13:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(3)
                        elif tt4.pontos_13 > tt1.pontos_12:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt2 == 1:
                                desempate(tt1, 1, 2, tt4)
                            elif tt2 == 4:
                                desempate(tt1, 4, 1, tt4)
                            arruma[0] += 1
                            arruma[2] += 1
                            arruma[3] += 1
                    elif tt4.pontos_13 > tt3.pontos_23:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(2)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(2, 1, tt3, tt4)
                        elif tt2 == 4:
                            desempate(1, 4, tt3, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                else:
                    if tt1.pontos_12 > tt4.pontos_13:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 4)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 3)
                        arruma[3] += 3
                    elif tt4.pontos_13 > tt1.pontos_12:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, tt3, 2)
                        elif tt2 == 4:
                            desempate(tt1, 4, tt3, 1)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                    else:
                        n = 4
        elif type(tt3) == int:
            if type(tt4) == int:
                if tt1.pontos3 > tt2.pontos3:
                    arruma.append(1)
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(0)
                elif tt2.pontos3 > tt1.pontos3:
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                    arruma.append(0)
                else:
                    a = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(0)
                    elif a == 2:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(0)
            else:
                if tt1.pontos_13 > tt2.pontos_23:
                    if tt1.pontos_13 > tt4.pontos_12:
                        arruma.append(1)
                        if tt2.pontos_23 > tt4.pontos_12:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.pontos_12 > tt2.pontos_23:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(2, tt2, 1, tt4)
                            elif tt3 == 4:
                                desempate(1, tt2, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.pontos_12 > tt1.pontos_13:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, 4, 1, tt4)
                        elif tt3 == 4:
                            desempate(tt1, 3, 4, tt4)
                        arruma[1] += 3
                elif tt2.pontos_23 > tt1.pontos_13:
                    if tt2.pontos_23 > tt4.pontos_12:
                        if tt1.pontos_13 > tt4.pontos_12:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(3)
                        elif tt4.pontos_12 > tt1.pontos_13:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(2)
                        else:
                            arruma.clear()
                            if tt3 == 1:
                                desempate(tt1, 2, 1, tt4)
                            elif tt3 == 4:
                                desempate(tt1, 1, 4, tt4)
                            arruma[0] += 1
                            arruma[1] += 1
                            arruma[3] += 1
                    elif tt4.pontos_12 > tt2.pontos_23:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(2, tt2, 1, tt4)
                        elif tt3 == 4:
                            desempate(1, tt2, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                else:
                    arruma.clear()
                    if tt1.pontos_13 > tt4.pontos_12:
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 4)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 3)
                        arruma[3] += 3
                    elif tt4.pontos_12 > tt1.pontos_13:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, tt2, 1, 2)
                        elif tt3 == 4:
                            desempate(tt1, tt2, 4, 1)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                    else:
                        n = 4
        elif type(tt4) == int:
            if tt1.pontos_23 > tt2.pontos13:
                if tt1.pontos_23 > tt3.pontos_12:
                    arruma.append(1)
                    if tt2.pontos13 > tt3.pontos_12:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.pontos_12 > tt2.pontos13:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(2, tt2, tt3, 1)
                        elif tt4 == 4:
                            desempate(1, tt2, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.pontos_12 > tt1.pontos_23:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, 4, tt3, 1)
                    elif tt4 == 4:
                        desempate(tt1, 3, tt3, 4)
                    arruma[1] += 3
            elif tt2.pontos13 > tt1.pontos_23:
                if tt2.pontos13 > tt3.pontos_12:
                    if tt1.pontos_23 > tt3.pontos_12:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.pontos_12 > tt1.pontos_23:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(tt1, 2, tt3, 1)
                        elif tt4 == 4:
                            desempate(tt1, 1, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.pontos_12 > tt2.pontos13:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(2, tt2, tt3, 1)
                    elif tt4 == 4:
                        desempate(1, tt2, tt3, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
            else:
                if tt1.pontos_23 > tt3.pontos_12:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 4, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 3, 4)
                    arruma[2] += 3
                elif tt3.pontos_12 > tt1.pontos_23:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 2, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 1, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
                else:
                    n = 4
    if n == 4:
        if type(tt1) == int:
            if tt2.saldo_12 > tt3.saldo_13:
                if tt2.saldo_12 > tt4.saldo_23:
                    arruma.append(1)
                    if tt3.saldo_13 > tt4.saldo_23:
                        arruma.append(2)
                        arruma.append(3)
                    elif tt4.saldo_23 > tt3.saldo_13:
                        arruma.append(3)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, 2, tt3, tt4)
                        elif tt1 == 4:
                            desempate(4, 1, tt3, tt4)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.saldo_23 > tt2.saldo_12:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, 4, tt4)
                    elif tt1 == 4:
                        desempate(4, tt2, 3, tt4)
                    arruma[2] += 3
            elif tt3.saldo_13 > tt2.saldo_12:
                if tt3.saldo_13 > tt4.saldo_23:
                    if tt2.saldo_12 > tt4.saldo_23:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                    elif tt4.saldo_23 > tt2.saldo_12:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, 2, tt4)
                        elif tt1 == 4:
                            desempate(4, tt2, 1, tt4)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.saldo_23 > tt3.saldo_13:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, 4, tt3, tt4)
                    elif tt1 == 4:
                        desempate(4, 3, tt3, tt4)
                    arruma[1] += 3
            else:
                if tt2.saldo_12 > tt4.saldo_23:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, tt3, 4)
                    elif tt1 == 4:
                        desempate(4, tt2, tt3, 3)
                    arruma[3] += 3
                elif tt4.saldo_23 > tt2.saldo_12:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, tt3, 2)
                    elif tt1 == 4:
                        desempate(4, tt2, tt3, 1)
                    arruma[1] += 1
                    arruma[2] += 1
                    arruma[3] += 1
                else:
                    n = 5
        elif type(tt2) == int:
            if tt1.saldo_12 > tt3.saldo_23:
                if tt1.saldo_12 > tt4.saldo_13:
                    arruma.append(1)
                    arruma.append(0)
                    if tt3.saldo_23 > tt4.saldo_13:
                        arruma.append(2)
                        arruma.append(3)
                    elif tt4.saldo_13 > tt3.saldo_23:
                        arruma.append(3)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(2, 1, tt3, tt4)
                        elif tt2 == 4:
                            desempate(1, 4, tt3, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.saldo_13 > tt1.saldo_12:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(3)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, 4, tt4)
                    elif tt2 == 4:
                        desempate(tt1, 4, 3, tt4)
                    arruma[2] += 3
            elif tt3.saldo_23 > tt1.saldo_12:
                if tt3.saldo_23 > tt4.saldo_13:
                    if tt1.saldo_12 > tt4.saldo_13:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                        arruma.append(3)
                    elif tt4.saldo_13 > tt1.saldo_12:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(1)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, 2, tt4)
                        elif tt2 == 4:
                            desempate(tt1, 4, 1, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.saldo_13 > tt3.saldo_23:
                    arruma.append(3)
                    arruma.append(0)
                    arruma.append(2)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(2, 1, tt3, tt4)
                    elif tt2 == 4:
                        desempate(1, 4, tt3, tt4)
                    arruma[0] += 1
                    arruma[2] += 1
                    arruma[3] += 1
            else:
                if tt1.saldo_12 > tt4.saldo_13:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, tt3, 4)
                    elif tt2 == 4:
                        desempate(tt1, 4, tt3, 3)
                    arruma[3] += 3
                elif tt4.saldo_13 > tt1.saldo_12:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, tt3, 2)
                    elif tt2 == 4:
                        desempate(tt1, 4, tt3, 1)
                    arruma[0] += 1
                    arruma[2] += 1
                    arruma[3] += 1
                else:
                    n = 5
        elif type(tt3) == int:
            if tt1.saldo_13 > tt2.saldo_23:
                if tt1.saldo_13 > tt4.saldo_12:
                    arruma.append(1)
                    if tt2.saldo_23 > tt4.saldo_12:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(3)
                    elif tt4.saldo_12 > tt2.saldo_23:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(2, tt2, 1, tt4)
                        elif tt3 == 4:
                            desempate(1, tt2, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                elif tt4.saldo_12 > tt1.saldo_13:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, 4, 1, tt4)
                    elif tt3 == 4:
                        desempate(tt1, 3, 4, tt4)
                    arruma[1] += 3
            elif tt2.saldo_23 > tt1.saldo_13:
                if tt2.saldo_23 > tt4.saldo_12:
                    if tt1.saldo_13 > tt4.saldo_12:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(3)
                    elif tt4.saldo_12 > tt1.saldo_13:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, 2, 1, tt4)
                        elif tt3 == 4:
                            desempate(tt1, 1, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                elif tt4.saldo_12 > tt2.saldo_23:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(2, tt2, 1, tt4)
                    elif tt3 == 4:
                        desempate(1, tt2, 4, tt4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[3] += 1
            else:
                if tt1.saldo_13 > tt4.saldo_12:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, tt2, 1, 4)
                    elif tt3 == 4:
                        desempate(tt1, tt2, 4, 3)
                    arruma[3] += 3
                elif tt4.saldo_12 > tt1.saldo_13:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, tt2, 1, 2)
                    elif tt3 == 4:
                        desempate(tt1, tt2, 4, 1)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[3] += 1
                else:
                    n = 5
        elif type(tt4) == int:
            if tt1.saldo_23 > tt2.saldo_13:
                if tt1.saldo_23 > tt3.saldo_12:
                    arruma.append(1)
                    if tt2.pontos13 > tt3.saldo_12:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.saldo_12 > tt2.saldo_13:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(2, tt2, tt3, 1)
                        elif tt4 == 4:
                            desempate(1, tt2, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.saldo_12 > tt1.saldo_23:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, 4, tt3, 1)
                    elif tt4 == 4:
                        desempate(tt1, 3, tt3, 4)
                    arruma[1] += 3
            elif tt2.saldo_13 > tt1.saldo_23:
                if tt2.saldo_13 > tt3.saldo_12:
                    if tt1.saldo_23 > tt3.saldo_12:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.saldo_12 > tt1.saldo_23:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(tt1, 2, tt3, 1)
                        elif tt4 == 4:
                            desempate(tt1, 1, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.saldo_12 > tt2.saldo_13:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(2, tt2, tt3, 1)
                    elif tt4 == 4:
                        desempate(1, tt2, tt3, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
            else:
                if tt1.saldo_23 > tt3.saldo_12:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 4, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 3, 4)
                    arruma[2] += 3
                elif tt3.saldo_12 > tt1.saldo_23:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 2, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 1, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
                else:
                    n = 5
    if n == 5:
        if type(tt1) == int:
            if tt2.gols_feitos_12 > tt3.gols_feitos_13:
                if tt2.gols_feitos_12 > tt4.gols_feitos_23:
                    arruma.append(1)
                    if tt3.gols_feitos_13 > tt4.gols_feitos_23:
                        arruma.append(2)
                        arruma.append(3)
                    elif tt4.gols_feitos_23 > tt3.gols_feitos_13:
                        arruma.append(3)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, 2, tt3, tt4)
                        elif tt1 == 4:
                            desempate(4, 1, tt3, tt4)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_23 > tt2.gols_feitos_12:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, 4, tt4)
                    elif tt1 == 4:
                        desempate(4, tt2, 3, tt4)
                    arruma[2] += 3
            elif tt3.gols_feitos_13 > tt2.gols_feitos_12:
                if tt3.gols_feitos_13 > tt4.gols_feitos_23:
                    if tt2.gols_feitos_12 > tt4.gols_feitos_23:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                    elif tt4.gols_feitos_23 > tt2.gols_feitos_12:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt1 == 1:
                            desempate(1, tt2, 2, tt4)
                        elif tt1 == 4:
                            desempate(4, tt2, 1, tt4)
                        arruma[1] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_23 > tt3.gols_feitos_13:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, 4, tt3, tt4)
                    elif tt1 == 4:
                        desempate(4, 3, tt3, tt4)
                    arruma[1] += 3
            else:
                if tt2.gols_feitos_12 > tt4.gols_feitos_23:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, tt3, 4)
                    elif tt1 == 4:
                        desempate(4, tt2, tt3, 3)
                    arruma[3] += 3
                elif tt4.gols_feitos_23 > tt2.gols_feitos_12:
                    arruma.clear()
                    if tt1 == 1:
                        desempate(1, tt2, tt3, 2)
                    elif tt1 == 4:
                        desempate(4, tt2, tt3, 1)
                    arruma[1] += 1
                    arruma[2] += 1
                    arruma[3] += 1
                else:
                    a = random.randint(1, 3)
                    b = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                    elif a == 2:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(2)
                    elif a == 3:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                            arruma.append(1)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                            arruma.append(1)
        elif type(tt2) == int:
            if tt1.gols_feitos_12 > tt3.gols_feitos_23:
                if tt1.saldo_12 > tt4.gols_feitos_13:
                    arruma.append(1)
                    arruma.append(0)
                    if tt3.gols_feitos_23 > tt4.gols_feitos_13:
                        arruma.append(2)
                        arruma.append(3)
                    elif tt4.gols_feitos_13 > tt3.gols_feitos_23:
                        arruma.append(3)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(2, 1, tt3, tt4)
                        elif tt2 == 4:
                            desempate(1, 4, tt3, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_13 > tt1.gols_feitos_12:
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(3)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, 4, tt4)
                    elif tt2 == 4:
                        desempate(tt1, 4, 3, tt4)
                    arruma[2] += 3
            elif tt3.gols_feitos_23 > tt1.gols_feitos_12:
                if tt3.gols_feitos_23 > tt4.gols_feitos_13:
                    if tt1.gols_feitos_12 > tt4.gols_feitos_13:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(1)
                        arruma.append(3)
                    elif tt4.gols_feitos_13 > tt1.gols_feitos_12:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(1)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt2 == 1:
                            desempate(tt1, 1, 2, tt4)
                        elif tt2 == 4:
                            desempate(tt1, 4, 1, tt4)
                        arruma[0] += 1
                        arruma[2] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_13 > tt3.gols_feitos_23:
                    arruma.append(3)
                    arruma.append(0)
                    arruma.append(2)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(2, 1, tt3, tt4)
                    elif tt2 == 4:
                        desempate(1, 4, tt3, tt4)
                    arruma[0] += 1
                    arruma[2] += 1
                    arruma[3] += 1
            else:
                if tt1.gols_feitos_12 > tt4.gols_feitos_13:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, tt3, 4)
                    elif tt2 == 4:
                        desempate(tt1, 4, tt3, 3)
                    arruma[3] += 3
                elif tt4.gols_feitos_13 > tt1.gols_feitos_12:
                    arruma.clear()
                    if tt2 == 1:
                        desempate(tt1, 1, tt3, 2)
                    elif tt2 == 4:
                        desempate(tt1, 4, tt3, 1)
                    arruma[0] += 1
                    arruma[2] += 1
                    arruma[3] += 1
                else:
                    a = random.randint(1, 3)
                    b = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        arruma.append(0)
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                    elif a == 2:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(1)
                            arruma.append(2)
                    elif a == 3:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(3)
                            arruma.append(1)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(2)
                            arruma.append(1)
        elif type(tt3) == int:
            if tt1.gols_feitos_13 > tt2.gols_feitos_23:
                if tt1.gols_feitos_13 > tt4.gols_feitos_12:
                    arruma.append(1)
                    if tt2.gols_feitos_23 > tt4.gols_feitos_12:
                        arruma.append(2)
                        arruma.append(0)
                        arruma.append(3)
                    elif tt4.gols_feitos_12 > tt2.gols_feitos_23:
                        arruma.append(3)
                        arruma.append(0)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(2, tt2, 1, tt4)
                        elif tt3 == 4:
                            desempate(1, tt2, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_12 > tt1.gols_feitos_13:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, 4, 1, tt4)
                    elif tt3 == 4:
                        desempate(tt1, 3, 4, tt4)
                    arruma[1] += 3
            elif tt2.gols_feitos_23 > tt1.gols_feitos_13:
                if tt2.gols_feitos_23 > tt4.gols_feitos_12:
                    if tt1.gols_feitos_13 > tt4.gols_feitos_12:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(3)
                    elif tt4.gols_feitos_12 > tt1.gols_feitos_13:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(0)
                        arruma.append(2)
                    else:
                        arruma.clear()
                        if tt3 == 1:
                            desempate(tt1, 2, 1, tt4)
                        elif tt3 == 4:
                            desempate(tt1, 1, 4, tt4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[3] += 1
                elif tt4.gols_feitos_12 > tt2.gols_feitos_23:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(0)
                    arruma.append(1)
                else:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(2, tt2, 1, tt4)
                    elif tt3 == 4:
                        desempate(1, tt2, 4, tt4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[3] += 1
            else:
                if tt1.gols_feitos_13 > tt4.gols_feitos_12:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, tt2, 1, 4)
                    elif tt3 == 4:
                        desempate(tt1, tt2, 4, 3)
                    arruma[3] += 3
                elif tt4.gols_feitos_12 > tt1.gols_feitos_13:
                    arruma.clear()
                    if tt3 == 1:
                        desempate(tt1, tt2, 1, 2)
                    elif tt3 == 4:
                        desempate(tt1, tt2, 4, 1)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[3] += 1
                else:
                    a = random.randint(1, 3)
                    b = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        if b == 1:
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(2)
                    elif a == 2:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(0)
                            arruma.append(2)
                    elif a == 3:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                            arruma.append(0)
                            arruma.append(1)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                            arruma.append(0)
                            arruma.append(1)
        elif type(tt4) == int:
            if tt1.gols_feitos_23 > tt2.gols_feitos_13:
                if tt1.gols_feitos_23 > tt3.gols_feitos_12:
                    arruma.append(1)
                    if tt2.gols_feitos_13 > tt3.gols_feitos_12:
                        arruma.append(2)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.gols_feitos_12 > tt2.gols_feitos_13:
                        arruma.append(3)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(2, tt2, tt3, 1)
                        elif tt4 == 4:
                            desempate(1, tt2, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.gols_feitos_12 > tt1.gols_feitos_23:
                    arruma.append(2)
                    arruma.append(3)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, 4, tt3, 1)
                    elif tt4 == 4:
                        desempate(tt1, 3, tt3, 4)
                    arruma[1] += 3
            elif tt2.gols_feitos_13 > tt1.gols_feitos_23:
                if tt2.gols_feitos_13 > tt3.gols_feitos_12:
                    if tt1.gols_feitos_23 > tt3.gols_feitos_12:
                        arruma.append(2)
                        arruma.append(1)
                        arruma.append(3)
                        arruma.append(0)
                    elif tt3.gols_feitos_12 > tt1.gols_feitos_23:
                        arruma.append(3)
                        arruma.append(1)
                        arruma.append(2)
                        arruma.append(0)
                    else:
                        arruma.clear()
                        if tt4 == 1:
                            desempate(tt1, 2, tt3, 1)
                        elif tt4 == 4:
                            desempate(tt1, 1, tt3, 4)
                        arruma[0] += 1
                        arruma[1] += 1
                        arruma[2] += 1
                elif tt3.gols_feitos_12 > tt2.gols_feitos_13:
                    arruma.append(3)
                    arruma.append(2)
                    arruma.append(1)
                    arruma.append(0)
                else:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(2, tt2, tt3, 1)
                    elif tt4 == 4:
                        desempate(1, tt2, tt3, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
            else:
                if tt1.gols_feitos_23 > tt3.gols_feitos_12:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 4, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 3, 4)
                    arruma[2] += 3
                elif tt3.gols_feitos_12 > tt1.gols_feitos_23:
                    arruma.clear()
                    if tt4 == 1:
                        desempate(tt1, tt2, 2, 1)
                    elif tt4 == 4:
                        desempate(tt1, tt2, 1, 4)
                    arruma[0] += 1
                    arruma[1] += 1
                    arruma[2] += 1
                else:
                    a = random.randint(1, 3)
                    b = random.randint(1, 2)
                    if a == 1:
                        arruma.append(1)
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                        arruma.append(0)
                    elif a == 2:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(1)
                            arruma.append(3)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(1)
                            arruma.append(2)
                        arruma.append(0)
                    elif a == 3:
                        if b == 1:
                            arruma.append(2)
                            arruma.append(3)
                            arruma.append(1)
                        elif b == 2:
                            arruma.append(3)
                            arruma.append(2)
                            arruma.append(1)
                        arruma.append(0)
    if tt1 == 1:
        if tt2 == 2:
            if arruma[2] == 1:
                tt3.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt3.quarto = True
                tt4.terceiro = True
        elif tt2 == 4:
            if arruma[2] == 1:
                tt3.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt3.terceiro = True
                tt4.segundo = True
        elif tt3 == 2:
            if arruma[1] == 1:
                tt2.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt2.quarto = True
                tt4.terceiro = True
        elif tt3 == 4:
            if arruma[1] == 1:
                tt2.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt2.terceiro = True
                tt4.segundo = True
        elif tt4 == 2:
            if arruma[1] == 1:
                tt2.terceiro = True
                tt3.quarto = True
            elif arruma[2] == 1:
                tt2.quarto = True
                tt3.terceiro = True
        elif tt4 == 4:
            if arruma[1] == 1:
                tt2.segundo = True
                tt3.terceiro = True
            elif arruma[2] == 1:
                tt2.terceiro = True
                tt3.segundo = True
        else:
            if arruma[1] == 1:
                tt2.segundo = True
            elif arruma[1] == 2:
                tt2.terceiro = True
            elif arruma[1] == 3:
                tt2.quarto = True
            if arruma[2] == 1:
                tt3.segundo = True
            elif arruma[2] == 2:
                tt3.terceiro = True
            elif arruma[2] == 3:
                tt3.quarto = True
            if arruma[3] == 1:
                tt4.segundo = True
            elif arruma[3] == 2:
                tt4.terceiro = True
            elif arruma[3] == 3:
                tt4.quarto = True
    elif tt1 == 2:
        if tt2 == 1:
            if arruma[2] == 1:
                tt3.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt3.quarto = True
                tt4.terceiro = True
        elif tt3 == 1:
            if arruma[1] == 1:
                tt2.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt2.quarto = True
                tt4.terceiro = True
        elif tt4 == 1:
            if arruma[1] == 1:
                tt2.terceiro = True
                tt3.quarto = True
            elif arruma[2] == 1:
                tt2.quarto = True
                tt3.terceiro = True
    elif tt1 == 3:
        if tt2 == 4:
            if arruma[2] == 1:
                tt3.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt3.segundo = True
                tt4.primeiro = True
        elif tt3 == 4:
            if arruma[1] == 1:
                tt2.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt2.segundo = True
                tt4.primeiro = True
        elif tt4 == 4:
            if arruma[1] == 1:
                tt2.primeiro = True
                tt3.segundo = True
            elif arruma[2] == 1:
                tt2.segundo = True
                tt3.primeiro = True
    elif tt1 == 4:
        if tt2 == 1:
            if arruma[2] == 1:
                tt3.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt3.terceiro = True
                tt4.segundo = True
        elif tt2 == 3:
            if arruma[2] == 1:
                tt3.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt3.segundo = True
                tt4.primeiro = True
        elif tt3 == 1:
            if arruma[1] == 1:
                tt2.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt2.terceiro = True
                tt4.segundo = True
        elif tt3 == 3:
            if arruma[1] == 1:
                tt2.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt2.segundo = True
                tt4.primeiro = True
        elif tt4 == 1:
            if arruma[1] == 1:
                tt2.segundo = True
                tt3.terceiro = True
            elif arruma[2] == 1:
                tt2.terceiro = True
                tt3.segundo = True
        elif tt4 == 3:
            if arruma[1] == 1:
                tt2.primeiro = True
                tt3.segundo = True
            elif arruma[2] == 1:
                tt2.segundo = True
                tt3.primeiro = True
        else:
            if arruma[1] == 1:
                tt2.primeiro = True
            elif arruma[1] == 2:
                tt2.segundo = True
            elif arruma[1] == 3:
                tt2.terceiro = True
            if arruma[2] == 1:
                tt3.primeiro = True
            elif arruma[2] == 2:
                tt3.segundo = True
            elif arruma[2] == 3:
                tt3.terceiro = True
            if arruma[3] == 1:
                tt4.primeiro = True
            elif arruma[3] == 2:
                tt4.segundo = True
            elif arruma[3] == 3:
                tt4.terceiro = True
    elif tt2 == 1:
        if tt3 == 2:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt1.quarto = True
                tt4.terceiro = True
        elif tt3 == 4:
            if arruma[0] == 1:
                tt1.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt1.terceiro = True
                tt4.segundo = True
        elif tt4 == 2:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt3.quarto = True
            elif arruma[2] == 1:
                tt1.quarto = True
                tt3.terceiro = True
        elif tt4 == 4:
            if arruma[0] == 1:
                tt1.segundo = True
                tt3.terceiro = True
            elif arruma[2] == 1:
                tt1.terceiro = True
                tt3.segundo = True
        else:
            if arruma[0] == 1:
                tt1.segundo = True
            elif arruma[0] == 2:
                tt1.terceiro = True
            elif arruma[0] == 3:
                tt1.quarto = True
            if arruma[2] == 1:
                tt3.segundo = True
            elif arruma[2] == 2:
                tt3.terceiro = True
            elif arruma[2] == 3:
                tt3.quarto = True
            if arruma[3] == 1:
                tt4.segundo = True
            elif arruma[3] == 2:
                tt4.terceiro = True
            elif arruma[3] == 3:
                tt4.quarto = True
    elif tt2 == 2:
        if tt3 == 1:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt4.quarto = True
            elif arruma[3] == 1:
                tt1.quarto = True
                tt4.terceiro = True
        elif tt4 == 1:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt3.quarto = True
            elif arruma[2] == 1:
                tt1.quarto = True
                tt3.terceiro = True
    elif tt2 == 3:
        if tt3 == 4:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt1.segundo = True
                tt4.primeiro = True
        elif tt4 == 4:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt3.segundo = True
            elif arruma[2] == 1:
                tt1.segundo = True
                tt3.primeiro = True
    elif tt2 == 4:
        if tt3 == 1:
            if arruma[0] == 1:
                tt1.segundo = True
                tt4.terceiro = True
            elif arruma[3] == 1:
                tt1.terceiro = True
                tt4.segundo = True
        elif tt3 == 3:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt4.segundo = True
            elif arruma[3] == 1:
                tt1.segundo = True
                tt4.primeiro = True
        elif tt4 == 1:
            if arruma[0] == 1:
                tt1.segundo = True
                tt3.terceiro = True
            elif arruma[2] == 1:
                tt1.terceiro = True
                tt3.segundo = True
        elif tt4 == 3:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt3.segundo = True
            elif arruma[2] == 1:
                tt1.segundo = True
                tt3.primeiro = True
        else:
            if arruma[0] == 1:
                tt1.primeiro = True
            elif arruma[0] == 2:
                tt1.segundo = True
            elif arruma[0] == 3:
                tt1.terceiro = True
            if arruma[2] == 1:
                tt3.primeiro = True
            elif arruma[2] == 2:
                tt3.segundo = True
            elif arruma[2] == 3:
                tt3.terceiro = True
            if arruma[3] == 1:
                tt4.primeiro = True
            elif arruma[3] == 2:
                tt4.segundo = True
            elif arruma[3] == 3:
                tt4.terceiro = True
    elif tt3 == 1:
        if tt4 == 2:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt2.quarto = True
            elif arruma[1] == 1:
                tt1.quarto = True
                tt2.terceiro = True
        elif tt4 == 4:
            if arruma[0] == 1:
                tt1.segundo = True
                tt2.terceiro = True
            elif arruma[1] == 1:
                tt1.terceiro = True
                tt2.segundo = True
        else:
            if arruma[0] == 1:
                tt1.segundo = True
            elif arruma[0] == 2:
                tt1.terceiro = True
            elif arruma[0] == 3:
                tt1.quarto = True
            if arruma[1] == 1:
                tt2.segundo = True
            elif arruma[1] == 2:
                tt2.terceiro = True
            elif arruma[1] == 3:
                tt2.quarto = True
            if arruma[3] == 1:
                tt4.segundo = True
            elif arruma[3] == 2:
                tt4.terceiro = True
            elif arruma[3] == 3:
                tt4.quarto = True
    elif tt3 == 2:
        if tt4 == 1:
            if arruma[0] == 1:
                tt1.terceiro = True
                tt2.quarto = True
            elif arruma[1] == 1:
                tt1.quarto = True
                tt2.terceiro = True
    elif tt3 == 3:
        if tt4 == 4:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt2.segundo = True
            elif arruma[1] == 1:
                tt1.segundo = True
                tt2.primeiro = True
    elif tt3 == 4:
        if tt4 == 1:
            if arruma[0] == 1:
                tt1.segundo = True
                tt2.terceiro = True
            elif arruma[1] == 1:
                tt1.terceiro = True
                tt2.segundo = True
        elif tt4 == 3:
            if arruma[0] == 1:
                tt1.primeiro = True
                tt2.segundo = True
            elif arruma[1] == 1:
                tt1.segundo = True
                tt2.primeiro = True
        else:
            if arruma[0] == 1:
                tt1.primeiro = True
            elif arruma[0] == 2:
                tt1.segundo = True
            elif arruma[0] == 3:
                tt1.terceiro = True
            if arruma[1] == 1:
                tt2.primeiro = True
            elif arruma[1] == 2:
                tt2.segundo = True
            elif arruma[1] == 3:
                tt2.terceiro = True
            if arruma[3] == 1:
                tt4.primeiro = True
            elif arruma[3] == 2:
                tt4.segundo = True
            elif arruma[3] == 3:
                tt4.terceiro = True
    elif tt4 == 1:
        if arruma[0] == 1:
            tt1.segundo = True
        elif arruma[0] == 2:
            tt1.terceiro = True
        elif arruma[0] == 3:
            tt1.quarto = True
        if arruma[1] == 1:
            tt2.segundo = True
        elif arruma[1] == 2:
            tt2.terceiro = True
        elif arruma[1] == 3:
            tt2.quarto = True
        if arruma[2] == 1:
            tt3.segundo = True
        elif arruma[2] == 2:
            tt3.terceiro = True
        elif arruma[2] == 3:
            tt3.quarto = True
    elif tt4 == 4:
        if arruma[0] == 1:
            tt1.primeiro = True
        elif arruma[0] == 2:
            tt1.segundo = True
        elif arruma[0] == 3:
            tt1.terceiro = True
        if arruma[1] == 1:
            tt2.primeiro = True
        elif arruma[1] == 2:
            tt2.segundo = True
        elif arruma[1] == 3:
            tt2.terceiro = True
        if arruma[2] == 1:
            tt3.primeiro = True
        elif arruma[2] == 2:
            tt3.segundo = True
        elif arruma[2] == 3:
            tt3.terceiro = True


def verificador(t1, t2, t3, t4):
    if t1.pontos > t2.pontos:
        if t1.pontos > t3.pontos:
            if t1.pontos > t4.pontos:
                t1.primeiro = True
                if t2.pontos > t3.pontos:
                    if t2.pontos > t4.pontos:
                        t2.segundo = True
                        if t3.pontos > t4.pontos:
                            t3.terceiro = True
                            t4.quarto = True
                        elif t4.pontos > t3.pontos:
                            t3.quarto = True
                            t4.terceiro = True
                        else:
                            desempate(1, 2, t3, t4)
                    elif t4.pontos > t2.pontos:
                        t4.segundo = True
                        t2.terceiro = True
                        t3.quarto = True
                    else:
                        t3.quarto = True
                        desempate(1, t2, 4, t4)
                elif t3.pontos > t2.pontos:
                    if t3.pontos > t4.pontos:
                        t3.segundo = True
                        if t2.pontos > t4.pontos:
                            t2.terceiro = True
                            t4.quarto = True
                        elif t4.pontos > t2.pontos:
                            t4.terceiro = True
                            t2.quarto = True
                        else:
                            desempate(1, t2, 2, t4)
                    elif t4.pontos > t3.pontos:
                        t4.segundo = True
                        t3.terceiro = True
                        t2.quarto = True
                    else:
                        t2.quarto = True
                        desempate(1, 4, t3, t4)
                else:
                    if t2.pontos > t4.pontos:
                        t4.quarto = True
                        desempate(1, t2, t3, 4)
                    elif t4.pontos > t2.pontos:
                        t4.segundo = True
                        desempate(1, t2, t3, 2)
                    else:
                        desempate(1, t2, t3, t4)
            elif t4.pontos > t1.pontos:
                t4.primeiro = True
                t1.segundo = True
                if t2.pontos > t3.pontos:
                    t2.terceiro = True
                    t3.quarto = True
                elif t3.pontos > t2.pontos:
                    t3.terceiro = True
                    t2.quarto = True
                else:
                    desempate(2, t2, t3, 1)
            else:
                desempate(t1, 3, 4, t4)
                if t2.pontos > t3.pontos:
                    t2.terceiro = True
                    t3.quarto = True
                elif t3.pontos > t2.pontos:
                    t3.terceiro = True
                    t2.quarto = True
                else:
                    arruma.clear()
                    desempate(2, t2, t3, 1)
        elif t3.pontos > t1.pontos:
            if t3.pontos > t4.pontos:
                t3.primeiro = True
                if t1.pontos > t4.pontos:
                    t1.segundo = True
                    if t2.pontos > t4.pontos:
                        t2.terceiro = True
                        t4.quarto = True
                    elif t4.pontos > t2.pontos:
                        t4.terceiro = True
                        t2.quarto = True
                    else:
                        desempate(2, t2, 1, t4)
                elif t4.pontos > t1.pontos:
                    t4.segundo = True
                    t1.terceiro = True
                    t2.quarto = True
                else:
                    t2.quarto = True
                    arruma.clear()
                    desempate(t1, 4, 1, t4)
            elif t4.pontos > t3.pontos:
                t4.primeiro = True
                t3.segundo = True
                t1.terceiro = True
                t2.quarto = True
            else:
                desempate(3, 4, t3, t4)
                t1.terceiro = True
                t2.quarto = True
        else:
            if t1.pontos > t4.pontos:
                desempate(t1, 3, t3, 4)
                if t2.pontos > t4.pontos:
                    t2.terceiro = True
                    t4.quarto = True
                elif t4.pontos > t2.pontos:
                    t4.terceiro = True
                    t2.quarto = True
                else:
                    arruma.clear()
                    desempate(1, t2, 2, t4)
            elif t4.pontos > t1.pontos:
                t4.primeiro = True
                t2.quarto = True
                desempate(t1, 4, t3, 1)
            else:
                t2.quarto = True
                desempate(t1, 4, t3, t4)
    elif t2.pontos > t1.pontos:
        if t2.pontos > t3.pontos:
            if t2.pontos > t4.pontos:
                t2.primeiro = True
                if t1.pontos > t3.pontos:
                    if t1.pontos > t4.pontos:
                        t1.segundo = True
                        if t3.pontos > t4.pontos:
                            t3.terceiro = True
                            t4.quarto = True
                        elif t4.pontos > t3.pontos:
                            t3.quarto = True
                            t4.terceiro = True
                        else:
                            desempate(2, 1, t3, t4)
                    elif t4.pontos > t1.pontos:
                        t4.segundo = True
                        t1.terceiro = True
                        t3.quarto = True
                    else:
                        t3.quarto = True
                        desempate(t1, 1, 4, t4)
                elif t3.pontos > t1.pontos:
                    if t3.pontos > t4.pontos:
                        t3.segundo = True
                        if t1.pontos > t4.pontos:
                            t1.terceiro = True
                            t4.quarto = True
                        elif t4.pontos > t1.pontos:
                            t4.terceiro = True
                            t1.quarto = True
                        else:
                            desempate(t1, 1, 2, t4)
                    elif t4.pontos > t3.pontos:
                        t4.segundo = True
                        t3.terceiro = True
                        t1.quarto = True
                    else:
                        t1.quarto = True
                        desempate(4, 1, t3, t4)
                else:
                    if t1.pontos > t4.pontos:
                        t4.quarto = True
                        desempate(t1, 1, t3, 4)
                    elif t4.pontos > t1.pontos:
                        t4.segundo = True
                        desempate(t1, 1, t3, 2)
                    else:
                        desempate(t1, 1, t3, t4)
            elif t4.pontos > t2.pontos:
                t4.primeiro = True
                t2.segundo = True
                if t1.pontos > t3.pontos:
                    t1.terceiro = True
                    t3.quarto = True
                elif t3.pontos > t1.pontos:
                    t3.terceiro = True
                    t1.quarto = True
                else:
                    desempate(t1, 2, t3, 1)
            else:
                desempate(3, t2, 4, t4)
                if t1.pontos > t3.pontos:
                    t1.terceiro = True
                    t3.quarto = True
                elif t3.pontos > t1.pontos:
                    t3.terceiro = True
                    t1.quarto = True
                else:
                    arruma.clear()
                    desempate(t1, 2, t3, 1)
        elif t3.pontos > t2.pontos:
            if t3.pontos > t4.pontos:
                t3.primeiro = True
                if t2.pontos > t4.pontos:
                    t2.segundo = True
                    if t1.pontos > t4.pontos:
                        t1.terceiro = True
                        t4.quarto = True
                    elif t4.pontos > t1.pontos:
                        t4.terceiro = True
                        t1.quarto = True
                    else:
                        desempate(t1, 2, 1, t4)
                elif t4.pontos > t2.pontos:
                    t4.segundo = True
                    t2.terceiro = True
                    t1.quarto = True
                else:
                    t1.quarto = True
                    desempate(4, t2, 1, t4)
            elif t4.pontos > t3.pontos:
                t4.primeiro = True
                t3.segundo = True
                t2.terceiro = True
                t1.quarto = True
            else:
                desempate(4, 3, t3, t4)
                t2.terceiro = True
                t1.quarto = True
        else:
            if t2.pontos > t4.pontos:
                desempate(3, t2, t3, 4)
                if t1.pontos > t4.pontos:
                    t1.terceiro = True
                    t4.quarto = True
                elif t4.pontos > t1.pontos:
                    t4.terceiro = True
                    t1.quarto = True
                else:
                    arruma.clear()
                    desempate(t1, 1, 2, t4)
            elif t4.pontos > t2.pontos:
                t4.primeiro = True
                t1.quarto = True
                desempate(4, t2, t3, 1)
            else:
                t1.quarto = True
                desempate(4, t2, t3, t4)
    else:
        if t1.pontos > t3.pontos:
            if t1.pontos > t4.pontos:
                desempate(t1, t2, 3, 4)
                if t3.pontos > t4.pontos:
                    t3.terceiro = True
                    t4.quarto = True
                elif t4.pontos > t3.pontos:
                    t4.terceiro = True
                    t3.quarto = True
                else:
                    arruma.clear()
                    desempate(1, 2, t3, t4)
            elif t4.pontos > t1.pontos:
                t4.primeiro = True
                t3.quarto = True
                desempate(t1, t2, 4, 1)
            else:
                t3.quarto = True
                desempate(t1, t2, 4, t4)
        elif t3.pontos > t1.pontos:
            if t3.pontos > t4.pontos:
                t3.primeiro = True
                if t1.pontos > t4.pontos:
                    t4.quarto = True
                    desempate(t1, t2, 1, 4)
                elif t4.pontos > t1.pontos:
                    t4.segundo = True
                    desempate(t1, t2, 1, 2)
                else:
                    desempate(t1, t2, 1, t4)
            elif t4.pontos > t3.pontos:
                t4.primeiro = True
                t3.segundo = True
                desempate(t1, t2, 2, 1)
            else:
                desempate(3, 4, t3, t4)
                arruma.clear()
                desempate(t1, t2, 1, 2)
        else:
            if t1.pontos > t4.pontos:
                t4.quarto = True
                desempate(t1, t2, t3, 4)
            elif t4.pontos > t1.pontos:
                t4.primeiro = True
                desempate(t1, t2, t3, 1)
            else:
                if t1.saldo > t2.saldo:
                    if t1.saldo > t3.saldo:
                        if t1.saldo > t4.saldo:
                            t1.primeiro = True
                            if t2.saldo > t3.saldo:
                                if t2.saldo > t4.saldo:
                                    t2.segundo = True
                                    if t3.saldo > t4.saldo:
                                        t3.terceiro = True
                                        t4.quarto = True
                                    elif t4.saldo > t3.saldo:
                                        t3.quarto = True
                                        t4.terceiro = True
                                    else:
                                        desempate(1, 2, t3, t4)
                                elif t4.saldo > t2.saldo:
                                    t4.segundo = True
                                    t2.terceiro = True
                                    t3.quarto = True
                                else:
                                    t3.quarto = True
                                    desempate(1, t2, 4, t4)
                            elif t3.saldo > t2.saldo:
                                if t3.saldo > t4.saldo:
                                    t3.segundo = True
                                    if t2.saldo > t4.saldo:
                                        t2.terceiro = True
                                        t4.quarto = True
                                    elif t4.saldo > t2.saldo:
                                        t4.terceiro = True
                                        t2.quarto = True
                                    else:
                                        desempate(1, t2, 2, t4)
                                elif t4.pontos > t3.pontos:
                                    t4.segundo = True
                                    t3.terceiro = True
                                    t2.quarto = True
                                else:
                                    t2.quarto = True
                                    desempate(1, 4, t3, t4)
                            else:
                                if t2.saldo > t4.saldo:
                                    t4.quarto = True
                                    desempate(1, t2, t3, 4)
                                elif t4.saldo > t2.saldo:
                                    t4.segundo = True
                                    desempate(1, t2, t3, 2)
                                else:
                                    desempate(1, t2, t3, t4)
                        elif t4.saldo > t1.saldo:
                            t4.primeiro = True
                            t1.segundo = True
                            if t2.saldo > t3.saldo:
                                t2.terceiro = True
                                t3.quarto = True
                            elif t3.saldo > t2.saldo:
                                t3.terceiro = True
                                t2.quarto = True
                            else:
                                desempate(2, t2, t3, 1)
                        else:
                            desempate(t1, 3, 4, t4)
                            if t2.saldo > t3.saldo:
                                t2.terceiro = True
                                t3.quarto = True
                            elif t3.saldo > t2.saldo:
                                t3.terceiro = True
                                t2.quarto = True
                            else:
                                arruma.clear()
                                desempate(2, t2, t3, 1)
                    elif t3.saldo > t1.saldo:
                        if t3.saldo > t4.saldo:
                            t3.primeiro = True
                            if t1.saldo > t4.saldo:
                                t1.segundo = True
                                if t2.saldo > t4.saldo:
                                    t2.terceiro = True
                                    t4.quarto = True
                                elif t4.saldo > t2.saldo:
                                    t4.terceiro = True
                                    t2.quarto = True
                                else:
                                    desempate(2, t2, 1, t4)
                            elif t4.saldo > t1.saldo:
                                t4.segundo = True
                                t1.terceiro = True
                                t2.quarto = True
                            else:
                                t2.quarto = True
                                desempate(t1, 4, 1, t4)
                        elif t4.saldo > t3.saldo:
                            t4.primeiro = True
                            t3.segundo = True
                            t1.terceiro = True
                            t2.quarto = True
                        else:
                            desempate(3, 4, t3, t4)
                            t1.terceiro = True
                            t2.quarto = True
                    else:
                        if t1.saldo > t4.saldo:
                            desempate(t1, 3, t3, 4)
                            if t2.saldo > t4.saldo:
                                t2.terceiro = True
                                t4.quarto = True
                            elif t4.saldo > t2.saldo:
                                t4.terceiro = True
                                t2.quarto = True
                            else:
                                arruma.clear()
                                desempate(1, t2, 2, t4)
                        elif t4.saldo > t1.saldo:
                            t4.primeiro = True
                            t2.quarto = True
                            desempate(t1, 4, t3, 1)
                        else:
                            t2.quarto = True
                            desempate(t1, 4, t3, t4)
                elif t2.saldo > t1.saldo:
                    if t2.saldo > t3.saldo:
                        if t2.saldo > t4.saldo:
                            t2.primeiro = True
                            if t1.saldo > t3.saldo:
                                if t1.saldo > t4.saldo:
                                    t1.segundo = True
                                    if t3.saldo > t4.saldo:
                                        t3.terceiro = True
                                        t4.quarto = True
                                    elif t4.saldo > t3.saldo:
                                        t3.quarto = True
                                        t4.terceiro = True
                                    else:
                                        desempate(2, 1, t3, t4)
                                elif t4.saldo > t1.saldo:
                                    t4.segundo = True
                                    t1.terceiro = True
                                    t3.quarto = True
                                else:
                                    t3.quarto = True
                                    desempate(t1, 1, 4, t4)
                            elif t3.saldo > t1.saldo:
                                if t3.saldo > t4.saldo:
                                    t3.segundo = True
                                    if t1.saldo > t4.saldo:
                                        t1.terceiro = True
                                        t4.quarto = True
                                    elif t4.saldo > t1.saldo:
                                        t4.terceiro = True
                                        t1.quarto = True
                                    else:
                                        desempate(t1, 1, 2, t4)
                                elif t4.saldo > t3.saldo:
                                    t4.segundo = True
                                    t3.terceiro = True
                                    t1.quarto = True
                                else:
                                    t1.quarto = True
                                    desempate(4, 1, t3, t4)
                            else:
                                if t1.saldo > t4.saldo:
                                    t4.quarto = True
                                    desempate(t1, 1, t3, 4)
                                elif t4.saldo > t1.saldo:
                                    t4.segundo = True
                                    desempate(t1, 1, t3, 2)
                                else:
                                    desempate(t1, 1, t3, t4)
                        elif t4.saldo > t2.saldo:
                            t4.primeiro = True
                            t2.segundo = True
                            if t1.saldo > t3.saldo:
                                t1.terceiro = True
                                t3.quarto = True
                            elif t3.saldo > t1.saldo:
                                t3.terceiro = True
                                t1.quarto = True
                            else:
                                desempate(t1, 2, t3, 1)
                        else:
                            desempate(3, t2, 4, t4)
                            if t1.saldo > t3.saldo:
                                t1.terceiro = True
                                t3.quarto = True
                            elif t3.saldo > t1.saldo:
                                t3.terceiro = True
                                t1.quarto = True
                            else:
                                arruma.clear()
                                desempate(t1, 2, t3, 1)
                    elif t3.saldo > t2.saldo:
                        if t3.saldo > t4.saldo:
                            t3.primeiro = True
                            if t2.saldo > t4.saldo:
                                t2.segundo = True
                                if t1.saldo > t4.saldo:
                                    t1.terceiro = True
                                    t4.quarto = True
                                elif t4.saldo > t1.saldo:
                                    t4.terceiro = True
                                    t1.quarto = True
                                else:
                                    desempate(t1, 2, 1, t4)
                            elif t4.saldo > t2.saldo:
                                t4.segundo = True
                                t2.terceiro = True
                                t1.quarto = True
                            else:
                                t1.quarto = True
                                desempate(4, t2, 1, t4)
                        elif t4.saldo > t3.saldo:
                            t4.primeiro = True
                            t3.segundo = True
                            t2.terceiro = True
                            t1.quarto = True
                        else:
                            desempate(4, 3, t3, t4)
                            t2.terceiro = True
                            t1.quarto = True
                    else:
                        if t2.saldo > t4.saldo:
                            desempate(3, t2, t3, 4)
                            if t1.saldo > t4.saldo:
                                t1.terceiro = True
                                t4.quarto = True
                            elif t4.saldo > t1.saldo:
                                t4.terceiro = True
                                t1.quarto = True
                            else:
                                arruma.clear()
                                desempate(t1, 1, 2, t4)
                        elif t4.saldo > t2.saldo:
                            t4.primeiro = True
                            t1.quarto = True
                            desempate(4, t2, t3, 1)
                        else:
                            t1.quarto = True
                            desempate(4, t2, t3, t4)
                else:
                    if t1.saldo > t3.saldo:
                        if t1.saldo > t4.saldo:
                            desempate(t1, t2, 3, 4)
                            if t3.saldo > t4.saldo:
                                t3.terceiro = True
                                t4.quarto = True
                            elif t4.saldo > t3.saldo:
                                t4.terceiro = True
                                t3.quarto = True
                            else:
                                arruma.clear()
                                desempate(1, 2, t3, t4)
                        elif t4.saldo > t1.saldo:
                            t4.primeiro = True
                            t3.quarto = True
                            desempate(t1, t2, 4, 1)
                        else:
                            t3.quarto = True
                            desempate(t1, t2, 4, t4)
                    elif t3.saldo > t1.saldo:
                        if t3.saldo > t4.saldo:
                            t3.primeiro = True
                            if t1.saldo > t4.saldo:
                                t4.quarto = True
                                desempate(t1, t2, 1, 4)
                            elif t4.saldo > t1.saldo:
                                t4.segundo = True
                                desempate(t1, t2, 1, 2)
                            else:
                                desempate(t1, t2, 1, t4)
                        elif t4.saldo > t3.saldo:
                            t4.primeiro = True
                            t3.segundo = True
                            desempate(t1, t2, 2, 1)
                        else:
                            desempate(3, 4, t3, t4)
                            arruma.clear()
                            desempate(t1, t2, 1, 2)
                    else:
                        if t1.saldo > t4.saldo:
                            t4.quarto = True
                            desempate(t1, t2, t3, 4)
                        elif t4.saldo > t1.saldo:
                            t4.primeiro = True
                            desempate(t1, t2, t3, 1)
                        else:
                            if t1.gols_feitos > t2.gols_feitos:
                                if t1.gols_feitos > t3.gols_feitos:
                                    if t1.gols_feitos > t4.gols_feitos:
                                        t1.primeiro = True
                                        if t2.gols_feitos > t3.gols_feitos:
                                            if t2.gols_feitos > t4.gols_feitos:
                                                t2.segundo = True
                                                if t3.gols_feitos > t4.gols_feitos:
                                                    t3.terceiro = True
                                                    t4.quarto = True
                                                elif t4.gols_feitos > t3.gols_feitos:
                                                    t3.quarto = True
                                                    t4.terceiro = True
                                                else:
                                                    desempate(1, 2, t3, t4)
                                            elif t4.gols_feitos > t2.gols_feitos:
                                                t4.segundo = True
                                                t2.terceiro = True
                                                t3.quarto = True
                                            else:
                                                t3.quarto = True
                                                desempate(1, t2, 4, t4)
                                        elif t3.gols_feitos > t2.gols_feitos:
                                            if t3.saldo > t4.saldo:
                                                t3.segundo = True
                                                if t2.gols_feitos > t4.gols_feitos:
                                                    t2.terceiro = True
                                                    t4.quarto = True
                                                elif t4.gols_feitos > t2.gols_feitos:
                                                    t4.terceiro = True
                                                    t2.quarto = True
                                                else:
                                                    desempate(1, t2, 2, t4)
                                            elif t4.gols_feitos > t3.gols_feitos:
                                                t4.segundo = True
                                                t3.terceiro = True
                                                t2.quarto = True
                                            else:
                                                t2.quarto = True
                                                desempate(1, 4, t3, t4)
                                        else:
                                            if t2.gols_feitos > t4.gols_feitos:
                                                t4.quarto = True
                                                desempate(1, t2, t3, 4)
                                            elif t4.gols_feitos > t2.gols_feitos:
                                                t4.segundo = True
                                                desempate(1, t2, t3, 2)
                                            else:
                                                desempate(1, t2, t3, t4)
                                    elif t4.gols_feitos > t1.gols_feitos:
                                        t4.primeiro = True
                                        t1.segundo = True
                                        if t2.gols_feitos > t3.gols_feitos:
                                            t2.terceiro = True
                                            t3.quarto = True
                                        elif t3.gols_feitos > t2.gols_feitos:
                                            t3.terceiro = True
                                            t2.quarto = True
                                        else:
                                            desempate(2, t2, t3, 1)
                                    else:
                                        desempate(t1, 3, 4, t4)
                                        if t2.gols_feitos > t3.gols_feitos:
                                            t2.terceiro = True
                                            t3.quarto = True
                                        elif t3.gols_feitos > t2.gols_feitos:
                                            t3.terceiro = True
                                            t2.quarto = True
                                        else:
                                            arruma.clear()
                                            desempate(2, t2, t3, 1)
                                elif t3.gols_feitos > t1.gols_feitos:
                                    if t3.gols_feitos > t4.gols_feitos:
                                        t3.primeiro = True
                                        if t1.gols_feitos > t4.gols_feitos:
                                            t1.segundo = True
                                            if t2.gols_feitos > t4.gols_feitos:
                                                t2.terceiro = True
                                                t4.quarto = True
                                            elif t4.gols_feitos > t2.gols_feitos:
                                                t4.terceiro = True
                                                t2.quarto = True
                                            else:
                                                desempate(2, t2, 1, t4)
                                        elif t4.gols_feitos > t1.gols_feitos:
                                            t4.segundo = True
                                            t1.terceiro = True
                                            t2.quarto = True
                                        else:
                                            t2.quarto = True
                                            desempate(t1, 4, 1, t4)
                                    elif t4.gols_feitos > t3.gols_feitos:
                                        t4.primeiro = True
                                        t3.segundo = True
                                        t1.terceiro = True
                                        t2.quarto = True
                                    else:
                                        desempate(3, 4, t3, t4)
                                        t1.terceiro = True
                                        t2.quarto = True
                                else:
                                    if t1.gols_feitos > t4.gols_feitos:
                                        desempate(t1, 3, t3, 4)
                                        if t2.gols_feitos > t4.gols_feitos:
                                            t2.terceiro = True
                                            t4.quarto = True
                                        elif t4.gols_feitos > t2.gols_feitos:
                                            t4.terceiro = True
                                            t2.quarto = True
                                        else:
                                            arruma.clear()
                                            desempate(1, t2, 2, t4)
                                    elif t4.gols_feitos > t1.gols_feitos:
                                        t4.primeiro = True
                                        t2.quarto = True
                                        desempate(t1, 4, t3, 1)
                                    else:
                                        t2.quarto = True
                                        desempate(t1, 4, t3, t4)
                            elif t2.gols_feitos > t1.gols_feitos:
                                if t2.gols_feitos > t3.gols_feitos:
                                    if t2.gols_feitos > t4.gols_feitos:
                                        t2.primeiro = True
                                        if t1.gols_feitos > t3.gols_feitos:
                                            if t1.gols_feitos > t4.gols_feitos:
                                                t1.segundo = True
                                                if t3.gols_feitos > t4.gols_feitos:
                                                    t3.terceiro = True
                                                    t4.quarto = True
                                                elif t4.gols_feitos > t3.gols_feitos:
                                                    t3.quarto = True
                                                    t4.terceiro = True
                                                else:
                                                    desempate(2, 1, t3, t4)
                                            elif t4.gols_feitos > t1.gols_feitos:
                                                t4.segundo = True
                                                t1.terceiro = True
                                                t3.quarto = True
                                            else:
                                                t3.quarto = True
                                                desempate(t1, 1, 4, t4)
                                        elif t3.gols_feitos > t1.gols_feitos:
                                            if t3.gols_feitos > t4.gols_feitos:
                                                t3.segundo = True
                                                if t1.gols_feitos > t4.gols_feitos:
                                                    t1.terceiro = True
                                                    t4.quarto = True
                                                elif t4.gols_feitos > t1.gols_feitos:
                                                    t4.terceiro = True
                                                    t1.quarto = True
                                                else:
                                                    desempate(t1, 1, 2, t4)
                                            elif t4.gols_feitos > t3.gols_feitos:
                                                t4.segundo = True
                                                t3.terceiro = True
                                                t1.quarto = True
                                            else:
                                                t1.quarto = True
                                                desempate(4, 1, t3, t4)
                                        else:
                                            if t1.gols_feitos > t4.gols_feitos:
                                                t4.quarto = True
                                                desempate(t1, 1, t3, 4)
                                            elif t4.gols_feitos > t1.gols_feitos:
                                                t4.segundo = True
                                                desempate(t1, 1, t3, 2)
                                            else:
                                                desempate(t1, 1, t3, t4)
                                    elif t4.gols_feitos > t2.gols_feitos:
                                        t4.primeiro = True
                                        t2.segundo = True
                                        if t1.gols_feitos > t3.gols_feitos:
                                            t1.terceiro = True
                                            t3.quarto = True
                                        elif t3.gols_feitos > t1.gols_feitos:
                                            t3.terceiro = True
                                            t1.quarto = True
                                        else:
                                            desempate(t1, 2, t3, 1)
                                    else:
                                        desempate(3, t2, 4, t4)
                                        if t1.gols_feitos > t3.gols_feitos:
                                            t1.terceiro = True
                                            t3.quarto = True
                                        elif t3.gols_feitos > t1.gols_feitos:
                                            t3.terceiro = True
                                            t1.quarto = True
                                        else:
                                            arruma.clear()
                                            desempate(t1, 2, t3, 1)
                                elif t3.gols_feitos > t2.gols_feitos:
                                    if t3.gols_feitos > t4.gols_feitos:
                                        t3.primeiro = True
                                        if t2.gols_feitos > t4.gols_feitos:
                                            t2.segundo = True
                                            if t1.gols_feitos > t4.gols_feitos:
                                                t1.terceiro = True
                                                t4.quarto = True
                                            elif t4.saldo > t1.saldo:
                                                t4.terceiro = True
                                                t1.quarto = True
                                            else:
                                                desempate(t1, 2, 1, t4)
                                        elif t4.gols_feitos > t2.gols_feitos:
                                            t4.segundo = True
                                            t2.terceiro = True
                                            t1.quarto = True
                                        else:
                                            t1.quarto = True
                                            desempate(4, t2, 1, t4)
                                    elif t4.gols_feitos > t3.gols_feitos:
                                        t4.primeiro = True
                                        t3.segundo = True
                                        t2.terceiro = True
                                        t1.quarto = True
                                    else:
                                        desempate(4, 3, t3, t4)
                                        t2.terceiro = True
                                        t1.quarto = True
                                else:
                                    if t2.gols_feitos > t4.gols_feitos:
                                        desempate(3, t2, t3, 4)
                                        if t1.gols_feitos > t4.gols_feitos:
                                            t1.terceiro = True
                                            t4.quarto = True
                                        elif t4.gols_feitos > t1.gols_feitos:
                                            t4.terceiro = True
                                            t1.quarto = True
                                        else:
                                            arruma.clear()
                                            desempate(t1, 1, 2, t4)
                                    elif t4.gols_feitos > t2.gols_feitos:
                                        t4.primeiro = True
                                        t1.quarto = True
                                        desempate(4, t2, t3, 1)
                                    else:
                                        t1.quarto = True
                                        desempate(4, t2, t3, t4)
                            else:
                                if t1.gols_feitos > t3.gols_feitos:
                                    if t1.gols_feitos > t4.gols_feitos:
                                        desempate(t1, t2, 3, 4)
                                        if t3.gols_feitos > t4.gols_feitos:
                                            t3.terceiro = True
                                            t4.quarto = True
                                        elif t4.gols_feitos > t3.gols_feitos:
                                            t4.terceiro = True
                                            t3.quarto = True
                                        else:
                                            arruma.clear()
                                            desempate(1, 2, t3, t4)
                                    elif t4.gols_feitos > t1.gols_feitos:
                                        t4.primeiro = True
                                        t3.quarto = True
                                        desempate(t1, t2, 4, 1)
                                    else:
                                        t3.quarto = True
                                        desempate(t1, t2, 4, t4)
                                elif t3.gols_feitos > t1.gols_feitos:
                                    if t3.gols_feitos > t4.gols_feitos:
                                        t3.primeiro = True
                                        if t1.gols_feitos > t4.gols_feitos:
                                            t4.quarto = True
                                            desempate(t1, t2, 1, 4)
                                        elif t4.gols_feitos > t1.gols_feitos:
                                            t4.segundo = True
                                            desempate(t1, t2, 1, 2)
                                        else:
                                            desempate(t1, t2, 1, t4)
                                    elif t4.gols_feitos > t3.gols_feitos:
                                        t4.primeiro = True
                                        t3.segundo = True
                                        desempate(t1, t2, 2, 1)
                                    else:
                                        desempate(3, 4, t3, t4)
                                        arruma.clear()
                                        desempate(t1, t2, 1, 2)
                                else:
                                    if t1.gols_feitos > t4.gols_feitos:
                                        t4.quarto = True
                                        desempate(t1, t2, t3, 4)
                                    elif t4.gols_feitos > t1.gols_feitos:
                                        t4.primeiro = True
                                        desempate(t1, t2, t3, 1)
                                    else:
                                        a = random.randint(1, 4)
                                        b = random.randint(1, 3)
                                        c = random.randint(1, 2)
                                        if a == 1:
                                            t1.primeiro = True
                                            if b == 1:
                                                t2.segundo = True
                                                if c == 1:
                                                    t3.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t3.quarto = True
                                                    t4.terceiro = True
                                            elif b == 2:
                                                t3.segundo = True
                                                if c == 1:
                                                    t2.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t2.quarto = True
                                                    t4.terceiro = True
                                            elif b == 3:
                                                t4.segundo = True
                                                if c == 1:
                                                    t2.terceiro = True
                                                    t3.quarto = True
                                                elif c == 2:
                                                    t2.quarto = True
                                                    t3.terceiro = True
                                        elif a == 2:
                                            t2.primeiro = True
                                            if b == 1:
                                                t1.segundo = True
                                                if c == 1:
                                                    t3.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t3.quarto = True
                                                    t4.terceiro = True
                                            elif b == 2:
                                                t3.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t4.terceiro = True
                                            elif b == 3:
                                                t4.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t3.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t3.terceiro = True
                                        elif a == 3:
                                            t3.primeiro = True
                                            if b == 1:
                                                t1.segundo = True
                                                if c == 1:
                                                    t2.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t2.quarto = True
                                                    t4.terceiro = True
                                            elif b == 2:
                                                t2.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t4.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t4.terceiro = True
                                            elif b == 3:
                                                t4.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t2.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t2.terceiro = True
                                        elif a == 4:
                                            t4.primeiro = True
                                            if b == 1:
                                                t1.segundo = True
                                                if c == 1:
                                                    t2.terceiro = True
                                                    t3.quarto = True
                                                elif c == 2:
                                                    t2.quarto = True
                                                    t3.terceiro = True
                                            elif b == 2:
                                                t2.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t3.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t3.terceiro = True
                                            elif b == 3:
                                                t3.segundo = True
                                                if c == 1:
                                                    t1.terceiro = True
                                                    t2.quarto = True
                                                elif c == 2:
                                                    t1.quarto = True
                                                    t2.terceiro = True


def acre(seu, seu2, seu3, seu4, grux):
    if seu.primeiro is True:
        grux.append(seu)
    elif seu2.primeiro is True:
        grux.append(seu2)
    elif seu3.primeiro is True:
        grux.append(seu3)
    elif seu4.primeiro is True:
        grux.append(seu4)
    if seu.segundo is True:
        grux.append(seu)
    elif seu2.segundo is True:
        grux.append(seu2)
    elif seu3.segundo is True:
        grux.append(seu3)
    elif seu4.segundo is True:
        grux.append(seu4)
    if seu.terceiro is True:
        grux.append(seu)
    elif seu2.terceiro is True:
        grux.append(seu2)
    elif seu3.terceiro is True:
        grux.append(seu3)
    elif seu4.terceiro is True:
        grux.append(seu4)
    if seu.quarto is True:
        grux.append(seu)
    elif seu2.quarto is True:
        grux.append(seu2)
    elif seu3.quarto is True:
        grux.append(seu3)
    elif seu4.quarto is True:
        grux.append(seu4)


def reseta(um, dois, tres, quatro, grupooo):
    grupooo.clear()
    arruma.clear()
    um.primeiro = False
    um.segundo = False
    um.terceiro = False
    um.quarto = False
    dois.primeiro = False
    dois.segundo = False
    dois.terceiro = False
    dois.quarto = False
    tres.primeiro = False
    tres.segundo = False
    tres.terceiro = False
    tres.quarto = False
    quatro.primeiro = False
    quatro.segundo = False
    quatro.terceiro = False
    quatro.quarto = False


arruma = []

grupoa = []
grupob = []
grupoc = []
grupod = []
grupoe = []
grupof = []
grupog = []
grupoh = []

# R1

jogo_real(sel1, sel4, 1, False)
jogo_real(sel2, sel3, 1, False)
jogo_real(sel5, sel8, 1, False)
jogo_real(sel6, sel7, 1, False)
jogo_real(sel9, sel12, 1, False)
jogo_real(sel10, sel11, 1, False)
jogo_real(sel13, sel16, 1, False)
jogo_real(sel14, sel15, 1, False)
jogo_real(sel17, sel20, 1, False)
jogo_real(sel18, sel19, 1, False)
jogo_real(sel21, sel24, 1, False)
jogo_real(sel22, sel23, 1, False)
jogo_real(sel25, sel28, 1, False)
jogo_real(sel26, sel27, 1, False)
jogo_real(sel29, sel32, 1, False)
jogo_real(sel30, sel31, 1, False)
verificador(sel1, sel2, sel3, sel4)
acre(sel1, sel2, sel3, sel4, grupoa)
print(f'{sel1.nome_sigla} {sel1.pla1} X {sel4.pla1} {sel4.nome_sigla}')
print(f'{sel2.nome_sigla} {sel2.pla1} X {sel3.pla1} {sel3.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoa[0].nome_sigla} {grupoa[0].pontos} {grupoa[0].gols_feitos} {grupoa[0].saldo}')
print(f'2° {grupoa[1].nome_sigla} {grupoa[1].pontos} {grupoa[1].gols_feitos} {grupoa[1].saldo}')
print(f'3° {grupoa[2].nome_sigla} {grupoa[2].pontos} {grupoa[2].gols_feitos} {grupoa[2].saldo}')
print(f'4° {grupoa[3].nome_sigla} {grupoa[3].pontos} {grupoa[3].gols_feitos} {grupoa[3].saldo}')
reseta(sel1, sel2, sel3, sel4, grupoa)
sleep(10)
verificador(sel5, sel6, sel7, sel8)
acre(sel5, sel6, sel7, sel8, grupob)
print(f'{sel5.nome_sigla} {sel5.pla1} X {sel8.pla1} {sel8.nome_sigla}')
print(f'{sel6.nome_sigla} {sel6.pla1} X {sel7.pla1} {sel7.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupob[0].nome_sigla} {grupob[0].pontos} {grupob[0].gols_feitos} {grupob[0].saldo}')
print(f'2° {grupob[1].nome_sigla} {grupob[1].pontos} {grupob[1].gols_feitos} {grupob[1].saldo}')
print(f'3° {grupob[2].nome_sigla} {grupob[2].pontos} {grupob[2].gols_feitos} {grupob[2].saldo}')
print(f'4° {grupob[3].nome_sigla} {grupob[3].pontos} {grupob[3].gols_feitos} {grupob[3].saldo}')
reseta(sel5, sel6, sel7, sel8, grupob)
sleep(10)
verificador(sel9, sel10, sel11, sel12)
acre(sel9, sel10, sel11, sel12, grupoc)
print(f'{sel9.nome_sigla} {sel9.pla1} X {sel12.pla1} {sel12.nome_sigla}')
print(f'{sel10.nome_sigla} {sel10.pla1} X {sel11.pla1} {sel11.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoc[0].nome_sigla} {grupoc[0].pontos} {grupoc[0].gols_feitos} {grupoc[0].saldo}')
print(f'2° {grupoc[1].nome_sigla} {grupoc[1].pontos} {grupoc[1].gols_feitos} {grupoc[1].saldo}')
print(f'3° {grupoc[2].nome_sigla} {grupoc[2].pontos} {grupoc[2].gols_feitos} {grupoc[2].saldo}')
print(f'4° {grupoc[3].nome_sigla} {grupoc[3].pontos} {grupoc[3].gols_feitos} {grupoc[3].saldo}')
reseta(sel9, sel10, sel11, sel12, grupoc)
sleep(10)
verificador(sel13, sel14, sel15, sel16)
acre(sel13, sel14, sel15, sel16, grupod)
print(f'{sel13.nome_sigla} {sel13.pla1} X {sel16.pla1} {sel16.nome_sigla}')
print(f'{sel14.nome_sigla} {sel14.pla1} X {sel15.pla1} {sel15.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupod[0].nome_sigla} {grupod[0].pontos} {grupod[0].gols_feitos} {grupod[0].saldo}')
print(f'2° {grupod[1].nome_sigla} {grupod[1].pontos} {grupod[1].gols_feitos} {grupod[1].saldo}')
print(f'3° {grupod[2].nome_sigla} {grupod[2].pontos} {grupod[2].gols_feitos} {grupod[2].saldo}')
print(f'4° {grupod[3].nome_sigla} {grupod[3].pontos} {grupod[3].gols_feitos} {grupod[3].saldo}')
reseta(sel13, sel14, sel15, sel16, grupod)
sleep(10)
verificador(sel17, sel18, sel19, sel20)
acre(sel17, sel18, sel19, sel20, grupoe)
print(f'{sel17.nome_sigla} {sel17.pla1} X {sel20.pla1} {sel20.nome_sigla}')
print(f'{sel18.nome_sigla} {sel18.pla1} X {sel19.pla1} {sel19.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoe[0].nome_sigla} {grupoe[0].pontos} {grupoe[0].gols_feitos} {grupoe[0].saldo}')
print(f'2° {grupoe[1].nome_sigla} {grupoe[1].pontos} {grupoe[1].gols_feitos} {grupoe[1].saldo}')
print(f'3° {grupoe[2].nome_sigla} {grupoe[2].pontos} {grupoe[2].gols_feitos} {grupoe[2].saldo}')
print(f'4° {grupoe[3].nome_sigla} {grupoe[3].pontos} {grupoe[3].gols_feitos} {grupoe[3].saldo}')
reseta(sel17, sel18, sel19, sel20, grupoe)
sleep(10)
verificador(sel21, sel22, sel23, sel24)
acre(sel21, sel22, sel23, sel24, grupof)
print(f'{sel21.nome_sigla} {sel21.pla1} X {sel24.pla1} {sel24.nome_sigla}')
print(f'{sel22.nome_sigla} {sel22.pla1} X {sel23.pla1} {sel23.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupof[0].nome_sigla} {grupof[0].pontos} {grupof[0].gols_feitos} {grupof[0].saldo}')
print(f'2° {grupof[1].nome_sigla} {grupof[1].pontos} {grupof[1].gols_feitos} {grupof[1].saldo}')
print(f'3° {grupof[2].nome_sigla} {grupof[2].pontos} {grupof[2].gols_feitos} {grupof[2].saldo}')
print(f'4° {grupof[3].nome_sigla} {grupof[3].pontos} {grupof[3].gols_feitos} {grupof[3].saldo}')
reseta(sel21, sel22, sel23, sel24, grupof)
sleep(10)
verificador(sel25, sel26, sel27, sel28)
acre(sel25, sel26, sel27, sel28, grupog)
print(f'{sel25.nome_sigla} {sel25.pla1} X {sel28.pla1} {sel28.nome_sigla}')
print(f'{sel26.nome_sigla} {sel26.pla1} X {sel27.pla1} {sel27.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupog[0].nome_sigla} {grupog[0].pontos} {grupog[0].gols_feitos} {grupog[0].saldo}')
print(f'2° {grupog[1].nome_sigla} {grupog[1].pontos} {grupog[1].gols_feitos} {grupog[1].saldo}')
print(f'3° {grupog[2].nome_sigla} {grupog[2].pontos} {grupog[2].gols_feitos} {grupog[2].saldo}')
print(f'4° {grupog[3].nome_sigla} {grupog[3].pontos} {grupog[3].gols_feitos} {grupog[3].saldo}')
reseta(sel25, sel26, sel27, sel28, grupog)
sleep(10)
verificador(sel29, sel30, sel31, sel32)
acre(sel29, sel30, sel31, sel32, grupoh)
print(f'{sel29.nome_sigla} {sel29.pla1} X {sel32.pla1} {sel32.nome_sigla}')
print(f'{sel30.nome_sigla} {sel30.pla1} X {sel31.pla1} {sel31.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoh[0].nome_sigla} {grupoh[0].pontos} {grupoh[0].gols_feitos} {grupoh[0].saldo}')
print(f'2° {grupoh[1].nome_sigla} {grupoh[1].pontos} {grupoh[1].gols_feitos} {grupoh[1].saldo}')
print(f'3° {grupoh[2].nome_sigla} {grupoh[2].pontos} {grupoh[2].gols_feitos} {grupoh[2].saldo}')
print(f'4° {grupoh[3].nome_sigla} {grupoh[3].pontos} {grupoh[3].gols_feitos} {grupoh[3].saldo}')
reseta(sel29, sel30, sel31, sel32, grupoh)
continua1 = input("Rodada 1: Continuar? \n")
jogo_real(sel1, sel3, 2, False)
jogo_real(sel2, sel4, 2, False)
jogo_real(sel5, sel7, 2, False)
jogo_real(sel6, sel8, 2, False)
jogo_real(sel9, sel11, 2, False)
jogo_real(sel10, sel12, 2, False)
jogo_real(sel13, sel15, 2, False)
jogo_real(sel14, sel16, 2, False)
jogo_real(sel17, sel19, 2, False)
jogo_real(sel18, sel20, 2, False)
jogo_real(sel21, sel23, 2, False)
jogo_real(sel22, sel24, 2, False)
jogo_real(sel25, sel27, 2, False)
jogo_real(sel26, sel28, 2, False)
jogo_real(sel29, sel31, 2, False)
jogo_real(sel30, sel32, 2, False)
verificador(sel1, sel2, sel3, sel4)
acre(sel1, sel2, sel3, sel4, grupoa)
print(f'{sel1.nome_sigla} {sel1.pla1} X {sel4.pla1} {sel4.nome_sigla}')
print(f'{sel2.nome_sigla} {sel2.pla1} X {sel3.pla1} {sel3.nome_sigla}')
print(f'{sel1.nome_sigla} {sel1.pla2} X {sel3.pla2} {sel3.nome_sigla}')
print(f'{sel2.nome_sigla} {sel2.pla2} X {sel4.pla2} {sel4.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoa[0].nome_sigla} {grupoa[0].pontos} {grupoa[0].gols_feitos} {grupoa[0].saldo}')
print(f'2° {grupoa[1].nome_sigla} {grupoa[1].pontos} {grupoa[1].gols_feitos} {grupoa[1].saldo}')
print(f'3° {grupoa[2].nome_sigla} {grupoa[2].pontos} {grupoa[2].gols_feitos} {grupoa[2].saldo}')
print(f'4° {grupoa[3].nome_sigla} {grupoa[3].pontos} {grupoa[3].gols_feitos} {grupoa[3].saldo}')
reseta(sel1, sel2, sel3, sel4, grupoa)
sleep(10)
verificador(sel5, sel6, sel7, sel8)
acre(sel5, sel6, sel7, sel8, grupob)
print(f'{sel5.nome_sigla} {sel5.pla1} X {sel8.pla1} {sel8.nome_sigla}')
print(f'{sel6.nome_sigla} {sel6.pla1} X {sel7.pla1} {sel7.nome_sigla}')
print(f'{sel5.nome_sigla} {sel5.pla2} X {sel7.pla2} {sel7.nome_sigla}')
print(f'{sel6.nome_sigla} {sel6.pla2} X {sel8.pla2} {sel8.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupob[0].nome_sigla} {grupob[0].pontos} {grupob[0].gols_feitos} {grupob[0].saldo}')
print(f'2° {grupob[1].nome_sigla} {grupob[1].pontos} {grupob[1].gols_feitos} {grupob[1].saldo}')
print(f'3° {grupob[2].nome_sigla} {grupob[2].pontos} {grupob[2].gols_feitos} {grupob[2].saldo}')
print(f'4° {grupob[3].nome_sigla} {grupob[3].pontos} {grupob[3].gols_feitos} {grupob[3].saldo}')
reseta(sel5, sel6, sel7, sel8, grupob)
sleep(10)
verificador(sel9, sel10, sel11, sel12)
acre(sel9, sel10, sel11, sel12, grupoc)
print(f'{sel9.nome_sigla} {sel9.pla1} X {sel12.pla1} {sel12.nome_sigla}')
print(f'{sel10.nome_sigla} {sel10.pla1} X {sel11.pla1} {sel11.nome_sigla}')
print(f'{sel9.nome_sigla} {sel9.pla2} X {sel11.pla2} {sel11.nome_sigla}')
print(f'{sel10.nome_sigla} {sel10.pla2} X {sel12.pla2} {sel12.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoc[0].nome_sigla} {grupoc[0].pontos} {grupoc[0].gols_feitos} {grupoc[0].saldo}')
print(f'2° {grupoc[1].nome_sigla} {grupoc[1].pontos} {grupoc[1].gols_feitos} {grupoc[1].saldo}')
print(f'3° {grupoc[2].nome_sigla} {grupoc[2].pontos} {grupoc[2].gols_feitos} {grupoc[2].saldo}')
print(f'4° {grupoc[3].nome_sigla} {grupoc[3].pontos} {grupoc[3].gols_feitos} {grupoc[3].saldo}')
reseta(sel9, sel10, sel11, sel12, grupoc)
sleep(10)
verificador(sel13, sel14, sel15, sel16)
acre(sel13, sel14, sel15, sel16, grupod)
print(f'{sel13.nome_sigla} {sel13.pla1} X {sel16.pla1} {sel16.nome_sigla}')
print(f'{sel14.nome_sigla} {sel14.pla1} X {sel15.pla1} {sel15.nome_sigla}')
print(f'{sel13.nome_sigla} {sel13.pla2} X {sel15.pla2} {sel15.nome_sigla}')
print(f'{sel14.nome_sigla} {sel14.pla2} X {sel16.pla2} {sel16.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupod[0].nome_sigla} {grupod[0].pontos} {grupod[0].gols_feitos} {grupod[0].saldo}')
print(f'2° {grupod[1].nome_sigla} {grupod[1].pontos} {grupod[1].gols_feitos} {grupod[1].saldo}')
print(f'3° {grupod[2].nome_sigla} {grupod[2].pontos} {grupod[2].gols_feitos} {grupod[2].saldo}')
print(f'4° {grupod[3].nome_sigla} {grupod[3].pontos} {grupod[3].gols_feitos} {grupod[3].saldo}')
reseta(sel13, sel14, sel15, sel16, grupod)
sleep(10)
verificador(sel17, sel18, sel19, sel20)
acre(sel17, sel18, sel19, sel20, grupoe)
print(f'{sel17.nome_sigla} {sel17.pla1} X {sel20.pla1} {sel20.nome_sigla}')
print(f'{sel18.nome_sigla} {sel18.pla1} X {sel19.pla1} {sel19.nome_sigla}')
print(f'{sel17.nome_sigla} {sel17.pla2} X {sel19.pla2} {sel19.nome_sigla}')
print(f'{sel18.nome_sigla} {sel18.pla2} X {sel20.pla2} {sel20.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoe[0].nome_sigla} {grupoe[0].pontos} {grupoe[0].gols_feitos} {grupoe[0].saldo}')
print(f'2° {grupoe[1].nome_sigla} {grupoe[1].pontos} {grupoe[1].gols_feitos} {grupoe[1].saldo}')
print(f'3° {grupoe[2].nome_sigla} {grupoe[2].pontos} {grupoe[2].gols_feitos} {grupoe[2].saldo}')
print(f'4° {grupoe[3].nome_sigla} {grupoe[3].pontos} {grupoe[3].gols_feitos} {grupoe[3].saldo}')
reseta(sel17, sel18, sel19, sel20, grupoe)
sleep(10)
verificador(sel21, sel22, sel23, sel24)
acre(sel21, sel22, sel23, sel24, grupof)
print(f'{sel21.nome_sigla} {sel21.pla1} X {sel24.pla1} {sel24.nome_sigla}')
print(f'{sel22.nome_sigla} {sel22.pla1} X {sel23.pla1} {sel23.nome_sigla}')
print(f'{sel21.nome_sigla} {sel21.pla2} X {sel23.pla2} {sel23.nome_sigla}')
print(f'{sel22.nome_sigla} {sel22.pla2} X {sel24.pla2} {sel24.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupof[0].nome_sigla} {grupof[0].pontos} {grupof[0].gols_feitos} {grupof[0].saldo}')
print(f'2° {grupof[1].nome_sigla} {grupof[1].pontos} {grupof[1].gols_feitos} {grupof[1].saldo}')
print(f'3° {grupof[2].nome_sigla} {grupof[2].pontos} {grupof[2].gols_feitos} {grupof[2].saldo}')
print(f'4° {grupof[3].nome_sigla} {grupof[3].pontos} {grupof[3].gols_feitos} {grupof[3].saldo}')
reseta(sel21, sel22, sel23, sel24, grupof)
sleep(10)
verificador(sel25, sel26, sel27, sel28)
acre(sel25, sel26, sel27, sel28, grupog)
print(f'{sel25.nome_sigla} {sel25.pla1} X {sel28.pla1} {sel28.nome_sigla}')
print(f'{sel26.nome_sigla} {sel26.pla1} X {sel27.pla1} {sel27.nome_sigla}')
print(f'{sel25.nome_sigla} {sel25.pla2} X {sel27.pla2} {sel27.nome_sigla}')
print(f'{sel26.nome_sigla} {sel26.pla2} X {sel28.pla2} {sel28.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupog[0].nome_sigla} {grupog[0].pontos} {grupog[0].gols_feitos} {grupog[0].saldo}')
print(f'2° {grupog[1].nome_sigla} {grupog[1].pontos} {grupog[1].gols_feitos} {grupog[1].saldo}')
print(f'3° {grupog[2].nome_sigla} {grupog[2].pontos} {grupog[2].gols_feitos} {grupog[2].saldo}')
print(f'4° {grupog[3].nome_sigla} {grupog[3].pontos} {grupog[3].gols_feitos} {grupog[3].saldo}')
reseta(sel25, sel26, sel27, sel28, grupog)
sleep(10)
verificador(sel29, sel30, sel31, sel32)
acre(sel29, sel30, sel31, sel32, grupoh)
print(f'{sel29.nome_sigla} {sel29.pla1} X {sel32.pla1} {sel32.nome_sigla}')
print(f'{sel30.nome_sigla} {sel30.pla1} X {sel31.pla1} {sel31.nome_sigla}')
print(f'{sel29.nome_sigla} {sel29.pla2} X {sel31.pla2} {sel31.nome_sigla}')
print(f'{sel30.nome_sigla} {sel30.pla2} X {sel32.pla2} {sel32.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoh[0].nome_sigla} {grupoh[0].pontos} {grupoh[0].gols_feitos} {grupoh[0].saldo}')
print(f'2° {grupoh[1].nome_sigla} {grupoh[1].pontos} {grupoh[1].gols_feitos} {grupoh[1].saldo}')
print(f'3° {grupoh[2].nome_sigla} {grupoh[2].pontos} {grupoh[2].gols_feitos} {grupoh[2].saldo}')
print(f'4° {grupoh[3].nome_sigla} {grupoh[3].pontos} {grupoh[3].gols_feitos} {grupoh[3].saldo}')
reseta(sel29, sel30, sel31, sel32, grupoh)
continua2 = input("Rodada 2: Continuar? \n")
jogo_real(sel1, sel2, 3, False)
jogo_real(sel3, sel4, 3, False)
jogo_real(sel5, sel6, 3, False)
jogo_real(sel7, sel8, 3, False)
jogo_real(sel9, sel10, 3, False)
jogo_real(sel11, sel12, 3, False)
jogo_real(sel13, sel14, 3, False)
jogo_real(sel15, sel16, 3, False)
jogo_real(sel17, sel18, 3, False)
jogo_real(sel19, sel20, 3, False)
jogo_real(sel21, sel22, 3, False)
jogo_real(sel23, sel24, 3, False)
jogo_real(sel25, sel26, 3, False)
jogo_real(sel27, sel28, 3, False)
jogo_real(sel29, sel30, 3, False)
jogo_real(sel31, sel32, 3, False)
verificador(sel1, sel2, sel3, sel4)
acre(sel1, sel2, sel3, sel4, grupoa)
print(f'{sel1.nome_sigla} {sel1.pla1} X {sel4.pla1} {sel4.nome_sigla}')
print(f'{sel2.nome_sigla} {sel2.pla1} X {sel3.pla1} {sel3.nome_sigla}')
print(f'{sel1.nome_sigla} {sel1.pla2} X {sel3.pla2} {sel3.nome_sigla}')
print(f'{sel2.nome_sigla} {sel2.pla2} X {sel4.pla2} {sel4.nome_sigla}')
print(f'{sel1.nome_sigla} {sel1.pla3} X {sel2.pla3} {sel2.nome_sigla}')
print(f'{sel3.nome_sigla} {sel3.pla3} X {sel4.pla3} {sel4.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoa[0].nome_sigla} {grupoa[0].pontos} {grupoa[0].gols_feitos} {grupoa[0].saldo}')
print(f'2° {grupoa[1].nome_sigla} {grupoa[1].pontos} {grupoa[1].gols_feitos} {grupoa[1].saldo}')
print(f'3° {grupoa[2].nome_sigla} {grupoa[2].pontos} {grupoa[2].gols_feitos} {grupoa[2].saldo}')
print(f'4° {grupoa[3].nome_sigla} {grupoa[3].pontos} {grupoa[3].gols_feitos} {grupoa[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel5, sel6, sel7, sel8)
acre(sel5, sel6, sel7, sel8, grupob)
print(f'{sel5.nome_sigla} {sel5.pla1} X {sel8.pla1} {sel8.nome_sigla}')
print(f'{sel6.nome_sigla} {sel6.pla1} X {sel7.pla1} {sel7.nome_sigla}')
print(f'{sel5.nome_sigla} {sel5.pla2} X {sel7.pla2} {sel7.nome_sigla}')
print(f'{sel6.nome_sigla} {sel6.pla2} X {sel8.pla2} {sel8.nome_sigla}')
print(f'{sel5.nome_sigla} {sel5.pla3} X {sel6.pla3} {sel6.nome_sigla}')
print(f'{sel7.nome_sigla} {sel7.pla3} X {sel8.pla3} {sel8.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupob[0].nome_sigla} {grupob[0].pontos} {grupob[0].gols_feitos} {grupob[0].saldo}')
print(f'2° {grupob[1].nome_sigla} {grupob[1].pontos} {grupob[1].gols_feitos} {grupob[1].saldo}')
print(f'3° {grupob[2].nome_sigla} {grupob[2].pontos} {grupob[2].gols_feitos} {grupob[2].saldo}')
print(f'4° {grupob[3].nome_sigla} {grupob[3].pontos} {grupob[3].gols_feitos} {grupob[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel9, sel10, sel11, sel12)
acre(sel9, sel10, sel11, sel12, grupoc)
print(f'{sel9.nome_sigla} {sel9.pla1} X {sel12.pla1} {sel12.nome_sigla}')
print(f'{sel10.nome_sigla} {sel10.pla1} X {sel11.pla1} {sel11.nome_sigla}')
print(f'{sel9.nome_sigla} {sel9.pla2} X {sel11.pla2} {sel11.nome_sigla}')
print(f'{sel10.nome_sigla} {sel10.pla2} X {sel12.pla2} {sel12.nome_sigla}')
print(f'{sel9.nome_sigla} {sel9.pla3} X {sel10.pla3} {sel10.nome_sigla}')
print(f'{sel11.nome_sigla} {sel11.pla3} X {sel12.pla3} {sel12.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoc[0].nome_sigla} {grupoc[0].pontos} {grupoc[0].gols_feitos} {grupoc[0].saldo}')
print(f'2° {grupoc[1].nome_sigla} {grupoc[1].pontos} {grupoc[1].gols_feitos} {grupoc[1].saldo}')
print(f'3° {grupoc[2].nome_sigla} {grupoc[2].pontos} {grupoc[2].gols_feitos} {grupoc[2].saldo}')
print(f'4° {grupoc[3].nome_sigla} {grupoc[3].pontos} {grupoc[3].gols_feitos} {grupoc[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel13, sel14, sel15, sel16)
acre(sel13, sel14, sel15, sel16, grupod)
print(f'{sel13.nome_sigla} {sel13.pla1} X {sel16.pla1} {sel16.nome_sigla}')
print(f'{sel14.nome_sigla} {sel14.pla1} X {sel15.pla1} {sel15.nome_sigla}')
print(f'{sel13.nome_sigla} {sel13.pla2} X {sel15.pla2} {sel15.nome_sigla}')
print(f'{sel14.nome_sigla} {sel14.pla2} X {sel16.pla2} {sel16.nome_sigla}')
print(f'{sel13.nome_sigla} {sel13.pla3} X {sel14.pla3} {sel14.nome_sigla}')
print(f'{sel15.nome_sigla} {sel15.pla3} X {sel16.pla3} {sel16.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupod[0].nome_sigla} {grupod[0].pontos} {grupod[0].gols_feitos} {grupod[0].saldo}')
print(f'2° {grupod[1].nome_sigla} {grupod[1].pontos} {grupod[1].gols_feitos} {grupod[1].saldo}')
print(f'3° {grupod[2].nome_sigla} {grupod[2].pontos} {grupod[2].gols_feitos} {grupod[2].saldo}')
print(f'4° {grupod[3].nome_sigla} {grupod[3].pontos} {grupod[3].gols_feitos} {grupod[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel17, sel18, sel19, sel20)
acre(sel17, sel18, sel19, sel20, grupoe)
print(f'{sel17.nome_sigla} {sel17.pla1} X {sel20.pla1} {sel20.nome_sigla}')
print(f'{sel18.nome_sigla} {sel18.pla1} X {sel19.pla1} {sel19.nome_sigla}')
print(f'{sel17.nome_sigla} {sel17.pla2} X {sel19.pla2} {sel19.nome_sigla}')
print(f'{sel18.nome_sigla} {sel18.pla2} X {sel20.pla2} {sel20.nome_sigla}')
print(f'{sel17.nome_sigla} {sel17.pla3} X {sel18.pla3} {sel18.nome_sigla}')
print(f'{sel19.nome_sigla} {sel19.pla3} X {sel20.pla3} {sel20.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoe[0].nome_sigla} {grupoe[0].pontos} {grupoe[0].gols_feitos} {grupoe[0].saldo}')
print(f'2° {grupoe[1].nome_sigla} {grupoe[1].pontos} {grupoe[1].gols_feitos} {grupoe[1].saldo}')
print(f'3° {grupoe[2].nome_sigla} {grupoe[2].pontos} {grupoe[2].gols_feitos} {grupoe[2].saldo}')
print(f'4° {grupoe[3].nome_sigla} {grupoe[3].pontos} {grupoe[3].gols_feitos} {grupoe[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel21, sel22, sel23, sel24)
acre(sel21, sel22, sel23, sel24, grupof)
print(f'{sel21.nome_sigla} {sel21.pla1} X {sel24.pla1} {sel24.nome_sigla}')
print(f'{sel22.nome_sigla} {sel22.pla1} X {sel23.pla1} {sel23.nome_sigla}')
print(f'{sel21.nome_sigla} {sel21.pla2} X {sel23.pla2} {sel23.nome_sigla}')
print(f'{sel22.nome_sigla} {sel22.pla2} X {sel24.pla2} {sel24.nome_sigla}')
print(f'{sel21.nome_sigla} {sel21.pla3} X {sel22.pla3} {sel22.nome_sigla}')
print(f'{sel23.nome_sigla} {sel23.pla3} X {sel24.pla3} {sel24.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupof[0].nome_sigla} {grupof[0].pontos} {grupof[0].gols_feitos} {grupof[0].saldo}')
print(f'2° {grupof[1].nome_sigla} {grupof[1].pontos} {grupof[1].gols_feitos} {grupof[1].saldo}')
print(f'3° {grupof[2].nome_sigla} {grupof[2].pontos} {grupof[2].gols_feitos} {grupof[2].saldo}')
print(f'4° {grupof[3].nome_sigla} {grupof[3].pontos} {grupof[3].gols_feitos} {grupof[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel25, sel26, sel27, sel28)
acre(sel25, sel26, sel27, sel28, grupog)
print(f'{sel25.nome_sigla} {sel25.pla1} X {sel28.pla1} {sel28.nome_sigla}')
print(f'{sel26.nome_sigla} {sel26.pla1} X {sel27.pla1} {sel27.nome_sigla}')
print(f'{sel25.nome_sigla} {sel25.pla2} X {sel27.pla2} {sel27.nome_sigla}')
print(f'{sel26.nome_sigla} {sel26.pla2} X {sel28.pla2} {sel28.nome_sigla}')
print(f'{sel25.nome_sigla} {sel25.pla3} X {sel26.pla3} {sel26.nome_sigla}')
print(f'{sel27.nome_sigla} {sel27.pla3} X {sel28.pla3} {sel28.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupog[0].nome_sigla} {grupog[0].pontos} {grupog[0].gols_feitos} {grupog[0].saldo}')
print(f'2° {grupog[1].nome_sigla} {grupog[1].pontos} {grupog[1].gols_feitos} {grupog[1].saldo}')
print(f'3° {grupog[2].nome_sigla} {grupog[2].pontos} {grupog[2].gols_feitos} {grupog[2].saldo}')
print(f'4° {grupog[3].nome_sigla} {grupog[3].pontos} {grupog[3].gols_feitos} {grupog[3].saldo}')
arruma.clear()
sleep(10)
verificador(sel29, sel30, sel31, sel32)
acre(sel29, sel30, sel31, sel32, grupoh)
print(f'{sel29.nome_sigla} {sel29.pla1} X {sel32.pla1} {sel32.nome_sigla}')
print(f'{sel30.nome_sigla} {sel30.pla1} X {sel31.pla1} {sel31.nome_sigla}')
print(f'{sel29.nome_sigla} {sel29.pla2} X {sel31.pla2} {sel31.nome_sigla}')
print(f'{sel30.nome_sigla} {sel30.pla2} X {sel32.pla2} {sel32.nome_sigla}')
print(f'{sel29.nome_sigla} {sel29.pla3} X {sel30.pla3} {sel30.nome_sigla}')
print(f'{sel31.nome_sigla} {sel31.pla3} X {sel32.pla3} {sel32.nome_sigla}')
print("  NOM: P G S")
print(f'1° {grupoh[0].nome_sigla} {grupoh[0].pontos} {grupoh[0].gols_feitos} {grupoh[0].saldo}')
print(f'2° {grupoh[1].nome_sigla} {grupoh[1].pontos} {grupoh[1].gols_feitos} {grupoh[1].saldo}')
print(f'3° {grupoh[2].nome_sigla} {grupoh[2].pontos} {grupoh[2].gols_feitos} {grupoh[2].saldo}')
print(f'4° {grupoh[3].nome_sigla} {grupoh[3].pontos} {grupoh[3].gols_feitos} {grupoh[3].saldo}')
continua3 = input("Rodada 3: Continuar? \n")
arruma.clear()

# MATA-MATA

quartas = []
print("Oitavas de Final:")
sleep(3)

jogo_real(grupoa[0], grupob[1], 4, True)  # A1xB2
jogo_real(grupoc[0], grupod[1], 4, True)  # C1xD2
jogo_real(grupoe[0], grupof[1], 4, True)  # E1xF2
jogo_real(grupog[0], grupoh[1], 4, True)  # G1xH2

jogo_real(grupob[0], grupoa[1], 4, True)  # A2xB1
jogo_real(grupod[0], grupoc[1], 4, True)  # C2xD1
jogo_real(grupof[0], grupoe[1], 4, True)  # E2xF1
jogo_real(grupoh[0], grupog[1], 4, True)  # G2xH1

if grupoa[0].pen4 > 0 or grupob[1].pen4 > 0:
    print(f'{grupoa[0].nome_sigla} {grupoa[0].pla4}({grupoa[0].pen4}) X ({grupob[1].pen4}){grupob[1].pla4} '
          f'{grupob[1].nome_sigla}')
else:
    print(f'{grupoa[0].nome_sigla} {grupoa[0].pla4} X {grupob[1].pla4} {grupob[1].nome_sigla}')
if grupoc[0].pen4 > 0 or grupod[1].pen4 > 0:
    print(f'{grupoc[0].nome_sigla} {grupoc[0].pla4}({grupoc[0].pen4}) X ({grupod[1].pen4}){grupod[1].pla4} '
          f'{grupod[1].nome_sigla}')
else:
    print(f'{grupoc[0].nome_sigla} {grupoc[0].pla4} X {grupod[1].pla4} {grupod[1].nome_sigla}')
if grupoe[0].pen4 > 0 or grupof[1].pen4 > 0:
    print(f'{grupoe[0].nome_sigla} {grupoe[0].pla4}({grupoe[0].pen4}) X ({grupof[1].pen4}){grupof[1].pla4} '
          f'{grupof[1].nome_sigla}')
else:
    print(f'{grupoe[0].nome_sigla} {grupoe[0].pla4} X {grupof[1].pla4} {grupof[1].nome_sigla}')
if grupog[0].pen4 > 0 or grupoh[1].pen4 > 0:
    print(f'{grupog[0].nome_sigla} {grupog[0].pla4}({grupog[0].pen4}) X ({grupoh[1].pen4}){grupoh[1].pla4} '
          f'{grupoh[1].nome_sigla}')
else:
    print(f'{grupog[0].nome_sigla} {grupog[0].pla4} X {grupoh[1].pla4} {grupoh[1].nome_sigla}')
if grupob[0].pen4 > 0 or grupoa[1].pen4 > 0:
    print(f'{grupob[0].nome_sigla} {grupob[0].pla4}({grupob[0].pen4}) X ({grupoa[1].pen4}){grupoa[1].pla4} '
          f'{grupoa[1].nome_sigla}')
else:
    print(f'{grupob[0].nome_sigla} {grupob[0].pla4} X {grupoa[1].pla4} {grupoa[1].nome_sigla}')
if grupod[0].pen4 > 0 or grupoc[1].pen4 > 0:
    print(f'{grupod[0].nome_sigla} {grupod[0].pla4}({grupod[0].pen4}) X ({grupoc[1].pen4}){grupoc[1].pla4} '
          f'{grupoc[1].nome_sigla}')
else:
    print(f'{grupod[0].nome_sigla} {grupod[0].pla4} X {grupoc[1].pla4} {grupoc[1].nome_sigla}')
if grupof[0].pen4 > 0 or grupoe[1].pen4 > 0:
    print(f'{grupof[0].nome_sigla} {grupof[0].pla4}({grupof[0].pen4}) X ({grupoe[1].pen4}){grupoe[1].pla4} '
          f'{grupoe[1].nome_sigla}')
else:
    print(f'{grupof[0].nome_sigla} {grupof[0].pla4} X {grupoe[1].pla4} {grupoe[1].nome_sigla}')
if grupoh[0].pen4 > 0 or grupog[1].pen4 > 0:
    print(f'{grupoh[0].nome_sigla} {grupoh[0].pla4}({grupoh[0].pen4}) X ({grupog[1].pen4}){grupog[1].pla4} '
          f'{grupog[1].nome_sigla}')
else:
    print(f'{grupoh[0].nome_sigla} {grupoh[0].pla4} X {grupog[1].pla4} {grupog[1].nome_sigla}')

continua4 = input("Quartas de Final a frente. Continuar? \n")
# Quartas

semis = []

jogo_real(quartas[0], quartas[1], 5, True)
jogo_real(quartas[2], quartas[3], 5, True)
jogo_real(quartas[4], quartas[5], 5, True)
jogo_real(quartas[6], quartas[7], 5, True)

if quartas[0].pen5 > 0 or quartas[1].pen5 > 0:
    print(f'{quartas[0].nome_sigla} {quartas[0].pla5}({quartas[0].pen5}) X ({quartas[1].pen5}){quartas[1].pla5} '
          f'{quartas[1].nome_sigla}')
else:
    print(f'{quartas[0].nome_sigla} {quartas[0].pla5} X {quartas[1].pla5} {quartas[1].nome_sigla}')
if quartas[2].pen5 > 0 or quartas[3].pen5 > 0:
    print(f'{quartas[2].nome_sigla} {quartas[2].pla5}({quartas[2].pen5}) X ({quartas[3].pen5}){quartas[3].pla5} '
          f'{quartas[3].nome_sigla}')
else:
    print(f'{quartas[2].nome_sigla} {quartas[2].pla5} X {quartas[3].pla5} {quartas[3].nome_sigla}')
if quartas[4].pen5 > 0 or quartas[5].pen5 > 0:
    print(f'{quartas[4].nome_sigla} {quartas[4].pla5}({quartas[4].pen5}) X ({quartas[5].pen5}){quartas[5].pla5} '
          f'{quartas[5].nome_sigla}')
else:
    print(f'{quartas[4].nome_sigla} {quartas[4].pla5} X {quartas[5].pla5} {quartas[5].nome_sigla}')
if quartas[6].pen5 > 0 or quartas[7].pen5 > 0:
    print(f'{quartas[6].nome_sigla} {quartas[6].pla5}({quartas[6].pen5}) X ({quartas[7].pen5}){quartas[7].pla5} '
          f'{quartas[7].nome_sigla}')
else:
    print(f'{quartas[6].nome_sigla} {quartas[6].pla5} X {quartas[7].pla5} {quartas[7].nome_sigla}')

# SEMIFINAIS

final = []
continua5 = input("Semifinal a frente. Continuar? \n")

jogo_real(semis[0], semis[1], 6, True)
jogo_real(semis[2], semis[3], 6, True)

if semis[0].pen6 > 0 or semis[1].pen6 > 0:
    print(f'{semis[0].nome_sigla} {semis[0].pla6}({semis[0].pen6}) X ({semis[1].pen6}){semis[1].pla6} '
          f'{semis[1].nome_sigla}')
else:
    print(f'{semis[0].nome_sigla} {semis[0].pla6} X {semis[1].pla6} {semis[1].nome_sigla}')
if semis[2].pen5 > 0 or semis[3].pen5 > 0:
    print(f'{semis[2].nome_sigla} {semis[2].pla6}({semis[2].pen6}) X ({semis[3].pen6}){semis[3].pla6} '
          f'{semis[3].nome_sigla}')
else:
    print(f'{semis[2].nome_sigla} {semis[2].pla6} X {semis[3].pla6} {semis[3].nome_sigla}')

# FINAL

continua6 = input("Grande Final a frente. Continuar? \n")

jogo_real(final[0], final[1], 7, True)
