# Descrição do trabalho

## Dos objetivos

O objetivo deste trabalho é construir um algoritmo para calcular a **probabilidade de uma palavra ter vindo de um determinado texto.**

Deverá ser utilizado o [Teorema de Bayes](https://pt.wikipedia.org/wiki/Teorema_de_Bayes) para cálculo da probabilidade. O Teorema de Bayes assume independência entre as variáveis dada a sua classe.

## Do prazo

* O prazo para entrega deste trabalho é as 23:59 de **15/08/2020** (15 de agosto de 2020). 
* O trabalho deverá ser enviado por e-mail para henry.cagnini@edu.pucrs.br com o título **Trabalho Final Python**.
* Você deverá anexar um arquivo .zip com todos os arquivos que julgar pertinente para que eu consiga **executar a sua solução**.
* Tenha em mente que utilizarei as funções fornecidas neste trabalho para verificar a corretude do seu código (ver seção _Especificidades da solução_ para mais detalhes)
* Se você tiver dúvidas durante a realização do trabalho, me mande um e-mail com a sua dúvida, que responderei o mais breve possível. 

## Dos métodos

* A linguagem de programação Python deverá ser utilizada, e tão somente a linguagem Python; 
* Bibliotecas de alto nível poderão ser utilizadas.

### Especificidades da solução

* O algoritmo não deve ser _case sensitive_ ; isto é, todos os caracteres maiúsculos devem ser convertidos para minúsculos, e.g. Banana -> banana
* O algoritmo deverá tratar as strings, removendo por exemplo pontuações (ponto, vírgula, ponto e vírgula, dois pontos, travessão, etc);
* Não é estritamente necessário tratar siglas nem palavras hifenizadas (e.g. U.S., mind-blowing), pois elas não serão utilizadas para avaliar o trabalho; 
* Implemente as funções fornecidas no _template_ do trabalho; isto é, você pode até criar funções auxiliares, implementar classes, scripts, módulos, etc, para resolver os problemas; todavia, **as funções fornecidas à você deverão fazer o que se pede, pois é com elas que avaliarei o trabalho**

## Teorema de Bayes

O [Teorema de Bayes](https://pt.wikipedia.org/wiki/Teorema_de_Bayes) denota a probabilidade de um evento ocorrer, dado um conhecimento _a priori_ :

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

Com o Teorema de Bayes, você irá calcular a probabilidade de uma palavra ter vindo de um determinado texto, da coleção de textos disponíveis.

Utilizar o Teorema de Bayes neste contexto significa dizer que a probabilidade de uma palavra ocorrer em um determinado texto _é independente_ da presença ou não de outras palavras.

Sabemos que na prática isso não acontece: na palavra composta _mind-blowing_ , _blowing_ é diretamente dependente da presença de _mind_ para ocorrer; é muito mais difícil _blowing_ aparecer sem a presença de _mind_ em um texto. Todavia, para a maioria dos casos, Naïve Bayes (o classificador que utiliza o Teorema de Bayes) apresenta um desempenho razoavelmente competitivo.

---

Tome o seguinte exemplo para elucidar a equação.

Uma pessoa vai ao médico, reclamando de torcicolo. O médico sabe que uma pessoa que está com meningite apresenta pescoço rígido em 50% dos casos. A probabilidade de uma pessoa ter meningite é de 1 em 50000 casos, e a de ter torcicolo (independente da causa) é de 1 em 20. Logo, a probabilidade do paciente ter meningite, dado que está com torcicolo, é de

$$P(\text{meningite}|\text{torcicolo}) = \frac{P(\text{torcicolo}|\text{meningite})P(\text{meningite})}{P(\text{torcicolo})} = \frac{0.5 * 0.00002}{0.05} = 0.0002 = 0.02\%$$

## Textos

Cinco textos jornalísticos devem ser utilizados para este trabalho. Os textos são fornecidos tanto em formato .txt (para utilização no trabalho) quando .html (para leitura do artigo). Adicionalmente, a fonte dos artigos é dada nos seguintes links:

* [President Bolsonaro of Brazil Tests Positive for Coronavirus](https://www.nytimes.com/2020/07/07/world/americas/brazil-bolsonaro-coronavirus.html)
* [Brazil's Jair Bolsonaro tested again for coronavirus](https://www.theguardian.com/world/2020/jul/07/brazil-jair-bolsonaro-tested-again-for-coronavirus)
* [Brazil's president tested for COVID-19](https://www3.nhk.or.jp/nhkworld/en/news/20200707_18/)
* [Schadenfreude in Brazil as Jair Bolsonaro gets coronavirus](https://www.dw.com/en/schadenfreude-in-brazil-as-jair-bolsonaro-gets-coronavirus/a-54097353)
* [Brazil’s Bolsonaro tests positive for coronavirus](https://www.washingtonpost.com/world/the_americas/coronavirus-brazil-bolsonaro-tests-positive/2020/07/07/5fa71548-c049-11ea-b4f6-cb39cd8940fb_story.html)

### Exemplos de respostas corretas

Para auxiliar na resolução do problema, confira abaixo a probabilidade de ocorrência de algumas palavras. No desenvolvimento do seu trabalho, utilize estas respostas para verificar se o seu código está calculando as probabilidades corretamente.

|  Query                        |  Probabilidade  |
|:------------------------------|:----------------|
| P('pandemic')                 |  0.005          |
| P('pandemic' \| texto_1)      |  0.0071         |
| P('pandemic' \| texto_2)      |  0.0            |
| P('pandemic' \| texto_3)      |  0.0            |
| P('pandemic' \| texto_4)      |  0.0094         |
| P('pandemic' \| texto_5)      |  0.0021         |
|                               |                 |
| P('coronavirus')			    |  0.0101         |
| P('coronavirus' \| texto_1)	|  0.0071         |
| P('coronavirus' \| texto_2)	|  0.0146         |
| P('coronavirus' \| texto_3)	|  0.0088         |
| P('coronavirus' \| texto_4)	|  0.0141         |
| P('coronavirus' \| texto_5)	|  0.0084         |

## Ferramental

O ferramental necessário para realização do trabalho já foi apresentado nas aulas iniciais da disciplina, todavia uma recapitulação rápida é apresentada abaixo.

### Instalando Anaconda e criando ambiente virtual

1. Baixe o Python Anaconda: https://www.anaconda.com/products/individual
2. Instale na sua máquina
3. Lembre-se de adicionar o caminho para a instalação na sua variável PATH. O passo-a-passo para esta solução depende do seu sistema operacional: [What is the default path for installing Anaconda?](https://docs.anaconda.com/anaconda/user-guide/faq/#:~:text=If%20you%20accept%20the%20default,your%2Dusername%3E%5CAnaconda3%5C)
4. Abra o console/terminal no seu sistema operacional. Rode a instrução `conda --version` no terminal para ver se a configuração foi bem sucedida. Se o programa não for encontrado, volte ao passo 3
5. Crie um novo ambiente virtual: ```conda create --name py3 python=3```
6. Ative o ambiente virtual: ```conda activate py3```
7. Instale bibliotecas pertinentes: ```conda install jupyter nose numpy pandas matplotlib``` 
    * Nota: você pode instalar outras bibliotecas que achar pertinente para resolução deste trabalho. Google it!
8. Após a instalação, e com o ambiente virtual ativado (passo 6), abra um jupyter notebook: ```jupyter notebook```

### Fazendo download do repositório

Para baixar este repositório, simplesmente clique no botão verde `code` e selecione a opção `download zip`. Ou, se você já for um usuário do Github, clone o repositório.

--- 
Bom trabalho!

