# Lame Shooter

Welkom bij de Pygame workshop van WP1. We gaan in deze workshop een simpele space game opbouwen in Pygame. We gaan leren werken met de standaard elementen van Pygame zoals een "surface" en "rectangles". Ook gaan we leren hoe we input kunnen verwerken en hoe we objecten kunnen laten bewegen.

De "lame shooter" is een game waarin je een klein vliegtuigje beweegt die het op neemt tegen een aantal veel grotere vijanden. Raken deze je, dan is het einde spel. In de map "images" zie je de graphics staan die we gaan gebruiken. 

![img.png](docs%2Fimg.png)

Mocht je vast komen te zitten, je kunt een voorstel voor de code van de verschillende stappen vinden in de map "uitwerkingen". Het kan goed zijn dat jouw code afwijkt van onze aanpak en dat is prima! Let er op dat de code in de uitwerkingen verwijst naar de afbeeldingen in de map bovengelegen map "images". Als je code overneemt, vervang dan eventuele verwijzingen naar "../images" met "images". 

## Stap 1: Opzet en installatie
Laten we voordat je begint eerst de pygame library installeren. Dat doe je met het volgende commando:
```bash
pip install pygame
```
Als deze regel faalt controleer dan in de pygame presentatie op Teams of jouw specifieke fout niet één van de bekende problemen is. 

Een standaard Pygame heeft een aantal vaste bouwblokken. We hebben die code alvast in een bestand "game.py" gestopt voor je. *Probeer deze te starten*, als het goed is zie je een zwart scherm verschijnen en is deze weer te sluiten met het kruisje. 

We zullen verder niets doen met deze vaste bouwblokken, maar het is wel handig om te weten wat ze doen. Er zijn: 
- Globale variabelen: variabelen die overal in de code gebruikt kunnen worden
- Pygame componenten: de basis van Pygame, zoals het scherm en de game loop
- De game loop: de oneindige loop die het spel draaiende houdt. Iedere keer dat alle stappen in de loop worden gedaan noemen we een "tick" of een "frame".

#### Globale variabelen 
In eerste instantie maken we een aantal "globale variabelen" aan. Deze zetten we bovenin de code zodat we ze makkelijk kunnen aanpassen. Dit zijn de standaard instellingen voor ons spel. In dit geval hebben we de schermgrootte, de achtergrondkleur en de "tick time" (de snelheid waarmee het spel loopt) gedefinieerd. De achtergrondkleur is samengesteld uit rood, groen en blauw. (0, 0, 0) is zwart, (255, 0, 0) is bijvoorbeeld rood en (255, 255, 255) is wit. We zullen later nog nieuwe variabelen toevoegen. 
```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FRAMES_PER_SECOND = 60
```

#### Pygame componenten
Daarna starten we een aantal Pygame zaken. We starten de Pygame library, maken een "surface" aan (het stuk papier waarop we gaan tekenen) en een "game clock" (die bijhoudt hoe snel het spel loopt).

```python
pygame.init()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
```

#### De game loop
Vervolgens starten we de "game loop". Dit is een oneindige loop die het spel draaiende houdt. Aan het begin van de loop vragen we Pygame om te kijken of iemand toevallig probeert het scherm te sluiten. Zo ja, dan stappen we uit de loop en stopt het spel. 

```python
while True:
    quit_requested = pygame.event.get(eventtype=pygame.QUIT)
    if quit_requested:
        break
```

#### De game loop, deel 2
Daarna verversen we ons canvas, we "verven" het helemaal zwart. Daarna roepen we de (nu) lege "game_loop" functie aan. Deze functie gaan we in de volgende stappen vullen met code. Als laatste sturen we het canvas naar het scherm en wachten we een korte tijd. Dit zorgt ervoor dat het spel niet te snel loopt. 

```python
    canvas.fill(BACKGROUND_COLOR)
    game_loop()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
```

## Stap 2: De speler


