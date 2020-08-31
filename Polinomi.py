
class polinomio:
    def __init__(self, coefficienti: list):
        self.coefficienti = coefficienti
        self.grado = 0 if len(self.coefficienti) == 0 else len(
            self.coefficienti) - 1
        i = 0
        while i < len(self.coefficienti):
            if self.coefficienti[0] == 0:
                self.coefficienti.pop(0)
            i += 1

    # scrittura del polinomio:
    def __str__(self):
        output = ""
        for i in range(0, len(self.coefficienti)):
            # and x[grado_polinomio]!=0):
            if (((self.coefficienti[i] == 1 or self.coefficienti[i] == 1.0) and self.grado-i == 1)):
                output += "x "
            if self.grado-i == 1 and (self.coefficienti[i] != 0 and self.coefficienti[i] != 1 and self.coefficienti[i] != -1 and self.coefficienti[i] != 1.0 and self.coefficienti[i] != -1.0):
                output += "{}x ".format(self.coefficienti[i])
            if self.coefficienti[i] == 0:
                pass
                # continue
            if self.grado-i != 0 and self.grado-i != 1 and (self.coefficienti[i] != 0 and self.coefficienti[i] != 1 and self.coefficienti[i] != -1 and self.coefficienti[i] != 1.0 and self.coefficienti[i] != -1.0):
                output += "{}x^{} ".format(
                    self.coefficienti[i], self.grado-i)
                # continue
                #print(x[i], "$x^", grado_polinomio-i, "$ + ")
            if (self.coefficienti[i] == 1 or self.coefficienti[i] == 1.0) and self.grado-i != 1 and self.grado-i != 0:
                output += "x^{} ".format(self.grado-i)
                # continue
            elif (self.coefficienti[i] == -1 or self.coefficienti[i] == -1.0) and self.grado-i != 1 and self.grado-i != 0:
                output += "- x^{} ".format(self.grado-i)
                # continue
            elif self.coefficienti[i] != 0 and self.grado-i == 0 and (self.coefficienti[i] != 1 or self.coefficienti[i] != 1.0):
                output += "{} ".format(self.coefficienti[i])
            elif self.coefficienti[i] != 0 and self.grado-i == 0 and (self.coefficienti[i] == 1 or self.coefficienti[i] == 1.0):
                output += "1 "
            if ((self.coefficienti[i] == -1 or self.coefficienti[i] == -1.0) and self.grado-i == 1):
                output += "- x "
            if (i != self.grado and self.grado-i != 0) and self.coefficienti[i+1] > 0:
                output += "+ "
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
        i = 0
        while i < len(c):
            if c[0] == 0:
                c.pop(0)
            i += 1
        d = polinomio(c)
        return d

    def __sub__(self, y):
        c = []
        for i in y.coefficienti:
            c.append(-i)
        f = self + polinomio(c)
        return f

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
        i = 0
        while i < len(d[0]):
            if d[0][0] == 0:
                d[0].pop(0)
            i += 1
        return polinomio(d[0])

    def __pow__(self, var: int):
        p = self
        i = 0
        while i < var-1:
            p *= self
            i += 1
        return p

    def __truediv__(self, y, c=[]):
        d = []
        s = self.grado
        v = y.grado
        grado_polinomio_risultante = s-v
        output = ""
        if grado_polinomio_risultante > 0:
            d.append(self.coefficienti[0]/y.coefficienti[0])
            i = 0
            while i < grado_polinomio_risultante:
                d.append(0)
                i += 1
            c.append(d[0])
            a = polinomio(d)
            g = a*y
            f = self - g
            if (f.grado - y.grado) == 0 and (len(f.coefficienti)-len(c)) > 1:
                c.append(0)
            if (f.grado-y.grado) < 0 and f.grado != 0:
                j = 0
                while j < y.grado-f.grado:
                    c.append(0)
            self = f
            return f.__truediv__(y, c)
        elif grado_polinomio_risultante == 0:
            d.append(self.coefficienti[0]/y.coefficienti[0])
            c.append(d[0])
            a = polinomio(d)
            g = a*y
            f = self - g
            if f.grado == 0 and (f.coefficienti == [] or f.coefficienti[0] == 0):
                d = list(c)
                k = 0
                while k < len(c):
                    c.pop(0)
                    k += 1
                return polinomio(d)
            elif f.grado >= 0:
                self = f
                return f.__truediv__(y, c)
        elif grado_polinomio_risultante < 0:
            d = list(c)
            if polinomio(d).grado != 0:
                output += str(polinomio(d))
            if polinomio(d).grado != 0:
                output += "+"
            output += "(" + str(self) + ")/("
            output += str(y) + ")"
            k = 0
            while k < len(c):
                c.pop(0)
                k += 1
            return output

        elif s == 0:
            d = list(c)
            k = 0
            while k < len(c):
                c.pop(0)
                k += 1
            return polinomio(d)

    def __eq__(self, y):
        equality = 0
        if len(self.coefficienti) != len(y.coefficienti):
            return False
        for i in range(len(self.coefficienti)):
            if self.coefficienti[i] == y.coefficienti[i]:
                equality += 1
        if equality == len(self.coefficienti):
            return True
        else:
            return False

    def __ne__(self, y):
        inequality = 0
        if len(self.coefficienti) != len(y.coefficienti):
            return True
        else:
            for i in range(len(self.coefficienti)):
                if self.coefficienti[i] != y.coefficienti[i]:
                    inequality += 1
            if inequality == len(self.coefficienti):
                return True
            else:
                return False


x = [1, 1, 2, 1, 1]
y = [1, 1, 2, 1, 1]
c = polinomio(x)
d = polinomio(y)
print(c+d)
print(c==d)
x = [1,2,1]
y = [1,1]
c = polinomio(x)
d = polinomio(y)
print(c == d)
print(c != d)
x = [1, 0, 2, 0, 1]
y = [1, 0, 1]
c = polinomio(x)
d = polinomio(y)
h = c/d
print(h)
x =  [1,1,1]
y = [1,0]
c = polinomio(x)
d = polinomio(y)
g = c*d
print(g)
x = [1]
y = [1,1]
c = polinomio(x)
d = polinomio(y)
g = c/d
print(g)
x = [3,3,3]
y = [3]
c = polinomio(x)
d = polinomio(y)
g = c/d
print(g)