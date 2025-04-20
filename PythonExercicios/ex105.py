'''Minha Resolução: '''
# def notas(*n, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param n: uma ou mais notas dos alunos (aceita várias)
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação
#     :return: dicionário com várias informações sobre a situação da turma
#     """
#     n = list(n)
#     situação = ''
#     dicionario = {
#     'total': len(n),
#     'maior': max(n),
#     'menor': min(n),
#     'média': sum(n)/len(n)
#     }
#     if sit:
#         media = sum(n) / len(n)
#         if media <= 3.5:
#             situação = 'MUITO RUIM'
#         elif 3.5 <= media <= 6.0:
#             situação = 'RUIM'
#         elif 6.0 <= media <= 8.5:
#             situação = 'BOA'
#         elif 8.5 <= media <= 10.0:
#             situação = 'MUITO BOA'
#         dicionario.update({'situação': situação})
#     print(dicionario)
#
#
#
# #Programa Principal
# resp = notas(1.5, 1.0, 1, 2.5, 8.5, 4.5, 1, 0.5, sit=True)
# help(notas)
'''Resolução do vídeo:'''
#Programa Principal
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas( 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)