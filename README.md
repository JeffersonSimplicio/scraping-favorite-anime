<h1 align="center">Favorite Anime Scraping(V2.5.2)</h1>

## O que há de novo?
* Suporte ao BetterAnime e Anihub
* Corrigida falha de download das thunbs
* Gera arquivos vazios agora exigem confirmação do usuário
* CLI mais limpa
* Agora cada arquivo gerado possui um nome exclusivo
* Confirmação de resposta padrão
* O texto da quantidade de favoritos se ajusta a quantidade de animes

## Descrição
Favorite Anime Scraping, surgiu de um desejo meu de recuperar minha lista de animes, que está em um site onde costumava assisti-los. Por acreditar que outras pessoas poderiam ter o mesmo desejo, decidi compartilhar, criando um arquivo executável(.exe) para facilitar seu uso. O programa consegue obter o nome do anime, a URL de sua capa e até mesmo baixar a capa caso o usuário deseje. Com o tempo fui adicionando funcionalidades, corrigindo bugs, acrescentando novos sites suportados.

## Tecnologias
* [Python](https://www.python.org/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/)
* [Pyinstaller](https://pyinstaller.org/en/stable/)

Todo o projeto foi desenvolvido em **[Python](https://www.python.org/)**, o **[Venv](https://docs.python.org/pt-br/3/library/venv.html)** foi usado para criar um ambiente isolado de desenvolvimento e reduzir complexidade na geração do executável. A obtenção dos dados a partir do código do html foi feita usando o **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/)**. Uma das opções oferecidas é o download das capas dos animes, nessa tarefa é usada o **[Requests](https://requests.readthedocs.io/en/latest/#)**. O programa foi construído usando o padrão de projeto **[Strategy](https://pt.wikipedia.org/wiki/Strategy)**, para facilitar a implicação de raspagem de novos sites.

## Utilização
<details>
  <summary><strong>Executável(.exe)(Recomendado)</strong></summary>

  1. Baixe o executável do arquivo executável ([Download](https://github.com/JeffersonSimplicio/scraping-favorite-anime/raw/main/anime_scrapingV2.5.2.exe))
  - ⚠️: O Windows pode identificar o arquivo como malware, não se preocupe, o executável foi gerando com Pyinstaller a partir do código-fonte. Caso não se sinta confortável, é possível usar diretamente no código-fonte, <a href="#source-code">veja aqui</a>.

  2. Faça login no site(Better Anime ou Anihub), e navegue ate a pagina de favoritos

  3. Clique com o botão direito o mouse e depois em Inspecionar ou pressione F12 em seu teclado

  4. Uma tecla semelhante a esta surgira, clique em body e nos 3(três) pontos que surgirão a esquerda, conforme a imagem a baixo
  ![image](./images_docs/image1.png)

  5. Clique em `Cópia` e em seguida `Copiar elemento`
  ![image](./images_docs/image2.png)

  6. Abra o editor de texto que sua preferência, cole o código e salve o arquivo com a extensão `.html`
  - ✨ **Dica:** Recomendo que o executável e o HTML figuem na mesma pasta, esse é o local padrão onde um programa buscara o arquivo do site
  - ✨ **Dica:** O arquivo pode ser salvo com qualquer nome, mas recomendo que salve como `favorites-list-page.html`, esse é o nome padrão que o programa utiliza

  7. Abra o programa

  8. Caso tenha seguido as dicas dadas anteriormente, basta clicar Enter; do contrário sera necessário informar a rota até o html

  9. O programa lhe dará 4(quatro) opções, escolha uma delas, digite o número e pressione Enter. Você pode usar o programa quantas vezes quiser e testar cada opção
</details>

<details>
  <summary id="source-code">
    <strong>Via código-fonte</strong>
  </summary>
  Este método é uma alternativa para usuários de Linux ou Mac<br>
  Este procedimento <strong>não é recomendado</strong><br>
  Para usar esse método é preciso possuir o **python** instalado e recomendado o uso do venv

  1. Clone o repositório
  ```
  git clone git@github.com:JeffersonSimplicio/scraping-favorite-anime.git

  ```

  2. Entre no diretório gerado
  ```
  cd scraping-favorite-anime

  ``` 

  3. Inicialize o ambiente virtual de desenvolvimento(Este passo não é obrigatório, mas é recomendado)
  ```
  python3 -m venv .venv && source .venv/bin/activate

  ```

  4. Instale as dependências
  ```
  pip install -r requirements.txt  

  ```

  5. Faça login no site(Better Anime ou Anihub), e navegue ate a pagina de favoritos

  6. Clique com o botão direito o mouse e depois em Inspecionar ou pressione F12 em seu teclado

  7. Uma tecla semelhante a esta surgira, clique em body e nos 3(três) pontos que surgirão a esquerda, conforme a imagem a baixo
  ![image](./images_docs/image1.png)

  8. Clique em `Cópia` e em seguida `Copiar elemento`
  ![image](./images_docs/image2.png)

  9. Abra o editor de texto que sua preferência, cole o código e salve o arquivo com a extensão `.html`
  - ✨ **Dica:** Recomendo que o executável e o HTML figuem na mesma pasta, esse é o local padrão onde um programa buscara o arquivo do site
  - ✨ **Dica:** O arquivo pode ser salvo com qualquer nome, mas recomendo que salve como `favorites-list-page.html`, esse é o nome padrão que o programa utiliza

  10. Inicie o programa
  ```
  python3 src/main.py  
  ```

  11. Caso tenha seguido as dicas dadas anteriormente, basta clicar Enter; do contrário sera necessário informar a rota até o html
   
  12. O programa lhe dará 4(quatro) opções, escolha uma delas, digite o número e pressione Enter. Você pode usar o programa quantas vezes quiser e testar cada opção
</details>

## O que cada opção faz
  - `1 - Lista de nomes(txt)`: Gera um arquivo txt, com o nome de todos os animes favoritados no site
 - `2 - Lista com nome e URL da thunb(txt)`: Gera um arquivo txt, com o nome de todos os animes favoritados no site e ao lado a URL para sua capa
 - `3 - Lista com nome e URL da thunb(json)`: Gera um arquivo json, com uma lista de objetos contendo nome e URL da capa
 - `4 - Lista com nome e path da thumb(download da thunb)(json)`: Gera um arquivo json e também uma pasta *thunbs*, na pasta esta todas as capas dos animes favoritados, no json está uma lista de objetos contendo nome e o path para capa na pasta thunbs

## Respondendo algumas duvidas
<details>
  <summary><strong>Em quais sites é possível usado o programa?</strong></summary>
  A partir da versão 2.0, da suporte ao <a href="https://betteranime.net/">Better Anime</a> e ao <a href="https://anihub.tv/login?redirect=%2F">Anihub</a>
</details>
<details>
  <summary><strong>Por que programa não faz a raspagem direto na web?</strong></summary>
  O site usa reCaptcha dificultando tal tarefa, além disso, muitos usuários não se sentiriam confortáveis colocando suas credenciais.
</details>
<details>
  <summary><strong>É possível utilizar o programa também no Linux?</strong></summary>
  Sim. Por enquanto um modo simples de usar se limita ao Windows, para usar o programa no Linux, é necessário usá-lo a partir do código-fonte diretamente. <a href="#source-code">Tutorial para Linux</a>
</details>
