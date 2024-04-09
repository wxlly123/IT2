#--Sjuk-Quiz--

print('Velkommen til den sykeste quizzzzen!!!')
print('Denne quizzen har 20 spørsmål')
print('Du får 10 poeng for hvert spørsmål du svarer riktig')
print('Klarer du å få full pott?')

poeng = 0
første = print('1. Hva er hovedstaden i Norge?')

a_1 = print('--A: Bergen')
b_1 = print('--B: Paris')
c_1 = print('--C: Oslo')
d_1 = print('--D: Roma')

svar_1 = input('Svar: ')

if svar_1 == 'c' or svar_1 == 'C':
    poeng += 10
    print(f'Riktig!! Du har nå {poeng} poeng')
else:
    print(f'Feil! Du har nå {poeng} poeng')

