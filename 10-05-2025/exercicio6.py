lista = ["relatorio.docx", "atendimento.pdf", "planilha.xlsx", "resumo.txt","relatorio2.docx","relatorio3.docx"]

for arquivo in lista:
    if arquivo.endswith(".docx"):
        print(f"Arquivo {arquivo} é um documento do Word")

    elif arquivo.endswith(".pdf"):
        print(f"Arquivo {arquivo} é um documento do PDF")

    elif arquivo.endswith(".xlsx"):
        print(f"Arquivo {arquivo} é um documento do Excel")

    else:
        print(f"Arquivo {arquivo} é um arquivo de texto")
