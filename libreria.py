#ejercicio n°1
def es_mayor(intedad):
    """
    Verifica su intedad es mayor o igual de 18
    :param intedad:
    :return: str
    """
    if (intedad >= 18):
        return "MAYOR"
    else:
        return "MENOR"

#ejercicio n°2
def verifica_marcas_telefono(strnombremarca):
    """
    Verifica strnombremarca ingresado coincide coincide con algunas de las marcas de telefono de la lista.
    :param strnombremarca:
    :return: boolean
    """
    if (strnombremarca =="SAMSUNG" or strnombremarca == "HUAWEI" or strnombremarca == "IPHONE"):
        return True
    else:
        return False
    #fin_veriica_marcas_telefono

#ejercicio n°3
def verifica_partidos_politicos(strpartido):
    """
    Verifica si strpartido coincide con algunos partidos politicos de la lista.
    :param strpartido:
    :return: boolean
    """
    if (strpartido == "PPK" or strpartido == "K" or strpartido == "ALIANZA PARA EL PROGRESO"):
        return True
    else:
        return False
    #fin_verifica_partidos_politicos

#ejercicion°4
def verifica_artefactos(strartefactos):
    """
    Verifica si strartefactos coincide con los artefactos electrodomesticos de la lista.
    :param strartefactos:
    :return: str
    """
    if (strartefactos == "TELEVISION" or strartefactos == "LAVADORA" or strartefactos == "MICROONDAS"):
        return True
    else:
        return False
    #fin_verifica_artefactos.
#ejercicio n°5
def es_menor(intedad):
    """
    Verifica su intedad si es menor que 30
    :param intedad:
    :return: str
    """
    if (intedad < 30):
        return "SI"
    else:
        return "NO"
    #fin_es_menor.
#ejercicio n°6
def verifica_centros_educativos(strcolegios):
    """
    Verifica si strcolegios coinciden en el listado de centros educativos.
    :param strcolegios:
    :return: boolean
    """
    if (strcolegios == "MATER ADMIRABILIS" or strcolegios == "NICOLAS LA TORRE" or strcolegios == "NAZARENO"):
        return True
    else:
        return False
    #fin_verifica_centros_comerciales.
#ejercicio n°7
def verifica_longitud(intaltura):
    """
    Verifica su intaltura es verdadera como se muestra en la lista
    :param intaltura:
    :return: boolean
    """
    if (intaltura == 20):
        return False
    else:
        return True
    #fin_verifica_longitud
#ejercicio n°8
def buen_rendimiento(strrendimiento):
    """
    Verifica su strrendimiento si es bueno en la siguiente lista dada.
    :param strrendimiento:
    :return: str
    """
    if (strrendimiento == "EXCELENTE" or strrendimiento == "BUENO" or strrendimiento == "MUY BUENO"):
        return True
    else:
        return False
    #fin_buen_rendimiento.
#ejercicio n°9
def verificar_diamantes(strdiamntes):
    """
    Verifica su strdiamantes si coinciden con los diamantes en la lista.
    :param strdiamntes:
    :return: str
    """
    if (strdiamntes == "ESMERALDA" or strdiamntes == "RUBI" or strdiamntes == "PERLA"):
        return "SI"
    else:
        return "NO"
    #fin_verificar_diamantes.
#ejercicio n°10
def comprobar_estado(strvih):
    """
    Verificar su strvih si es positivo o negativo en la siguiente lista.
    :param strvih:
    :return: str
    """
    if (strvih == "POSITIVO" or strvih == "NEGATIVO"):
        return "SI"
    else:
        return "NO"
#ejercicio n°11
def productos_consumo(strproductos):
    """
    Verificar si strproductos mencionados si conciden con los productos de consumo en la lista mencionada.
    :param strproductos:
    :return: bool
    """
    if (strproductos == "ARROZ" or strproductos == "LECHE" or strproductos == "ATUN" or strproductos == "AVENA"):
        return True
    return False
    #fin_productos_consumo.
#ejercicio 12
def monto_sueldos(intmonto):
    """
    Verificar su intmonto si coinciden con los montos que estaran en la lista.
    :param intmonto:
    :return: str
    """
    if (intmonto == 930 or intmonto == 1000 or intmonto == 1500 or intmonto == 2000):
        return "SI"
    else:
        return "NO"
    #fin_montos_sueldos.
#ejercicio 13
def sexo(strsexo):
    """
    indicar su strsexo si es masculino o femenino y si coinciden en la lista.
    :param strsexo:
    :return: str
    """
    if (strsexo == "MASCULINO" or strsexo == "FEMENINO"):
        return "SI"
    else:
        return "NO"
    #fin_sexo
#ejercicio 14
def verificar_marcas_deportivas(strmarcas):
    """
    Verificar su strmarca coinciden con las marcas deportivas que aparecen en a lista.
    :param strmarcas:
    :return: bool
    """
    if (strmarcas == "REEBOK" or strmarcas == "ADDIDAS" or strmarcas == "PUMA"):
        return True
    else:
        return False
    #fin_marcas_deportivas.

#ejercicio 15
def lineas_telefonicas(strlineas):
    """
    Verificar  si coinciden con las lineas telefonicas que figuran en la lista.
    :param strlineas:
    :return: str
    """
    if (strlineas == "MOVISTAR" or strlineas == "CLARO" or strlineas == "ENTEL"):
        return "SI"
    else:
        return "NO"
    #fin_lineas_telefonicas.

