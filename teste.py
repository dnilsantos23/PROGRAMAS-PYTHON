import os

arquivo = open('teste.txt', 'w', encoding='utf-8')  # Abre o arquivo para escrita (w)
arquivo.write('Teste\n')  # Escreve no arquivo
#arquivo.close() # Fecha o arquivo   
print(os.path.abspath('teste.txt'))  # Mostra o caminho absoluto do arquivo

arquivo.write('Olá mundo!!!\n')  # Tenta escrever no arquivo novamente
arquivo.close()  # Fecha o arquivo novamente
# O arquivo já foi fechado, então não pode mais ser escrito