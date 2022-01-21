# Testando o uso de Diversas Coleções: Contar as letras de dois textos de diferentes assuntos:

# 1° passo: pegar dois textos e atribuir cada um em sua variavel:  No exemplo utilizamos dois textos do blog da Alura.

texto1 = '''
Repare que quando olhamos para este resultado temos um desconforto na leitura dos textos. Por que será que isso acontece?

A fonte muito clara em fundo branco, os buracos ao longo do texto, e mesmo as entrelinhas muito estreitas, geram uma dificuldade de leitura e, consequentemente, não nos sentimos motivados a ler o conteúdo da página.

Então, o que poderíamos fazer para melhorar essa página, pensando em usabilidade e legibilidade? Confira algumas dicas essenciais para fazer essas mudanças.

1. As cores e fontes corretas
O primeiro passo a considerar é se os textos estão legíveis, considerando alguns fatores como:

Contraste de cores entre plano de fundo e texto;
Tamanho da fonte;
Tipo de fonte utilizada.
No layout anterior temos um texto com fonte muito clara sobre um plano de fundo igualmente claro. Isso gera um baixo contraste entre os dois elementos e torna difícil a distinção dos caracteres e palavras, comprometendo a leitura, como podemos notar neste fragmento do layout:
Ao passo que, a simples alteração da cor para uma outra um pouco mais escura, ou mais contrastante, seria o suficiente:
Outra questão é o tipo de fonte . Em qual das opções abaixo você acredita ser mais confortável a leitura?
No segundo exemplo, onde temos uma fonte mais básica, sem serifa, a leitura fica muito mais fácil. Isso porque, a menos que sejam frases curtas, utilizar fontes mais trabalhadas (com muitos detalhes, cursivas, etc) nos gera um maior esforço para ler grandes blocos de texto.

Devemos ter cuidado no momento da escolha da fonte, pensando sempre na forma com a qual ela será aplicada, ou seja, se será utilizada em grandes blocos de texto, em títulos, com plano de fundo claro ou escuro, etc.

2. Espaços em branco
Um erro comum e que faz muita diferença no resultado final é pensar nos espaços em branco do layout.
Perceba que no primeiro exemplo quase não temos espaço entre os elementos e, no segundo, ao inserir os espaços, temos um respiro maior que gera também uma melhor compreensão.

Sem estes espaços, podemos dificultar a visualização geral do conteúdo, que não terá priorização. Separando adequadamente cada elemento, diminuimos o ruído visual e tornamos mais fácil a leitura.

Estes espaços não são simplesmente adicionandos como vazios aleatórios para distanciar um elemento do outro. Mais do que isso, os espaços em branco são parte integrante do layout.

Essa dica vale também, no caso dos textos, quando pensamos em entrelinhas.

Entrelinhas muito espaçadas ou muito estreitas, como no exemplo apresentado no post, causam uma sensação desagradável para a leitura.Note que, no segundo exemplo, a leitura fica muito mais fluida.

Contudo, mesmo com essa mudança, percebemos que ainda há alguns espaços no texto que causam um desconforto na leitura. Estes são os espaços em braco indesejáveis, que ao invés de auxiliar na usabilidade, acabam deixando tudo mais complicado. E como resolver essa questão?

3. Alinhamento de texto
Existem 4 tipos de alinhamento possíveis para a web: à esquerda, centralizado, à direita ou justificado.

No layout que analisamos, o alinhamento está como justificado, isto é, busca-se preencher todas as linhas de texto de uma ponta a outra.
Porém, note que este alinhamento cria diversas lacunas ao longo do texto, já que, diferente dos textos impressos, os textos na web não se ajustam muito bem ao formato das caixas de texto, portanto, podem não ser uma boa escolha para utilizarmos.

Quanto ao alinhamento à direita e centralizado, temos novamente um problema na leitura de textos mais longos, já que nestes dois casos temos mais dificuldade de identificar o início e fim das linhas, tornando a leitura mais cansativa.
O ideal para estes dois casos é que sejam usados principalmente em pequenos textos.

Por fim, temos o alinhamento à esquerda:
Note que, além deste ser o alinhamento mais comumente utilizado, baseado no nosso sistema ocidental de leitura, da esquerda para a direita, o texto fica muito mais fácil de ser lido e não causa um desconforto para o usuário que lerá longos blocos de texto na página.

4. Tamanho das caixas de texto
Outro ponto importante a ser observado no layout é o tamanho que atribuímos às áreas de texto.

Caixas de texto muito largas, por exemplo, dificultam a leitura, uma vez que a orientação do olhar se perde mais facilmente ao percorrer linhas muito longas.

Da mesma forma, caixas muito estreitas causam um estranhamento ao quebrar os textos em pequenas frases, que tornam a leitura muito menos fluida.
Para não cair neste problema, evite caixas muito largas ou muito estreitas, distribuindo o texto em larguras mais confortáveis de ler e variando o tamanho dos elementos de texto, para criar um layout mais limpo e agradável de ler.
'''

