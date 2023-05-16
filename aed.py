import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

rotulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
cores = ['red', 'orange', 'yellow', 'blue', 'purple']

anos = np.arange(start=1990, stop=2022)

industria = [165748, 173335, 119602, 137954, 133632, 129840, 147873, 172890, 202909, 229719, 250739, 241367, 233223, 224842, 231643, 232446, 233655, 252360, 281970, 240522, 261072, 292761, 282678, 277978, 229953, 240178, 230826, 201378, 123435, 136023, 234305, 175275]
residuos = [443991, 466103, 498166, 529223, 564878, 604413, 647357, 694326, 745910, 802362, 868364, 943232, 1046692, 1178731, 1231369, 1271401, 1341265, 1474938, 1751928, 1870073, 1990357, 2001427, 1584782, 1701111, 1689370, 1743752, 1906731, 1852917, 1901295, 1890875, 1929675, 1938633]
energia = [1658841, 2139581, 2748061, 2127341, 2280753, 3067810, 3236794, 3749342, 5011432, 4530191, 4476912, 4834213, 5174105, 5246602, 6044931, 6705587, 6899836, 7793635, 7987983, 7943082, 9491642, 8690559, 8981528, 7933636, 10053720, 9052963, 7601955, 6871618, 8732482, 9315481, 8817008, 8750817]
agropecuaria = [1695250, 1717488, 1691897, 1824539, 1971429, 2117797, 1883953, 1984823, 2102121, 2169370, 2212781, 2276678, 2325104, 2798041, 2870780, 2965834, 3038900, 2773589, 3035828, 3123784, 3165481, 3297551, 3323456, 3343939, 3216791, 2988903, 3052084, 3123103, 3203261, 3361296, 3330574, 3508736]
mutf = [17997441, 20742183, 35379107, 35767011, 33234297, 38719384, 44443642, 67801401, 70949798, 40609582, 39656855, 31037525, 44898980, 76654850, 64953345, 69580132, 62746189, 43690816, 34959052, 37494546, 46813828, 29663960, 34169836, 47845600, 44143001, 70593534, 108383808, 64540122, 65635103, 105183535, 127373987, 124471910]
total = [21961271, 25238690, 40436833, 40386068, 38184989, 44639244, 50359619, 74402782, 79012169, 48341223, 47465651, 39333015, 53678103, 86103066, 75332067, 80755401, 74259844, 55985338, 48016762, 50672007, 61722380, 43946258, 48342280, 61102264, 59332835, 84619330, 121175403, 76589138, 79595577, 119887210, 141685548, 138845371]

dataIndustria = {
    'anos' : anos,
    'industria' : industria,
}

dataResiduos = {
    'anos' : anos,
    'residuos' : residuos,
}

dataEnergia = {
    'anos' : anos,
    'energia': energia,
}

dataAgropecuaria = {
    'anos' : anos,
    'agropecuaria' : agropecuaria, 
}

dataMutf = {
    'anos' : anos,
    'mutf' : mutf, 
}

dataTotal = {
    'anos' : anos,
    'total' : total, 
}

data = {
    'anos' : anos,
    'industria' : industria,
    'residuos' : residuos,
    'energia': energia,
    'agropecuaria' : agropecuaria, 
    'mutf' : mutf, 
    'total' : total, 
}

df = pd.DataFrame(data,  
                  columns=["anos", 
                           "industria", 
                           "residuos", 
                           "energia", 
                           "agropecuaria", 
                           "mutf", 
                           "total"])


dfIndustria = pd.DataFrame(dataIndustria, columns=["anos", "industria"])
dfResiduos = pd.DataFrame(dataResiduos, columns=["anos", "residuos"])
dfEnergia = pd.DataFrame(dataEnergia, columns=["anos", "energia"])
dfAgropecuaria = pd.DataFrame(dataAgropecuaria, columns=["anos", "agropecuaria"])
dfMutf = pd.DataFrame(dataMutf, columns=["anos", "mutf"])
dfTotal = pd.DataFrame(dataTotal, columns=["anos", "total"])

# Visualizar as primeiras linhas do DataFrame
df.head()

# Resumo estatístico dos dados
print(df.describe())

#print(df.std())
print("\nMediana")
print(df.median())
print("\nAssimetria")
print(df.skew())
print("\nCurtose")
print(df.kurtosis())

def grafico_boxplot(serie, titulo):

    # Criação do gráfico boxplot usando Matplotlib
    plt.boxplot(serie)

    # Configurações adicionais do gráfico
    plt.xlabel('Anos')
    plt.ylabel('toneladas')
    plt.title(titulo)

    # Exibição do gráfico
    plt.show()

def grafico_boxplot_Y(serie, titulo):

    # Criação do gráfico boxplot usando Matplotlib
    fig, ax = plt.subplots()
    boxplot = ax.boxplot(serie)

    # Definindo o número de casas decimais no eixo Y
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Exibindo 2 casas decimais

    # Configurações adicionais do gráfico
    ax.set_xlabel('Variável')
    ax.set_ylabel('Valores')
    ax.set_title(titulo)

    # Exibição do gráfico
    plt.show()

def grafico_linha(x, y, titulo):
    # Criação do gráfico de linha
    plt.plot(x, y)

    # Configurações adicionais do gráfico
    plt.xlabel('Anos')
    plt.ylabel('Toneladas')
    plt.title(titulo)

    # Exibição do gráfico
    plt.show()

def grafico_pizza(serie):
    # Criar figura e eixos
    fig, ax = plt.subplots()

    # Criar um gráfico de pizza
    ax.pie(serie, labels=rotulos, colors=cores, autopct='%1.1f%%')

    # Adicionar título
    ax.set_title('Distribuição das Frutas')

    # Mostrar o gráfico plotado
    plt.show()

tamanho = []
tamanho.append(sum(industria))
tamanho.append(sum(residuos))
tamanho.append(sum(energia))
tamanho.append(sum(agropecuaria))
tamanho.append(sum(mutf))
tamanho.append(sum(total))

print(tamanho)

grafico_pizza(tamanho)

#print(dfIndustria)

grafico_linha(anos, industria, "Processos industriais")

grafico_boxplot(industria, "Processos industriais")
grafico_boxplot(residuos, "Tratamento de resíduos")
grafico_boxplot(energia, "Energia")
grafico_boxplot(agropecuaria, "Agropecuaria")
grafico_boxplot(mutf, "MUTF")
grafico_boxplot(total, "Emissões totais")