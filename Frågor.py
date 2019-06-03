
#Här finns 60 jeopardy frågor i 12 olika kategorier som jag har hittat på nätet
#Jag har skrivit en dictionary för varje fråga med kategori, frågan, svar(kanske flera beroende på om det fnns flera sätt att svara på frågan)
#och poängvärde
totfrågor = { 
    "1": [
        {"titel":"         New Countries          " , "fråga":"With independence in 1993, Eritrea made Ethiopia landlocked, cutting off its access to this sea" , "svar": ["red sea", "the red sea", "redsea"] , "poäng":200}, 
        {"titel":"         New Countries          " , "fråga":"A 24-year armed conflict led to the independence of this nation from South Africa in 1990" , "svar": ["namibia"] , "poäng":400}, 
        {"titel":"         New Countries          " , "fråga":"The 2 Saudi-adjacent countries called this (Aden) & this (Sanaa) merged in 1990 to form a new nation" , "svar": ["north and south yemen", "north yemen and south yemen"] , "poäng":600}, 
        {"titel":"         New Countries          " , "fråga":"Until 1994 the nation of Palau was part of this 'small' Pacific island group" , "svar":"micronesia" , "poäng":800}, 
        {"titel":"         New Countries          " , "fråga":"Russia & China do not recognize the sovereignty of this Muslim majority nation that broke away from Serbia in 2008" , "svar": ["kosovo"] , "poäng":1000}],
    #New Countries  #the red sea / redsea #north yemen and south yemen 

    "2": [
        {"titel":"       Science and Nature       " , "fråga":"Vitamin K is essential for blood to be able to do this normally" , "svar": ["clot"] , "poäng":200}, 
        {"titel":"       Science and Nature       " , "fråga":"This branch of physics deals with the relationship between heat & other forms of energy" , "svar": ["thermodynamics"] , "poäng":400}, 
        {"titel":"       Science and Nature       " , "fråga":"Resembling a hedgehog, the echidna is also known as the 'spiny' this creature" , "svar": ["anteater"] , "poäng":600}, 
        {"titel":"       Science and Nature       " , "fråga":"The difference between fluorescence & this type of glow named for element No. 15 is--complicated" , "svar": ["phosphorescence"] , "poäng":800}, 
        {"titel":"       Science and Nature       " , "fråga":"An experiment in which animals are reared in isolation to see what features are innate is named for this foundling of 19th c. Germany" , "svar": ["Kaspar Hauser"] , "poäng":1000}],
    #Science and Nature

    "3": [ 
        {"titel":"          Legal Terms           " , "fråga":"In early law, this wasn't a crime if it was to your own house; now, burning your place for insurance is a no-no" , "svar": ["arson"] , "poäng":200}, 
        {"titel":"          Legal Terms           " , "fråga":"You took property worth more than $100, so that's grand this, which is ironic, 'cause what you stole is worth about a grand" , "svar": ["larceny"] , "poäng":400}, 
        {"titel":"          Legal Terms           " , "fråga":"Yeah, there was no intention to kill or do grievous bodily harm, so we'll plead to this '2', the negligent or involuntary type" , "svar": ["manslaughter"] , "poäng":600}, 
        {"titel":"          Legal Terms           " , "fråga":"Using political office to collect unlawful fees is this; 'Futurama' was right! The 'X' does make it sound cool" , "svar": ["extortion"] , "poäng":800}, 
        {"titel":"          Legal Terms           " , "fråga":"You appeared to be adversaries, but had a secret pact with your pal to make illegal gains; you're guilty of this 9-letter crime" , "svar": ["collusion"] , "poäng":1000}],
    #Legal Terms    

    "4": [
        {"titel":"       Make Time for Time       " , "fråga":"This short span of time comes before 'messaging' or 'coffee'" , "svar": ["instant"] , "poäng":200}, 
        {"titel":"       Make Time for Time       " , "fråga":"This date is AKA Bissextile Day" , "svar": ["february 29th", "february 29", "29th of february", "29 of february", "29th february", "29 february", "february 29"] , "poäng":400}, 
        {"titel":"       Make Time for Time       " , "fråga":"It's the fixed time designated by authority by which citizens must be inside at night" , "svar": ["curfew"] , "poäng":600}, 
        {"titel":"       Make Time for Time       " , "fråga":"It's how you say 'tomorrow' in Madrid" , "svar": ["mañana", "manana"], "poäng":800}, 
        {"titel":"       Make Time for Time       " , "fråga":"Trust Brother Alex--it's the plural word for the time of evensong prayers, or for the prayers themselves" , "svar": ["vespers"] , "poäng":1000}],
    #Make Time for Time #february 29 / 29th of february / 29 of february / 29th february / 29 february / february 29 #manana
    
    "5": [
        {"titel":"        Moveable Feasts?        " , "fråga":"These game-day cookouts are named for the rear door of a pickup truck" , "svar": ["tailgates", "tailgate"] , "poäng":200}, 
        {"titel":"        Moveable Feasts?        " , "fråga":"In 1935 Mickey Mouse was the first cartoon character to appear on these meal containers for kids" , "svar": ["lunch boxes", "lunchbox", "lunch box", "lunchboxes"] , "poäng":400}, 
        {"titel":"        Moveable Feasts?        " , "fråga":"Unlike the rest of us, Yogi Bear pronounces this outdoor basket meal with 3 syllables" , "svar": ["picnic", "a picnic"] , "poäng":600}, 
        {"titel":"        Moveable Feasts?        " , "fråga":"Kogi, the food truck that started a trend in L.A., has a quesadilla made with this, Korean fermented veggies" , "svar": ["kimchi"] , "poäng":800}, 
        {"titel":"        Moveable Feasts?        " , "fråga":"The food carts that always seem to bump your elbows on airplane aisles are also called these, like streetcars" , "svar": ["trolleys", "trolley"] , "poäng":1000}],
    #Moveable Feasts? #tailgate #lunchbox / lunch box / lunchboxes #a picnic

    "6": [
        {"titel":"        Rhymes With All         " , "fråga":"Sloppy, illegible handwriting" , "svar": ["scrawl"] , "poäng":200}, 
        {"titel":"        Rhymes With All         " , "fråga":"A cozy compartment for a horse in a stable" , "svar": ["stall", "a stall"] , "poäng":400}, 
        {"titel":"        Rhymes With All         " , "fråga":"To examine extensively & then make any needed repairs" , "svar": ["overhaul"] , "poäng":600}, 
        {"titel":"        Rhymes With All         " , "fråga":"To cast one of these over things is to give them a gloomy atmosphere" , "svar": ["pall"] , "poäng":800}, 
        {"titel":"        Rhymes With All         " , "fråga":"A city's disorderly spread outward into surrounding areas" , "svar": ["sprawl", "urban sprawl", "urbansprawl"] , "poäng":1000}],
    #Rhymes With All #a stall  #urbansprawl urban sprawl


    "7": [
        {"titel":"   CIA World Factobook No. 1s   " , "fråga":"Monaco leads in this: it's 89.40 years from birth" , "svar": ["lifespan", "life expectancy", "lifeexpectancy"] , "poäng":200}, 
        {"titel":"   CIA World Factobook No. 1s   " , "fråga":"Saudi Arabia: exports of this, 7.3 million barrels a day" , "svar": ["oil"] , "poäng":400}, 
        {"titel":"   CIA World Factobook No. 1s   " , "fråga":"The United States: 13,513 of these, including Logan & McCarran" , "svar": ["airports", "airport"] , "poäng":600}, 
        {"titel":"   CIA World Factobook No. 1s   " , "fråga":"China: 731 million users of this technological network" , "svar": ["the internet", "internet"] , "poäng":800}, 
        {"titel":"   CIA World Factobook No. 1s   " , "fråga":"South Africa: 7.2 million people living with this communicable affliction" , "svar": ["aids"] , "poäng":1000}],
    #CIA World Factobook No. 1s #life expectancy #internet

    "8": [
        {"titel":" The Right To Remain Silent 'P' " , "fråga":"Sometimes found before 'intellectual', it has stepped out on its own as a 6-letter word for fake" , "svar": ["pseudo"] , "poäng":200}, 
        {"titel":" The Right To Remain Silent 'P' " , "fråga":"It means inflated with air, as in that type of tire" , "svar": ["pneumatic"] , "poäng":400}, 
        {"titel":" The Right To Remain Silent 'P' " , "fråga":"The silent 'P' comes third in this word for the place you might keep plates or spices" , "svar": ["cupboard", "cupboards", "a cupboard"] , "poäng":600}, 
        {"titel":" The Right To Remain Silent 'P' " , "fråga":"The 3 main forms of plague in humans are bubonic, septicemic & this one that strikes the lungs" , "svar": ["pneumonic"] , "poäng":800}, 
        {"titel":" The Right To Remain Silent 'P' " , "fråga":"A recent discovery in Utah: perhaps the oldest flying vertebrate, a 200-million-year-old one of these" , "svar": ["pterodactyl"] , "poäng":1000}],
    #The Right To Remain Silent "P"
    
    "9": [
        {"titel":"Google's Top Searches, 1999-2018" , "fråga":"Every year, this best pal has been the most searched-for type of animal" , "svar": ["dog", "dogs"] , "poäng":200}, 
        {"titel":"Google's Top Searches, 1999-2018" , "fråga":"The top movie searches of 2006 & 2016 were for this franchise with 'The Last Stand' & 'Apocalypse' installments" , "svar": ["x-men", "xmen", "x men"] , "poäng":400}, 
        {"titel":"Google's Top Searches, 1999-2018" , "fråga":"Each year the most searched-for author has been not a novelist but this man who penned 'Letter from Birmingham Jail'" , "svar": ["martin luther king", "mlk", "martin king"] , "poäng":600}, 
        {"titel":"Google's Top Searches, 1999-2018" , "fråga":"For 2016 & 2017 the most searched athlete was this Dublin-born MMA fighter" , "svar": ["conor mcgregor"] , "poäng":800}, 
        {"titel":"Google's Top Searches, 1999-2018" , "fråga":"Since 2005 the Bible has been the most searched book & No. 2 has been this somewhat more recent sacred text" , "svar": ["koran", "the koran"] , "poäng":1000}],
    #Google's Top Searches, 1999-2018 #xmen #mlk #the koran

    "10": [
        {"titel":"          Classic Film          " , "fråga":"A line from this 1972 classic: 'It's a Sicilian message. It means Luca Brasi sleeps with the fishes'" , "svar": ["the godfather", "godfather"] , "poäng":200}, 
        {"titel":"          Classic Film          " , "fråga":"This 1994 prison drama starring Tim Robbins & Morgan Freeman reminds us that hope can set you free" , "svar": ["shawshank redemption", "the shawshank redemtion"] , "poäng":400}, 
        {"titel":"          Classic Film          " , "fråga":"She won an Oscar for playing Clarice Starling in 'The Silence of the Lambs'" , "svar": ["jodie foster"] , "poäng":600}, 
        {"titel":"          Classic Film          " , "fråga":"1930s comedy classics starring this zany trio include 'A Day at the Races' & 'A Night at the Opera'" , "svar": ["marx brothers", "the marx brothers"] , "poäng":800}, 
        {"titel":"          Classic Film          " , "fråga":"In the U.S. Sergio Leone's spaghetti western 'Il Buono, il Brutto, il Cattivo' has this title" , "svar": ["the good, the bad and the ugly"] , "poäng":1000}],
    #Classic Film #the shawshank redemption

    "11": [
        {"titel":"          From B to C           " , "fråga":"The 'B' in ICBM stands for this kind of missile" , "svar": ["ballistic"] , "poäng":200}, 
        {"titel":"          From B to C           " , "fråga":"Also a simple programming language, it means unoriginal or mainstream in modern slang" , "svar": ["basic"] , "poäng":400}, 
        {"titel":"          From B to C           " , "fråga":"It's a cockroach's least favorite acid" , "svar": ["boric acid"] , "poäng":600}, 
        {"titel":"          From B to C           " , "fråga":"Adjective meaning related to the countryside, especially its pleasant aspects" , "svar": ["bucolic"] , "poäng":800}, 
        {"titel":"          From B to C           " , "fråga":"He wrote more than 90 stories examining the complexities of 19th century French society" , "svar": ["balzac"] , "poäng":1000}],
    #From B to C

    "12": [
        {"titel":" Classic Movies in 3 Sentences  " , "fråga":"Witch crushed to death. Victim's sister also killed. Killer sent to Kansas, not prison" , "svar": ["wizard of oz", "the wizard of oz"] , "poäng":200}, 
        {"titel":" Classic Movies in 3 Sentences  " , "fråga":"A snow globe falls from a hand. Xanadu makes news. A sled goes into an incinerator" , "svar": ["citizen kane"] , "poäng":400}, 
        {"titel":" Classic Movies in 3 Sentences  " , "fråga":"Cary Grant mistaken for a spy. He proposes between 2 giant heads. A train enters a tunnel" , "svar": ["north by northwest"] , "poäng":600}, 
        {"titel":" Classic Movies in 3 Sentences  " , "fråga":"A knife fight at an observatory. A cliffside drag race. A shooting at an observatory" , "svar": ["rebel without a cause", "the rebel without a cause", "a rebel without a cause"] , "poäng":800}, 
        {"titel":" Classic Movies in 3 Sentences  " , "fråga":"A marshal gets married. A train arrives right on time. A bride shoots a man in the back" , "svar": ["high noon"] , "poäng":1000}]
        #Classic Movies in 3 Sentences
}