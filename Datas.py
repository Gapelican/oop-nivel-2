
""""from datetime import date

data_atual = date.today()

data_em_texto = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'

print(data_em_texto)

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)"""

from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

print(data_e_hora_em_texto)