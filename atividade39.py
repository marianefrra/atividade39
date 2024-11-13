#lista com os nomes dos meses 

meses = {"Janeiro", "fevereiro", "março","abril", "maio", "junho", "julho", "agosto", "setembro","outubro", "novembro", "dezembro"}

#lista para armazenar as temperaturas dos meses 
temperaturas = []

#entrada das temperaturas 
for i in range(12):
    temp = float(input(f"digite a temperatura média de {meses[i]}:"))
    temperaturas.append(temp)


#calculo da média anual
media_anual = sum(temperaturas) / len(temperaturas)

#exibe a média anual
print(f"\nMédia anual das temperaturas: {media_anual:.2f} C")

#exibe as temperaturas acima da média anual 
print("\nMeses com temperaturas acima da média anual: ")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i + 1} - {meses[i]}:{temperaturas[i]:.2f } C")