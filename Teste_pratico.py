from bs4 import BeautifulSoup
codigo = '''
<html>
    <head>
      <title>Teste prático</title>
    </head>
    <body>
      <h1>Olá</h1>
      <p>Teste 1</p>
      <p>Teste 2</p>
      <p>Teste 3</p>
    </body>
</html>
'''
contador_de_tags = {}

def contar_tags(codigo):
    soup = BeautifulSoup(codigo, 'html.parser')
    tags = soup.find_all()
    
    for tag in tags:
        nome_tag = tag.name
        contador_de_tags[nome_tag] = contador_de_tags.get(nome_tag, 0) + 1

contar_tags(codigo)

if len(contador_de_tags) > 0:
    print("tag / quantidade")
    for nome_tag, i in contador_de_tags.items():
        print(f"{nome_tag} / {i}")
else:
    print("*Não há codigo de HTML")
