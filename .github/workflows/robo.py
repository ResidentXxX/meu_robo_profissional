import datetime
import pandas as pd

#Simulação de coleta de dados
def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "OK"},
    ]

#salvar em um csv
def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print("Relatorio salvo com sucesso!")

#Execução principal
if __name__ == "__main__":
    print("Iniciando Robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)