def contar_calorias(ejercicio,minutos):
    quemado={"futbol":5,"Bicicleta":10}
    return quemado.get(ejercicio,5)*minutos
