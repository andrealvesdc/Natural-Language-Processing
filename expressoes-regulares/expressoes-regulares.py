import re
import requests

#Exemplos de expressões regulares
'''
print(r"oi pessoal\nSegunda linha")

string_de_teste = 'O gato, a gata, os gatinhos, os gatoes'

padrao = re.search(r'gata',string_de_teste)

padrao = re.search(r'gat.',string_de_teste)

padrao = re.search(r'gat\w',string_de_teste)

padrao = re.findall(r'gat\w',string_de_teste) #RAW String

padrao = re.findall(r'gat\w+',string_de_teste)

padrao = re.findall(r'gat\w*',string_de_teste)

padrao = re.findall(r'[gat]',string_de_teste)

padrao = re.findall(r'[gat]+',string_de_teste)

padrao = re.findall(r'[gat]+\w+',string_de_teste)

padrao = re.findall(r'\w{4,6}',string_de_teste)

if padrao:
    #print(padrao.group())
    print(padrao)
else:
    print ("padrão não encontrado")
'''

#expressão para encontrar e-mails
email_de_teste = 'andre.alves@dce.ufb.br masterandre313@gmail.com testes@teste.com asdas@dasdasd.com das22as@da2das.com.br asdas11d-asdads@fisica.usp.br aaa@a.cs não é emailasdasdasdsad s ikhaskijdhsadlskhjdk asdasdasdsad outros textos'

#email_de_teste = re.findall(r'\w+@\w+\.\w+',email_de_teste)

email_de_teste = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',email_de_teste)

if email_de_teste:
    print(email_de_teste)
else:
    print ("padrão não encontrado")


#Capturando e-mail em paginas web  
requisicao = requests.get('https://www.gamegames.com.br/#contato')
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',requisicao.text)

if padrao:
    #print(padrao.group())
    print(padrao)
else:
    print ("padrão não encontrado")
