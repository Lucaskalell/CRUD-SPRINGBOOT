def contar_ocorrencias(corpus, palavra_chave, sinonimos):
    contagem = 0
    for documento in corpus:
        for palavra in documento.split():
            if palavra == palavra_chave or palavra in sinonimos:
                contagem += 1
    return contagem

# Exemplo de uso:
corpus = ["Este é um documento de exemplo.",
          "Outro documento contendo palavras-chave e sinônimos.",
          "Aqui está mais um documento para a análise."]
palavra_chave = "documento"
sinonimos = ["arquivo", "texto"]

ocorrencias = contar_ocorrencias(corpus, palavra_chave, sinonimos)
print("Ocorrências encontradas:", ocorrencias)
