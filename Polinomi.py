#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import display, Math
class polinomio:
    def __init__(self, x:list):
        self.x = x
        #scrittura del polinomio:
        i, j = 0, 0
        while i < len(x):
            if x[0] == 0:
                x.pop(0)
            i += 1
        while j < len(y):
            if y[0] == 0:
                y.pop(0)
            j += 1
        if len(x) > 0:
            grado_polinomio = len(x) - 1 
        else:
            grado_polinomio = 0
        print("Il polinomio inserito è di grado", grado_polinomio)
        for i in range(0, len(x)):
            if (((x[i] == 1 or x[i] == 1.0)and grado_polinomio-i == 1)):# and x[grado_polinomio]!=0):
                display(Math(r'x'))
                #continue
#             elif ((x[i] == 1 and grado_polinomio-i == 1) and x[grado_polinomio]==0):
#                 display(Math(r'x'))
#                 #continue
            if grado_polinomio-i == 1 and (x[i] != 0 and x[i] != 1 and x[i] != -1 and x[i] != 1.0 and x[i] != -1.0):
                display(Math(r'{}x'.format(x[i])))
            if x[i] == 0: 
                pass
                #continue
            if grado_polinomio-i != 0 and grado_polinomio-i != 1 and (x[i] != 0 and x[i] != 1 and x[i] != -1 and x[i] != 1.0 and x[i] != -1.0):
                display(Math(r'{}x^{}'.format(x[i], grado_polinomio-i)))
                #continue
                #print(x[i], "$x^", grado_polinomio-i, "$ + ")
            if (x[i] == 1 or x[i] == 1.0) and grado_polinomio-i != 1 and grado_polinomio-i != 0:
                display(Math(r'x^{}'.format(grado_polinomio-i)))
                #continue
            elif (x[i] == -1 or x[i] == -1.0) and grado_polinomio-i != 1 and grado_polinomio-i != 0:
                display(Math(r'-x^{}'.format(grado_polinomio-i)))
                #continue
            elif x[i] != 0 and grado_polinomio-i == 0:
                display(Math(r'{}'.format(x[i])))
#             if i != len(x)-1 and x[i+1] > 0:
#                 display(Math(r'+'))
#                 continue
            if ((x[i] == -1 or x[i] == -1.0) and grado_polinomio-i == 1):# and x[grado_polinomio]!=0):
                display(Math(r'-x'))
                #continue
#             elif ((x[i] == 1 and grado_polinomio-i == 1) and x[grado_polinomio]==0):
#                 display(Math(r'x'))
#                 #continue
            if grado_polinomio-i == 1 and (x[i] != 0 and (x[i] != -1 or x[i] != -1.0) and (x[i] != 1 or x[i] != 1.0)):
                display(Math(r'{}x'.format(x[i])))
            if i != len(x)-1 and x[i+1] != 0:
                display(Math(r'+'))
                continue

    def grado_polinomio(x):
        if len(x) > 0:
            grado_del_polinomio = len(x) - 1 
        else:
            grado_del_polinomio = 0
        return grado_del_polinomio
    
    def somma(x:list,y:list):
#         self = x
#         other = y
        c = []
        n = min(len(x), len(y))
        m = max(len(x), len(y))
        d = []
        if m == len(x):
            d = x
        else:
            d = y
        for i in range(0, m-n):
            c.append(d[i])
        if m == len(x):
            for j in range(m-n, m):
                z = x[j] + y[j-m+n]
                c.append(z)
        else:
            for j in range(m-n, m):
                z = x[j-m+n] + y[j]
                c.append(z)
        return (c)
    
    def differenza(x:list,y:list):
        if len(x) >= len(y):
            x = x
            y = y
            c = []
            n = min(len(x), len(y))
            m = max(len(x), len(y))
            d = []
            if m == len(x) :
                d = x
                for i in range(0, m-n):
                    c.append(d[i])
                for j in range(m-n, m):
                    z = x[j] - y[j-m+n]
                    c.append(z)
            else:
                d = y
                for i in range(0, m-n):
                    c.append(d[i])
                for j in range(m-n, m):
                    z = x[j-m+n] - y[j]
                    c.append(z)
        else:
            y = t
            x = y
            y = t
            c = []
            n = min(len(x), len(y))
            m = max(len(x), len(y))
            d = []
            if m == len(x) :
                d = x
                for i in range(0, m-n):
                    c.append(-d[i])
                for j in range(m-n, m):
                    z = -(x[j] - y[j-m+n])
                    c.append(z)
            else:
                d = y
                for i in range(0, m-n):
                    c.append(-d[i])
                for j in range(m-n, m):
                    z = -(x[j-m+n] - y[j])
                    c.append(z)
        return (c)
    
    def prodotto(x:list,y:list):
