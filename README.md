# Portfolio
Goedendag,

Mijn naam is Joeri Meijers en ik volg op dit moment de minor Applied Data Science aan de Haagse Hogeschool. Gedurende deze minor hebben wij geleerd om aan de slag te gaan met Machine Learning modellen en Neurale Netwerken. Dit hier is mijn portfolio, een verplicht onderdeel van deze minor waarin ik kan laten zien wat ik heb geleerd tijdens deze minor en hoe ik mijzelf heb ontwikkeld op dit gebied. Dit portfolio zal uit zes verschillende beoordelingscriteria  bestaan waarin ik aan de hand van voorbeelden laat zien dat ik voldoe aan de norm. De verschillende onderwerpen zullen elk op hun eigen pagina nader worden toegelicht.

Het gaat om de volgende onderdelen:  
- DataCamp courses  
- Research project  
- Predictve Analytics  
- Domain knowledge  
- Data preprocessing  
- Communication  
        
Veel plezier met het lezen van mijn portfolio, ik hoop dat ik jullie op deze manier de groei kan laten zien die ik heb gemaakt het afgelopen half jaar.        
## DataCamp courses
Tijdens deze minor hebben wij toegang gehad tot de site DataCamp. Op deze site is er een pad aangemaakt die wij moesten volgen. Ik heb deze courses met plezier gedaan en er veel van geleerd. Ik heb niet alles voor de gestelde datum gemaakt omdat ik vond dat de courses op DataCamp soms niet echt raakvlak hadden met wat wij tijdens het project aan het doen waren. Dus dan ging de focus meer op het project en heb ik de DataCamp courses op een ander tijdstip weer ingehaald. Maar ik heb ze wel allemaal gedaan en er veel van geleerd. In [deze](https://user-images.githubusercontent.com/122271017/214064213-ecd58bc7-ef49-40f3-a2d6-190a59dd1952.png) foto is een screenshot van mijn afgeronde courses te zien, op deze manier kan ik aantonen dat ik meer dan 90% van de courses heb afgerond.

## Research project
### Onderzoeksvragen
In de eerste 10 weken van deze minor hebben wij als groep ons gericht op het foodboost project. Voor de rest van de minor hebben we ons gericht op het probleem van Cofano, om een zo optimaal mogelijke indeling van containers te maken voor de kade. Voor beide projecten hebben wij een hoofdvraag (streepje) met daarbij wat deelvragen (sterretje) bedacht. 

- Foodboost  
        - Hoe kan er een schema van avondmaaltijden voor een week worden opgebouwd voor mensen op basis van hun voorkeuren?   
                * Wat is er al bekend in de literatuur over het maken van een eetschema op bais van voorkeuren?  
                * Hoe kunnen gerechten het best gegroepeerd worden?  
                * Wat is een geschikte manier om voorkeuren van mensen te achterhalen?  
                * Op welke manier kan er het best een gevarieerd weekmenu geselecteerd worden?  
                * Wat is een goede applicatie om uiteindelijk het weekmenu voor de mensen te creeren?  
                
- Cofano  
        - Hoe kan er een model gemaakt worden dat een zo optimaal mogelijke opstelling maakt van de containers op een containerterminal?  
                * Wat is er al bekend vanuit de literatuur over het oplossen van een dynamisch plaatsingsprobleem?  
                * Welke factoren zijn van invloed bij het zo efficient mogelijk inrichten van een containerterminal?  
                * Welke wiskundige modellen kunnen gebruikt worden bij het bouwen van een model dat een zo optimaal mogelijke inrichting maakt?  
                * In wat voor een vorm moet de oplossing van dit probleem opgeleverd worden?  
                
Dit zijn opgestelde hoofd en deelvragen voor de onderzoeken die wij hebben uitgevoerd. Omdat we in het paper dat wij hebebn geschreven een beetje afstappen van het gebruik van hoofd en deelvragen, komt dit niet terug in het geschreven paper. In het paper zijn we meer uitgegaan van een doel dat we wilde behalen en hoe we dat dan het beste konden halen. En dat hebben we niet gedaan door hoofd en deelvragen op te stellen en die te beantwoorden. Dat we dit niet hebben gedaan vond ik achteraf gezien toch niet zo fijn. Ik heb het idee dat je door het gebruik van hoofd en deelvragen veel meer structuur krijgt in je werk. En dat was ik bij ons paper op sommige momenten wel even zoek. Ik heb bij nog geen van mijn projecten hiervoor een keer het gevoel gehad dat het echt fijn is om goede hoofd en deelvragen te hebben. Dat is wel iets dat ik heb geleerd bij het schrijven van het paper. 

### Evaluatie
Bij beide problemen, maar zeker bij het probleem van Cofano ging het om een proof of concept. Dit houdt in dat we wilde laten zien dat wat er gemaakt wordt in het klein met weinig restricties werkt. Daardoor is het van groot belang dat er duidelijk wordt gemaakt dat er nog vele stappen na de stappen die wij hebben gemaakt kunnen volgen. Dat hebben we dan ook zeker gedaan door in de discussie duidelijk te schrijven wat mogelijke opties zijn als hier verder onderzoek in gedaan wordt. Voorbeelden hiervan zijn; een model ontwikkelen dat de opstelling van containers controleerd in plaats van dat handmatig te doen, het aantal zetten van een stacker te minimaliseren of het verder uitbreiden van de visualisaties in de app. Deze aanbevelingen zijn ook terug te vinden in het paper. Maar gedurende de hele minor hadden wij wel goed in de gaten wat mogelijke vervolgstappen zijn. Zo vertelden we bij elke presentatie die wij hebben gedaan over wat we de komende tijd wilden gaan onderzoeken. 

### Conclusie
Dit stukje zal in 2 delen worden opgesplitst om de conclusies die gedaan zijn vanuit beide projecten duidelijk te krijgen.
#### Foodboost
Het model dat wij hebben gebouwd voor het foodboost probleem kon uiteindelijk erg goed verschillende keukens van elkaar onderscheiden. Dat was niet vanaf het begin ons doel, maar omdat wij er tijdens het project achter kwamen dat de eerder gestelde hoofdvraag veel te complex was hebben wij ervoor gekozen om het probleem wat behapbaarder te maken. Uiteindelijk hebben we dus een model gemaakt dat goed verschillende keukens met elkaar kon vergelijken. Wat hiermee gedaan kan worden is op basis van voorkeuren voor mensen een mix maken met gerechten die ook van dezelfde keukens af komen. 
#### Cofano
In het paper hebben wij onze conclusie geschreven voor het container probleem. In deze conclusie komt naar voren dat we aan de hand van de onderzoeksresultaten kunnen zien dat er een model is ontwikkeld dat een 3 bij 3 bij 3 yard op een zo optimale manier kan invullen. We hebben hier Reinforcement Learning voor toegepast en het PPO-model gebruikt. Door penalty's en rewards mee te geven aan de agent kan deze van zijn gemaakte acties leren. Het model dat wij behandelen in het paper is getraind in 350000 timesteps en deed er in totaal 334 seconden over. De oplossing die hieruit voort kwam, moest nog geevalueerd worden. Dat evalueren is handmatig gedaan door te bekijken of elk schip direct bij al zijn bestemde containers kan. In dit geval lukte dat en dus kunnen we stellen dat het model een optimale opstelling van de container terminal heeft gemaakt. Daarnaast kunnen we ook aantonen dat het model dat wij hebben gemaakt schaalbaar is. Want door kleine aanpassingen door te voeren zijn wij van een 3x3 yard naar een 3x3x3 yard gegaan (met tussenstappen als 4x4, 5x5 en 2x2x2).

### Planning
In de beginweken van deze minor hebben wij van meneer Andrioli les gekregen over de scrum methode. Met behulp van lego is ons toen uitgelegd over hoe we op een juiste manier de scrum methode konden toepassen. Door middel van sprints van 2 weken konden we onszelf elke keer een nieuw doel stellen. Voor deze minor had ik nog nooit gehoord over de scrum methode. We hebben met het groepje geprobeerd het te gebruiken. Met de nadruk op geprobeerd, want het ging ons niet goed af. We vergaten constant het trello bord te grbuiken en up to date te houden. Dus die methode hebben we na een tijdje losgelaten. Wij hielden nog wel vast aan de sprints van 2 weken, maar tussendoor kwamen we dagelijks bij elkaar om samen aan het project te werken. Ik heb zelf het idee dat ik continu wel duidelijk had wat er allemaal gedaan moest worden en wat ik zelf kon doen om daar aan mee te werken. Het idee van onze planning draaide eigenlijk om het toewerken naar de interne of externe presentaties. Daarmee bedoel ik dat we onszelf een doel stelde om af te krijgen binnen die 2 weken en dat we daar samen naar toe zouden werken. Achteraf gezien is heb ik het idee dat ik ontzettend veel heb geleerd hiervan. Plannen is nooit mijn sterktse punt geweest, dat heb ik bij eerder projecten ook al aangegeven als verbeter punten. En nu zou ik dat weer doen. Ik heb elke keer wel in de gaten wat er gebeurt en wat er moet gebeuren maar er had gedurende deze minor wel beter gepland kunnen worden. Zo was de samenwerking tussen een aantal uit ons groepjes soms ver te zoeken en dat vind ik zonde, dan vraag ik me af hoeveel ik had kunnen leren als die samenwerking beter was geweest.

## Predictive Analytics
Bij dit onderdeel zal ik een aantal verschillende notebooks voorbij laten komen met daarin voorbeelden van hoe ik de dingen die ik heb geleerd heb toegepast. Als eerst zal ik een voorbeeld laten zien van een simpele calssifier, vervolgens zal ik een model laten zien waar ik de data wat moest aanpassen om uiteindelijk een lineaire regressiemodel toe te kunnen passen, daarna zal ik een voorbeeld laten zien van een wat complexer model voor het foodboost project en als laatst zal ik een model laten zien dat we hebben gebruikt voor het project van de containers. 

### Voorbeeld 1
Het gaat om [deze](https://github.com/JoeriHHS/Portfolio/blob/main/Simpele%20Classififer%20(1).ipynb) notebook. In deze notebook kan ik laten zien dat ik een simpele calssifier kan bouwen. Ik zal van begin tot eind even kort toelichten wat er gedaan wordt. Als eerst moeten alle datasets worden ingeladen, dan maak ik uit die datasets 2 lijsten. Een lijst met recepten en een lijst met ingredienten. Vervolgens wordt er een dataframe gemaakt met de recepten op de rijen en de ingredienten in de kolommen, met een 1 als dat ingredient in het recept zit en een 0 als het ingredient niet in het recept zit. Uit deze dataframe wordt de kolom met knoflook gehaald, dat wordt de kolom die ik wil gaan voorspellen. De rest van het dataframe wordt de data waar de voorspelling op gedaan wordt. De data wordt gesplitst in een train en een test gedeelte om uiteindelijk te kunnen evalueren. Bij deze classifier worden 2 modellen aangemaakt. Het gaat beide om een classifier model omdat ik als uitkomst van de voorspelling een 1 of een 0 wil hebben. Dan worden de modellen getrained en wordt de y voor beide modellen voorspelt. Aan de hand van de confusion matrix, de recall score en de accuracy score kan je dan wat over de verklarende waarde van het model zeggen. In dit voorbeeld kunnen we zien dat de accuracy best redelijk is, maar door de confusion matrix en de recall score te bestuderen kunnen we eigenlijk stellen dat dit model het niet heel goed doet. Een lage recall score betekend dat de classifier een hoog aantal valse negatieve scores heeft. Dat komt omdat er in de data maar relatief weinig gerechten met knoflook zijn. Dan gaat de classifier bij elke voorspelling een 0 als uitkomst geven (extreem voorbeeld). Dat is niet de bedoeling van de calssifier. Dit probleem kan onder andere opgelost worden door de data te balanceren door net zoveel gerechten met knoflook als gerechten zonder knoflook in de dataset te hebben. Dat heb ik hier niet meer gedaan omdat dit een voorbeeld is wat ik in de eerste weken heb gemaakt om te leren hoe je een simpele calssifier kan opbouwen. 

### Voorbeeld 2
[Dit](https://github.com/JoeriHHS/Portfolio/blob/main/FoodBoostJoeri%20(1).ipynb) is een notebook waarin ik een lineaire regressie heb toegepast. Ik wilde naast een classifier ook een continue variabele gaan voorspellen. Dat heb ik hier gedaan, ik heb hier gekeken of er een verband is tussen het aantal eiwitten dat in een gerecht zit en de totale energie die in dat gerecht zit. In [dit](https://user-images.githubusercontent.com/122271017/214322067-c071d14b-2f5b-4d16-8421-54b868bb0256.png) plaatje is ook de lineaire regressielijn te zien. De coefficient of determination is 0.57. Dit is een evaluatiemetriek die gebruikt kan worden voor een lineaire regressiemodel, deze metriek vertegenwoordigt het deel van de variantie van de afhankelijke variabele dat wordt verklaard door de onafhankelijke variabelen van het model. Met 0.57 is dat niet hoog en dus kan ik dan stellen dat er een klein positief verband is tussen het aantal eiwitten in een gerecht en de totale energie in een gerecht. In deze notebook laat ik ook al zien dat ik data kan voorbereiden om uiteindelijk er een model mee te bouwen. Door alle 0-waardes eruit te filteren, door visualisaties te maken en door het storen van data in variabelen bereid ik mijn data voor op het bouwen van een model. Dit komt ook terug in het hoofdstuk over data preprocessing.

### Voorbeeld 3
In [het derde voorbeeld](https://github.com/JoeriHHS/Portfolio/blob/main/Classifier500ingred.ipynb) wil ik laten zien dat we voor het foodboost project nog complexere modellen wilden maken. Omdat wij gebruik maakten van gesimuleerde data hebben wij een train, validate en test matrix een keer centraal gemaakt met daarin alle data. Die matrix was als volgt opgebouwd; ieder gesimuleerd persoon heeft 10 favoriete gerechten. Door gebruik te maken van de 'leave one out' constructie maakte wij onszelf rijker aan data. Op die manier is de matrix ook opgebouwd, de eerste 9 gerechten daar de unieke verzmaleing ingredienten van werden geplaatst in de eertse 500 kolommen van de matrix. De ingredeienten van het 10e gerecht werd dan geplaatst in de tweede 500 kolommen van de matrix. De regel daaronder werd dan hetzelfde gedaan, maar werd niet het 10e gerecht meegenomen, maar een random gerecht. En van dat random gerecht werd dan gesteld dat die persoon dat niet lekker zou vinden. Die matrices zijn dus 1 keer centraal aangemaakt en kunnen we elke keer aanroepen zodat we verschillende berekeningen kunnen vergelijken. De berekening die ik hier toepas is door alleen de top 500 vaakst voorkomende ingredienten in de database mee te nemen. Er worden 2 classifier modellen gemaakt die beide op de standaard hyperparameters staan, ik heb nog wel geprobeerd om die aan te passen door bijvoorbeeld cross-validation toe te passen maar dan bleven de uitkomsten eigenlijk hetzelfde. Als uitkomst blijkt dat in ongeveer 50% van de gevallen de modellen aangeven dat de persoon die recepten lekker zal gaan vinden. Omdat dit eigenlijk gelijk is aan een munt opgooien kunnen we niet stellen dat ik model goed zijn werk doet. Dat is balen en dus moesten we op zoek naar iets anders. Dat was eigenlijk elke keer zo tijdens het foodboost project. Elke keer dachten we dat we iet goeds hadden gevonden, maar telkens werden we teleurgesteld en bleek dat het eigenlijk niet zo goed werkte. Dat is ook een van de redenen waarom ik blij ben dat we zijn overgestapt naar het project van de containers, daar begonnen we met een schone lei.

### Voorbeeld 4
In [voorbeeld 4](https://github.com/JoeriHHS/Portfolio/blob/main/Containers%20%20(1).ipynb) laat ik een model zien dat perfect een 3x3 yard met containers kan invullen. In deze notebook bouw ik een neuraal netwerk op. Eerst ben ik aan het bekijken wat ik allemaal nodig heb voor het bouwen van een reinforcement learning algrotime. Ik heb bij het bouwen van dit model veel gekeken naar dit [filmpje](https://www.youtube.com/watch?v=Mut_u40Sqz4&ab_channel=NicholasRenotte). In dit filmpje wordt stap voor stap een RL-model gebouwd om ervoor te zorgen dat de temperatuur van een douche tussen bepaalde waardes blijft. Dit is een totaal verschillend probleem, maar door de problemen naast elkaar te leggen ben ik er toch uitgekomen om dit ook zelf te bouwen, overigens ook met hulp van Jesse die ook deze minor volgt. In de notebook worden eerst 5 episodes gespeeld zodner dat er een RL-model aan te pas komt, met de uitkomsten daarvan kunnen we zien dat het geven van scores wel werkt, maar dat er eigenlijk helemaal niks geleerd wordt. Door het model te trainen, in dit geval met 100000 timesteps gaat het model leren van zijn gemaakte fouten en gaat het geode zetten herkennen. Op het eind is nog de visualisatie te zien van hoe het model dan een 3x3 yard invult. Bij de laatste stap zien we alleen een hele lege matrix, dat komt omdat er eerst wordt gereset voordat de resutaten gedisplayed worden. Het is mij niet gelukt om dit aan te passen, maar door naar de score van de uitkomst te kijken kan er wel worden gezegd dat dit model een 3x3 yard met containers prefect indeeld. 

Ik hoop dat ik met deze voorbeelden kan laten zien dat ik gedurende deze minor een hoop heb geleerd op het gebied van het bouwen van Machine Learning modellen en Neurale Netwerken. 

## Domain knowledge
Ik vind het lastig om aan de hand van geschreven tekst te laten zien dat ik gedurende deze minor mijn domein kennis heb ontwikkeld. En toch ga ik een poging wagen. Toen ik met deze minor ben begonnen wist ik nog helemaal niks af van Machine Learning of Neurale Netwerken. Door deze minor kan ik stellen dat ik een goede basis heb gelegd voor de kennis over deze begrippen. Ik heb dat geleerd door het bijwonen van de lessen van deze minor, maar ook door altijd aanwezig te zijn bij de meetings met de docenten en ook door het werken aan de projecten waar de kennis werd toegepast in de praktijk. Het maken van de DataCamps heeft ook de nodige kennis opgeleverd. Het opzoeken en lezen van bestaande onderzoeken die verduidelijking geven over technieken die ik wilde toepassen bij de projecten. Maar het is lastig om met behulp van voorbeelden toe te lichten waarmee ik kan laten zien dat ik een hoop kennis heb opgedaan tijdens deze minor.  

In mijn notebooks, dit portfolio, het paper en de gesprekken die we met elkaar hebben gevoerd kan ik hopelijk ook aantonen dat ik over voldoende kennis beschik om de juiste begrippen te gebruiken. Met het tentamen is ook getoetst of ik als student voldoende kennis heb over de onderdelen van de Machine Learning. Het tentamen heb ik met een mooi cijfer gehaald dus ook daarmee kan ik aantonen dat het met de domein kennis goed zit. Voor het tentamen heb ik alle begrippen die bij de powerpoints erbij stonden opgeschreven en voor mijzelf omschreven. Daardoor heb ik ook op die manier begripkennis uitgebreid.  

Ik zal nog een aantal gevonden artikelen hier delen waarvan ik denk dat die van toepassing waren op de projecten waaraan ik heb meegewerkt.  
- [Artikel 1](https://www.tandfonline.com/doi/abs/10.3846/16484142.2011.638022)  
- Zeng, Q., Yang, Z., & Hu, X. (2011). A method integrating simulation and reinforcement learning for operation scheduling in container terminals. Transport, 26(4), 383-393. (APA geprobeerd)  
- In dit artikel behandelen de auteurs een Q-learning algoritme (reinforcement learning model) om op basis van simulaties de processen in een container terminal te optimaliseren. Dit artikel komt veel overeen met wat wij wilden onderzoeken, waar het in verschilt is het model dat gebruikt wordt. Wij hebben niet het Q-learning algoritme gebruikt, wij hebben het PPO-model gebruikt.
- [Artikel 2](https://www.sciencedirect.com/science/article/abs/pii/S0370157312000828)  
- Lü, L., Medo, M., Yeung, C. H., Zhang, Y. C., Zhang, Z. K., & Zhou, T. (2012). Recommender systems. Physics reports, 519(1), 1-49. (APA gebprobeerd)  
- In dit artikel worden de meest recente ontwikkelingen van recommender systems besproken en de uitdagingen hiervan. Wat wij met het foodboost wilden doen is in het klein een recommender systeem opbouwen. We hadden uit dit artikel het een en ander aan informatie kunnen gebruiken.
- [Artikel 3](https://iopscience.iop.org/article/10.1088/1742-6596/1873/1/012050/meta)
- Jiang, T., Zeng, B., Wang, Y., & Yan, W. (2021, April). A New Heuristic Reinforcement Learning for Container Relocation Problem. In Journal of Physics: Conference Series (Vol. 1873, No. 1, p. 012050). IOP Publishing.
- In dit onderzoek leggen de auteurs de focus op het zo optimaal mogelijk opstapelen van containers op basis van prioriteit van de container. Het doel is om het aantal relocaties te minimaliseren. Dit is bij ons ook van toepassing, wij willen ook aan de hand van een reinforcement learning model containers zo optimaal mogelijk opstapelen zodat er zo min mogelijk relocaties nodig zijn.


## Data preprocessing


## Communication
Dit stukje wordt beoordeeld op basis van de presentaties en het aandeel in het paper. Ik denk dat communicatie een van mijn sterkere punten is. Daarom wil ik ook graag even vertellen waarom ik denk dat ik dat tijdens deze minor heb laten zien door middel van andere voorbeelden dan het paper en de presentaties.   

### Presentaties
Hier kan ik heel kort over zijn. Ik heb 2 externe presentaties gegeven en daarnaast geholpen bij meerdere interne presentaties. Dit was de [eerste]() externe presentatie en dit was de [tweede]() externe presentatie. Daarnaast is dit een voorbeeld van een [interne]() presentatie die ik heb gegeven. Wij wilde als groepje iedereen de gelegenheid geven om een externe presentatie te doen. De presentaties deden we eigenlijk altijd met 2 personen. Ik vond deze presentaties een fijn onderdeel van deze minor. Hierdoor had ik een moment om naartoe te werken, dat vind ik zelf altijd erg prettig. Het geven van een presentatie vind ik zelf soms wel lastig omdat het dan spannend is, maar door het vaker te doen ga je er wel beter in worden. De presentaties waren ook een moment van feedback dat erg prettig is. Ik heb tijdens de presentaties denk ik wel laten zien dat ik goed kan communiceren

### Paper
Het schrijven van het paper is na de kerstvakantie het doel geweest van ons groepje. We zijn druk bezig geweest met zijn allen om een goed verzorgd paper neer te zetten. Ik heb samen met Hidde de onderzoeksopzet van het paper geschreven. Daarnaast heb ik ook de conclusie en een deel van de discussie geschreven. In de laatste dagen voor de deadline hebben wij met elkaar gezeten om met iedereen samen het paper compleet te maken. Dit hield in dat we allemaal het paper geconcentreerd door zouden lezen en daarbij opmerkingen zouden maken. Die opmerkingen hebben we met elkaar behandeld en uiteindelijk is, nadat iedereen het goed had gekeurd, het paper ingeleverd. 

### Overige communicatie
Wat vaker voorgekomen is bij projecten waaraan ik heb gewerkt is dat ik onbedoeld veel de leiding neem. Ik voel mijzelf verantwoordelijk voor wat de groep preseteert. Ik denk dat dit tijdens deze minor heel goed terug te zien was door de gesprekjes die wij met de docenten hebben gehad en de communicatie onderling in ons groepje. Ik nam elke keer het initatief en wilde iedereen op sleeptouw nemen. Ik ging het gesprek met docenten aan en wilde aan hen laten zien wat wij hebben gedaan. Op deze manier vind ik ook dat ik kan laten zien dat ik op het gebied van communicatie goed scoor.




