def contaSegundos():
    segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
    
    dias = segundos // (24 * 3600)  # Calcula o número de dias
    segundos = segundos % (24 * 3600)  # Calcula o número de segundos restantes

    horas = segundos // 3600  # Calcula o número de horas
    segundos = segundos % 3600  # Calcula o número de segundos restantes

    minutos = segundos // 60  # Calcula o número de minutos
    segundos = segundos % 60  # Calcula o número de segundos restantes

    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")


contaSegundos()
