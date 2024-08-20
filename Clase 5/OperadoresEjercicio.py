tengo_dinero = True
esta_lloviendo = False
tengo_paraguas = True

jugar_al_futbol = tengo_dinero and (not esta_lloviendo or tengo_paraguas)
print(jugar_al_futbol)
