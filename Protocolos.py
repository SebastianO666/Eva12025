#el nombre del protocolo
protocolo = input("Ingrese el nombre del protocolo (OSPF, RIP, EIGRP, BGP): ").upper()

# Evaluación usando if / elif / else
if protocolo == "OSPF":
    print("La distancia administrativa de OSPF es 110.")
elif protocolo == "RIP":
    print("La distancia administrativa de RIP es 120.")
elif protocolo == "EIGRP":
    print("La distancia administrativa de EIGRP es 90.")
elif protocolo == "BGP":
    print("La distancia administrativa de BGP es 20.")
else:
    print("Protocolo no reconocido. Intente con OSPF, RIP, EIGRP o BGP.")
