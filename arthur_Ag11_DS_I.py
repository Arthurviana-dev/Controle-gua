from colorama import Fore, Style, init
init(autoreset=True)

# Lista com os níveis e suas respectivas mensagens e cores
niveis = [
    ("Nível 1 - Muito baixo (crítico)", Fore.RED),
    ("Nível 2 - Baixo", Fore.YELLOW),
    ("Nível 3 - Médio", Fore.GREEN),
    ("Nível 4 - Alto", Fore.CYAN),
    ("Nível 5 - Muito alto (alerta)", Fore.BLUE),
]


def exibir_alerta(mensagem, cor):
  print(cor + mensagem)


# Simulação do monitoramento exibindo todos os níveis
print("--- Monitoramento do Reservatório de Água ---")
for mensagem, cor in niveis:
  exibir_alerta(mensagem, cor)