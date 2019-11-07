from simpleai.search import SearchProblem
from simpleai.search.traditional import breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer

IslaFran = [0,2]
IslaPira = [5,5]

def manhattan(pos1,pos2):
		return (abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]))


class entrega1(SearchProblem):
	def actions(self,state):
		piratas = list(state[1])
		movimientos = []
		num_pirata = 0
		for pirata in piratas:
			if pirata[0]>0:
				movimientos.append([pirata[0]-1,pirata[1],num_pirata]) #Fila resultante, columna y pirata a mover
			if pirata[0]<5:
				movimientos.append([pirata[0]+1,pirata[1],num_pirata]) #Fila resultante, columna y pirata a mover
			if pirata[1]>0:
				movimientos.append([pirata[0],pirata[1]-1,num_pirata]) #Fila, columna resultante y pirata a mover
			if pirata[1]<5:
				movimientos.append([pirata[0],pirata[1]+1,num_pirata]) #Fila, columna resultante y pirata a mover
			num_pirata=num_pirata+1 
		return movimientos

	def result(self, state, action):
		fila, columna, pos_pirata = action              #Divido las 3 partes de la acción.
		franceses = list(state[0])
		piratas = list(state[1])
		barco = list(state[1][pos_pirata])
		if (fila,columna) in franceses:
			posicion = fila,columna
			franceses.remove(posicion)
			piratas.pop(num_pirata)
		else:
			if IslaFran[0] == fila and IslaFran[1] == columna:
				piratas[num_pirata][2] = 1
			barco[0] = fila
			barco[1] = columna
		piratas[pos_pirata] = tuple(barco)
		state = (tuple(franceses),tuple(piratas))
		print(state)
		return state

	def is_goal(self, state):
		piratas = list(state[1])
		filagoal = IslaPira[0]
		columnagoal = IslaPira[1]
		GOAL = (filagoal,columnagoal,1)

		return (GOAL in piratas)

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state): #Distancia de manhattan del pirata más cerca de la solución.
		primero = True                                          
		distancia = 0
		franceses = list(state[0])
		piratas = list(state[1])
		for pirata in piratas:                                  #Recorro los piratas
			if pirata[2]==1:                                    #SI EL PIRATA TIENE EL MAPA
				pos_pirata= [pirata[0],pirata[1]]             
				distancia = manhattan(pos_pirata,IslaPira)      #Guardo en distancia la distancia entre el pirata y la salida
				if primero == true:                             #Si es el primer pirata
					heuristica = distancia                      #Guardo la distancia en heuristica
					primero = False
				elif distancia < heuristica:                    #Si no es el primero pero la distancia de este pirata a la salida
					heuristica = distancia                      #es menor a la guardada previamente en heuristica se cambia
			if pirata[2]==0:                                    #SI EL PIRATA NO TIENE EL MAPA
				pos_pirata= [piratas[0],piratas[1]]
				distancia = manhattan(pos_pirata,IslaPira)+manhattan(IslaFran,IslaPira) #Guardo en distancia la distancia entre el pirata y el mapa+el mapa y la salida
				if primero == True:                              #Si es el primer pirata
					heuristica = distancia                      #Guardo la distancia en heuristica
					primero = False
				elif distancia < heuristica:                    #Si no es el primero pero la distancia de este pirata al mapa y a la salida
					heuristica = distancia                      #es menor a la guardada previamente en heuristica se cambia
		return heuristica

def resolver(metodo_busqueda, franceses, piratas):
	viewer = None
	barcos = []

	inicial = (tuple(franceses),tuple(piratas))

	problem = entrega1(inicial)
	if metodo_busqueda == "breadth_first":    
		resultado = breadth_first(problem, graph_search=True, viewer = viewer)
	elif metodo_busqueda == "greedy":    
		resultado = greedy(problem, graph_search=True, viewer = viewer)
	elif metodo_busqueda == "depth_first":    
		resultado = depth_first(problem, graph_search=True, viewer = viewer)
	elif metodo_busqueda == "astar":
		resultado = astar(problem, graph_search=True, viewer = viewer)
	elif metodo_busqueda == "uniform_cost":
		resultado = uniform_cost(problem, graph_search=True, viewer = viewer)

	return resultado


#if __name__ == '__main__':

#viewer = WebViewer()
viewer = ConsoleViewer()
#viewer = None
#viewer = BaseViewer()

#metodo = "greedy"
metodo = "breadth_first"
#metodo = "astar"
#metodo = "uniform_cost"
#metodo = "depth_first"

franceses = [(0,2), (0,3), (1,2), (1,3), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (4,0), (4,1), (5,0)]
piratas = [(4,4,0), (4,5,0), (5,4,0)]

result = resolver(metodo, franceses, piratas)

print("#" * 80)
print("Franceses:")
print(franceses)
print("Piratas:")
print(piratas)
print("#" * 80)
print("Estado final: {}".format(result.state))
print("#" * 80)
for accion, resultado in enumerate(result.path()):
	print('Accion',accion, ':', resultado[0])
	print('Resultado:', resultado[1])

print("#" * 80)
print("Nodos Visitados: {}".format(viewer.stats['visited_nodes']))
print("Profundidad solucion: {}".format(len(result.path())))
print("Costo: {}".format(result.cost))
print("Tamaño máximo frontera: {}".format(viewer.stats['max_fringe_size']))
