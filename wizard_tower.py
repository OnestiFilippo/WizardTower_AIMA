import sys
import matplotlib.pyplot as plt
from search import Problem, astar_search, depth_first_graph_search, best_first_graph_search, uniform_cost_search, breadth_first_graph_search
import time
import os
import math

# Nome del file passato come argomento da riga di comando
try:
    filename = "instances/"+sys.argv[1]
except IndexError:
    print("Usage: wizard_tower.py <filename>")
    print("Examples: ")
    print("\t - wizard_tower.py input.txt")
    print("\t - wizard_tower.py iwt01.txt")
    sys.exit()

# Lista dei valori dell'euristica per il grafico
list_h = []

# Variabile contatore per il numero di nodi esplorati
counter = 0

# Definizione della classe WizardTower
class WizardTower(Problem):
    def __init__(self, inState):
        # Lo stato iniziale è una tupla che contiene lo stato, il numero di creature e se il mago ha la pozione
        super().__init__(inState)

    def actions(self, actState):
        #Restituisce la lista delle azioni possibili nello stato attuale.

        state, num_creature, pozione_poss = actState

        # Calcolo la posizione del mago che può essere X, XM, XP o XC
        for i in range(0, len(state)):
            if state[i] == "X" or state[i] == "XM" or state[i] == "XC" or state[i] == "XP":
                (xM, yM) = (i//dim_Y, i%dim_Y)
                break

        # Calcolo la posizione delle pozioni
        pos_pozioni = []
        for i in range(0, len(state)):
            if state[i] == "M" or state[i] == "XM":
                (xP, yP) = (i//dim_Y, i%dim_Y)
                pos_pozioni.append((xP, yP))

        # Calcolo la posizione delle creature
        pos_creature = []
        for i in range(0, len(state)):
            if state[i] == "C" or state[i] == "XC":
                (xC, yC) = (i//dim_Y, i%dim_Y)
                pos_creature.append((xC, yC))

        # Calcolo la posizione dei muri
        pos_muri = []
        for i in range(0, len(state)):
            if state[i] == "B":
                (xB, yB) = (i//dim_Y, i%dim_Y)
                pos_muri.append((xB, yB))

        possible_actions = []

        # Calcolo delle azioni possibili
        if (xM > 0) and ((xM-1, yM) not in pos_muri) and (((xM-1, yM) not in pos_creature) or ((xM-1, yM) in pos_creature and pozione_poss == 1)):
            possible_actions.append("UP")
        if (xM < dim_X-1) and ((xM+1, yM) not in pos_muri) and (((xM+1, yM) not in pos_creature) or ((xM+1, yM) in pos_creature and pozione_poss == 1)):
            possible_actions.append("DOWN")
        if (yM > 0) and ((xM, yM-1) not in pos_muri) and (((xM, yM-1) not in pos_creature) or ((xM, yM-1) in pos_creature and pozione_poss == 1)):
            possible_actions.append("LEFT")
        if (yM < dim_Y-1) and ((xM, yM+1) not in pos_muri) and (((xM, yM+1) not in pos_creature) or ((xM, yM+1) in pos_creature and pozione_poss == 1)):
            possible_actions.append("RIGHT")
        if (xM, yM) in pos_pozioni and pozione_poss == 0:
            possible_actions.append("POTION")
        if ((xM, yM) in pos_creature) and (pozione_poss == 1):
            possible_actions.append("KILL")
        
        return possible_actions
            
    # funzione che applica un'azione e restituisce il nuovo stato
    def result(self, actState, action):

        state, num_creature, pozione_poss = actState

        global counter
        counter += 1

        # Calcolo la posizione del mago che può essere X, XM, XP o XC
        for i in range(0, len(state)):
            if state[i] == "X" or state[i] == "XM" or state[i] == "XC" or state[i] == "XP":
                pos_mago = i
                (xM, yM) = (i//dim_Y, i%dim_Y)
                break
        
        # Trasfromazione dello stato in una lista
        state = list(state)

        if action == "UP":
            swap =  pos_mago-dim_Y
        elif action == "DOWN":
            swap = pos_mago+dim_Y
        elif action == "LEFT":
            swap = pos_mago-1
        elif action == "RIGHT": 
            swap = pos_mago+1
        
        elif action == "POTION":
            pozione_poss = 1
            state[pos_mago] = "X"
        elif action == "KILL":
            state[pos_mago] = "X"
            pozione_poss = 0
            num_creature -= 1

        if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if state[pos_mago] == "XM":
                if state[swap] == "_":
                    state[swap] = "X"
                    state[pos_mago] = "M"
                elif state[swap] == "C":
                    state[swap] = "XC"
                    state[pos_mago] = "M"
            elif state[pos_mago] == "XC":
                if state[swap] == "_":
                    state[swap] = "X"
                    state[pos_mago] = "C"
                elif state[swap] == "P":
                    state[swap] = "XP"
                    state[pos_mago] = "C"
                elif state[swap] == "M":
                    state[swap] = "XM"
                    state[pos_mago] = "C"
            elif state[pos_mago] == "XP":
                if state[swap] == "_":
                    state[swap] = "X"
                    state[pos_mago] = "P"
                elif state[swap] == "C":
                    state[swap] = "XC"
                    state[pos_mago] = "P"
            elif state[swap] == "M":
                state[swap] = "XM"
                state[pos_mago] = "_"
            elif state[swap] == "C":
                state[swap] = "XC"
                state[pos_mago] = "_"
            elif state[swap] == "P":
                state[swap] = "XP"
                state[pos_mago] = "_"
            else:
                state[pos_mago] = "_"
                state[swap] = "X"

        # Trasformazione dello stato in una tupla
        state = tuple(state)

        if xM < 0 or xM >= dim_X or yM < 0 or yM >= dim_Y:
            print((xM, yM))
            print((dim_X, dim_Y))
            print("Errore: posizione mago non valida")
            sys.exit()

        return (state, num_creature, pozione_poss)
    
    # Funzione che aggiorna il costo del percorso in base all'azione
    def path_cost(self, c, state1, action, state2):
        if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            return c + 1
        elif action in ["POTION", "KILL"]:
            return c

    # Funzione goal che restituisce True se lo stato attuale è uno stato goal
    def goal_test(self, actState):
        state, num_creature, pozione_poss = actState

        # Calcolo la posizione del portale
        for i in range(0, len(state)):
            if state[i] == 'P' or state[i] == "XP":
                pos_portale = i

        # Calcolo la posizione del mago
        for i in range(0, len(state)):
            if state[i] == "X" or state[i] == "XM" or state[i] == "XC" or state[i] == "XP":
                pos_mago = i

        # se non ci sono più creature e il mago è sul portale è lo stato goal
        if num_creature == 0 and pos_mago == pos_portale:
            return True
        else:
            return False
            
    #Funzione euristica
    def h(self, node):
        
        actState = node.state
        state, num_creature, pozione_poss = actState

        pos_pozioni = []
        pos_creature = []
        pos_portale = None

        # Calcolo delle posizioni del mago, delle pozioni, delle creature e del portale
        for i in range(len(state)):
            if state[i] in {"X", "XM", "XC", "XP"}:
                (xM, yM) = (i // dim_Y, i % dim_Y)  # posizione del mago
            if state[i] in {"M", "XM"}:
                (xPoz, yPoz) = (i // dim_Y, i % dim_Y)  # posizione delle pozioni
                pos_pozioni.append((xPoz, yPoz))
            elif state[i] in {"C", "XC"}:
                (xC, yC) = (i // dim_Y, i % dim_Y)  # posizione delle creature
                pos_creature.append((xC, yC))
            elif state[i] in {"P", "XP"}:
                (xP, yP) = (i // dim_Y, i % dim_Y)  # posizione del portale
                pos_portale = (xP, yP)
        
        num_pozioni = len(pos_pozioni)

        # Restituisce la distanza minima tra il mago e le pozioni se il mago non possiede la pozione e se ci sono creature
        if pozione_poss == 0 and num_creature > 0 and num_pozioni > 0:
            num_creature = num_creature+1
            num_pozioni = num_pozioni+2
            h = min([math.dist((xM, yM), pos_pozione) for pos_pozione in pos_pozioni])+(num_creature*num_creature)+(num_pozioni*num_pozioni)
            #print(f"A: {h}")
            list_h.append(h)
            return h

        # Restituisce la distanza minima tra il mago e le creature se il mago possiede la pozione
        elif pozione_poss == 1 and num_creature > 0 and num_pozioni > 0:
            num_creature = num_creature+2
            num_pozioni = num_pozioni+1
            h = min([math.dist((xM, yM), pos_creatura) for pos_creatura in pos_creature])+(num_creature*num_creature+num_pozioni*num_pozioni)
            #print(f"B: {h}")
            list_h.append(h)
            return h


        # Restituisce la distanza tra il mago e l'ultima creatura se non ci sono pozioni
        elif num_pozioni == 0 and num_creature > 0:
            num_creature = num_creature+2
            h = min([math.dist((xM, yM), pos_creatura) for pos_creatura in pos_creature])+(num_creature)
            #print(f"C: {h}")
            list_h.append(h)
            return h

        # Restituisce la distanza tra il mago e il portale se non ci sono creature
        elif num_creature == 0:
            h = math.dist((xM, yM), pos_portale)
            #print(f"D: {h}")
            list_h.append(h)
            return h
    
    # Stampa dello stato attuale
    def print_state(self, actState):
        state, num_creature, pozione_poss = actState
        # stampa della configurazione attuale
        for i in range(0, len(state)):
            if i % dim_Y == 0:
                print()
            print(state[i], end="  ")
        print()

        # Calcolo la posizione del mago che può essere X, XM, XP o XC
        for i in range(0, len(state)):
            if state[i] == "X" or state[i] == "XM" or state[i] == "XC" or state[i] == "XP":
                pos_mago = i
                (xM, yM) = (i//dim_Y, i%dim_Y)
                break

        print("Pozione:",pozione_poss)
        print("Creature:",num_creature)
        print()

# Funzione per la creazione del grafico dell'euristica
def create_graph(list_h):
    plt.plot(list_h)
    plt.ylabel('h(n)')
    plt.xlabel('nodi')
    plt.title('Funzione euristica')
    plt.show()

# Lettura del file di input
def read_file(file):
    dim_X = 0
    dim_Y = 0
    num_pozioni = 0
    num_creature = 0
    (xM, yM) = (0, 0)

    initial_state = list()

    with open(file, "r") as f:
        dim_X = int(f.readline().strip())
        dim_Y = int(f.readline().strip())
        num_pozioni = int(f.readline().strip())
        num_creature = int(f.readline().strip())
        (xM, yM) = tuple(map(int, f.readline().strip().split()))

        for line in f:
            for char in line:
                if(char == '_'):
                    initial_state.append("_")
                elif(char == 'P'):
                    initial_state.append("P")
                elif(char == 'C'):
                    initial_state.append("C")
                elif(char == 'M'):
                    initial_state.append("M")
                elif(char == 'B'):
                    initial_state.append("B")
        
        # posizione del mago
        initial_state[xM*dim_Y + yM] = "X"
        

    return dim_X, dim_Y, num_pozioni, num_creature, xM, yM, tuple(initial_state)

# Visualizzazione della soluzione trovata
def executeSolution(initialState, result):
    state = initialState
    for action in result.solution():
        os.system('clear')
        state = problem.result(state, action)
        problem.print_state(state)
        time.sleep(0.3)
        

# Lettura del file di input
dim_X, dim_Y, num_pozioni, num_creature, xM, yM, initial_state = read_file(filename)

# Stampa delle informazioni iniziali
print("dimensione X =",dim_X)
print("dimensione Y =",dim_Y)
print("numero pozioni =",num_pozioni)
print("numero creature =",num_creature)
print("posizione mago =",xM, yM)

# Creazione dell'istanza del problema
problem = WizardTower((initial_state, num_creature, 0))
problem.print_state((initial_state, num_creature, 0))

try:
    start_time = time.time()
    print("Ricerca della soluzione...\n")

    #result = astar_search(problem)
    #result = uniform_cost_search(problem)
    result = best_first_graph_search(problem, problem.h)
    #result = depth_first_graph_search(problem)
    #result = breadth_first_graph_search(problem)
    
    end_time = time.time()
    if result == None:
        print("Soluzione non trovata")
    else:
        print("Soluzione trovata:")
        print(f"Nodi esplorati: {counter}")
        print(f"Tempo di esecuzione: {end_time-start_time}")
        print(f"Percorso: {result.solution()}")
        print(f"Costo: {result.path_cost}")
        if list_h != []:
            create_graph(list_h)
        #executeSolution((initial_state, num_creature, 0), result)
except KeyboardInterrupt:
    print("Numero di nodi esplorati prima dell'uscita:", counter)
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()