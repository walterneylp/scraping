import requests
from bs4 import BeautifulSoup

url = 'https://placaipva.com.br/placa/PYB7C19'
response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")

#veiculo = html.find_all('div', attrs = {'class': 'fipeTablePriceDetail'})
veiculo = html.find_all(attrs={'class': 'fipeTablePriceDetail'})

tabela = []
for box in veiculo:
  dic = {}
  dic['Marca'] = box.findAll('td')[1].get_text()
  dic['Modelo'] = box.find_all('td')[3].get_text()
  dic['Importado'] = box.find_all('td')[5].get_text()
  dic['Ano'] = box.find_all('td')[7].get_text()
  dic['Ano Modelo'] = box.find_all('td')[9].get_text()
  dic['Cor'] = box.findAll('td')[11].get_text()
  dic['Cilindrada'] = box.find_all('td')[13].get_text()
  dic['Potencia'] = box.find_all('td')[15].get_text()
  dic['Combustível'] = box.find_all('td')[17].get_text()
  dic['Chassi'] = box.find_all('td')[19].get_text()
  dic['Motor'] = box.find_all('td')[21].get_text()
  dic['Passageiros'] = box.find_all('td')[23].get_text()
  dic['UF'] = box.find_all('td')[25].get_text()
  dic['Município'] = box.find_all('td')[27].get_text()
  dic['Tipo Veículo'] = box.find_all('td')[29].get_text()
  dic['Especie Veículo'] = box.find_all('td')[31].get_text()
  dic['Segmento'] = box.find_all('td')[33].get_text()
  dic['Carroceria'] = box.find_all('td')[35].get_text()
  tabela.append(dic)

print(tabela)
print(tabela[0]['Marca'])
print(tabela[0]['Modelo'])
print(tabela[0]['Ano'])
print(tabela[0]['Ano Modelo'])
print(tabela[0]['Cor'])
print(tabela[0]['Município'])
print(tabela[0]['UF'])

arquivo = open("veiculos.txt", "a")
linhas = list()
linhas.append(tabela[0]['Marca'])
linhas.append("; ")
linhas.append(tabela[0]['Modelo'])
linhas.append("; ")
linhas.append(tabela[0]['Ano'])
linhas.append("; ")
linhas.append(tabela[0]['Ano Modelo'])
linhas.append("; ")
linhas.append(tabela[0]['Cor'])
linhas.append("; ")
linhas.append(tabela[0]['Município'])
linhas.append("; ")
linhas.append(tabela[0]['UF'])
linhas.append("\r\n")
arquivo.writelines(linhas)
arquivo.close()
