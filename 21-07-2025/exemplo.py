#Abrindo e/ou criando um arquivo para escrita
arquivo = open('exemplo.txt', 'w', encoding="utf-8")
arquivo.write('Esta é uma nova linha de texto.\n')
arquivo.write('Adicionando outra linha.\n')
arquivo.close()

# Abrindo um arquivo para leitura
arquivo = open("21-07-2025/exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

linhas = ['Esta é uma linha de texto.\n','Esta é outra linha de texto.\n'] 
with open('exemplo.txt', 'a', encoding="utf-8") as arquivo: 
     arquivo.writelines(linhas)