> Vanaf dit punt ga je code wijzigen in de game.py file die mee is geleverd.


We gaan nu de speler op het scherm zetten. We hebben hiervoor een afbeelding van een vliegtuigje. Deze afbeelding gaan we inladen en op het scherm zetten met behulp van een "rectangle". Verwijder de code uit de "game_loop" functie voordat je verder gaat. 

#### De speler afbeelding
We vragen eerst Pygame om de afbeelding van de speler in te laden. Dit doen we met de "pygame.image.load" functie. We geven de locatie van de afbeelding mee als parameter. Inladen van images kost een hoop processorkracht, we gaan dit daarom maar één keer doen. Besef ook dat op dit moment is de afbeelding nog niet op het scherm te zien, we hebben alleen de afbeelding in het geheugen geladen. 

Zoek in de code de opmerking "## Hier initialiseren we de speler en de vijand" en voeg de volgende regel toe:
```python
player_image = pygame.image.load("images/player.png").convert_alpha()
```

#### De speler op het scherm
De kern van Pygame is het gebruik van "rectangles". Een rectangle is een vierkant of rechthoek die we kunnen gebruiken om objecten op het scherm te positioneren. Een rectangle bevat 4 belangrijke attributen:
- x: de x positie van de rectangle 
- y: de y positie van de rectangle
- width: de breedte van de rectangle
- height: de hoogte van de rectangle

We kunnen met de hand deze rectangle samenstellen, maar we kunnen ook aan Pygame vragen om van ons eerdere plaatje een rectangle te maken. Dit doen we met de "get_rect" functie. Deze zet de x en y standaard op 0 en 0 - dat is dus linksboven in het scherm. Omdat deze rectangle ook gebruikt gaat worden om bij te houden waar de speler is op het scherm, moeten we deze rectangle opslaan in een variabele die bewaard blijft buiten de game loop  

```python
player_image = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_image.get_rect() 
```
Met de huidige player_rect rectangle staat het scheepje in de startpositie linksboven in het scherm. Da's niet mooi, we willen het scheepje in het midden van het scherm hebben. Dit kunnen we doen door de x en y positie van de rectangle aan te passen. We doen dit met de "move_ip" functie ("move in place"). De "move_ip" vraagt om een x en een y en zal de rectangle dan verplaatsen met die waarden. Dit is ook de functie die we later gaan gebruiken om onze figuren te animeren. Als de rectangle op (0, 0) staat en we doen "move_ip(10, 10)" dan staat de rectangle op (10, 10). Doen we daarna "move_ip(5, 5)" dan staat de rectangle op (15, 15).

```python
player_image = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_image.get_rect() 
center_height = SCREEN_HEIGHT // 2
player_rect.move_ip(0, center_height)
```
Besef dat op dit moment er nog steeds niets op het scherm staat. We hebben alleen een afbeelding ingeladen in het geheugen en een rectangle gemaakt en er is nog geen verband tussen deze twee.

#### De speler op het scherm, deel 2 
Als laatste stap vertellen we Pygame om de afbeelding van de speler op het canvas te zetten. Dit doen we met de "blit" functie. Deze functie heeft twee parameters: de afbeelding die we willen tekenen en de rectangle waar we de afbeelding willen tekenen. Beide hebben we in de voorgaande stappen gemaakt. 

Blitten zal ieder frame moeten gebeuren, anders verdwijnt de speler weer van het scherm op het moment dat we het canvas zwart wassen! We gaan deze code toevoegen aan de "game_loop" functie. Verwijder daar de "pass" uit voordat je jouw code toevoegt. 

```python

def game_loop():
    canvas.blit(player_image, player_rect)
```

(Optioneel) We hebben nog geen achtergrond. In de images map staat een "starfield.png". Zet deze ook op het scherm. Een probleem van deze afbeelding is dat deze niet groot genoeg is voor ons scherm. Je zou deze eerst moeten vergroten met bijvoorbeeld de _pygame.transform.smoothscale_ functie. Let erop dat pygame.transform functies een heleboel processorkracht kosten, dus doe dit maar één keer en doe dat buiten de game loop.   


