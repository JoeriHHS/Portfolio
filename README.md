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
Bij dit onderdeel zal ik een aantal verschillende notebooks voorbij laten komen met daarin voorbeelden van hoe ik de dingen die ik heb geleerd heb toegepast. Als eerst zal ik een voorbeeld laten zien van een simpele calssifier, daarna zal ik een voorbeeld laten zien van een wat complexer model voor het foodboost project en als laatst zal ik een model laten zien dat we hebben gebruikt voor het project van de containers. 

### Voorbeeld 1
Het gaat om [deze](https://github.com/JoeriHHS/Portfolio/blob/main/Simpele%20Classififer.ipynb) notebook. In deze notebook kan ik laten zien dat ik een simpele calssifier kan bouwen. Ik zal van begin tot eind even kort toelichten wat er gedaan wordt. Als eerst moeten alle datasets worden ingeladen, dan maak ik uit die datasets 2 lijsten. Een lijst met recepten en een lijst met ingredienten. Vervolgens wordt er een dataframe gemaakt met de recepten op de rijen en de ingredienten in de kolommen, met een 1 als dat ingredient in het recept zit en een 0 als het ingredient niet in het recept zit. 





