"""
@author: anabeatrizmacedo
"""
1. 
divisivel_2_e_5 = [k for k in range(101) if k%2==0 if k%5==0]
print(divisivel_2_e_5)

2. 
#Set
par_impar = {k:"Par" if k%2==0 else "Ímpar" for k in range(11)}
print(par_impar)

#List
par_impar2 = ['Par' if k%2==0 else 'Ímpar'for k in range(11)]
print(par_impar2)

3.
times = ['Cowboys', 'Ravens', 'Colts', '49ers', 'Chargers', 'Rams', 'Bills', 'Chiefs', 'Dolphins', 'Raiders']
[time for time in times if time.startswith('C')]

4.
palavras = ['Python', 'Code', 'List', 'Set', 'Comprehension']
palavras2 = []
for k in palavras:
    if len(k)<4:
        palavras2.append(k)
print(palavras2)