## Stap 3: Een eerste vijand
We gaan nu een eerste vijand op het scherm zetten. Deze willen we helemaal réchts op het scherm hebben, op een willekeurige hoogte. Je kunt hiervoor de "images/lameenemy.png" gebruiken: 

![lameenemy.png](images%2Flameenemy.png)

We gaan dezelfde stappen volgen als bij de speler. De enige complicatie is, hoe zorg je ervoor dat deze niet rechts van het scherm af schuift? Als we heel naïef de breedte van het scherm nemen (SCREEN_WIDTH) en die als x coördinaat voor onze move_ip() opdracht gebruiken dan zal de vijand exact buiten het scherm vallen. Die moet dus een stukje naar links zetten, precies even veel beeldpunten als de rectangle van de vijand breed is. Je zult de locatie moeten berekenen als SCREEN_WIDTH - enemy_rect.width

Doorloop de code van de speler, maar nu voor de vijand. In de code onder "## Hier initialiseren we de speler en de vijand" voeg je de volgende stappen toe:
- Laad de afbeelding van de vijand in in een eigen variabele
- Maak een rectangle aan voor de vijand
- Bepaal de start positie van de vijand en pas de coordinaten in de rectangle aan

Als laatste stap voeg je de vijand toe aan de "game_loop" functie.
- Zet de vijand op het scherm

We zijn dan wel langs een deel van de opdracht gestapt, de vijand moet op een willekeurige hoogte beginnen. Laten we daarvoor een functie gebruiken die, gegeven de hoogte van een rectangle een willekeurige y positie teruggeeft en dus rekening houdt met de hoogte van de vijand om te voorkomen dat die buiten het veld valt:  
- Maak een functie "get_random_enemy_y" die een willekeurige y positie teruggeeft. 
- Vraag als input de hoogte van de vijand
- Gebruik de "randint" functie van de "random" module om een willekeurig getal te genereren. randint geeft een willekeurig getal terug tussen de twee getallen die je meegeeft:

```python
import random
random.randint(0, 10) # geeft een willekeurig getal tussen 0 en 10
```
- Let erop dat je geen hoogtes genereert die de vijand buiten het scherm zetten.
- Vervang de vaste y positie van de vijand door de uitkomst van de "get_random_enemy_y" functie.

Het resultaat zou dus iets moeten zijn als:
```python
def get_random_y(image_height):
    return ... 
```

## Stap 4: Beweging van de speler
Je hebt het niet door nu de boel stil staat, maar onze game loop functie draait 60 keer per seconde. Beweging is eigenlijk zo simpel als het aanpassen van de x en y coordinaten van de rectangle zodat deze een klein stukje verplaatst de volgende keer dat het canvas wordt opgetekend. We gaan de speler laten bewegen met de pijltjestoetsen op het toetsenbord. We zullen elke keer dat de game loop draait kijken of er een toets is ingedrukt en zo ja, de positie van de speler rectangle aanpassen.

#### Input verwerken
Pygame houdt bij welke toetsen er ingedrukt zijn. Dit doen we met de "pygame.key.get_pressed()" functie. Deze functie geeft een dictionary terug van alle toetsen met een key voor de toets en een waarde "True" als deze is ingedrukt en een waarde "False" als die niet is ingedrukt. We kunnen deze lijst gebruiken om te kijken of de pijltjestoetsen ingedrukt zijn en als een toets ingedrukt is, dan passen we de positie van de speler aan.

Bijvoorbeeld: 
```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -1)
```
...toegevoegd aan de game loop zal de speler omhoog bewegen als de pijltjestoets omhoog is ingedrukt. Kun je zelf de code schrijven om de speler naar beneden, links en rechts te laten bewegen? De toetsen daarvoor zijn "pygame.K_DOWN", "pygame.K_LEFT" en "pygame.K_RIGHT".