#ejercicio16
def calles_chiclayo(strcalles):
    """
    Verificar su strcalles  si coinciden con las clles de chiclayo que apareceran en la lista.
    :param strcalles:
    :return: str
    """
    if (strcalles == "BALTA" or strcalles == "BOLOGNESI" or strcalles == "SAENZ PEÑA"):
        return "SI"
    else:
        return "NO"
#ejercicio 17
def idiomas_peruanos(stridiomas):
    """
    Verificar su stridiomas conciden con los idiomas peruanos que aparecen en el listado.
    :param stridiomas:
    :return: bool
    """
    if (stridiomas == "ESPAÑOL" or stridiomas == "QUECHUA" or stridiomas == "AYMARA"):
        return True
    else:
        return False
    #fin_idiomas_peruanos.
#ejercicio18
def comidas(strcom):
    """
    Verificar su strcom si coinciden con las comidas tipicos que hay en la lista
    :param strcom:
    :return: str
    """
    if (strcom == "ARROZ CON PATO" or strcom == "CEVICHE" or strcom == "PARIHUELA"):
        return "TIPICOS"
    else:
        return "NO TIPICOS"
    #fin_comidas.

#ejercicio19
def nombres(strnombre):
    """
    Verificar si strnombre si son nombres de varones que figuran en el listado.
    :param strnombre:
    :return: str
    """
    if (strnombre == "BRYAN" or strnombre == "GEYSON" or strnombre == "DENNIS" or strnombre == "DICK"):
        return "VARONES"
    else:
        return "MUJERES"

#ejercicio20
def juegos_niños(strjuegos):
    """
    Verifica si strjeugos son antiguos o modernos y coinciden cn los de la lista.
    :param strjuegos:
    :return: str
    """
    if (strjuegos == "AMPAY" or strjuegos == "COLUMPIO" or strjuegos == "AVIONSITO"):
        return "ANTIGUOS"
    else:
        return "MODERNOS"
    #fin_juegos_niños.
#ejercicio 21
def estado_civil(strestado):
    """
    Verifica su strestado si su estado civil coinciden con los que figuran en la lista.
    :param strestado:
    :return: str
    """
    if (strestado == "SOLTERO" or strestado == "CASADO" or strestado == "VIUDO" or strestado == "DIVORSIADO"):
        return "SI"
    else:
        return False
    #fin_estado_civil

#ejercicio 22
def colores(strcolores):
    """
    Verificar su strcolores son primarios o secundarios segun el listado dado.
    :param strcolores:
    :return: str
    """
    if (strcolores == "AZUL" or strcolores == "ROJO" or strcolores == "AMARILLO"):
        return "PRIMARIOS"
    else:
        return "SECUNDARIOS"

#ejercicio23
def deportes(strdeport):
    """
    Verificar si strdeport si coinciden con los deportes que estan en la lista.
    :param strdeport:
    :return: bool
    """
    if(strdeport == "NATACION" or strdeport == "FUTTBOL" or strdeport == "VOLEY"):
        return True
    else:
        return False
#ejercicios24
def distrito_chiclayo(strdistritos):
    """
    Verificar si strdistritos si coinciden con los distritos de chiclayo de la lista.
    :param strdistritos:
    :return: str
    """
    if (strdistritos == "VICTORIA" or strdistritos == "JLO" or strdistritos == "PIMENTEL" or strdistritos == "REQUE"):
        return  "SI"
    else:
        return "NO"
    #fin_distritos_chiclayo.

#ejercicio25
def letras(strletras):
    """
    Verifica si strletras si son vocales o son letras del abecedario de la lista.
    :param strvocales:
    :return:str
    """
    if (strletras == "A" or strletras == "E" or strletras == "I" or strletras == "O" or strletras == "U"):
        return "VOCALES"
    else:
        return "ABECEDARIO"
#ejercicio 26
def navegadores(strnavegadores):
    """
    Verifica su strnavageadores coinnciden con los navegadores que se encuentran en la lista.
    :param strnavegadores:
    :return: bool
    """
    if (strnavegadores == "CHROME" or strnavegadores == "MOZILLA" or strnavegadores == "EXPLORE"):
        return True
    else:
        return False
#ejercicio 27
def planetas(strplanetas):
    """
    Verifica su strplnetas si coinciden co los planetas de la lista.
    :param strplanetas:
    :return: str
    """
    if (strplanetas == "TIERRA" or strplanetas == "JUPITER" or strplanetas == "SATURNO"):
        return True
    else:
        return False

#ejercicio 28
def cursos(strareas):
    """
    Verifica su strareas si coinciden con los cursos mencionasdos en la lista.
    :param strareas:
    :return: bool
    """
    if (strareas == "MATEMATICA" or strareas == "CTA" or strareas == "COMUNICACION"):
        return True
    else:
        return False

#ejercicio 29
def licores(strbebidas):
    """
    Verifica su strbebidas si coinciden con los licores emncionados en la lista.
    :param strbebidas:
    :return: str
    """
    if (strbebidas == "VODKA" or strbebidas == "ROM" or strbebidas == "PISCO"):
        return True
    else:
        return False
#ejercciio 30
def obras_literarias(strobras):
    """
    Verificar su strobras si coinciden con las obras literarias en l lista.
    :param strobras:
    :return: str
    """
    if(strobras == "ODISEA" or strobras == "ILIADA" or strobras == "METAMORFOSIS"):
        return True
    else:
        return False
