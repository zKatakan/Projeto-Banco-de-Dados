from faker import Faker
import random
## aluno_id possui 8 digitos 
## prof_id possui 7 digitos
## curso_id possui 6 digitos
## tcc_id possui 5 digitos
## dept_id possui 4 digitos
## disc_id possui 3 digitos

# arquivo = open("dadosSQL","w") ##arquivo para depois usar no sql

faker = Faker("pt_BR") ##nomes brasileiros
qtnomes = 30 ## 30 nomes

nomes = [] ##nomes de alunos e profs
for x in range(qtnomes):
    novonome = ""
    novo1onome = faker.unique.first_name()
    novo2onome = faker.unique.last_name()
    novonome += novo1onome
    novonome += " "
    novonome += novo2onome
    nomes.append(novonome)

print(nomes)
qtalunos = 20 ## qtde de alunos 
qtprof = qtnomes-qtalunos ## qtde de prof
aluno_id = [] ##ids dos alunos

for x in range(qtalunos): ##criando id dos alunos (8 digitos)
    novoid = random.randint(10000000,99999999) ##atualmente eh completamente aleatorio

    if novoid in aluno_id: ##para nao ter id igual
        novoid = random.randint(10000000,99999999)

    aluno_id.append(novoid)

print(aluno_id)








