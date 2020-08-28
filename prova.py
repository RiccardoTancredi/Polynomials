
class polinomio:
    def __init__(self, coefficienti: list):
        self.coefficienti = coefficienti
        self.grado = 0 if len(self.coefficienti) == 0 else len(self.coefficienti) - 1
        self.c = []
    # scrittura del polinomio:
    def __str__(self):
        output = ""
        for i in range(0, len(self.coefficienti)):
            # and x[grado_polinomio]!=0):
            if (((self.coefficienti[i] == 1 or self.coefficienti[i] == 1.0) and self.grado-i == 1)):
                output += "x"
            if self.grado-i == 1 and (self.coefficienti[i] != 0 and self.coefficienti[i] != 1 and self.coefficienti[i] != -1 and self.coefficienti[i] != 1.0 and self.coefficienti[i] != -1.0):
                output += "{}x".format(self.coefficienti[i])
            if self.coefficienti[i] == 0:
                pass
                # continue
            if self.grado-i != 0 and self.grado-i != 1 and (self.coefficienti[i] != 0 and self.coefficienti[i] != 1 and self.coefficienti[i] != -1 and self.coefficienti[i] != 1.0 and self.coefficienti[i] != -1.0):
                output += "{}x^{}".format(
                    self.coefficienti[i], self.grado-i)
                # continue
                #print(x[i], "$x^", grado_polinomio-i, "$ + ")
            if (self.coefficienti[i] == 1 or self.coefficienti[i] == 1.0) and self.grado-i != 1 and self.grado-i != 0:
                output += "x^{}".format(self.grado-i)
                # continue
            elif (self.coefficienti[i] == -1 or self.coefficienti[i] == -1.0) and self.grado-i != 1 and self.grado-i != 0:
                output += "-x^{}".format(self.grado-i)
                # continue
            elif self.coefficienti[i] != 0 and self.grado-i == 0:
                output += "{}".format(self.coefficienti[i])
            # and x[grado_polinomio]!=0):
            if ((self.coefficienti[i] == -1 or self.coefficienti[i] == -1.0) and self.grado-i == 1):
                output += "-x"
            if self.grado-i == 1 and (self.coefficienti[i] != 0 and (self.coefficienti[i] != -1 or self.coefficienti[i] != -1.0) and (self.coefficienti[i] != 1 or self.coefficienti[i] != 1.0)):
                output += "{}x".format(self.coefficienti[i])
            if i != self.grado and self.coefficienti[i+1] != 0:
                output += " + "
                continue
        return output

    def __add__(self, y):
        if type(y).__name__ != "polinomio":
            raise Exception(
                f"You are trying to sum a polinomio with a {type(y).__name__}")

        c = []
        n = min(len(self.coefficienti), len(y.coefficienti))
        m = max(len(self.coefficienti), len(y.coefficienti))
        d = []
        if m == len(self.coefficienti):
            d = self.coefficienti
        else:
            d = y.coefficienti
        for i in range(0, m-n):
            c.append(d[i])
        if m == len(self.coefficienti):
            for j in range(m-n, m):
                z = self.coefficienti[j] + y.coefficienti[j-m+n]
                c.append(z)
        else:
            for j in range(m-n, m):
                z = self.coefficienti[j-m+n] + y.coefficienti[j]
                c.append(z)
        return polinomio(c)  # si può fare (return print)?

    def __sub__(self, y):
        c = []
        for i in y.coefficienti:
            c.append(-i)
        f = self.coefficienti + c
        return polinomio(f)

    def __mul__(self, y):
        grado_prodotto = self.grado + y.grado
        d = [[], []]
        for i in range(len(self.coefficienti)):
            for j in range(len(y.coefficienti)):
                d[0].append(self.coefficienti[i]*y.coefficienti[j])
                d[1].append(i+j)  # grado del monomio
        d[1] = d[1][::-1]
        # print(d)
        for i in range(grado_prodotto+1):
            if d[1].count(grado_prodotto-i) > 1:
                j = d[1].index(grado_prodotto - i)
                #print("j vale: ", j)
                z = j+1
                while z < len(d[1]):
                    if d[1][z] == d[1][j]:
                        #print("z vale:", z)
                        d[0][j] = d[0][j]+d[0][z]
                        d[1].pop(z)
                        d[0].pop(z)
                        # print(d)
                    z += 1
        return polinomio(d[0])

    def __pow__(self, var:int):
        p = self
        i = 0
        while i < var-1:
            p *= self
            i += 1
        return p

    def __truediv__(self, y):
        # if isinstance(self, list) == True:
        #     self.c.append(self[0].coefficienti)
        #     self = self[0]
        i, j = 0, 0
        while i < len(self.coefficienti):
            if self.coefficienti[0] == 0:
                self.coefficienti.pop(0)
            i += 1
        while j < len(y.coefficienti):
            if y.coefficienti[0] == 0:
                y.coefficienti.pop(0)
            j += 1

        d = [[], []]
        s = self.grado
        v = y.grado
        grado_polinomio_risultante = s-v
        #output = ""
        if s < v:
            print(polinomio(self.c), "+ (", self,")/(", polinomio(y),")" )
            # output += str()  # capisce che questo è un polinomio???
            # output += "+"
            # output += "("+str(self.coefficienti)+")"
            # output += "/"
            # output += str(polinomio(y))  # capisce che questo è un polinomio???
            # return output
        elif s == 0:
            return polinomio(self.c)
        else:
            d[1].append(grado_polinomio_risultante)
            d[0].append(self.coefficienti[0]/y.coefficienti[0])
            for i in range(0, grado_polinomio_risultante):
                d[0].append(0)
            self.c.append(d[0][0])
            #g = polinomio.prodotto(d[0], y)
            a = polinomio(d[0])
            g = a*y
            if len(g.coefficienti) != len(self.coefficienti):
                e = 0
                # for e in range(0, len(self.coefficienti)-len(g.coefficienti)):
                while e < len(self.coefficienti)-len(g.coefficienti):
                    g.coefficienti.append(0)
                    e += 1
            # print(g)
            f = self-g
            i = 0
            while i < len(f.coefficienti):
                if f.coefficienti[0] == 0:
                    f.coefficienti.pop(0)
                i += 1
            if (f.grado - y.grado) == 0 and (len(f.coefficienti)-len(self.c)) > 1:
                self.c.append(0)
            # ??? e mo? __truediv__ prende 2 argomenti, ma io ne voglio 3
            f / y
            #return  list(q, q/y)


# x = [1, 1, 2, 1, 1]
# y = [1, 1, 2, 1, 1]
# x = [1,0,1]
# y = [1,0,1]
# c = polinomio(x)
# d = polinomio(y)
# #print(c == d) #ToDo 
# print(c*d)
# print(c.grado)
# print(c**2)
x = [1,0,2,0,1]
y = [1,0,1]
c = polinomio(x)
d = polinomio(y)
print(c / d)
