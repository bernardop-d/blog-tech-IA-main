# Blog Tech IA — Blog que publica posts automaticamente sobre tecnologia

Um blog simples feito com Jekyll e hospedado no GitHub Pages. A parte interessante é que ele se atualiza sozinho: um script Python escolhe um tópico da área de tech, cria um post em Markdown e um robô do GitHub faz o commit duas vezes por dia — sem precisar de nenhuma intervenção manual.

🔗 Blog ao vivo: [https://bernardop-d.github.io/blog-tech-IA-main/](https://bernardop-d.github.io/blog-tech-IA-main/)

---

## Tecnologias usadas

- **Python 3** — gera os posts (stdlib apenas: `os`, `json`, `re`, `datetime`, `random`)
- - **Jekyll** — transforma os arquivos Markdown em um site estático
  - - **GitHub Actions** — roda o script automaticamente 2x por dia
    - - **GitHub Pages** — hospeda o site de graça
      - - **Markdown** — formato dos posts
       
        - > Não há dependências externas de Python. Não é usada nenhuma API de IA — o conteúdo é baseado em templates pré-escritos.
          >
          > ---
          >
          > ## O que o projeto faz (na prática)
          >
          > 1. Há uma lista de ~40 tópicos de tecnologia (IA, segurança, backend, DevOps, etc.) dentro do script Python.
          > 2. 2. Quando o script roda, ele escolhe um tópico que ainda não foi usado recentemente.
          >    3. 3. Com base na categoria do tópico, ele preenche um template de post com título, tags e um corpo de texto fixo.
          >       4. 4. O post é salvo como um arquivo `.md` na pasta `_posts/` com a data de hoje no nome.
          >          5. 5. O GitHub Actions faz commit e push desse arquivo automaticamente.
          >             6. 6. O GitHub Pages publica o site atualizado em alguns minutos.
          >               
          >                7. O controle de tópicos já usados fica salvo em `.used_topics.json`. Quando todos os tópicos forem usados, a lista reseta e começa de novo.
          >               
          >                8. ---
          >               
          >                9. ## Como rodar localmente
          >                10.
          > ### Pré-requisitos
          >
          > - Python 3.8 ou superior instalado
          > - - Git
          >  
          >   - ### Passo a passo
          >  
          >   - ```bash
          >     # 1. Clone o repositório
          >     git clone https://github.com/bernardop-d/blog-tech-IA-main.git
          >     cd blog-tech-IA-main
          >
          >     # 2. Rode o gerador de posts
          >     python post_generator.py
          >
          >     # 3. Confira o post criado
          >     ls _posts/
          >     ```
          >
          > Não há dependências para instalar — o script usa apenas bibliotecas padrão do Python.
          >
          > ### (Opcional) Rodar o blog localmente
          >
          > Para visualizar o site no navegador, você vai precisar ter Ruby e Jekyll instalados:
          >
          > ```bash
          > gem install jekyll bundler
          > jekyll serve
          > ```
          >
          > Depois acesse `http://localhost:4000` no navegador.
          >
          > ---
          >
          > ## Como rodar os testes
          >
          > ```bash
          > # Instale o pytest se ainda não tiver
          > pip install pytest
          >
          > # Rode todos os testes
          > pytest test_post_generator.py -v
          > ```
          >
          > ---
          >
          > ## Estrutura de pastas
          >
          > ```
          > blog-tech-IA-main/
          > │
          > ├── .github/
          > │   └── workflows/
          > │       └── main.yml          # Agendamento automático (GitHub Actions)
          > │
          > ├── .vscode/                  # Configurações do editor (pode ignorar)
          > │
          > ├── _layouts/                 # Templates HTML do Jekyll
          > │
          > ├── _posts/                   # Posts gerados ficam aqui (arquivos .md)
          > │
          > ├── .used_topics.json         # Guarda quais tópicos já foram usados
          > ├── _config.yml               # Configurações do Jekyll (título, URL, tema)
          > ├── index.html                # Página inicial do blog
          > ├── tags.html                 # Página de tags
          > ├── post_generator.py         # Script principal — gera os posts
          > └── test_post_generator.py    # Testes do script principal
          > ```
          >
          > ---
          >
          > ## Melhorias implementadas
          >
          > - Adicionado arquivo `test_post_generator.py` com testes das funções principais
          > - - Adicionado este README
          >  
          >   - ---
          >
          > ## Observações
          >
          > - O conteúdo dos posts é baseado em templates fixos, não gerado por IA em tempo real.
          > - - O script não precisa de chave de API nem conexão com a internet para funcionar.
          >   - - Se quiser adicionar novos tópicos, basta editar a lista `topics` dentro de `post_generator.py`.
