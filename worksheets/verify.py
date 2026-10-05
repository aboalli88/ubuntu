# تحقق عددي من كل إجابة صحيحة وكل مشتت (مشتقة بفروق مركزية)
from math import sin, cos, pi, exp
from fractions import Fraction as F
def d(f, x, h=1e-6): return (f(x+h)-f(x-h))/(2*h)
def eq(a,b,t=1e-4): return abs(a-b)<t
ok=True
def chk(name, cond):
    global ok; ok &= bool(cond); print(("OK  " if cond else "FAIL"), name)

# ---- الضرب ----
f=lambda x:(x*x+1)*(x-3)
chk("P1 f'(x)=3x^2-6x+1", all(eq(d(f,x),3*x*x-6*x+1) for x in (-2,0.5,3)))
chk("P1 distractors differ", not eq(d(f,2),2*2) and not eq(d(f,2),4-12-1))
chk("P2 (uv)'(2)=3*... ", -2*4+3*5==7 and 7 not in (-10,-23,23) and (-2)*4-3*5==-23 and 3*5+2*4==23 and (-2)*5==-10)
g=lambda x:x*x*sin(x); chk("P3 slope pi = -pi^2", eq(d(g,pi),-pi*pi,1e-3))
chk("P3 distractors 0,pi^2,-2pi differ", all(not eq(-pi*pi,v,1e-3) for v in (0,pi*pi,-2*pi)))
f=lambda x:x**3*(2*x+5); chk("P4 8x^3+15x^2",all(eq(d(f,x),8*x**3+15*x**2) for x in (-1,1,2)))
f=lambda x:(x*x+3*x)*(x*x-2); chk("P5 h'(1)=3", eq(d(f,1),3)); chk("P5 distr",(5*-1-4*2,5*2,4*2+5)==(-13,10,13))
f=lambda x:x*x*exp(x); chk("P6 f'=0 at 0,-2 not 2", eq(d(f,0),0) and eq(d(f,-2),0) and not eq(d(f,2),0,1e-2))
f=lambda x:(2*x-1)*(x*x+3*x); chk("S1 f'=6x^2+10x-3, f'(1)=13,f(1)=4,y=13x-9",
   all(eq(d(f,x),6*x*x+10*x-3) for x in (0,1,2)) and eq(d(f,1),13) and f(1)==4 and 4-13*1==-9)
chk("S2 (uv)'(3)=-7; (x^2u)'=57; tangent y=-7x+15", 2*(-3)*0 or (5*-3+2*4==-7 and 2*3*2+9*5==57 and (2*-3)==-6 and -6+7*3==15))
f=lambda t:(t+1)*(50-2*t); chk("S3 R'=48-4t; R'(3)=36; zero t=12", all(eq(d(f,t),48-4*t) for t in (0,3,5)) and eq(d(f,3),36) and 48-4*12==0)

# ---- القسمة ----
f=lambda x:3*x/(x+2); chk("Q1 6/(x+2)^2", all(eq(d(f,x),6/(x+2)**2) for x in (0,1,3)))
chk("Q2 (u/v)'=-15/2", F(-3*2-6*4,4)==F(-15,2) and F(6*4+3*2,4)==F(15,2) and F(-30,2)==-15 and F(-3,4)==F(-3,4))
f=lambda x:sin(x)/x; chk("Q3 -1/pi", eq(d(f,pi),-1/pi,1e-4) and all(not eq(-1/pi,v,1e-3) for v in (-pi,1/pi,-1/pi**2)))
f=lambda x:x*x/(x-1); chk("Q4 (x^2-2x)/(x-1)^2", all(eq(d(f,x),(x*x-2*x)/(x-1)**2) for x in (-1,2,3)))
f=lambda x:(2*x+3)/(x-2); chk("Q5 f'(4)=-7/4", eq(d(f,4),-7/4) and all(abs(-7/4-v)>1e-3 for v in (7/4,-7/2,2)))
f=lambda x:x/(x*x+1); chk("Q6 f'=0 at +-1 only", eq(d(f,1),0) and eq(d(f,-1),0) and not eq(d(f,0),0,1e-2))
f=lambda x:(x*x+1)/(x-2); chk("T1 f'=(x^2-4x-1)/(x-2)^2, f'(3)=-4,f(3)=10,y=-4x+22",
   all(eq(d(f,x),(x*x-4*x-1)/(x-2)**2) for x in (0,1,4)) and eq(d(f,3),-4) and f(3)==10 and 10+12==22)
chk("T2 (u/v)'(1)=5/2; (v/u)'(1)=-5/8; 1/(5/2)=2/5!=-5/8", F(3*2-4*-1,4)==F(5,2) and F(-1*4-2*3,16)==F(-5,8) and F(2,5)!=F(-5,8))
f=lambda t:5*t/(t*t+4); chk("T3 C'=(20-5t^2)/(t^2+4)^2, C'(1)=3/5, t=2, C(2)=1.25",
   all(eq(d(f,t),(20-5*t*t)/(t*t+4)**2) for t in (0,1,3)) and eq(d(f,1),0.6) and eq(d(f,2),0) and eq(f(2),1.25))
print("ALL OK" if ok else "SOME FAILED")
