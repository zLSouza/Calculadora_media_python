#=======================================================

#Atividade - 04/08/2026 Professor Guilherme

#VOCÊ FOI CONTRATADO PARA FAZER O SISTEMA DE UMA ESCOLA

#O PROGRAMA DEVE TER:

#    SOLICITAÇÃO DE NOME
#    SOLICITAÇÃO DE NOTA 1
#    SOLICITAÇÃO DE NOTA 2
#    CALCULA A MÉDIA
#    INFORMAR A SITUAÇÃO DO ALUNO
#        MAIOR QUE 7 = APROVADO
#        ENTRE 5 e 6,9 = RECUPERAÇÃO
#        MENOR 5 = REPROVADO
#    PERGUNTAR SE QUER FAZER UM NOVO CADASTRO
#    O PROGRAMA SÓ PARA QUANDO USUÁRIO RESPONDER "N"

#=======================================================

def menu_aluno():
    print("===============================================" , "\n")
    print("Bem-vindo ao sistema de notas escolar!" , "\n")
    print("===============================================")
    print("Informe o nome do aluno(a)")
    nome_aluno = str(input(": "))

    print("Informe a primeira nota do aluno(a)")
    nota01 = float(input(": "))
    print("Informe a segunda nota do aluno(a)")
    nota02 = float(input(": "))

    print("Confirme as notas:" , "\n")
    print(nota01 , " | " , nota02 , "\n")
    print("1 - Tudo certo!")
    print("2 - Preciso fazer algumas mudanças..." , "\n")
    escolha = int(input(": "))

    match escolha:
        case 1:
            menu_media(nome_aluno , nota01 , nota02)
        case 2:
            print("Retornando para o menu anterior")
            menu_aluno()

    return nome_aluno , nota01 , nota02


def menu_media(nome_aluno , nota01 , nota02):
    media = 7
    media_do_aluno = (nota01 + nota02) /2

    if media_do_aluno > media:
        print("O Aluno(a)" , nome_aluno , "Foi aprovado com a media de:" , media_do_aluno , "\n")
        print("Deseja calcular a média de outro aluno(a)?")
        print("1 - Sim")
        print("2 - Não")
        escolha = int(input(": "))

        match escolha:
            case 1:
                print("Retornando para o menu do Aluno(a)")
                menu_aluno()
            case 2:
                print("Obrigado por usar o sistema!")

    else:
        print("O Aluno(a)" , nome_aluno , "Foi reprovado com a media de:" , media_do_aluno , "\n")
        print("Deseja calcular a média de outro aluno(a)?")
        print("1 - Sim")
        print("2 - Não")
        escolha = int(input(": "))

        match escolha:
            case 1:
                print("Retornando para o menu do Aluno(a)")
                menu_aluno()
            case 2:
                print("Obrigado por usar o sistema!")

menu_aluno()