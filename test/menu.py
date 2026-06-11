from datetime import date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Professor import Professor
from models.Responsavel import Responsavel
from models.Aluno import Aluno
from models.Avaliacao import Avaliacao
from models.Prova import Prova
from models.Disciplina import Disciplina
from models.Grade import Grade
from models.Turma import Turma
from models.Calculos import MediaPonderada, Somatorio

professores = []
responsaveis = []
alunos = []
avaliacoes = []
disciplinas = []
grades = []
turmas = []
matriculas = []
provas = []

opcao = ""
while opcao != "0":
    print("\n=============================")
    print("  SISTEMA DE GESTAO ESCOLAR")
    print("=============================")
    print("1 - Professores")
    print("2 - Responsaveis")
    print("3 - Alunos")
    print("4 - Disciplinas e Avaliacoes")
    print("5 - Grades e Turmas")
    print("6 - Matriculas")
    print("7 - Notas")
    print("0 - Sair")
    print("=============================")
    opcao = input("Opcao: ").strip()

    if opcao == "1":
        op = ""
        while op != "0":
            print("\n=== PROFESSORES ===")
            print("1 - Cadastrar professor")
            print("2 - Listar professores")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                while True:
                    try:
                        texto = input("Data de nascimento (dd/mm/aaaa): ")
                        dia, mes, ano = texto.strip().split("/")
                        nascimento = date(int(ano), int(mes), int(dia))
                        break
                    except:
                        print("Data invalida, tente novamente.")
                formacao = input("Formacao: ")
                prof = Professor(nome, cpf, nascimento, formacao)
                professores.append(prof)
                print("Professor cadastrado!")
                print(prof)

            elif op == "2":
                print("\n--- Professores ---")
                if len(professores) == 0:
                    print("Nenhum cadastrado.")
                else:
                    i = 0
                    while i < len(professores):
                        print(str(i + 1) + ". " + str(professores[i]))
                        i += 1

    elif opcao == "2":
        op = ""
        while op != "0":
            print("\n=== RESPONSAVEIS ===")
            print("1 - Cadastrar responsavel")
            print("2 - Listar responsaveis")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                while True:
                    try:
                        texto = input("Data de nascimento (dd/mm/aaaa): ")
                        dia, mes, ano = texto.strip().split("/")
                        nascimento = date(int(ano), int(mes), int(dia))
                        break
                    except:
                        print("Data invalida, tente novamente.")
                r = Responsavel(nome, cpf, nascimento)
                responsaveis.append(r)
                print("Responsavel cadastrado!")
                print(r)

            elif op == "2":
                print("\n--- Responsaveis ---")
                if len(responsaveis) == 0:
                    print("Nenhum cadastrado.")
                else:
                    i = 0
                    while i < len(responsaveis):
                        print(str(i + 1) + ". " + str(responsaveis[i]))
                        i += 1

    elif opcao == "3":
        op = ""
        while op != "0":
            print("\n=== ALUNOS ===")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                while True:
                    try:
                        texto = input("Data de nascimento (dd/mm/aaaa): ")
                        dia, mes, ano = texto.strip().split("/")
                        nascimento = date(int(ano), int(mes), int(dia))
                        break
                    except:
                        print("Data invalida, tente novamente.")
                pai = None
                mae = None
                resps = []
                if len(responsaveis) > 0:
                    print("Vincular pai? (s/n)")
                    if input().strip().lower() == "s":
                        i = 0
                        while i < len(responsaveis):
                            print(str(i + 1) + ". " + str(responsaveis[i]))
                            i += 1
                        try:
                            idx = int(input("Numero: ")) - 1
                            if 0 <= idx < len(responsaveis):
                                pai = responsaveis[idx]
                        except:
                            pass
                    print("Vincular mae? (s/n)")
                    if input().strip().lower() == "s":
                        i = 0
                        while i < len(responsaveis):
                            print(str(i + 1) + ". " + str(responsaveis[i]))
                            i += 1
                        try:
                            idx = int(input("Numero: ")) - 1
                            if 0 <= idx < len(responsaveis):
                                mae = responsaveis[idx]
                        except:
                            pass
                    print("Adicionar outros responsaveis? (s/n)")
                    while input().strip().lower() == "s":
                        i = 0
                        while i < len(responsaveis):
                            print(str(i + 1) + ". " + str(responsaveis[i]))
                            i += 1
                        try:
                            idx = int(input("Numero: ")) - 1
                            if 0 <= idx < len(responsaveis):
                                resps.append(responsaveis[idx])
                        except:
                            pass
                        print("Adicionar mais? (s/n)")
                aluno = Aluno(nome, cpf, nascimento, pai, mae, resps)
                alunos.append(aluno)
                print("Aluno cadastrado!")
                print(aluno)

            elif op == "2":
                print("\n--- Alunos ---")
                if len(alunos) == 0:
                    print("Nenhum cadastrado.")
                else:
                    i = 0
                    while i < len(alunos):
                        print(str(i + 1) + ". " + str(alunos[i]))
                        i += 1

    elif opcao == "4":
        op = ""
        while op != "0":
            print("\n=== DISCIPLINAS E AVALIACOES ===")
            print("1 - Cadastrar avaliacao")
            print("2 - Cadastrar disciplina")
            print("3 - Listar avaliacoes")
            print("4 - Listar disciplinas")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                while True:
                    try:
                        texto = input("Data da avaliacao (dd/mm/aaaa): ")
                        dia, mes, ano = texto.strip().split("/")
                        data_av = date(int(ano), int(mes), int(dia))
                        break
                    except:
                        print("Data invalida, tente novamente.")
              
                    
                peso = int(input("Peso: "))
                      
                    
                       
                av = Avaliacao(data_av, peso, [])
                avaliacoes.append(av)
                print("Avaliacao cadastrada!")
                print(av)

            elif op == "2":
                if len(professores) == 0:
                    print("Cadastre um professor primeiro.")
                else:
                    nome = input("Nome da disciplina: ")
                    i = 0
                    while i < len(professores):
                        print(str(i + 1) + ". " + str(professores[i]))
                        i += 1
                    prof = None
                   
                        
                    idx = int(input("Escolha o professor: ")) - 1
                    if 0 <= idx and idx < len(professores):
                        prof = professores[idx]
                              
                    else:
                        print("Invalido.")
                    print("Calculo: 1 - Media Ponderada  2 - Somatorio")
                    calculo = None
                    if input("Opcao: ").strip() == "2":
                        calculo = Somatorio() 
                    else:
                        calculo = MediaPonderada()
                    disc = Disciplina(nome, prof, [], calculo)
                    if len(avaliacoes) > 0:
                        print("Adicionar avaliacoes? (s/n)")
                        while input().strip().lower() == "s":
                            i = 0
                            while i < len(avaliacoes):
                                print(str(i + 1) + ". " + str(avaliacoes[i]))
                                i += 1
                            try:
                                idx = int(input("Numero: ")) - 1
                                if 0 <= idx < len(avaliacoes):
                                    disc.adicionar_avaliacao(avaliacoes[idx])
                            except:
                                pass
                            print("Adicionar mais? (s/n)")
                    disciplinas.append(disc)
                    print("Disciplina cadastrada!")
                    print(disc)

            elif op == "3":
                print("\n--- Avaliacoes ---")
                if len(avaliacoes) == 0:
                    print("Nenhuma cadastrada.")
                else:
                    i = 0
                    while i < len(avaliacoes):
                        print(str(i + 1) + ". " + str(avaliacoes[i]))
                        i += 1

            elif op == "4":
                print("\n--- Disciplinas ---")
                if len(disciplinas) == 0:
                    print("Nenhuma cadastrada.")
                else:
                    i = 0
                    while i < len(disciplinas):
                        print(str(i + 1) + ". " + str(disciplinas[i]))
                        i += 1

    elif opcao == "5":
        op = ""
        while op != "0":
            print("\n=== GRADES E TURMAS ===")
            print("1 - Cadastrar grade")
            print("2 - Cadastrar turma")
            print("3 - Listar grades")
            print("4 - Listar turmas")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
               
                competencias = int(input("Numero de competencias: "))
                      
                discs = []
                if len(disciplinas) > 0:
                    print("Adicionar disciplinas? (s/n)")
                    while input().strip().lower() == "s":
                        i = 0
                        while i < len(disciplinas):
                            print(str(i + 1) + ". " + str(disciplinas[i]))
                            i += 1
                       
                        idx = int(input("Numero: ")) - 1
                        if 0 <= idx < len(disciplinas):
                            discs.append(disciplinas[idx])
                        
                        print("Adicionar mais? (s/n)")
                grade = Grade(competencias, discs)
                grades.append(grade)
                print("Grade cadastrada!")
                print(grade)

            elif op == "2":
                if len(grades) == 0:
                    print("Cadastre uma grade primeiro.")
                else:
                    sala = input("Identificacao da sala: ")
                    while True:
                        try:
                            quantidade = int(input("Capacidade maxima: "))
                            break
                        except:
                            print("Valor invalido.")
                    i = 0
                    while i < len(grades):
                        print(str(i + 1) + ". " + str(grades[i]))
                        i += 1
                    grade = None
                  
                        
                    while True:
                        idx = int(input("Escolha a grade: ")) - 1
                        if 0 <= idx and idx < len(grades):
                            grade = grades[idx]
                            break
                        else:
                            print("Erro")
                    turma = Turma(sala, quantidade, [], grade)
                    turmas.append(turma)
                    print("Turma cadastrada!")
                    print(turma)

            elif op == "3":
                print("\n--- Grades ---")
                if len(grades) == 0:
                    print("Nenhuma cadastrada.")
                else:
                    i = 0
                    while i < len(grades):
                        print(str(i + 1) + ". " + str(grades[i]))
                        i += 1

            elif op == "4":
                print("\n--- Turmas ---")
                if len(turmas) == 0:
                    print("Nenhuma cadastrada.")
                else:
                    i = 0
                    while i < len(turmas):
                        print(str(i + 1) + ". " + str(turmas[i]))
                        i += 1

    elif opcao == "6":
        op = ""
        while op != "0":
            print("\n=== MATRICULAS ===")
            print("1 - Matricular aluno")
            print("2 - Listar matriculas")
            print("3 - Cancelar matricula")
            print("4 - Concluir matricula")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                if len(alunos) == 0 or len(turmas) == 0:
                    print("Cadastre alunos e turmas primeiro.")
                else:
                    i = 0
                    while i < len(alunos):
                        print(str(i + 1) + ". " + str(alunos[i]))
                        i += 1
                    aluno = None
                    while True:
                        try:
                            idx = int(input("Escolha o aluno: ")) - 1
                            if 0 <= idx < len(alunos):
                                aluno = alunos[idx]
                                break
                        except:
                            pass
                        print("Invalido.")
                    i = 0
                    while i < len(turmas):
                        print(str(i + 1) + ". " + str(turmas[i]))
                        i += 1
                    turma = None
                    while True:
                
                        idx = int(input("Escolha a turma: ")) - 1
                        if 0 <= idx and idx < len(turmas):
                            turma = turmas[idx]
                            break
                        else:
                            print("Invalido.")
                    m = turma.matricular(aluno)
                    if m is not None:
                        matriculas.append(m)
                        print("Matriculado com sucesso!")
                        print(m)
                    else:
                        print("Nao foi possivel matricular, turma cheia.")

            elif op == "2":
                print("\n--- Matriculas ---")
                if len(matriculas) == 0:
                    print("Nenhuma cadastrada.")
                else:
                    i = 0
                    while i < len(matriculas):
                        print(str(i + 1) + ". " + str(matriculas[i]))
                        i += 1

            elif op == "3":
                if len(matriculas) == 0:
                    print("Nenhuma matricula cadastrada.")
                else:
                    i = 0
                    while i < len(matriculas):
                        print(str(i + 1) + ". " + str(matriculas[i]))
                        i += 1
                    while True:
                        idx = int(input("Escolha a matricula: ")) - 1
                        if 0 <= idx and idx < len(matriculas):
                            matriculas[idx].cancelar()
                            break
                        else:
                            print("Invalido.")

            elif op == "4":
                if len(matriculas) == 0:
                    print("Nenhuma matricula cadastrada.")
                else:
                    i = 0
                    while i < len(matriculas):
                        print(str(i + 1) + ". " + str(matriculas[i]))
                        i += 1
                    while True:
                        idx = int(input("Escolha a matricula: ")) - 1
                        if 0 <= idx and idx < len(matriculas):
                            matriculas[idx].concluir()
                        else:
                            print("Invalido.")

    elif opcao == "7":
        op = ""
        while op != "0":
            print("\n=== NOTAS ===")
            print("1 - Lancar nota")
            print("2 - Calcular nota final do aluno")
            print("3 - Calcular media da turma")
            print("0 - Voltar")
            op = input("Opcao: ").strip()

            if op == "1":
                if len(matriculas) == 0 or len(avaliacoes) == 0:
                    print("Cadastre matriculas e avaliacoes primeiro.")
                else:
                    i = 0
                    while i < len(matriculas):
                        print(str(i + 1) + ". " + str(matriculas[i]))
                        i += 1
                    mat = None
                    while True:
                        
                        idx = int(input("Escolha a matricula: ")) - 1
                        if 0 <= idx < len(matriculas):
                            mat = matriculas[idx]
                            break
                    
                        else:
                            print("Invalido.")
                    i = 0
                    while i < len(avaliacoes):
                        print(str(i + 1) + ". " + str(avaliacoes[i]))
                        i += 1
                    av = None
                    while True:
                        
                        idx = int(input("Escolha a avaliacao: ")) - 1
                        if 0 <= idx < len(avaliacoes):
                            av = avaliacoes[idx]
                            break
                        else:
                            print("Invalido.")
                    while True:
                        nota = float(input("Nota (0 a 10): "))
                        if nota<0 or nota > 10 :
                            print("Valor invalido.")
                        else:
                            break
                    p = Prova(mat, av, nota)
                    av.prova.append(p)
                    provas.append(p)
                    print("Nota lancada!")
                    print(p)

            elif op == "2":
                if len(matriculas) == 0 or len(disciplinas) == 0:
                    print("Cadastre matriculas e disciplinas primeiro.")
                else:
                    i = 0
                    while i < len(matriculas):
                        print(str(i + 1) + ". " + str(matriculas[i]))
                        i += 1
                    try:
                        idx = int(input("Escolha a matricula: ")) - 1
                        mat = matriculas[idx]
                        i = 0
                        while i < len(disciplinas):
                            print(str(i + 1) + ". " + str(disciplinas[i]))
                            i += 1
                        idx = int(input("Escolha a disciplina: ")) - 1
                        disc = disciplinas[idx]
                        nota = mat.calcular_nota_final(disc)
                        print("Nota final de " + mat.aluno.nome + " em " + disc.nome + ": " + str(round(nota, 2)))
                    except:
                        print("Invalido.")

            elif op == "3":
                if len(disciplinas) == 0:
                    print("Nenhuma disciplina cadastrada.")
                else:
                    i = 0
                    while i < len(disciplinas):
                        print(str(i + 1) + ". " + str(disciplinas[i]))
                        i += 1
                    try:
                        idx = int(input("Escolha a disciplina: ")) - 1
                        disc = disciplinas[idx]
                        media = disc.get_media_turma()
                        print("Media da turma em " + disc.nome + ": " + str(round(media, 2)))
                    except:
                        print("Invalido.")

    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opcao invalida.")