texto2 = '''
A melhor forma de atrair público para o seu blog é criando conteúdo relevante e de qualidade. Ao oferecer materiais que ajudam, educam e entretêm, você cria um vínculo instantâneo com cada visitante, e essa relação é fundamental para o sucesso do blog!

Produza conteúdo relevante
Você já reparou a quantidade enorme de conteúdo que você consome todos os dias? São notícias, vídeos engraçados, posts de opinião nas redes sociais, músicas, videoclipes, imagens, GIFs, fotografias, etc. Mas, quanto disso realmente é relevante?

Se você passar agora pela sua timeline em qualquer rede social, quais produtores de conteúdo vão cativar sua atenção e ganhar seu clique?

Esse é o pensamento que precisa nortear a sua produção de conteúdo. Nós somos atingidos por conteúdo o tempo inteiro, e o que define se ele é bom é a relevância que tem para o público. Ao criar conteúdo para o seu blog, procure fazê-lo seguindo esses dois princípios:

1. Conheça seu público
O primeiro passo da produção de conteúdo é traçar bem a sua persona. A persona é uma representação do seu público ideal, com as características e problemas que você deseja atingir e solucionar.

Ao definir sua persona, você consegue entender melhor como cada conteúdo vai se encaixar dentro da sua estratégia. Se ela gosta de textos longos, você não precisa perder tempo produzindo conteúdos menores; se ela não tem tempo para ler, você pode investir em criar vídeos ou um podcast.

Conhecer seu público é fundamental para produzir conteúdo relevante, e, com uma persona bem definida, o processo de criação se torna muito mais tranquilo!

Utilizar personas é uma dica que pode facilitar bastante a sua vida caso você deseje atuar como redator freelancer, uma vez que ajuda você a conhecer melhor quem seus clientes desejam atingir com conteúdo.

2. Planeje cada conteúdo
O planejamento é a alma do conteúdo de qualidade. Ao ter uma ideia, coloque-a no papel e faça uma pauta bem detalhada do que será produzido. Defina:

formato: será um e-mail marketing ou conteúdo para o blog? Post, e-book, infográfico, vídeo?
tamanho e linguagem: curto, médio ou mais denso? Linguagem mais técnica ou mais acessível?
Call To Action (CTA): qual será o objetivo do seu conteúdo? Pedir que o visitante compartilhe nas redes sociais, baixe um e-book, acesse outro artigo ou vídeo, assine a newsletter?
Lembre-se de adequar cada um desses pontos aos objetivos e interesses da sua persona. Uma pauta bem estruturada funciona tão bem porque permite que você ou qualquer outra pessoa produza o conteúdo, sem prejuízos.

Aposte em formatos diferentes
Além de um tema relevante, o formato também é importantíssimo para o sucesso do conteúdo. A internet oferece muita liberdade nesse sentido, e a vantagem está ao lado daqueles que sabem aproveitar todas as oportunidades. Confira os formatos mais utilizados atualmente:

Post
O bom e velho post de blog. Escrito em texto corrido, com imagens apenas ilustrando o conteúdo, o post é o formato mais conhecido e produzido internet afora. Pode ser curto ou longo, informativo ou educativo, tutorial, lista, guia e até mesmo um texto opinativo.

Esse é um formato muito bacana de trabalhar, e a sua eficácia vai depender de cada persona. Como falamos anteriormente, a linguagem, a extensão e até mesmo o estilo de formatação do post vão depender das preferências da sua persona.

Entretanto, algumas dicas são universais:

lembre-se de que poucas pessoas utilizam apenas o computador para ler posts. Adapte seus textos para serem lidos em smartphones e tablets, utilizando fontes de fácil leitura, cores contrastantes e tamanhos confortáveis. Um site responsivo é fundamental;

a internet é bastante flexível quando o assunto é Português. Gírias, abreviações e até mesmo alguns errinhos de ortografia são aceitos nas redes sociais, mas nos posts podem gerar uma má impressão. Não é preciso escrever como em uma tese de doutorado, mas o básico da concordância, acentuação e gramática precisa ser respeitado;

textos bem escritos são aqueles que o leitor consegue ler e entender sem dificuldades. Não se preocupe em enfeitar demais o post com citações, exemplos e explicações. Na maioria das vezes, ser objetivo é a chave para o sucesso;

Infográfico
Os infográficos são ótimos para fazer listas, mostrar números e estatísticas ou explicar um assunto um pouco mais complicado. São materiais relevantes e ricos e podem ser disponibilizados como conteúdo exclusivo (mediante cadastro, por exemplo).

Assim, você conquista e-mails para a sua base de leads e recompensa o visitante com um material rico. Para os e-mails cadastrados, você pode criar uma newsletter semanal ou mensal, fazer e-mail marketing e muito mais.

A dica para criar bons infográficos é apostar em imagens e cores fortes, chamativas, mas sem sobrecarregar o visual. Cores contrastantes e pouco texto tornam a leitura mais fácil, ainda mais se você estiver trabalhando com números e porcentagens, por exemplo.

Áudio e vídeo
Os formatos audiovisuais fazem muito sucesso aonde quer que apareçam. Mais dinâmicos, dão a sensação de conversa, de proximidade, muito mais do que um texto ou imagem.

Existem várias formas de consumir esses conteúdos, o que os tornam uma alternativa viável para os mais diferentes tipos de persona. Hoje, qualquer smartphone reproduz vídeos com boa qualidade, e se não possui ferramentas próprias para executar áudios, permite pelo menos a reprodução em navegadores.

Além disso, esses formatos podem ser consumidos em qualquer ambiente — basta que o usuário esteja com seus fones de ouvido. Você pode levar conteúdo relevante para o seu público enquanto seus leitores estão na academia, pegam ônibus ou metrô ou, até mesmo, durante as pausas no trabalho.

Veja algumas dicas:

não importa se você vai gravar um vídeo para o Youtube ou um áudio para podcast, qualidade é fundamental. Escolha uma câmera com boa resolução (pode ser até a do seu celular), um ambiente organizado, bem iluminado e silencioso e mande ver na gravação;

sobre edições: na maioria das vezes, menos é mais. Grandes produções demandam investimento em equipamento de alta qualidade e tratamento pós-produção. É possível criar produtos audiovisuais de boa qualidade sem gastar muito. Basta manter a simplicidade e a objetividade, fazendo edições pontuais apenas para lapidar o produto;

você pode adaptar alguns conteúdos para formatos audiovisuais, como aulas e tutoriais, e até transformar seus posts em vlogs. Estude sua persona e faça testes, até encontrar o melhor formato para cada conteúdo.

E aí, já está preparado para produzir materiais irresistíveis para o seu blog? Compartilhe este post nas suas redes sociais e ajude outros blogueiros a darem o primeiro passo na produção de conteúdo relevante!
'''