(Optioneel) De speler kan nu het hele scherm over. Met een simpele beperking zou je hem ook kunnen laten stoppen bij de randen van het scherm, of zorgen dat de speler niet verder dan de linkerhelft van het scherm kan bewegen.  

## Stap 5: Beweging van de vijand
De vijand bewegen is een stuk simpeler dan de speler. We willen dat de vijand van rechts naar links beweegt. Dit betekent dat we elke frame de x positie van de vijand met een bepaalde waarde moeten verlagen. 

```python
    enemy_rect.move_ip(-1, 0)
```

Maar, wat moeten we doen als de vijand links van het scherm is? Dan valt hij er vanaf en vliegt onzichtbaar door tot in het oneindige. Laten we daarom de vijandelijke rectangle vervangen door een nieuwe rectangle als de vijand links van het scherm is. Dan kan door simpelweg de code die de vijand initialiseert te herhalen, maar mooier is het om hier een aparte functie voor te maken, "create_enemy()" die een nieuwe rectangle teruggeeft. Dat betekend wel dat we een globale variabele overschijven - en dat moet met "global" aangegeven worden. 

```python 
    global enemy_rect
    enemy_rect.move_ip(-1, 0)
    if enemy_rect.x + enemy_rect.width < 0:
        enemy_rect = create_enemy()
```

Natuurlijk kun je deze functie ook gebruiken voor het eerste instantie aanmaken van de vijand

Zo'n langzaam bewegende vijand is natuurlijk niet heel spannend. Kun je de vijand sneller laten bewegen? Dit is het mooiste als je de snelheid van de vijand in een globale variabele zet, zodat je die makkelijk kunt aanpassen.

En dan een laatste puntje: omdat de vijand nu beweegt kunnen we hem ook buiten het scherm laten beginnen. Hij zal vanzelf naar binnen vliegen namelijk. 

(Optioneel) Wat niet heel mooi is is dat de vijand nu puur rechtdoor vliegt. Kun je de vijand ook naar boven en beneden laten bewegen? 

## Stap 6: Collision detection
Het laatste puzzelstukje dat je nodig hebt om een spel te maken is collision detection. Dit is het detecteren van botsingen tussen objecten. In ons geval willen we weten of de speler en de vijand elkaar raken.

Pygame heeft een handige functie hiervoor: "colliderect". Deze functie kijkt of twee rectangles elkaar raken. Als dat zo is, dan geeft de functie "True" terug.

Voeg de volgende code toe aan de "game_loop" functie:
```python
    if player_rect.colliderect(enemy_rect):
        print("Game over!")
```
Deze éne regel code kun je op een eindeloos aantal manieren uitbreiden. Bijvoorbeeld, je kunt de speler een leven afnemen als hij een vijand raakt. Of je kunt de vijand laten verdwijnen als de speler hem raakt. Of als een kogel de vijand raakt, of als een vijandelijke kogel de speler raakt. 

Collision detection gebruik je om te voorkomen dat een speler door een platform zakt, of om te kijken of een speler een muntje heeft opgepakt. Met de puzzelstukjes die je nu in handen hebt kun je praktisch elk spel maken.

(Optioneel) Geef de speler 3 levens. Als de speler botst zet je hem terug op het scherm, zet je de vijand terug en trek je een leven af. Als de speler geen levens meer heeft, dan is het game over.

## Stap 7: De vijand haalt versterking 
Die éne vijand, die is makkelijk te ontwijken. Laten we de vijand versterking halen. Dat doen we door een lijst van vijanden te maken. Alle acties die we met die ene vijand hebben gedaan, gaan we nu doen met een lijst van vijanden. 

We gaan de vijanden op willekeurige momenten laten verschijnen. Bijvoorbeeld door een willekeurig getal van 1 tot 100 te genereren en als dat getal 5 of minder is, dan maken we een nieuwe vijand aan.

