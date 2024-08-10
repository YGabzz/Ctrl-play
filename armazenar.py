def carregar_biblioteca(nome_arquivo):
    biblioteca = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, genero, plataforma = linha.split(";")
                biblioteca.append({"nome": nome, "genero": genero, "plataforma": plataforma})
    except FileNotFoundError:
        pass
    return biblioteca

def salvar_biblioteca(nome_arquivo, biblioteca):
    with open(nome_arquivo, 'w') as arquivo:
        for jogo in biblioteca:
            arquivo.write(f"{jogo['nome']}; {jogo['genero']}; {jogo['plataforma']}\n")
    print(f"biblioteca salva no arquivo '{nome_arquivo}'")