#         self = x
#         other = y
        grado_polinomio = (len(x)-1)+(len(y)-1)
        d = [[],[]]
        for i in range(len(x)):
            for j in range(len(y)):
                d[0].append(x[i]*y[j])
                d[1].append(i+j)#grado del monomio
        d[1] = d[1][::-1] 
        #print(d)
        for i in range(grado_polinomio+1): 
            if d[1].count(grado_polinomio-i) > 1:
                j = d[1].index(grado_polinomio -i)
                #print("j vale: ", j)
                z = j+1
                while z < len(d[1]):
                    if d[1][z] == d[1][j]:
                        #print("z vale:", z)
                        d[0][j] = d[0][j]+d[0][z]
                        d[1].pop(z)
                        d[0].pop(z)
                        #print(d)
                    z += 1
        return (d[0])
    
    def potenza(x:list,var:int):
        f = x
        for i in range(0,var-1):
            h = polinomio.prodotto(f,x)
            f = h
        return f
    
#     def scrittura_rapporto(c:list, x:list, y:list):
#             polinomio(c)
#             display(Math(r'+'))
#             polinomio(x)
#             display(Math(r'/'))
#             polinomio(y)
            
    def rapporto(x:list,y:list, c = []):
#         self = x
#         other = y
        i, j = 0, 0
        while i < len(x):
            if x[0] == 0:
                x.pop(0)
            i += 1
        while j < len(y):
            if y[0] == 0:
                y.pop(0)
            j += 1
        d = [[],[]]
        s = polinomio.grado_polinomio(x)
        v = polinomio.grado_polinomio(y)
        grado_polinomio_risultante = s-v
        #while (s-v) >= 0:
        #for b in  range(0, grado_polinomio_risultante):
        if s < v:
            polinomio(c)
            display(Math(r'+'))
            polinomio(x)
            display(Math(r'//'))
            polinomio(y)
            
        elif s == 0:
            return(c)
        
        else:
            d[1].append(grado_polinomio_risultante)
            d[0].append(x[0]/y[0])
            for i in range(0,grado_polinomio_risultante):
                d[0].append(0)
            c.append(d[0][0])   
            g = polinomio.prodotto(d[0], y)
            if len(g) != len(x):
                for e in range(0, len(x)-len(g)):
                    g.append(0)                
            print(g)
            f = polinomio.differenza(x,g)
            i = 0
            while i < len(f):
                if f[0] == 0:
                    f.pop(0)
                i += 1
            if (polinomio.grado_polinomio(f) - polinomio.grado_polinomio(y)) == 0 and (len(f)-len(c))> 1:
                c.append(0)
            return polinomio.rapporto(f,y,c)
        


# In[2]:


x = [1,1,2,1,1]
y = [1,0,1]
polinomio(y)


# In[3]:


f = polinomio.somma(y,x)
polinomio(f)


# In[4]:


f = polinomio.differenza(x,y)
polinomio(f)


# In[5]:


f = polinomio.prodotto(x,y)
polinomio(f)


# In[6]:


x = [1,0,0]
y = [1,0,1]
f = polinomio.prodotto(x,y)
print(f)
polinomio(f)


# In[7]:


x = [1,0,1]
f = polinomio.potenza(x,3)
print(f)
polinomio(f)


# In[9]:


x = [1,1,2,1,1]
y = [1,0,1]
# x = [1,0,2,0,1]
# y = [1,0,1]
f = polinomio.rapporto(x,y)
print(f)


# In[10]:


x = [1]
y = [1,0,1]
# x = [1,0,2,0,1]
# y = [1,0,1]
f = polinomio.rapporto(x,y)

