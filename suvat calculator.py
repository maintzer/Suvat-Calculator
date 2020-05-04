import numbers
import time
# trust me, we do need time. dont question it.

# print is way too many letters that are far apart. 
# w & d are right next to each other. 
# wd is the new print!
# and God tells us that print is a legitimate debugging tool.

def wd(var):
    answer = print(var)
    return answer

# imagine writing a genuine program instead of just defining a billion functions. 
# dont lie this is ridiculously user friendly.
# GUIDE TO FUNCTION NAMES: letter to find, then 'no' and letter that you dont have. 
# eg to find time without a value for acceleration, write tnoa. then enter values in SUVAT order.

def snou(v, a, t):
    s = (v*t)-0.5*a*(t*t)
    return s
def snov(u, a, t):
    s = (u*t)+0.5*a*(t*t)
    return s
def snoa(u, v, t):
    s = t*((u+v)/2)
    return s
def snot(u, v, a):
    s = ((v*v)-(u*u))/(2*a)
    return s

def unos(v, a, t):
    u = v-(a*t)
    return u
def unov(s, a, t):
    u = (s-(0.5*a*(t*t)))/t
    return u
def unoa(s, v, t):
    u = ((2*s)/t)-v
    return u
def unot(s, v, a):
    u = ((v**2)-2*a*s)**0.5
    return u 

def vnos(u, a, t):
    v = u+(a*t)
    return v
def vnou(s, a, t):
    v = (s+(0.5*a*(t**2)))/t
    return v
def vnoa(s, u, t):
    v = ((2*s)/t)-u
    return v
def vnot(s, u, a):
    v = ((u**2)+2*(a*s))**0.5
    return v

def anos(u, v, t):
    a = (v-u)/t
    return a
def anou(s, v, t):
    a = (-2*(s-(v*t)))/(t**2)
    return a
def anov(s, u, t):
    a = (2*(s-(u*t)))/(t**2)
    return a
def anot(s, u, v):
    a = ((v**2)-(u**2))/(2*s)
    return a

def tnos(u, v, a):
    t = (v-u)/a
    return t
def tnou(s, v, a):
    t = ((v)+(((v**2)-(2*a*s))**0.5))/a
    return t
def tnov(s, u, a):
    t = ((-u)+(((u**2)+(2*a*s))**0.5))/a
    return t
def tnoa(s, u, v):
    t = (2*s)/(v+u)
    return t