We maken een lijst van vijanden. In onderstaande code voeg ik als voorbeeld ook meteen een eerste vijand toe aan die lijst met de "append" methode:  

```python
enemy_image = pygame.image.load("images/lameenemy.png").convert_alpha()
enemies_list = []
enemies_list.append(create_enemy())
```
We moeten ook de game loop methode aanpassen. Waar we hiervoor maar één vijand hadden, hebben we er straks misschien meerdere. We moeten dus door de lijst van vijanden heen lopen en voor elke vijand de beweging en collision detection doen, ook al is die lijst misschien leeg.  

```python
for enemy_rect in enemies_list:
    ## ..beweeg de vijand en daarna: 
    if enemy_rect.x + enemy_rect.width < 0:
        enemies_list.remove(enemy_rect)
    ## ..collision detection
    ## ..blit de vijand naar het canvas
```

..en als laatste gaan we een muntje gooien om misschien een nieuwe vijand aan de lijst toe te voegen: 
```python
    if random.randint(1, 100) <= ENEMIES_SPAWN_CHANCE:
        enemies_list.append(create_enemy())
```
Hoe hoger de "ENEMIES_SPAWN_CHANCE" hoe meer vijanden er zullen verschijnen.

Vergeet niet om nu nog alle code die verwijst naar een enkele vijand te verwijderen. Dat is bijvoorbeeld de globale "enemy_rect" variabele en verwijzingen daar naar in de game loop.

(Optioneel) Eigenlijk zou de spawn chance omhoog moeten gaan na verloop van tijd. De gebruikelijke aanpak is een waarde voor de "spawn_chance" overnemen van de start instelling en deze daarna elke X seconden te verhogen. 

(Optioneel) Wat het geheel meteen een stuk speelbaarder maakt is als er iets valt te winnen. Maak een conditie die, als de speler de andere kant van het veld haalt, het spel afsluit met een "You win!" melding.

## Stap 8: "Make it work, then make it good"
Als je de code hebt gevolgd tot hier, dan heb je een werkende game. Maar waarschijnlijk is jouw code ook een beetje een zooitje. Dat is prima. Een hele bekende uitspraak in software ontwikkeling is "Make it work, then make it good".

Nu je een werkende game hebt, kun je gaan kijken of je de code netter kunt maken. Dat houdt in: 
- Pycharm zal bij een aantal code constructies kringels geven. Kun je die oplossen? 
- Stop waar mogelijk code in functies, zoals bijvoorbeeld de initialisatie van de speler
- Vervang de globale variabelen zoals player_rect en enemies_list door een enkele dictionary die je "game_state" noemt.

Maar, ben je al tot hier gekomen? In dat geval, goed gewerkt! Jouw eerste game is een feit. En met de bouwblokken die je hier hebt gebruikt kun je alles nabouwen aan arcade klassiekers die je maar kunt bedenken!

## Stap 9: (Optioneel) Shooting!
Leuk, deze game, en met een hoge spawn rate ook moeilijk, maar het is nogal eenzijdig. De speler kan alleen maar bewegen en de vijand kan alleen maar bewegen. Laten we daarom de speler ook laten schieten.

- In de map images staat ook een "rocket.png"
- Als de speler op spatie drukt, dan moet er een raket verschijnen vlak voor de speler
- Deze raket moet dan in hoge snelheid naar rechts bewegen
- Als de raket een vijand raakt, dan moeten vijand en raket verdwijnen
- Als de raket het scherm uitvliegt, dan moet de raket verdwijnen
- En tenslotte, we willen voorkomen dat je de spatiebalk ingedrukt houdt en zo een oneindige hoeveelheid raketten afvuurt. Daarvoor kun je een timer gebruiken zoals ook te zien is in de werkplaats1_starter code met het stuiterende logo. 
