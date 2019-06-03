# python-kompendium-abbadalor
python-kompendium-abbadalor created by GitHub Classroom

”Frågesport.py” är där själva programmet ligger
”Frågor.py” Är en Dictionary med alla frågor och kategorier i
”Värden.py” Är en Dictionary med alla värden för att kunna visa dem för spelaren

Mitt projekt är egen version av Jeopardy. Eftersom frågorna måste vara i en kategori och ska bara ha ett svar så kunde jag inte använda api för att slumpa fram frågor. Därför skrev jag in 60 frågor från 12 olika kategorier manuellt från J! Archive. Även om det inte är automatiskt så är det lätt att lägga in fler frågor då jag använder ett separat Dictionary för att spara frågorna.

Problemen som jag ser med programmet just nu är att det inte fungerar att köra mer än två rundor, både för att det inte finns tillräckligt många frågor för att för att ha fler rundor och för att sättet jag kodade gör att frågor kan upprepas på den tredje rundan. För att fixa det borde jag kunna använda .append i variabeln kategori2 som visar vilka kategorier redan har används.

Saker som jag skulle kunna lägga till om jag fortsatte arbeta med detta så skulle jag kunna göra så att man kan vara flera spelare och tävla mot varandra. 
En till sak skulle vara att låta spelare spara sina high-scores i ett annat dokument när de har spelat klart.

För att göra det lättare att testa flera rundor kan man ändra siffran 30 på rad 123. Den kontrollerar hur många frågor man måste svara på varje runda.
