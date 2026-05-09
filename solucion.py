import re

texto = "En el año 2025, 26 programadores desarrollan juntos. ¡Hola! ¿Te gusta programar? El cielo digital, las estrellas (★) brillan. 22 niños codifican, 21.50 horas de trabajo. Lista: teclado, monitor, mouse. El costo es $105.20. ¿Sabías que el código #3344 es especial? La vida es código, @todos participan. El tiempo pasa, 23 días de desarrollo. ¡Programa! El número especial es 1616. ¿Qué harías con 66.90 pesos? La respuesta está en la lista: escribir, depurar, crear. ¡Desarrolla tu futuro! 100 palabras, 23 enteros, 3 decimales, 2 listas."
                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\.\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]ista:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)



import re

texto = "Salut! En 2025, 24 programmeurs codent ensemble. Liste: clavier, écran, souris. Le prix est de 103,40€. Les étoiles (★) brillent la nuit. 20 chats codent, 19 chiens testent. Le code #5566 est spécial. 23 jours de développement, 17 jours de repos. @tous codent. Le numéro magique est 1626. Que feriez-vous avec 69,70€? La réponse est dans la liste: écrire, tester, créer. Développez votre avenir! 100 mots, 23 entiers, 3 decimales, 2 listas."

                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\,\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]iste:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚ]+\b"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)


import re

texto = "Ciao! Nel 2025, 25 programmatori sviluppano insieme. Lista: tastiera, schermo, mouse. Il prezzo è €100,80. Le stelle (★) brillano sopra il computer. 19 gatti scrivono, 18 cani testano. Il codice #7788 è speciale. 22 giorni di sviluppo, 18 di riposo. @tutti sviluppano. Il numero magico è 1636. Cosa faresti con 63,90€? La risposta è nella lista: scrivere, testare, creare. Sviluppa il tuo futuro! 100 parole, 22 interi, 3 decimales, 2 listas."
                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\,\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]ista:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b|è"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)