# 2° Passo: Quero contar as letras dos textos. Séra que consigo?
# Vou criar um contador em cima do texto1 para saber quantas letras aparece no texto1:
# Saber a quantidade de cada caractere

from collections import Counter
quantidade_de_caractere = Counter(texto1)
print(f'Caractere e sua quantidade: {quantidade_de_caractere}')
print()

# 3° passo colocar todas as letras em minusculo:
# Na contagem acima, as letras estão misturadas em maiusculas e minuscula. Vou colocar tudo em minusculo.
quantidade_de_caractere = Counter(texto1.lower())
for letra, frequencia in quantidade_de_caractere.items():
    print(letra, frequencia)
#print(f'Deixando tudo em minusculo: {quantidade_de_caractere}')
print()

# 4° Passo: Jogo tudo isso em uma variavel, onde essa variavel vou saber qual o total de caracteres no texto.
quantidade_de_caractere = Counter(texto1.lower())
total_de_caractere = sum(quantidade_de_caractere.values()) # Somando os valores de quantidade_de_caractere. total de 4.740 caractere.
print(f'Total de: {total_de_caractere} caracteres.')
print()

# 5° Passo: Para cada uma das letras, quero pegar a letra, ver quantas vezes ela apareceu, dividir pelo total de letras no texto e colocar o percetual
# que ela representa do total de caracteres.
quantidade_de_caractere = Counter(texto1.lower())
total_de_caractere = sum(quantidade_de_caractere.values())
for letra, frequencia in quantidade_de_caractere.items(): # para mostrar a chave e o valor do iteravel. Ou seja pra cada letra e frequencia dela em aparicoes_letra
    tupla = (letra, frequencia / total_de_caractere) # Vamos colocar em uma tupla, a frequencia divide pelo total de caractere. essa letra teve essa frequencia
    print(tupla) # Quando imprimir vai mostrar quantos porcentos cada letra(caractere) aparece.
