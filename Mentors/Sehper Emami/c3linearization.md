# C3 Linearization remember notes

24 may 2023

I am going to summarize all that I learned from C3 linearization here
c3 linearization in simple words is the algorithm we use to obtain method resolution in multiple inheritance systems

how does class hierarchy affect method callings?



well let's first define the c3 linearizaion:
> the linearization of C is the sum of C plus the merge of the linearizations of the parents and the list of the parents.

L[C] = C + merge(C + merge(parents)+ parents)

but what is the meaning of this? 
meaning that 
```
l(C(B1...Bn)) = C + merge(B1...Bn), B1...bn
```

lets break this down. 
we have C which we want to c3 linearize. we have to first say: C, obviously we can't go ahead without C. so there you have C. 
then after that you linearize everything else that C inherits from. if C inherits from B, then L[B]. and then there is B itself. 
so what would linearizing B look like in this example?
```py
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(E,D): pass
>>> class A(B,C): pass
```
L[B] = B + merge(EO, DO, DE)

wait wait what is merge? well according to wikipedia:
> The merge of parents' linearizations and parents list is done by selecting the first head of the lists which does not appear in the tail (all elements of a list except the first) of any of the lists. 

Thank you wikipedia, This doesn't make sense at all. what it means is that for example in the 'EO', E is the head, and the rest which is O is the tail. now when we want to choose a head that comes out and joins B we must be careful that the head we choose is not a tail of other components. so now we can continue:

```
L[B] = B + merge(EO, DO, DE)
```
is E that tail of any other component? yesthen it is not a good head. we move on to D. is D a good head? yes
```py
L[B] = BD + merge(EO, O, E)
```
is O a good head? (remember the thing with tail?) no 
is E a good head? yes
```py
L[B] = BDE + merge(O, O)
L[B] = BDEO
```
here is out method resolution order obtained from c3 linearization.


of course there aren't always sunshines and roses in the field of multiple inheritance and c3. somethings even god can't handle (isn't that what he is supposed to?)

have this:


```py
class A:...
class B(A):...
class C(A, B):...
TypeError: Cannot create a consistent mro
```
let's take a closer look

l(B) = b + a

l(c) = c + a + ba + ab

well I want to take A out, but wait, A is the tail of the second component. so let's take B out, but you can't! B is the tail of the third component. It's like a recursion error. what a headache. 

so designing good MROs and fine multiple inheritance systems requires some knowledge and percision.


# Resourses 
- [Awesome Guide I find randomly](https://www.python.org/download/releases/2.3/mro/)
- [some irrelevant repo on design patterns](https://github.com/3lf/design-patterns-for-humans)