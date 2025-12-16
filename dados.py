# dados.py - LOTE 1 (01-35)

database = {
    # --- LÍDERES & GUERREIROS ---
    "Napoleão Bonaparte": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Líder Militar", "Morte": 1821,
        "Dicas": [
            "Nasci em uma ilha no Mediterrâneo, falava com sotaque, mas tornei-me o maior símbolo da França. Minha ascensão nasceu do caos de uma revolução.",
            "Não me contentei em ser general; coroei a mim mesmo Imperador. Criei um Código Civil que influencia leis até hoje e fiz a Europa tremer com minha artilharia.",
            "Minha ambição encontrou seu fim no inverno russo e na batalha de Waterloo. Morri exilado na remota Santa Helena, sozinho e vigiado."
        ]
    },
    "Júlio César": {
        "Era": "Antiga", "Continente": "Europa", "Função": "Líder Militar", "Morte": -44,
        "Dicas": [
            "Minha família alegava descender de Vênus. Fui sequestrado por piratas e prometi crucificá-los — e cumpri. A Gália inteira curvou-se perante minhas legiões.",
            "Desafiei o Senado ao atravessar o rio Rubicão, dizendo 'A sorte está lançada'. Deixei de ser apenas um cônsul para me tornar o Ditador Perpétuo de Roma.",
            "Não temi os idos de março, mas deveria. Fui traído por aqueles que perdoei, caindo sob 23 facadas aos pés da estátua de meu rival Pompeu."
        ]
    },
    "Genghis Khan": {
        "Era": "Medieval", "Continente": "Ásia", "Função": "Líder Militar", "Morte": 1227,
        "Dicas": [
            "Fui um pária na minha juventude, caçado nas estepes geladas. Jurei unir as tribos nômades sob um único arco e flecha.",
            "Criei o maior império em extensão contínua da história. Minha tática de 'retirada falsa' enganou exércitos inteiros, da China à Europa Oriental.",
            "Dizem que onde meu cavalo passava, a grama não crescia mais. Meu túmulo é um segredo tão bem guardado que até hoje ninguém o encontrou."
        ]
    },
    "Alexandre, o Grande": {
        "Era": "Antiga", "Continente": "Europa", "Função": "Líder Militar", "Morte": -323,
        "Dicas": [
            "Fui aluno de Aristóteles e dormia com a Ilíada sob o travesseiro. Aos 20 anos, herdei um reino; aos 30, era dono do mundo conhecido.",
            "Desatei o Nó Górdio com minha espada. Levei a cultura helênica até as margens do rio Indo, fundando dezenas de cidades com meu nome.",
            "Nunca perdi uma batalha, mas fui derrotado por uma febre na Babilônia. Ao morrer, disse que deixava meu império 'ao mais forte'."
        ]
    },
    "Joana d'Arc": {
        "Era": "Medieval", "Continente": "Europa", "Função": "Líder Militar", "Morte": 1431,
        "Dicas": [
            "Eu era apenas uma camponesa analfabeta, mas vozes celestiais me disseram que eu libertaria a França dos ingleses.",
            "Cortei meu cabelo, vesti armadura masculina e guiei soldados veteranos. Levantei o cerco de Orléans e levei o Delfim à sua coroação.",
            "Fui capturada, julgada como herege e bruxa. Minha recompensa foi a fogueira, onde gritei por Jesus enquanto as chamas me consumiam."
        ]
    },
    "Saladino": {
        "Era": "Medieval", "Continente": "Ásia", "Função": "Líder Militar", "Morte": 1193,
        "Dicas": [
            "Unifiquei o Egito e a Síria sob a bandeira do Islã. Fui o grande oponente dos Cruzados, mas sempre respeitado por minha nobreza e cavalheirismo.",
            "Retomei Jerusalém para os muçulmanos, mas permiti que os cristãos partissem em paz, ao contrário do massacre que fizeram anos antes.",
            "Troquei presentes e médicos com Ricardo Coração de Leão. Morri com pouco dinheiro, pois doei quase tudo aos pobres."
        ]
    },

    # --- MONARCAS & POLÍTICOS ---
    "Cleópatra": {
        "Era": "Antiga", "Continente": "África", "Função": "Monarca", "Morte": -30,
        "Dicas": [
            "Fui a última faraó ativa do Egito Ptolomaico. Diferente dos meus antecessores, aprendi a falar a língua do povo egípcio.",
            "Para proteger meu trono, aliei-me aos homens mais poderosos de Roma. Cheguei até César enrolada em um tapete e tive gêmeos com Marco Antônio.",
            "Com a derrota naval em Áccio e a invasão de Otaviano, escolhi o fim pela picada de uma serpente a ser exibida como troféu em Roma."
        ]
    },
    "Dom Pedro II": {
        "Era": "Moderna", "Continente": "América do Sul", "Função": "Monarca", "Morte": 1891,
        "Dicas": [
            "Tornei-me imperador ainda criança, o 'menino' de uma nação continental. Governei por quase 50 anos, preferindo os livros aos bailes.",
            "Fui um monarca cidadão, patrono das ciências e artes. Viajei o mundo, conheci Graham Bell e Nietzsche, mas vi meu trono cair num golpe militar sem sangue.",
            "Exilado na Europa, levei comigo um travesseiro cheio de terra do meu país. Morri em Paris, sonhando com as palmeiras do Brasil."
        ]
    },
    "Rainha Vitória": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Monarca", "Morte": 1901,
        "Dicas": [
            "Assumi o trono aos 18 anos. Sob meu reinado, o Império Britânico expandiu-se até que 'o sol nunca se punha' em meus domínios.",
            "Casei-me com meu primo Albert, um amor intenso. Sua morte precoce me fez vestir preto e viver em luto pelo resto das minhas longas décadas de vida.",
            "Dei nome a uma Era marcada pela rigidez moral e revolução industrial. Fui a 'Avó da Europa', com descendentes em quase todos os tronos."
        ]
    },
    "Abraham Lincoln": {
        "Era": "Moderna", "Continente": "América do Norte", "Função": "Político", "Morte": 1865,
        "Dicas": [
            "Nascido numa cabana de troncos, autodidata e lenhador. Tornei-me advogado e cheguei à Casa Branca com o país à beira do abismo.",
            "Liderei a União durante a sangrenta Guerra Civil. Minha Proclamação de Emancipação foi o passo decisivo para o fim da escravidão.",
            "Cinco dias após o fim da guerra, fui ao teatro Ford. O tiro de John Wilkes Booth me tornou o primeiro presidente americano assassinado."
        ]
    },
    "Nelson Mandela": {
        "Era": "Contemporânea", "Continente": "África", "Função": "Político", "Morte": 2013,
        "Dicas": [
            "Fui um advogado e boxeador amador que lutou contra o Apartheid. Fui classificado como terrorista e passei 27 anos na prisão.",
            "Na Ilha Robben, quebrava pedras mas não quebrei meu espírito. Saí da prisão para pregar a reconciliação, não a vingança.",
            "Tornei-me o primeiro presidente negro da África do Sul e ganhei o Nobel da Paz. Meu sorriso e camisas coloridas tornaram-se símbolos de esperança."
        ]
    },
    "Getúlio Vargas": {
        "Era": "Contemporânea", "Continente": "América do Sul", "Função": "Político", "Morte": 1954,
        "Dicas": [
            "Do pampa gaúcho marchei para o Rio de Janeiro. Liderei a Revolução de 30 e governei o Brasil por 15 anos consecutivos, ora como ditador, ora não.",
            "Fui o 'Pai dos Pobres', criando a CLT e a Petrobras, mas também flertei com o autoritarismo no Estado Novo.",
            "Pressionado pelos militares e opositores, cumpri minha promessa no Palácio do Catete: 'Saio da vida para entrar na história'."
        ]
    },
    "Winston Churchill": {
        "Era": "Contemporânea", "Continente": "Europa", "Função": "Político", "Morte": 1965,
        "Dicas": [
            "Fui soldado, jornalista e prisioneiro de guerra antes da política. Gaguejava, bebia muito e fumava charutos o dia todo.",
            "Quando a Europa caiu perante o nazismo, fui a única voz a dizer 'jamais nos renderemos'. Prometi apenas sangue, suor e lágrimas.",
            "Venci a guerra, mas perdi a eleição seguinte. Ganhei o Nobel de Literatura por minhas memórias históricas."
        ]
    },

    # --- RELIGIÃO & PENSAMENTO ---
    "Jesus Cristo": {
        "Era": "Antiga", "Continente": "Ásia", "Função": "Líder Religioso", "Morte": 33,
        "Dicas": [
            "Nasci em um estábulo na periferia do Império Romano. Trabalhei com madeira até os 30 anos, quando comecei a andar sobre as águas e curar enfermos.",
            "Expulsei vendilhões do templo e desafiei os fariseus. Não deixei nada escrito, mas meus sermões sobre amor e perdão mudaram o mundo.",
            "Traído por um beijo e trocado por um assassino. Na cruz, pedi perdão pelos meus algozes. Para bilhões, venci a morte ao terceiro dia."
        ]
    },
    "Buda (Siddhartha Gautama)": {
        "Era": "Antiga", "Continente": "Ásia", "Função": "Líder Religioso", "Morte": -483,
        "Dicas": [
            "Vivi protegido em um palácio, cercado de luxo. Ao sair, vi um velho, um doente e um cadáver, e entendi que a vida é sofrimento.",
            "Abandonei minha herança real e minha família para viver como asceta. Sob a árvore Bodhi, encontrei o 'Caminho do Meio' e a Iluminação.",
            "Não me considerei um deus, apenas o 'Desperto'. Ensinei o desapego e o Nirvana até meus 80 anos."
        ]
    },
    "Sócrates": {
        "Era": "Antiga", "Continente": "Europa", "Função": "Filósofo", "Morte": -399,
        "Dicas": [
            "Andava descalço pelas ruas de Atenas, incomodando as pessoas com perguntas. Minha mãe era parteira, e eu dizia fazer o parto das ideias.",
            "Nunca escrevi uma linha sequer; tudo que sabem de mim veio do meu aluno Platão. O Oráculo disse que eu era o mais sábio, pois eu sabia que nada sabia.",
            "Acusado de corromper a juventude, recusei a fuga ou o exílio. Bebi o cálice de cicuta discutindo a imortalidade da alma até o fim."
        ]
    },
    "Mahatma Gandhi": {
        "Era": "Contemporânea", "Continente": "Ásia", "Função": "Líder Político", "Morte": 1948,
        "Dicas": [
            "Advogado formado em Londres, comecei minha luta contra a discriminação na África do Sul. Voltei à Índia para desafiar o Império Britânico.",
            "Minhas armas eram o jejum, a roca de fiar e a desobediência civil. Liderei a Marcha do Sal e provei que a não-violência (Ahimsa) é poderosa.",
            "Conquistei a independência do meu país, mas sofri com a partição religiosa. Fui assassinado por um radical hindu enquanto ia orar."
        ]
    },
    "Martin Luther King Jr.": {
        "Era": "Contemporânea", "Continente": "América do Norte", "Função": "Ativista", "Morte": 1968,
        "Dicas": [
            "Pastor batista inspirado por Gandhi. Liderei o boicote aos ônibus de Montgomery depois que Rosa Parks se recusou a levantar.",
            "No degrau do Lincoln Memorial, contei ao mundo o meu sonho: que meus filhos não fossem julgados pela cor de sua pele.",
            "Fui o homem mais jovem a ganhar o Nobel da Paz. Em Memphis, uma bala de rifle silenciou minha voz, mas não o meu movimento."
        ]
    },

    # --- CIÊNCIA & INVENÇÃO ---
    "Albert Einstein": {
        "Era": "Contemporânea", "Continente": "Europa", "Função": "Cientista", "Morte": 1955,
        "Dicas": [
            "Trabalhava num escritório de patentes quando publiquei quatro artigos que mudaram a física. Provei que o tempo não é absoluto.",
            "Minha fórmula E=mc² explicou a energia das estrelas e da bomba. Tive que fugir da Alemanha nazista por ser judeu.",
            "Recusei a presidência de Israel. Minha foto mostrando a língua é mais famosa que minhas teorias. Meu cérebro foi roubado após minha morte."
        ]
    },
    "Santos Dumont": {
        "Era": "Contemporânea", "Continente": "América do Sul", "Função": "Inventor", "Morte": 1932,
        "Dicas": [
            "Filho do rei do café, fui a Paris gastar minha herança com balões. Contornei a Torre Eiffel de dirigível e ganhei o prêmio Deutsch.",
            "Com o 14-Bis, fiz o primeiro voo homologado de um 'mais pesado que o ar', decolando sem catapultas diante de uma multidão.",
            "Popularizei o relógio de pulso. Deprimido ao ver o avião usado como arma de guerra e com a esclerose múltipla, tirei minha própria vida."
        ]
    },
    "Leonardo da Vinci": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Artista", "Morte": 1519,
        "Dicas": [
            "Filho ilegítimo, tornei-me o arquétipo do homem renascentista. Dissecava cadáveres para desenhar músculos perfeitos.",
            "Projetei tanques, helicópteros e paraquedas séculos antes de existirem. Servia a duques tanto como pintor quanto como engenheiro militar.",
            "Pintei a Última Ceia e o sorriso mais enigmático do mundo, a Mona Lisa. Morri na França, nos braços do rei Francisco I."
        ]
    },
    "Marie Curie": {
        "Era": "Contemporânea", "Continente": "Europa", "Função": "Cientista", "Morte": 1934,
        "Dicas": [
            "Polonesa, tive que estudar numa universidade clandestina. Em Paris, com meu marido, isolei novos elementos em um barracão precário.",
            "Fui a primeira mulher a ganhar um Nobel, e a única pessoa a ganhar em Física e Química. Cunhei o termo 'radioatividade'.",
            "Meus cadernos de anotações ainda são perigosos de tocar. A exposição prolongada ao rádio que descobri causou a anemia que me matou."
        ]
    },
    "Isaac Newton": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Cientista", "Morte": 1727,
        "Dicas": [
            "Nasci prematuro e pequeno. Durante uma praga, isolei-me e desenvolvi o cálculo e a teoria das cores.",
            "Dizem que uma maçã me inspirou, mas foi a matemática que usou para descrever a gravidade universal. Escrevi os 'Principia'.",
            "Fui presidente da Royal Society e caçador de falsificadores de moedas. Passei meus últimos anos mais obcecado com alquimia e profecias bíblicas que com física."
        ]
    },

    # --- ARTISTAS & MÚSICOS ---
    "Beethoven": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Artista", "Morte": 1827,
        "Dicas": [
            "Tive uma infância dura com um pai alcoólatra. Fui o gigante que fez a transição do Classicismo para o Romantismo na música.",
            "O destino bateu à minha porta: comecei a perder a audição. Pensei em suicídio, mas decidi viver pela minha arte.",
            "Regi a estreia da minha Nona Sinfonia totalmente surdo, precisando ser virado para ver os aplausos. O 'Hino à Alegria' é meu legado."
        ]
    },
    "Tupac Shakur": {
        "Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1996,
        "Dicas": [
            "Filho de Panteras Negras, cresci cercado de revolução e pobreza. Estudei balé e Shakespeare antes de pegar o microfone.",
            "Tatuagem 'Thug Life' na barriga, poesia na alma. Fui a voz do gueto nos anos 90, misturando gangsta rap com crítica social.",
            "Sobrevivi a cinco tiros em 94, mas o drive-by em Las Vegas foi fatal. Minha morte ainda gera teorias de que estou vivo em Cuba."
        ]
    },
    "Elvis Presley": {
        "Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1977,
        "Dicas": [
            "Caminhoneiro de Memphis que entrou num estúdio para gravar um disco para a mãe. Misturei o blues negro com o country branco.",
            "Meu rebolado foi censurado na TV. Fui o Rei do Rock, causei histeria mundial e servi no exército no auge da fama.",
            "Os macacões brancos com lantejoulas marcaram minha fase final em Las Vegas. Morri cedo, em Graceland, mas dizem que o Rei nunca perde a majestade."
        ]
    },
    "Marilyn Monroe": {
        "Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1962,
        "Dicas": [
            "Nasci Norma Jeane, morena e órfã de pai vivo. Tingi o cabelo de loiro platina e tornei-me o maior sex symbol do século XX.",
            "A cena do meu vestido branco voando sobre o metrô é icônica. Cantei 'Happy Birthday' para o presidente Kennedy de um jeito inesquecível.",
            "Por trás do glamour, sofria com a solidão e abusos. Fui encontrada morta com o telefone na mão, vítima de overdose, aos 36 anos."
        ]
    },
    "Van Gogh": {
        "Era": "Moderna", "Continente": "Europa", "Função": "Artista", "Morte": 1890,
        "Dicas": [
            "Fracassei como pastor e vendedor de arte antes de pegar os pincéis. Em vida, vendi apenas um quadro, 'O Vinhedo Vermelho'.",
            "Minha amizade com Gauguin acabou em briga e com minha orelha cortada. Pintei a 'Noite Estrelada' olhando da janela de um asilo.",
            "A tragédia da minha mente perturbada culminou em um tiro no peito em um campo de trigo. Morri nos braços do meu irmão Theo."
        ]
    },
    "Frida Kahlo": {
        "Era": "Contemporânea", "Continente": "América do Norte", "Função": "Artista", "Morte": 1954,
        "Dicas": [
            "Aos 18 anos, um bonde colidiu com o ônibus onde eu estava. Passei a vida pintando em camas de hospital e usando coletes de gesso.",
            "Minha obra é um diário de dor e cores vibrantes do México. Casei-me com Diego Rivera, um amor 'de elefante e pomba'.",
            "Minhas sobrancelhas unidas e flores no cabelo são minha marca. Minha última pintura mostra melancias com a frase: 'Viva la Vida'."
        ]
    },
    "Machado de Assis": {
        "Era": "Moderna", "Continente": "América do Sul", "Função": "Escritor", "Morte": 1908,
        "Dicas": [
            "Neto de escravos, nasci no Morro do Livramento, gago e epilético. Aprendi francês na padaria e tornei-me o maior nome da literatura nacional.",
            "Fundei a Academia Brasileira de Letras. Com ironia fina, escrevi 'Memórias Póstumas de Brás Cubas', dedicado ao verme que roeria minha carne.",
            "Criei Capitu e seus olhos de cigana oblíqua e dissimulada, deixando ao leitor a eterna dúvida: traiu ou não traiu Bentinho?"
        ]
    },

    # --- ATLETAS & HERÓIS ---
    "Pelé": {
        "Era": "Contemporânea", "Continente": "América do Sul", "Função": "Atleta", "Morte": 2022,
        "Dicas": [
            "Garoto de Três Corações que prometeu ao pai ganhar uma Copa após vê-lo chorar em 1950. Cumpri a promessa aos 17 anos.",
            "Fiz o mundo parar para me ver jogar. Marquei mais de mil gols e venci três Copas do Mundo, feito inigualável.",
            "Fui Ministro do Esporte e parei uma guerra na Nigéria. Sou o eterno Camisa 10, o Rei do Futebol."
        ]
    },
    "Ayrton Senna": {
        "Era": "Contemporânea", "Continente": "América do Sul", "Função": "Atleta", "Morte": 1994,
        "Dicas": [
            "Comecei no kart e logo fui para a Europa. Na chuva, eu não tinha rivais. Minha rivalidade com Prost dividiu a Fórmula 1.",
            "Venci três campeonatos mundiais. Eu não corria apenas para vencer, corria para sentir Deus. Levava a bandeira do Brasil no cockpit.",
            "A curva Tamburello, em Ímola, silenciou meu motor num domingo de maio. O Brasil inteiro chorou no meu cortejo."
        ]
    },
    "Tiradentes": {
        "Era": "Moderna", "Continente": "América do Sul", "Função": "Ativista", "Morte": 1792,
        "Dicas": [
            "Fui dentista prático, tropeiro e alferes. Indignei-me com a 'Derrama' e os impostos abusivos da Coroa Portuguesa sobre o ouro.",
            "Participei da Inconfidência Mineira, sonhando com uma república livre. Quando o movimento foi traído, fui o único a assumir a responsabilidade.",
            "Enforcado e esquartejado, minhas partes foram expostas na estrada para Vila Rica. Tornei-me o mártir da independência brasileira."
        ]
    },
    "Anita Garibaldi": {
        "Era": "Moderna", "Continente": "América do Sul", "Função": "Revolucionária", "Morte": 1849,
        "Dicas": [
            "Catarinense de Laguna, abandonei um casamento forçado para seguir um guerrilheiro italiano. Lutei na Revolução Farroupilha.",
            "Grávida, combati em batalhas navais e terrestres no Brasil, Uruguai e Itália. Fui chamada de 'Heroína de Dois Mundos'.",
            "Morri na Itália, fugindo de exércitos inimigos, doente e carregada nos braços do meu amor, Giuseppe."
        ]
    },
    "Zumbi dos Palmares": {
        "Era": "Moderna", "Continente": "América do Sul", "Função": "Líder Militar", "Morte": 1695,
        "Dicas": [
            "Nasci livre, fui capturado e educado por um padre, mas fugi para retornar ao meu povo. Tornei-me o líder do maior quilombo das Américas.",
            "Resisti aos ataques portugueses e holandeses por anos, defendendo a Serra da Barriga. Não aceitei a paz que mantinha outros escravizados.",
            "Traído, fui degolado em 20 de novembro. Minha cabeça foi exposta em Recife para provar que eu não era imortal, mas minha lenda vive."
        ]
    }
}
