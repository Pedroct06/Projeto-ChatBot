# 🤖 PedroBot

Um chatbot inteligente desenvolvido em Python que utiliza o modelo Llama 3.3 70B (via Groq) para conversar e responder perguntas com base em diferentes fontes de informação.

## 📋 Descrição

O PedroBot é um assistente virtual que pode processar informações de múltiplas fontes e responder perguntas de forma contextualizada. Ele suporta:

- 🌐 **Sites** - Carrega e processa conteúdo de URLs
- 📄 **PDFs** - Extrai texto de arquivos PDF
- 🎥 **Vídeos do YouTube** - Transcreve e processa legendas de vídeos
- 💬 **Chat livre** - Conversa sem contexto adicional

## 🚀 Funcionalidades

- Interface de linha de comando simples e intuitiva
- Suporte a múltiplas fontes de dados
- Histórico de conversa mantido durante a sessão
- Respostas contextualizadas baseadas no documento carregado
- Tratamento de erros robusto

## 📦 Requisitos

- Python 3.8 ou superior
- Conta na [Groq](https://groq.com/) para obter uma API key
- Conexão com a internet

## 🔧 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/pedrobot.git
cd pedrobot
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
GROQ_API_KEY=sua_chave_api_aqui
```

Para obter sua chave API:
- Acesse [console.groq.com](https://console.groq.com/)
- Crie uma conta ou faça login
- Gere uma nova API key na seção de configurações

## 💻 Como Usar

1. **Execute o programa:**
```bash
python chatbot.py
```

2. **Escolha uma opção:**
   - `1` - Carregar conteúdo de um site
   - `2` - Carregar conteúdo de um arquivo PDF
   - `3` - Carregar legendas de um vídeo do YouTube
   - `4` - Iniciar chat sem contexto adicional
   - `X` - Sair do programa

3. **Converse com o bot:**
   - Digite suas perguntas
   - Digite `x` para encerrar o chat

## 📝 Exemplos de Uso

### Exemplo 1: Analisando um site
```
Digite 1 para me mandar um site
Sua escolha: 1
Digite a URL do site: https://exemplo.com/artigo
Você: Qual é o tema principal deste artigo?
PedroBot: [Resposta baseada no conteúdo do site]
```

### Exemplo 2: Processando um PDF
```
Digite 2 para me mandar um PDF
Sua escolha: 2
Digite o caminho do arquivo PDF: /caminho/para/documento.pdf
PDF carregado com sucesso.
Você: Resuma os pontos principais
PedroBot: [Resumo do PDF]
```

### Exemplo 3: Analisando vídeo do YouTube
```
Digite 3 para me mandar um vídeo do YouTube
Sua escolha: 3
Digite a URL do vídeo do YouTube: https://www.youtube.com/watch?v=exemplo
Vídeo carregado com sucesso.
Você: Sobre o que fala este vídeo?
PedroBot: [Resumo baseado nas legendas]
```

## 🛠️ Tecnologias Utilizadas

- **LangChain** - Framework para desenvolvimento de aplicações com LLMs
- **Groq** - API para acesso ao modelo Llama 3.3 70B
- **pypdf** - Extração de texto de arquivos PDF
- **BeautifulSoup4** - Scraping de conteúdo web
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## ⚙️ Estrutura do Projeto

```
pedrobot/
│
├── chatbot.py          # Código principal do chatbot
├── requirements.txt    # Dependências do projeto
├── .env               # Variáveis de ambiente (não incluído no repositório)
├── .gitignore         # Arquivos ignorados pelo git
└── README.md          # Este arquivo
```

## ⚠️ Observações Importantes

- O bot requer uma chave API válida do Groq para funcionar
- Para vídeos do YouTube, certifique-se de que possuem legendas em português
- Arquivos PDF muito grandes podem levar mais tempo para processar
- O histórico da conversa é perdido ao encerrar o programa

## 🔒 Segurança

- **Nunca compartilhe sua chave API** em repositórios públicos
- Adicione o arquivo `.env` ao `.gitignore`
- Mantenha suas dependências atualizadas

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!





