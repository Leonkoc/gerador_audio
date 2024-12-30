import edge_tts # type: ignore
import asyncio

async def text_to_mp3(text,arquivo):
    #Escolher a voz pt-BR
    voz = "pt-BR-AntonioNeural"
    tts = edge_tts.Communicate(text, voz)

    print('Ai vem o áudio')
    await tts.save(arquivo)
    print(f'O áudio foi salvo como {arquivo}')

def main():
    texto =  """
        Coloque aqui o texto que deseja converter em áudio.
    """
    
    arquivo = "texto_convertido.mp3"
    
    asyncio.run(text_to_mp3(texto,arquivo))

if __name__ == "__main__":
    main()