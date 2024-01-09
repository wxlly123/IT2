# Psuedokode

- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske uttrykk fungerer sammen for å løse et bestemt problem.

## Eksempel: Penger tjent på Spotify

> En algoritme som regner ut hvor mye penger vi tjener på Spotify

### Psuedokose i *naturlig språk*
```psuedo
Hent inn alle streams
Hvis antall streams er større en 30 000 000:
    Returner antall streams * 70%(0.7)
Ellers hvis antall streams er større en 1 400 000:
    Returner antall streams * 40%(0.4)
Ellers:
    Returner 0
```

### Psuedokode som følger UDIR sin standard
```psuedo
SET antall_streams TO READ 'Hvor mange streams?'
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streams GREATER THAN 1 400 00
    THEN DISPLAY antall_streams * 0.4
ELSE DISPLAY 0
```

### Python
```python
antall_streams = input(int('hvor mange streams?'))
if antall_streams > 30_000_000:
    print(antall_streams * 0.7)
elif antall_streams > 1_400_000:
    print (antall_streams * 0.4)
else:
    print (0)
```
