import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)
from simpleai.search.csp import _find_conflicts
from datetime import datetime

Charlas = [
    'DjgG', #   40 personas_   computadoras
    'IntoP',#                  computadoras_                    turno mañana
    'Div',#     150 personas_               proyector/audio_    turno tarde     unica charla en horario
    'DevP',#    150 personas_               proyector/audio_    turno tarde_    unica charla en horario
    'ApiDjg',#                              proyector
    'DSA',#                                                                     planta baja
    'Unitst',#                              proyector
    'EditCP',#                              proyector/audio
    'MscP',#    >60 personas_               proyector
    'Neg',#                                                     turno mañana_   42/lab
    'AnImg',#                                                                   magna/42
    'SatEsp',#                              proyector_          turno tarde
    'PubLib',#                              proyector
    'Pand'#:                                proyector_                          planta alta
]
horarios = [10,11,14,15,16,17]
Aulas = [
    1,#Magna:   200per  _pBaja  _proyector/audio
    2,#42:      100per  _pAlta  _proyector
    3,#Lab:     50per   _pBaja  _computadoras
]
""""
def t_mañana(horas):
    for h in horas:
        if h < 12:
            horarios.append(h)
    return horarios
def t_tarde(horas):
    for h in horas:
        if h > 12:
            horarios.append(h)
    return horarios
    def for_horario(horas):
    horario = []
    for horario in horas:
        horario.append()
    return horario 
""" # CUANDO AGREGO EL DOMINIO PARA CHARLAS[X] TENGO QUE AGREGARLE LA LISTA DE HORARIOS POSIBLES (Ej.:(Aula[3], (10,11,12)
    # o por cada horario como unico Ej.: (Aula[3],10) (Aula[3],11) (Aula[3],12) -> La respuesta correcta es esta ultima
def generar_problema_charlas():

    variables = Charlas
    Dom = {variable: [] for variable in variables}
    for horario in horarios:
        Dom[Charlas[0]].append((Aulas[3],horario))
        if horario <12: #charlas solo por la mañana
            Dom[Charlas[1]].append((Aulas[3],horario))
            Dom[Charlas[9]].append((aulas, horario) for aulas in Aulas if aulas != 1)
        if horario >=12: #charlas solo por la tarde
            Dom[Charlas[2]].append((Aulas[1],horario))
            Dom[Charlas[3]].append((Aulas[1],horario))
            Dom[Charlas[11]].append((aulas, horario) for aulas in Aulas if aulas != 3)
        Dom[Charlas[4]].append((aulas,horario)for aulas in Aulas if aulas!=3)
        Dom[Charlas[5]].append((aulas,horario)for aulas in Aulas if aulas!=2)
        Dom[Charlas[6]].append((aulas,horario)for aulas in Aulas if aulas!=3)
        Dom[Charlas[7]].append((Aulas[1],horario))
        Dom[Charlas[8]].append((aulas,horario)for aulas in Aulas if aulas!=3)

        Dom[Charlas[10]].append((aulas,horario)for aulas in Aulas if aulas!=3)

        Dom[Charlas[12]].append((aulas,horario)for aulas in Aulas if aulas!=3)
        Dom[Charlas[13]].append((Aulas[2],horario))

    restricciones = []

    for vars in itertools.combinations(variables,2):
        restricciones.append(((vars[0],vars[1]), charla_asig))

    for var in variables:
        if var != Charlas[2]:
            restricciones.append(((Charlas[2],var),charla_unica))
        if var != Charlas[3]:
            restricciones.append(((Charlas[3],var),charla_unica))
    return  CspProblem(variables, Dom, restricciones)


#no debe haber otra charla en horario para Charla[3] y Charla[4]
def charla_unica(var1, var2):
    return var1[0][1] != var2[0][1]

#no debe haber charlas asignadas a un mismo horario misma aula
def charla_asig(vars, vals):
    return vals[0] != vals[1]

def resolver(metodo_busqueda, iteraciones):
    problema = generar_problema_charlas()

    if metodo_busqueda == "backtrack":
        resultado = backtrack(problema)

    elif metodo_busqueda == "min_conflicts":
        resultado = min_conflicts(problema, iterations_limit=iteraciones)

    return resultado


if __name__ == '__main__':
    metodo = "backtrack"
    iteraciones = None
    #viewer = BaseViewer()

    #metodo = "min_conflicts"
    #iteraciones = 100

    inicio = datetime.now()
    result = resolver(metodo, iteraciones)
    print("tiempo {}".format((datetime.now() - inicio).total_seconds()))
    print(result)
    print(repr(result))


    #problema = generar_problema_charlas()
    #conflictos = _find_conflicts(problema, resultado)
    #print("Numero de conflictos en la solucion: {}".format(len(conflictos)))