valor1 = input("Insera um valor com casas decimais:")
entrada1 = float(valor1.replace(",", "."))
valor2 = input("Insera outro valor com casas decimais:")
entrada2 = float(valor2.replace(",", "."))
divisao = entrada1 / entrada2
divisaoFormatada = "{:.2f}".format(divisao)
print(divisaoFormatada)