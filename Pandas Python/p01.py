# P01: Hello Series!
import pandas as pd

# cria a Series notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# cria a Series alunos
lst_matriculas = ['M02', 'M05', 'M13', 'M14', 'M19']
lst_nomes = ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

# cria a Serie alunos a partir de um dicionário
dic_alunos = {
    'M02': 'Bob', 'M05': 'Dayse', 'M13': 'Bill',
    'M14': 'Cris', 'M19': 'Jimi'
}
alunos2 = pd.Series(dic_alunos)

# imprime as duas Series
print(notas)
print("---------------")
print(alunos)
print("---------------")
print(alunos2)
