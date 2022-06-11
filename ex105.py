def notas(*n, sit=False):
    """
    ->    -> Função para analizalizar notas e situações de vários alunos.
    :param n: Recebe uma valor indefinido de notas para serem analizadas.
    :param sit: Parametro opcional se ocorre ou não tal situação.
    :return: Dicionário com as informções sobre a situação das notas.
    """
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n) / len(n)
    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['média'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


resp = notas(5.5, 8.5, 9, 2, sit=True)
print(resp)
