def calcValorFinal():  
    # Loop geral do sistema
    while True:  
        valorInicial = float(input("Digite o valor inicial da compra: R$ "))  

        # Loop para garantir a entrada válida do segundo valor  
        while True:  
            segundoValorEntrada = input("Digite o valor para desconto ou juros (informe '0' para não calcular , ou 'd' para desconto, 'j' para juros): ")  
            if segundoValorEntrada.strip() == "":  
                print("O segundo valor é obrigatório. Por favor, digite um valor válido.")  
            elif segundoValorEntrada.lower() in ['d', 'j']: 
                break  
            else:  
                try:  
                    segundoValor = float(segundoValorEntrada)  
                    break  
                except ValueError:  
                    print("Entrada inválida. Por favor, digite um número ou 'd'/'j'.")  

        # Inicia checagem para calculo do desconto
        if segundoValorEntrada.lower() == 'd':  
            tipoDesconto = input("Você deseja aplicar um desconto em percentual ou valor monetário? (digite 'p' para percentual ou 'v' para valor monetário): ").strip().lower()  
            if tipoDesconto == 'p':  
                percentualDesconto  = float(input("Digite o percentual de desconto: "))  
                desconto            = (percentualDesconto / 100) * valorInicial  
                valorFinal          = valorInicial - desconto  

                print(f"\n--- Desconto Aplicado ---")  
                print(f"Valor do desconto: R$ {desconto:.2f}")  
                print(f"Percentual de desconto: {percentualDesconto:.2f}%")  
                print(f"Valor final com desconto: R$ {valorFinal:.2f}")  

            elif tipoDesconto == 'v':  
                desconto            = float(input("Digite o valor do desconto: R$ "))  
                percentualDesconto  = (desconto / valorInicial) * 100  # Cálculo do percentual  
                valorFinal          = valorInicial - desconto  

                print(f"\n--- Desconto Aplicado ---")  
                print(f"Valor do desconto: R$ {desconto:.2f}")  
                print(f"Percentual de desconto: {percentualDesconto:.2f}%")  
                print(f"Valor final com desconto: R$ {valorFinal:.2f}")  

            else:  
                print("Opção de desconto inválida. Nenhum desconto aplicado.")  

        # Inicia checagem para calculo do juros
        elif segundoValorEntrada.lower() == 'j':  
            tipoJuros = input("Você deseja aplicar juros em percentual ou valor monetário? (digite 'p' para percentual ou 'v' para valor monetário): ").strip().lower()  
            if tipoJuros == 'p':  
                percentualJuros = float(input("Digite o percentual de juros: "))  
                juros           = (percentualJuros / 100) * valorInicial  
                valorFinal      = valorInicial + juros  

                print(f"\n--- Juros Aplicados ---")  
                print(f"Valor dos juros: R$ {juros:.2f}")  
                print(f"Percentual de juros: {percentualJuros:.2f}%")  
                print(f"Valor final com juros: R$ {valorFinal:.2f}")  

            elif tipoJuros == 'v':  
                juros           = float(input("Digite o valor dos juros: R$ "))  
                percentualJuros = (juros / valorInicial) * 100    
                valorFinal      = valorInicial + juros  

                print(f"\n--- Juros Aplicados ---")  
                print(f"Valor dos juros: R$ {juros:.2f}")  
                print(f"Percentual de juros: {percentualJuros:.2f}%")  
                print(f"Valor final com juros: R$ {valorFinal:.2f}")  

            else:  
                print("Opção de juros inválida. Nenhum juros aplicado.")  

        # Checagem do valor final e inicial, se forem iguais informa que não foi aplicado juros ou desconto
        else:  
            valorFinal = valorInicial  
            print("\n--- Nenhum Desconto ou Juros Aplicados ---")  
            print(f"Valor final: R$ {valorFinal:.2f}")  

        # Perguntar se deseja realizar outra operação  
        novaOperacao = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()  
        if novaOperacao != 's':  
            print("Encerrando o programa.")  
            break  

calcValorFinal()
#teste
