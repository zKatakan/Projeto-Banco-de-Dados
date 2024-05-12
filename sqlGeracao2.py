from faker import Faker
import random
## FUTURO: 
## - 
faker = Faker("pt_BR") ##nomes brasileiros
## aluno_id possui 8 digitos 
## prof_id possui 7 digitos
## curso_id possui 6 digitos
## tcc_id possui 5 digitos
## dept_id possui 4 digitos
## disc_id possui 3 digitos

def montarID (qtIds,qtDigitos): ##monta IDs aleatorios
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

def criarnome (): ##cria nomes unicos

    novonome = ""
    novo1onome = faker.unique.first_name()
    novo2onome = faker.unique.last_name()
    novonome += novo1onome
    novonome += " "
    novonome += novo2onome
    
    return novonome


anoinicio = 2015 ##ano minimo para historico
anofinal = 2024 ##ano maximo para historico



qtalunos = 10 ## qtde de alunos 
aluno_id = montarID(qtalunos,8) ##ids dos alunos


curso_nomes = ["Ciência da Computação","Engenharia Civil","Administração",] ##adicionar na mao 
## vv Relação entre cursos e disc
curso_disc = {"Ciência da Computação":["Cálculo","Engenharia de Software"],"Engenharia Civil":["Cálculo","Materia Engen."],"Administração":["Cálculo","Materia Admin."]} ##quais cursos tem quais disciplinas (adicionar na mão)

qtcurso = len(curso_nomes) ##qt de cursos
curso_id = montarID(qtcurso,6)## ids dos cursos

qtprof = 5 ## qtde de prof (TEM QUE SER MAIOR OU IGUAL A QTDE DE DISC!!!) 
prof_id = montarID(qtprof,7) ##ids dos profs

tcc_nomes = ["Super Leonardo Bros.","Engenhocas Dos Cidadões","Reino-ministração","DS de Pulso"] ##adicionar na mao 
qttcc = len(tcc_nomes) ##qt de tccs
tcc_id = montarID(qttcc,5) ##ids dos tccs
integrantestcc = 2 ##qt de integrantes por tcc

dept_nomes = ["Exatas","Ciências","Humanas"] ##adicionar na mao (ter certeza que ha mais nomes que qt!) 
dept_cursos = {"Exatas":["Engenharia Civil"],"Ciências":["Ciência da Computação"],"Humanas":["Administração"]} 

qtdept = len(dept_cursos) ##qt de dept, tem que ser igual ou menor que quantidade de prof
dept_id = montarID(qtdept,4) ##ids dos dept   

disc_nomes = ["Cálculo","Engenharia de Software","Materia Engen.","Materia Admin.","Materia Mat."] ##para referencia!
qtdisc = len(disc_nomes) ##qt de disc
disc_id = montarID(qtdisc,3) ##ids das disc




class aula:## para montar historico (mesma qtde que profs)
    def __init__(self,disc_id,semestre,ano):
        self.disc_id = disc_id
        self.semestre = semestre
        self.ano = ano
    def __str__(self):
        return f"{self.disc_id}\n{self.semestre}\n{self.ano}\n"
        

class aluno: ##Refazer com ideias futuras
    def __init__(self,aluno_id,curso_id,aula=0):
        self.aluno_id = aluno_id ##id do aluno
        self.nome = criarnome() ##nome do aluno

        self.curso_id = curso_id

        self.aula = aula
        self.semestre = self.aula.semestre
        self.ano = self.aula.ano
        self.disc_id = self.aula.disc_id
        self.nota = random.randint(0,10) ##nota aleatoria
        
        
        


    def __str__(self): ##print basico
        return f"ID: {self.aluno_id}\nNome: {self.nome}\nCurso: {self.curso_id}\n"
    def insertDados(self): ##insert dos dados
        return f"insert into aluno({self.aluno_id},{self.nome},{self.curso_id});\n"
    def historico(self): ##print do historico
        return f"Disc: {self.disc_id}\nNota: {self.nota}\nAno: {self.ano}\nSemestre: {self.semestre}\n"
    def insertHistorico(self): ##insert do historico
        return f"insert into historico_aluno({self.aluno_id},{self.disc_id},{self.nota},{self.semestre},{self.ano});\n"

