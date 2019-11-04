Charlas = {
    'DjgG', #   40 personas_   computadoras
    'IntoP',#                  computadoras_                    turno mañana
    'Div',#     150 personas_               proyector/audio_    turno tarde
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
}
horarios = [10,11,14,15,16,17]
Aulas = {
    1,#Magna:   200per  _pBaja  _proyector/audio
    2,#42:      100per  _pAlta  _proyector
    3,#Lab:     50per   _pBaja  _computadoras
}

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

def generar_problema_charlas():

    variables = Charlas
    Dom = {variable: [] for variable in variables}

    Dom[Charlas[0]].append((Aulas[3],horario) for horario in horarios)
    Dom[Charlas[1]].append((Aulas[3],t_mañana(horarios)))
    Dom[Charlas[2]].append((Aulas[1],t_tarde(horarios)))
    Dom[Charlas[3]].append((Aulas[3],t_mañana(horarios)))
    Dom[Charlas[4]].append((aulas,horario)for aulas in Aulas if aulas!=3 for horario in horarios)
    Dom[Charlas[5]].append((aulas,horario)for aulas in Aulas if aulas!=2 for horario in horarios)
    Dom[Charlas[6]].append((aulas,horario)for aulas in Aulas if aulas!=3 for horario in horarios)
    Dom[Charlas[7]].append((Aulas[1],horario) for horario in horarios)
    Dom[Charlas[8]].append((aulas,horario)for aulas in Aulas if aulas!=3 for horario in horarios)
    Dom[Charlas[9]].append((aulas,t_mañana(horarios))for aulas in Aulas if aulas!=1)
    Dom[Charlas[10]].append((aulas,horario)for aulas in Aulas if aulas!=3 for horario in horarios)
    Dom[Charlas[11]].append((aulas,t_tarde(horarios))for aulas in Aulas if aulas!=3)
    Dom[Charlas[12]].append((aulas,horario)for aulas in Aulas if aulas!=3 for horario in horarios)
    Dom[Charlas[13]].append((Aulas[2],horario) for horario in horarios)

    #no debe haber otra charla en horario de Charla[3]

    #no debe haber repetidas (intertools.combinations)