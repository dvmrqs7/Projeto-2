import random
import datetime

def menu():
    nome_arq = 'logs.txt' 
    while True:
        print('Monitor LogPy')
        print('1 - Gerar log')
        print('2 - Analisar logs')
        print('3 - Gerar e analisar logs')
        print('4 - Sair')
        opcao = input('Digite uma opção: ')
        if opcao == '1':
            try:
                qtd = int(input('Quantos logs deseja gerar? '))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Quantidade incorreta')
        elif opcao == '2':
            analisarLogs(nome_arq)
        elif opcao == '3':
            try:
                qtd = int(input('Quantos logs deseja gerar? '))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq)
            except:
                print('Quantidade incorreta')
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida')

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + '\n')
        print('Logs gerados')

def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIP(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f'{data} - {ip} - {recurso} - {metodo} - {status} - {tempo}ms - 500mb - HTTP/1.1 - {agente}'

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22, 8, 0)
    data = datetime.timedelta(seconds=i*random.randint(5, 20))
    return (base + data).strftime('%d/%m/%Y %H:%M:%S')

def gerarIP(i):
    r = random.randint(1, 6)

    if i >=20 and i <= 30:
        return '200.0.111.345'
    
    if r == 1:
        return '192.168.5.1'
    elif r == 2:
        return '192.168.5.2'
    elif r == 3:
        return '192.168.5.3'
    elif r == 4:
        return '192.168.5.4'
    elif r == 5:
        return '192.168.5.5'
    else:
        return '192.168.5.6'
