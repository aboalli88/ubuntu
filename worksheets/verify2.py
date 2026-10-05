from fractions import Fraction as F
from math import exp
def d(f,x,h=1e-6): return (f(x+h)-f(x-h))/(2*h)
def eq(a,b,t=1e-4): return abs(a-b)<t
ok=True
def chk(n,c):
    global ok; ok&=bool(c); print("OK  " if c else "FAIL",n)
# ---- ضرب ----
f=lambda x:(x*x+1)*(x**3-x); chk("P3 f'(2)=79; distract 44,-31,30", eq(d(f,2),79) and 4*11==44 and 24-55==-31 and 5*6==30)
f=lambda x:x*x*(3-x**3); chk("B1 6x-5x^4", all(eq(d(f,x),6*x-5*x**4) for x in (-1,1,2)))
chk("B2 (fg)'(2)=7", -1*5+3*4==7); chk("B3 y'(2)=-7", -3*4+5*1==-7)
f=lambda x:(2*x+1)*(x*x-3); chk("B4 y'(1)=2", eq(d(f,1),2))
f=lambda x:x**3*(x*x-4); chk("B5 f'(-1)=-7; distr -6,-11,11", eq(d(f,-1),-7) and 3*-2==-6 and -9-2==-11 and 2+9==11)
chk("B6 a=5", all(eq(d(lambda x,a=5:(x*x+a)*(x-2),1),4) for _ in [0]) and not eq(d(lambda x:(x*x+6)*(x-2),1),4))
f=lambda x:(x*x+5)*(3-2*x); chk("S4 f'=-6x^2+6x-10", all(eq(d(f,x),-6*x*x+6*x-10) for x in (-1,0,2)))
h=lambda x:x**3*(x*x-4); chk("S4 B,C h'(-1)=-7,h(-1)=3,y=-7x-4", eq(d(h,-1),-7) and h(-1)==3 and 3-7*(0)==3 and (3+(-7)*(0-(-1)))==-4)
f=lambda x:x*(x*x-12); chk("S5 f'=3x^2-12, pts (2,-16),(-2,16)", all(eq(d(f,x),3*x*x-12) for x in (-3,0,2)) and f(2)==-16 and f(-2)==16)
# ---- قسمة ----
f=lambda x:(x*x-1)/(x*x+1); chk("Q3 f'(2)=8/25; distr 8/5,1,-8/25", eq(d(f,2),8/25) and F(8,5)!=F(8,25))
f=lambda x:x/(x+3); chk("C1 3/(x+3)^2", all(eq(d(f,x),3/(x+3)**2) for x in (0,1,2)))
chk("C2 -17/25", F(-1*5-3*4,25)==F(-17,25))
f=lambda x:3/(x*x+1); chk("C3 -6x/(x^2+1)^2", all(eq(d(f,x),-6*x/(x*x+1)**2) for x in (-1,0.5,2)))
f=lambda x:(x+1)/(x-1); chk("C4 f'(3)=-1/2", eq(d(f,3),-0.5))
chk("C5 a=6", eq(d(lambda x:6*x/(x+2),0),3))
f=lambda x:x*x/(x-2); chk("C6 zero at 0 and 4", eq(d(f,0),0) and eq(d(f,4),0) and not eq(d(f,3),0,1e-2))
f=lambda x:3/(x*x+1); chk("T4 g(1)=3/2,g'(1)=-3/2,y=-3x/2+3,g'(0)=0,g(0)=3", f(1)==1.5 and eq(d(f,1),-1.5) and 1.5+1.5==3 and eq(d(f,0),0))
f=lambda x:(3*x-1)/(x+2); chk("T5 f'=7/(x+2)^2; slope 7/16 at 2,-6", all(eq(d(f,x),7/(x+2)**2) for x in (0,1,3)) and eq(d(f,2),7/16) and eq(d(f,-6),7/16))
print("ALL OK" if ok else "FAILED")
