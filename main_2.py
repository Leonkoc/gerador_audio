import os
import edge_tts # type: ignore
import asyncio

# Nome do arquivo padrão
ARQUIVO_PADRAO = "escreva_aqui.txt"

# Função para ler o conteúdo do arquivo escreva_aqui.txt
def ler_arquivo_texto():
    if not os.path.exists(ARQUIVO_PADRAO):
        print(f"Erro: O arquivo '{ARQUIVO_PADRAO}' não foi encontrado.")
        print("Por favor, crie o arquivo na mesma pasta do código e escreva o texto que deseja converter em áudio.")
        return None
    try:
        with open(ARQUIVO_PADRAO, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Erro ao ler o arquivo '{ARQUIVO_PADRAO}': {e}")
        return None

# Função para converter texto em áudio
async def text_to_mp3(text, arquivo, voz="pt-BR-AntonioNeural"):
    tts = edge_tts.Communicate(text, voz)
    print("Convertendo texto em áudio...")
    await tts.save(arquivo)
    print(f"O áudio foi salvo como {arquivo}")

# Gerar nome do arquivo com base na primeira palavra do texto
def gerar_nome_por_texto(texto, extensao="mp3"):
    primeira_palavra = texto.split()[0] if texto.strip() else "audio"
    return f"{primeira_palavra}.{extensao}"

# Função principal
def main():
    texto = ler_arquivo_texto()
    if texto is None:
        return  
    
    if not texto:
        print(f"O arquivo '{ARQUIVO_PADRAO}' está vazio. Escreva o texto desejado e execute o código novamente.")
        return

    arquivo = gerar_nome_por_texto(texto)
    asyncio.run(text_to_mp3(texto, arquivo))

if __name__ == "__main__":
    main()
