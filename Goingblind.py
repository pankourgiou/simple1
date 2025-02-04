import pyttsx3

# Quenya poem text (experimental translation)
quenya_poem = """
Essë tultien ve i etelárë mi tála.  
Mal, nu etë núta,  
essë nasta cendë i káppa órenna.  
Essë minë nildë.  
Ná ve úlacë.
Ar, ve i etelárë lavëa,  
ar lahta, ve Corma sanda, laita;  
ar lenda mi ósta nárë,  
(quentuvant ar nildavant)  
– cenin essë.  
Essë lenda úvë.
I etelárë, marillë,  
ve nísë, nauva cantëa  
mi alcarin parma;  
mi nalyallo, ya caluva alassëo,  
cala raltëa ve mi paurë.
Essë lendë lahta, ar nóren minya,  
ve i matta úva caurelyë mi nórë;  
ar ananta: ve, nu matta caurelya nórienna,  
essë nasta ve ilyë nórë –  
ar yelvea.
"""

# Initialize the TTS engine.
engine = pyttsx3.init()

# Optional: Adjust the speech rate (words per minute).
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)  # Slow it down a bit.

# Optional: Choose a voice.
voices = engine.getProperty('voices')
# You can choose a different voice by changing the index.
engine.setProperty('voice', voices[0].id)

# Read the poem aloud.
engine.say(quenya_poem)
engine.runAndWait()