class professor: ##Refazer com ideias futuras
    def __init__(self,prof_id,dept_id,aula): ##aula sendo um objeto
        self.prof_id = prof_id ##id do prof
        self.nome = criarnome() ##nome do prof
        self.dept_id = dept_id ##nome do dept
        self.aula = aula
        self.disc_id = self.aula.disc_id
        self.semestre = self.aula.semestre
        self.ano = self.aula.ano

        '''
        todoscursos = dept_cursos[self.dept_nome] ##todos os cursos do dept
        cursoespecifio = todoscursos[random.randint(0,len(todoscursos)-1)] ##um dos cursos do dept
        todasasdisc = curso_disc[cursoespecifio] ##todas as disc do curso
        disc = todasasdisc[random.randint(0,len(todasasdisc)-1)] ##disc aleatoria das disponíveis


        pos = 0
        for x in disc_nomes:
            if disc == x:
                break
            pos +=1
        self.disc_id = disc_id[pos] ##id da disc
        self.semestre = random.randint(1,2) ##semestre aleatorio
        self.ano = random.randint(anoinicio,anofinal) ##ano aleatorio
        '''



    def __str__(self):
        return f"ID: {self.prof_id}\nNome: {self.nome}\n"
    def insertDados(self):
        return f"insert into professor({self.prof_id},{self.nome});\n"
    def insertHistorico(self):
        return f"insert into historico_professor({self.prof_id},{self.disc_id},{self.semestre},{self.ano});\n"
        
        
    
    
    
class tcc: ##por fazer
    def __init__(self,tcc_id,tcc_nome,prof_id,integrantes_id,curso_id,semestre,ano):
        self.tcc_id = tcc_id ##id do tcc
        self.tcc_nome = tcc_nome ##nome do tcc
        self.prof_id = prof_id ##nome do prof responsavel
        self.integrantes_id = integrantes_id ##id dos integrantes (array)
        self.curso_id = curso_id ##id do curso
        self.semestre = semestre ##semestre
        self.ano = ano ##ano
    def __str__ (self):
        return
    
class curso: ##possui curso_id,curso_nome e dept_id
    def __init__(self,curso_id,curso_nome):
        self.curso_id = curso_id ##id do curso
        self.curso_nome = curso_nome ##nome do curso
        
        pos = 0
        for x in dept_cursos: ##procura curso dentro de dept
            tododept = dept_cursos[x]
            if self.curso_nome in tododept:
                break
            pos +=1

        self.dept_id = dept_id[pos] ##id do dept

    def __str__ (self):
        return f"Dept_ID: {self.dept_id}\nCurso_ID: {self.curso_id}\nNome: {self.curso_nome}\n"
    def insertDados(self):
        return f"insert into curso({self.curso_id},{self.curso_nome},{self.dept_id});\n"

class departamento: ##possui dept_id, dept_nome,chefe_id,cursos do dept,discs do dept
    def __init__(self,dept_id,dept_nome,chefe_id):
        self.dept_id = dept_id
        self.dept_nome = dept_nome
        self.chefe_id = chefe_id
        self.cursos = dept_cursos[dept_nome] ##todos os cursos no dept
        self.discs = [] ##todas as disc no dept
        for x in self.cursos: ##percorre para adicionar as disc
            self.discs.append(x)
    def insertDados(self):
        return f"insert into departamento({self.dept_id},{self.dept_nome},{self.chefe_id});\n"

depts = []
for x in range(qtdept):
    depts.append(departamento(dept_id[x],dept_nomes[x],prof_id[x]))

aulas = []
for x in range(qtprof):
    if x < len(disc_id): ##criar historicos ate ter 1 para cada disc
        aulas.append(aula(disc_id[x],random.randint(1,2),random.randint(anoinicio,anofinal)))
    
    




