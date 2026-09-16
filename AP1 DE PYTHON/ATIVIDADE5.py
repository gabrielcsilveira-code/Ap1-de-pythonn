# Atividade 5: menu com funções de aprovação e classificação de notas

# Função para verificar se o aluno foi aprovado
def verificar_aprovacao():
    print("\n=== VERIFICAR APROVAÇÃO ===")

    # Entrada das três notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Cálculo da média das notas
    media = (nota1 + nota2 + nota3) / 3

    # Verifica a situação do aluno
    if media >= 7:
        print(f"Média: {media:.2f} -> Aluno aprovado!")
    else:
        print(f"Média: {media:.2f} -> Aluno reprovado.")


# Função para classificar a nota em conceito
def classificar_nota():
    print("\n=== CLASSIFICAR NOTA ===")

    # Entrada da nota do aluno
    nota = float(input("Digite a nota: "))

    # Classificação da nota
    if nota >= 9:
        print("Conceito: A")
    elif nota >= 7:
        print("Conceito: B")
    elif nota >= 5:
        print("Conceito: C")
    else:
        print("Conceito: D")


# Função que exibe o menu principal
def escolher_opcao():
    print("\n=== MENU ===")
    print("1 - Verificar aprovação")
    print("2 - Classificar nota")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # Use match-case para controlar o menu
    match opcao:
        case "1":
            verificar_aprovacao()
        case "2":
            classificar_nota()
        case "3":
            print("Saindo do sistema...")
            return False
        case _:
            print("Opção inválida.")

    return True


# Loop principal do programa
while True:
    continuar = escolher_opcao()

    if continuar is False:
        break

    opcao = input("\nDeseja continuar? (s/n): ").lower()

    if opcao == "n":
        print("Programa encerrado.")
        break
