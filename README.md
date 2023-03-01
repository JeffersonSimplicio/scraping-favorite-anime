<h1 align="center">Favorite Anime Scraping</h1>

## Descrição
Favorite Anime Scraping, surgiu de um desejo meu de recuperar minha lista de animes, que está em um site onde costumava assisti-los. Por acreditar que outras pessoas poderiam ter o mesmo desejo, decidi compartilhar, criando um arquivo executável(.exe) para facilitar seu uso. O programa consegue obter o nome do anime, a URL de sua capa e até mesmo baixar a capa caso o usuário deseje.

## Tecnologias
* [Python]("https://www.python.org/")
* [Requests]("https://requests.readthedocs.io/en/latest/")
* [Beautiful Soup]("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/")
* [Pyinstaller]("https://pyinstaller.org/en/stable/")

Todo o projeto foi desenvolvido em **Python**, para garantir um ambiente isolado para o desenvolvimento e reduzir complexidade na conversão para .exe, utilizar o **venv**. O processo de raspagem foi feito com o **Beautiful Soup**, mapeado e filtrando os dos do html. Quanto a download de imagens foi usado o **Requests**. A conversão do código-fonte para executável foi feita através do **Pyinstaller**.