print()

# 6° Passo: jogar tudo em uma lista, pois quero pegar os 10 mais frequentes. Então eu posso fazer uma lista.
# Como é que eu faço para criar uma lista de todas essas tuplas? Lembra do list comprehension? Então eu posso pegar isso aqui, que é a minha tupla,
# jogo aqui no meu for, e agora eu tenho uma lista. Agora eu tenho uma lista, isto é, para cada letra "E" frequência, eu crio a tupla e jogo tudo isso em
# uma lista. Então poderia ser assim. Está lá, cada uma delas está calculada. Então eu tenho cada uma delas já em uma lista, só que agora eu queria ordenar pelo lado direito.

# Fazendo uma list comprehension
list_comprehension = [(letra, frequencia / total_de_caractere)for letra, frequencia in quantidade_de_caractere.items()]
print(list_comprehension)
print()

# 7° Passo: Após colocar minha tupla em uma lista atraves do list comprehension, quero ordenar pelo lado direito. Jogo tudo em um dicionario.
# Criando um dicionario:
list_comprehension = dict(list_comprehension)
for x, y in list_comprehension.items():
    print(x, y)
print()

# 8° Passo: Após jogar tudo em um dicionario:  Crio um contador nele e demois impimo utilizando o método most_common() ou seja os mais comuns:
list_comprehension = [(letra, frequencia / total_de_caractere)for letra, frequencia in quantidade_de_caractere.items()]
list_comprehension = Counter(dict(list_comprehension)) # Jogando o dicionario em um contador
print(f'Imprimindo somente os 10 que mais apareceram {list_comprehension.most_common(10)}') # Pedindo pra imprimir os 10 mais comunus ou seja os 10 caracteres que aparecem mais no texto
for x, y in list_comprehension.most_common(10):
    print(x, y)
print()


# 9° Passo: Pego tudo e jogo dentro de uma def:
def analisando_frequencia_de_letras(texto):
    quantidade_de_caractere = Counter(texto.lower())
    total_de_caractere = sum(quantidade_de_caractere.values())

    list_comprehension = [(letra, frequencia / total_de_caractere) for letra, frequencia in quantidade_de_caractere.items()]
    list_comprehension = Counter(dict(list_comprehension))
    mais_comun = list_comprehension.most_common(10)
    for caractere, proporcao in mais_comun:
        print(f'{caractere} -> {proporcao * 100:.2f}%')


analisando_frequencia_de_letras(texto1)
print()
analisando_frequencia_de_letras(texto2)
print()
print()


