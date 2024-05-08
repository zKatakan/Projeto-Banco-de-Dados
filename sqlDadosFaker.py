from faker import Faker
import random
## aluno_id possui 8 digitos 
## prof_id possui 7 digitos
## curso_id possui 6 digitos
## tcc_id possui 5 digitos
## dept_id possui 4 digitos
## disc_id possui 3 digitos



faker = Faker("pt_BR") ##nomes brasileiros

qtnomes = 60 ## 30 nomes
qtalunos = 50 ## qtde de alunos 
qtprof = qtnomes-qtalunos ## qtde de prof
curso_nomes = ["Ciência da Computação","Engenharia Civil","Administração","Engenharia de Materiais"] ##adicionar na mao (ter certeza que ha mais nomes que qt!)
qtcurso = 4 ##qt de cursos
tcc_nomes = ["Super Leonardo Bros.","Engenhocas Dos Cidadões","Reino-ministração","DS de Pulso"] ##adicionar na mao (ter certeza que ha mais nomes que qt!)
qttcc = 4 ##qt de tccs
dept_nomes = ["Exatas","Ciências","Humanas"] ##adicionar na mao (ter certeza que ha mais nomes que qt!)
qtdept = 3 ##qt de dept
disc_nomes = ["Cálculo","Cálculo 2","Filosofia","Física","Física 2","Engenharia de Software"] ##adicionar na mao (ter certeza que ha mais nomes que qt!)
qtdisc = 3 ##qt de disc

def montarID (qtIds,qtDigitos):
    Array = []
    digitomax = ""
    for x in range(qtDigitos):
        digitomax +="9"
    for x in range(qtIds):
        novoid = random.randint((10**(qtDigitos-1)),int(digitomax))
        while novoid in Array:
            novoid = random.randint((10**(qtDigitos-1)),int(digitomax))
        Array.append(novoid)
    return Array

nomes = [] ##nomes de alunos e profs
for x in range(qtnomes):
    novonome = ""
    novo1onome = faker.unique.first_name()
    novo2onome = faker.unique.last_name()
    novonome += novo1onome
    novonome += " "
    novonome += novo2onome
    nomes.append(novonome)
    
print("Nomes:")
print(nomes)




aluno_id = montarID(qtalunos,8)
print("ID Alunos: ")
print(aluno_id)





prof_id = montarID(qtprof,7)
print("ID prof: ")
print(prof_id)


curso_id = montarID(qtcurso,6)   

print("ID curso: ")
print(curso_id)




tcc_id = montarID(qttcc,5)
print("ID tcc: ")
print(tcc_id)



dept_id = montarID(qtdept,4)   
print("ID dept: ")
print(dept_id)



disc_id = montarID(qtdisc,3)
print("ID Disc: ")
print(disc_id)


##Comecar os inserts (colocar coisas no arquivo)

arquivo = open("dadosSQL.txt","w",encoding="utf-8") ##arquivo para depois usar no sql
copiacurso_id = curso_id
for x in range(qtalunos): ##inserir dados aluno
    indice = random.randint(0,len(copiacurso_id)-1) ##indice aleatorio
    curso = copiacurso_id[indice] ##curso aleatorio
    arquivo.write("insert into aluno (%s,%s,%s);\n" %(aluno_id[x],nomes[x],curso)) 
    arquivo.write("insert into historico_aluno (%s,disc_id,nota,semestre,ano);\n" %(aluno_id[x])) ##falta terminar logica
    copiacurso_id.pop(indice)

for x in range(qtcurso): ##inserir dados curso
    arquivo.write("insert into curso (%s,%s,dept_id);\n" %(curso_id[x],curso_nomes[x])) ##falta terminar logica

for x in range(qtdept): ##inserir dados dept
    arquivo.write("insert into departamento (%s,nome,chefe_id);\n" %(dept_id[x])) ##falta terminar logica
    
for x in range(qtdisc): ##inserir dados disc
    arquivo.write("insert into disciplina (%s,nome,dept_id);\n" %(disc_id[x])) ##falta terminar logica
    
integrantestcc = 2 ##qt de integrantes por tcc
for x in range(qttcc): ##inserir dados tcc
    arquivo.write("insert into tcc(%s,nome,prof_id,curso_id,ano,semestre);\n" %(tcc_id[x])) ##falta terminar logica
    for y in range(integrantestcc):
        arquivo.write("insert into part_tcc(%s,aluno_id);\n"%(tcc_id[x])) ##falta terminar logica

for x in range(qtprof): ##inserir dados prof
    arquivo.write("insert into professor (%s,%s);\n" % (prof_id[x],nomes[qtalunos+x])) ##falta terminar logica
    arquivo.write("insert into historico_professor(%s,disc_id,semestre,ano);\n" %(prof_id[x])) ##falta terminar logica

arquivo.close()







