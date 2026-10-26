import json

# Dicionário com as respostas do Alex
respostas = {
    "saudacao": "Olá! Eu sou um bot.",
    "nome": "Meu nome é Alex.",
    "funcao": "Eu converso com você!",
    "idade": "Eu não tenho idade, sou um bot!",
    "ajuda": "Posso conversar com você e responder algumas perguntas!",
    "despedida": "Até mais!"
}


# Memória padrão
def memoria_padrao():
    return {
        "nome": "Visitante",
        "cor_favorita": "Não informada",
        "jogo_favorito": "Não informado"
    }


# Salvar a memória no arquivo JSON
def salvar_memoria():
    with open("memoria.json", "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, ensure_ascii=False, indent=4)


# Carregar a memória do arquivo JSON
def carregar_memoria():
    try:
        with open("memoria.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            if isinstance(dados, dict):
                memoria_inicial = memoria_padrao()
                memoria_inicial.update(dados)
                return memoria_inicial

            return memoria_padrao()

    except (FileNotFoundError, json.JSONDecodeError):
        return memoria_padrao()


# Responder às mensagens
def responder(mensagem):
    if mensagem in ["oi", "olá", "ola", "eai", "e ai"]:
        return respostas["saudacao"]

    elif "seu nome" in mensagem:
        return respostas["nome"]

    elif "faz" in mensagem or "pode" in mensagem or "função" in mensagem:
        return respostas["funcao"]

    elif "idade" in mensagem:
        return respostas["idade"]

    elif "ajuda" in mensagem:
        return respostas["ajuda"]

    else:
        return "Não entendi. Pode falar de outra maneira?"


# Carregar a memória ao iniciar
memoria = carregar_memoria()


print("🤖 ChatBot Alex")
print("Digite 'tchau' para sair.")

while True:
    mensagem_original = input("\nVocê: ").strip()
    mensagem = mensagem_original.lower()

    # Encerrar o chatbot
    if mensagem in ["tchau", "até mais", "falou"]:
        print("Alex:", respostas["despedida"])
        break

    # Salvar o nome
    elif mensagem.startswith("meu nome é"):
        nome_usuario = mensagem_original[len("meu nome é"):].strip()

        if nome_usuario:
            memoria["nome"] = nome_usuario
            salvar_memoria()
            print(f"Alex: Prazer em te conhecer, {nome_usuario}!")
        else:
            print("Alex: Qual é o seu nome?")

        continue

    # Perguntar o nome
    elif mensagem in ["qual é meu nome", "meu nome", "quem sou eu"]:
        print(f"Alex: Seu nome é {memoria['nome']}!")

    # Atualizar a cor favorita
    elif mensagem.startswith("minha cor favorita é"):
        cor = mensagem_original[len("minha cor favorita é"):].strip()

        if cor:
            memoria["cor_favorita"] = cor
            salvar_memoria()
            print(f"Alex: Legal! Vou lembrar que sua cor favorita é {cor}.")
        else:
            print("Alex: Qual é sua cor favorita?")

        continue

    # Perguntar a cor favorita
    elif mensagem in [
        "qual é minha cor favorita",
        "minha cor favorita",
        "qual minha cor favorita"
    ]:
        print(f"Alex: Sua cor favorita é {memoria['cor_favorita']}!")

    # Atualizar o jogo favorito
    elif mensagem.startswith("meu jogo favorito é"):
        jogo = mensagem_original[len("meu jogo favorito é"):].strip()

        if jogo:
            memoria["jogo_favorito"] = jogo
            salvar_memoria()
            print(f"Alex: Vou lembrar que seu jogo favorito é {jogo}.")
        else:
            print("Alex: Qual é seu jogo favorito?")

        continue

    # Perguntar o jogo favorito
    elif mensagem in [
        "qual é meu jogo favorito",
        "meu jogo favorito",
        "qual meu jogo favorito"
    ]:
        print(f"Alex: Seu jogo favorito é {memoria['jogo_favorito']}!")

    # Responder às outras mensagens
    else:
        print("Alex:", responder(mensagem))
        