alunos = [] ##todos os alunos
for x in range(qtalunos):
    alunos.append(aluno(aluno_id[x],curso_id[x%qtcurso],aulas[x%len(aulas)]))
    print(alunos[x]) 
    print(alunos[x].historico()) 

profs = [] ##todos os prof
for x in range(qtprof):
    if x < qtcurso:
        profs.append(professor(prof_id[x],dept_nomes[x],aulas[x])) ##forca os primeiros a obrigatoriamente serem parte do dept que sao chefes
    else:
        profs.append(professor(prof_id[x],dept_nomes[random.randint(0,qtdept-1)],aulas[x])) ##adiciona objetos professor
    print(profs[x])
    print(profs[x].insertHistorico())


cursos = [] ##todos os cursos
for x in range(qtcurso):
    cursos.append(curso(curso_id[x],curso_nomes[x]))
    print(cursos[x])



arquivo = open("dadosInsert.txt","w",encoding="utf-8") ##arquivo para depois usar no sql

for x in range(qtalunos): ##insere dados dos alunos e seus historicos
    arquivo.write(alunos[x].insertDados())
    arquivo.write(alunos[x].insertHistorico())
 
for x in range(qtcurso): ##insere dados dos cursos
    arquivo.write(cursos[x].insertDados())

for x in range(qtdept): ##insere dados dos dept
    arquivo.write(depts[x].insertDados())

for x in range(qtprof): ##insere dados dos profs
    arquivo.write(profs[x].insertDados())
    arquivo.write(profs[x].insertHistorico())

for x in curso_disc: ##insere dados do matriz_curricular (nao sei oq eh :/)
    for y in x:
        arquivo.write("insert into matriz_curricular(disc_id,curso_id,semestre)\n")

for x in range(qttcc): ##insere dados do tcc
    arquivo.write("insert into tcc(nome,tcc_id,curso_id,prof_id,ano,semestre)\n")
    break
    
        




arquivo.close()






##Comecar os inserts (colocar coisas no arquivo)






'''

for x in range(qtalunos): ##inserir dados aluno
    indice = random.randint(0,qtcurso-1)
    disc_hist = curso_disc[curso_nomes[indice]][random.randint(0,len(curso_disc[curso_nomes[indice]])-1)] ##disc aleatoria dentro do curso selecionado
    arquivo.write("insert into aluno (%s,%s,%s);\n" %(aluno_id[x],nomes[x],curso_id[indice])) 
    arquivo.write("insert into historico_aluno (%s,%s,%s,%s,%s);\n" %(aluno_id[x], disc_hist ,random.randint(0,10),random.randint(1,2),random.randint(anoinicio,anofinal)))
    

for x in range(qtcurso): ##inserir dados curso
    arquivo.write("insert into curso (%s,%s,dept_id);\n" %(curso_id[x],curso_nomes[x])) ##falta atrelar curso a dept

for x in range(qtdept): ##inserir dados dept
    arquivo.write("insert into departamento (%s,%s,%s);\n" %(dept_id[x],dept_nomes[x],prof_id[x])) 
    
for x in range(qtdisc): ##inserir dados disc
    arquivo.write("insert into disciplina (%s,%s,dept_id);\n" %(disc_id[x],disc_nomes[x])) ##falta atrelar dept a disc
    

for x in range(qttcc): ##inserir dados tcc
    arquivo.write("insert into tcc(%s,%s,%s,curso_id,ano,semestre);\n" %(tcc_id[x],tcc_nomes[x], prof_id[random.randint(0,len(prof_id)-1)], )) ##falta atrelar id prof com curso
    for y in range(integrantestcc):
        arquivo.write("insert into part_tcc(%s,aluno_id);\n"%(tcc_id[x])) ##falta terminar logica

for x in range(qtprof): ##inserir dados prof
    arquivo.write("insert into professor (%s,%s);\n" % (prof_id[x],nomes[qtalunos+x])) 
    arquivo.write("insert into historico_professor(%s,disc_id,semestre,ano);\n" %(prof_id[x])) ##falta terminar logica

arquivo.close()
'''






