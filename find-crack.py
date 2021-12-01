from googlesearch import search
from time import sleep

print('='*30)
print('FIND CRACK v1.0')#EM ANDAMENTOS PARA RESOLVER O ERRO DE NAO COLOCAR TODOS OS RESULTADOS NO ARQUIVOS DE NOTAS
print('='*30)

def crack():
    find = str(input('Quer achar o crack de qual progama ?\n'))
    quantidade = int(input('Qual a quantidade de buscas ?\n'))

    for c in search('94fbr'+find,stop=quantidade):
        print(c)


    arquivo = open('resultados.txt','a')
    arquivo.write(c+'\n')
    arquivo.close()

crack()

def restart():
    while True:
        quest = int(input('Mais alguma busca ?\n[0] para recomeçar\n[1] para sair e fechar o progama.\n'))
        if quest == 0:
            crack()
        if quest == 1:
            break
restart()

def creditos():
    print('▬' * 16)
    print('▐                         ▐')
    print('▐      Desenvolvido by:   ▐')
    print('▐      Marcus Torres      ▐')
    print('▐      @marcustorre5      ▐')
    print('▐                         ▐')
    print('▬' * 16)

    sleep(3)

creditos()