import os 
os.environ['USER_AGENT'] = 'PedroBot/1.0'
import io
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
chat = ChatGroq(model = "llama-3.3-70b-versatile")

def resposta_bot(mensagens, documento):
    system_message = "Voce é um assistente chamado PedroBot que responde tudo com piadas e ironia, e tem acesso as seguintes informações para dar as suas respostas: {informações}"
    mensagens_formatadas = [('system', system_message)]
    mensagens_formatadas += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_formatadas)
    chain = template | chat    
    return chain.invoke({"informações": documento}).content

def carrega_site():
    url_site = input("Digite a URL do site: ")
    loader = WebBaseLoader(url_site)
    lista_docs = loader.load()
    documento = ""
    for doc in lista_docs:
        documento += doc.page_content
    return documento


def carrega_pdf(bytes_do_pdf):
    stream_bytes = io.BytesIO(bytes_do_pdf)
    documento = ""
    try:
        reader =  PdfReader(stream_bytes)
        for pagina in reader.pages:
            texto = pagina.extract_text()
            if texto:
                documento += texto
    except Exception as e:
        print(f"Erro ao ler PDF: {e}")
        return ""
    return documento


def carrega_youtube(url_video):
    try:
        loader = YoutubeLoader.from_youtube_url(url_video, language='pt', add_video_info=True)
        lista_docs = loader.load()
        documento = ""
        for doc in lista_docs:
            documento += doc.page_content
        return documento
    except Exception as e:
        print(f"Erro ao carregar vídeo do YouTube: {e}")
        return ""


print("Bem-vindo ao PedroBot!")

texto_selecao = '''
Digite 1 para me mandar um site
Digite 2 para me mandar um PDF
Digite 3 para me mandar um vídeo do YouTube
Digite 4 para conversar com o chat
Digite X para sair

Sua escolha:
'''
while True:
    selecao = input(texto_selecao)
    if(selecao == '1'): 
        documento = carrega_site()
        break
    elif(selecao == '2'):
        caminho_pdf = input("Digite o caminho do arquivo PDF: ")
        try:
            with open(caminho_pdf, 'rb') as arquivo_pdf:
                bytes_pdf = arquivo_pdf.read()
            documento = carrega_pdf(bytes_pdf)
            print("PDF carregado com sucesso.")
            print(f"Conteúdo do PDF:\n{documento}")
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
            continue
        except Exception as e:
            print(f"Erro ao abrir o arquivo PDF: {e}")
        break
    elif(selecao == '3'):
        url_video = input("Digite a URL do vídeo do YouTube: ")
        documento = carrega_youtube(url_video)
        if documento:
            print("Vídeo carregado com sucesso.")
            print(f"Conteúdo do vídeo:\n{documento}")
        else:
            print("Falha ao carregar o vídeo. Tente novamente.")
            continue
        break
    elif(selecao == '4'):
        print('--começando chat normal--')
        documento = ""
        break
    elif(selecao.lower() == 'x'):
        print("Encerrando o programa. Até mais!")
        exit()
    print("Digite um valor válido.")
    

mensagens = []
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "x":
        print("Encerrando o chat. Até mais!")
        break
    mensagens.append(("user", pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(("assistant", resposta))
    print(f'PedroBot: {resposta}')

print("Chat finalizado.")
