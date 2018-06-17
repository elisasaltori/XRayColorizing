# Projeto Final - Entrega Parcial
**SCC0251 - Processamento de Imagens**

**Prof. Moacir Ponti**

**Integrantes:**

Chan Ken Chen -  9436170

Elisa Saltori Trujillo - 8551100


## Métodos e resultados
Na execução do programa, todas as imagens passam pelas seguintes etapas de processamento:
- Suavização
- Realce de bordas
- Equalização
- Colorização

    Nos itens a seguir, detalharemos o que foi feito em cada uma dessas etapas, apresentando os métodos utilizados e os resultados com eles obtidos.

### Filtros de Suavização

Os filtros de suavização são utilizados a remoção de ruído da imagem.

Três métodos foram testados nessa etapa:    
- Filtro de média
- Filtro de mediana
- Filtro gaussiano

#### Filtro de média

Esse filtro consiste simplesmente na média dos valores na vizinhança de um pixel. Ele foi aplicado por ser um método simples e comum de suavização.

No entanto, notamos logo de cara os problemas típicos desse filtro: a perda de bordas, com "borramento" da imagem. Logo abaixo, podemos ver um exemplo da aplicação do filtro (aplicado com uma vizinha de tamanho 3x3). À esquerda, temos a imagem original; à direita, a imagem com o filtro aplicado.

 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/average.png" height="300">
 </p>

Esse filtro, logo, não possui um comportamento adequado para a aplicação. A perda de detalhes é excessiva e poderia causar dificuldade na análise da imagem.

#### Filtro de mediana

Para esse filtro, o valor de um pixel é definido pela mediana dos valores encontrados em uma janela de vizinhança determinada em torno do pixel.

Ele apresenta um comportomento mais desejado que o filtro de média, ocasionando menor "borramento" da imagem. Logo abaixo, podemos ver dois exemplos de aplicação do filtro (aplicado com uma vizinha de tamanho 3x3). Em ambos os casos, temos, a esquerda, temos a imagem original; à direita, a imagem com o filtro aplicado.

- **Imagem de bagagem:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/median.png" height="300">
 </p>

- **Radiografia:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/chest_median.png" height="300">
 </p>

#### Filtro gaussiano

O filtro gaussiano foi implementado por possuir um comportamento mais uniforme que o filtro de mediana.

Logo abaixo, podemos ver dois exemplos de aplicação do filtro (aplicado com uma vizinha de tamanho 3x3 e desvio padrão de valor 1). Em ambos os casos, temos, a esquerda, temos a imagem original; à direita, a imagem com o filtro aplicado.


- **Imagem de bagagem:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/gaussian_3_1.png" height="300">
 </p>

- **Radiografia:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/chest_gaussian.png" height="300">
 </p>
 
#### Comparação entre métodos

Temos abaixo as três imagens lado a lado: com filtro de média, com mediana e com filtro gaussiano.

 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/average.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/median.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/gaussian_3_1.png" height="300">
 </p>
 
 Como já observado antes, o uso do filtro da média causa uma distorção excessiva na imagem e, portanto, ele não será utilizado nas imagens finais. Já entre os filtros de mediana e gaussiano, o filtro mediana apresenta nos casos-teste uma maior redução de ruído na imagem, com uma distorção suficientemente contida. Por conta disso, ele será utilizado na colorização final da imagem. 


### Filtros de realce de bordas

Os filtros de realce de bordas são importantes para recuperar detalhes que possam ter sido perdidos com a suavização.

Dois métodos foram testados nessa etapa:
- Operador Sobel
- Filtro laplaciano

#### Operador Sobel

O operador sobel foi implementado por possuir um bom resultado na identificação de contornos. Em sua utilização, o operador é aplicado sobre a imagem de entrada e o resultado dessa operação é somado à imagem original.
Abaixo, estão os resultados da aplicação do filtro, com uma vizinhança de 3x3. Temos à esquerda a imagem original, e à direita, o resultado da aplicação do filtro. Ambos os conjuntos de imagens são apresentados já equalizados a fim de facilitar a visualização dos efeitos do operador.

- **Imagem de bagagem:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/gun_histogram.png" height="300">
 <img src="https://raw.githubusercontent.com/elisasaltori/XRayColorizing/master/Test_Images/Sharpening_Filters/sobel_histogram.png" height="300">
 </p>

 - **Radiografia:**
  <p float="left" align="middle">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/chest_histogram.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Sharpening_Filters/sobel_chest.png" height="300">
  </p>
  
  Como visto acima, o operador sobel apresentou um comportamento interessante para a distinção de elementos no raio-x da bagagem, destacando os diversos objetos na mala, que poderá ser útil na composição final da imagem.
  
  Já na imagem da radiografia, percebe-se também um aumento significativo no destaque das bordas. No entanto, foi considerado que a mudança provocada pelo efeito possa prejudicar o diagnóstico médico, uma vez que a imagem final é razoavelmente distinta da original, com a qual os profissionais médicos estão acostumados a trabalhar.

#### Filtro Laplaciano
O filtro implementado é o laplaciano da gaussiana. Diferentemente do filtro Sobel, que se trata de um filtro de derivada de primeira ordem, o filtro laplaciano aproxima uma derivada de segunda ordem e, portanto, é mais sensível a ruído. Esse método foi aplicado para comparar sua atuação com o operador anterior.
Abaixo, estão os resultados da aplicação do filtro, com uma vizinhança de 7x7 e desvio padrão 3. Temos à esquerda a imagem original, e à direita, o resultado da aplicação do filtro. Ambos os conjuntos de imagens são apresentados já equalizados a fim de facilitar a visualização dos efeitos do operador.

- **Imagem de bagagem:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/gun_histogram.png" height="300">
 <img src="https://raw.githubusercontent.com/elisasaltori/XRayColorizing/master/Test_Images/Sharpening_Filters/laplacian_7_3.png" height="300">
 </p>
 
 Como pode ser visto, não conseguimos obter um bom resultado com o filtro laplaciano. A imagem de saída é muito similar a de entrada e possui uma maior quantidade de ruído. A implementação do filtro será verificada para a próxima etapa a procura de possíveis erros.

### Métodos de equalização

Esses métodos visam aumentar o contraste da imagem, facilitando a distinção entre os elementos que a compõem.
Um método foi testado nessa etapa: a equalização por histograma.

#### Equalização por histograma

A equalização por histograma apresentou um comportamento adequado na maioria dos casos, aumentando significativamente o contraste entre os tons intermediários da imagem quando comparada à normalização comum. Abaixo, podemos verificar esse efeito em sua aplicação sobre duas imagens:

- **Normalização da imagem (esquerda) vs equalização por histograma (direita):**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/compare_chest_hist/00000013_026.png_1121_grey.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/compare_chest_hist/00000013_026.png_1122_grey.png" height="300">
 </p>
 
 - **Normalização da imagem (esquerda) vs equalização por histograma (direita):**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/gun_normal.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/gun_histogram.png" height="300">
 </p>
 
 No entanto, verificamos também que a equalização por histograma não funciona bem para todos os casos. Em particular, verificamos que, quando a imagem possui uma grande área de fundo branco, o contraste obtido pela equalização por histograma é distintamente pior que a obtida pela normalização. Isso observado no exemplo abaixo:
 
  - **Normalização da imagem (esquerda) vs equalização por histograma (direita):**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/hist_bad/normal_good.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/hist_bad/histbad.png" height="300">
 </p>

O resultado pode ser dito, inclusive, pior que o da imagem original. 

Portanto, embora o método do histograma tenha bons resultados para a maioria das imagens, devemos ter cuidado ao aplicá-la indiscriminadamente sobre todas. 


### Mapeamento de cores

O mapeamento para cores visa também aumentar a distinção entre os elementos da imagem, uma vez que pode-se distinguir mais tons de cores do que tons de cinza.

Três mapeamentos foram testados nessa etapa:
- Colorização de bagagens
- Hot colormap
- Inferno colormap

Dentre esses, tanto o hot colormap quanto o inferno colormap são funções prontas da biblioteca Matplotlib.

#### Colorização de bagagens

Esse mapeamento é inspirado nos mecanismos utilizados por aeroportos no scan de imagens, como exemplificado em [1]. A função de mapeamento foi feita utilizando o sistema de cores HSV.

Essa colorização utiliza três cores principais de acordo com o material encontrado:
- **Laranja**: materiais orgânicos, de menor densidade.
- **Verde**: materiais plásticos, de densidade média.
- **Azul**: materiais duros, como metal.

Na definição da matiz de um pixel, então, foi considerada que a intensidade de um pixel é inversamente proporcional à densidade do material: um pixel de menor intensidade (mais escuro) representa uma densidade maior e vice versa.

Foram então definidos limites simples inferiores e superiores sobre a intensidade dos pixels para a definição de sua matiz (laranja, verde ou azul):
- **Azul:** 0 a 40 (Matiz = 236/360)
- **Verde:** 41 a 105 (Matiz = 100/360)
- **Laranja:** 106 a 255 (Matiz = 47/360)

Esses valores foram obtidos por observação manual das intensidades de pixel em imagens de bagagem.

Já os canais de saturação e valor foram definidos da seguinte forma:
- **Saturação:** min(2*(255-img)/255.0, 1)
- **Valor:** img/255.0
    
Os canais foram assim definidos para manter pixels brancos (intensidade 255) em seu estado original (com saturação 0 e valor 1) e a fim de dar mais destaque às intensidades médias e baixas na imagem (densidade de material média e alta). 

No entanto, o mapeamento de cores ainda não alcançou completamente os objetivos de colorização. Abaixo temos três exemplos da aplicação do mapamento (os dois últimos com a aplicação do operador sobel):

<p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/test.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/sobel_color1.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/B0011_0001.png_1212.png" height="300">
 </p>

Como pode-se ver acima, a separação de cores funciona razoavelmente bem, principalmente para os elementos de alta densidade, tornando-os todos da cor azul. No entanto, os limites ideais de intensidade utilizados para a definição da matiz variam de acordo com a imagem, e muitos objetos ficam cortados ao meio com duas cores distintas. Também há muitas vezes um comportamento inadequado quanto ao fundo da bagagem, trazendo vários artefatos à colorização.

Sendo assim, buscaremos aperfeiçoar esse método de colorização para a entrega final. O primeiro objetivo será encontrar uma estratégia mais confiável que a divisão por limites de intensidade. 

#### Hot colormap

O hot colormap é um mapa de cores sequencial, utilizando, como seu nome indica, cores quentes, como amarelo e vermelho.

Podemos ver abaixo alguns exemplos de sua aplicação.

-**Bagagem:**
<p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/B0011_0001.png_1222.png" height="300">
 </p>
 
 A imagem acima utiliza o operador sobel e a equalização por histograma.
 
 -**Radiografias:**
<p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000013_026.png_1122.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000013_026.png_1222.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000132_002.png_1121.png" height="300">
 </p>
 
 As três imagens utilizam o filtro de mediana e a equalização por histograma. A primeira e a terceira utilizam o filtro laplaciano, enquanto que a segunda utiliza o operador sobel.

#### Inferno colormap

O inferno colormap é um mapa perceptualmente uniforme, facilitando a distinção de elementos em qualquer ponto de sua escala.

Podemos ver abaixo alguns exemplos de sua aplicação. 

-**Bagagens:**
<p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/B0011_0001.png_1232.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/Color_Bags/B0023_0001.png_2232.png" height="300">
 </p>
 
 Ambas as imagens utilizam o filtro de mediana, o operador sobel e a equalização por histograma.
 
 -**Radiografias:**
<p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000013_026.png_1132.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000013_026.png_1232.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Color_Images/color_chest/00000132_002.png_1131.png" height="300">
 </p>

As três imagens utilizam o filtro de mediana e a equalização por histograma. A primeira e a terceira utilizam o filtro laplaciano, enquanto que a segunda utiliza o operador sobel.

Pode-se observar, tanto no caso das bagagens quanto da radiografia, que o inferno colormap fornece à imagem uma boa distinção entre seus elementos. 

## Próximos passos

- **Verificar funcionamento de filtros já implementados**

    Pela falta de efeito do filtro laplaciano, acreditamos que haja um erro em sua implementação. Procuraremos corrigi-lo a seguir.

- **Aprimorar e testar novos mapeamentos de cores para bagagens**

    Como visto na discussão de resultados, o mapeamento implementado não funciona da forma esperada em todas as ocasiões. Será buscada uma nova estratégia de mapeamento de forma a se aproximar do resultado esperado, uma que não dependa apenas de thresholds sobre a intensidade da imagem.
    Pretende-se, inicialmente, examinar a possibilidade de definição dos thresholds com base na análise do histograma da imagem.
   
- **Testar novos mapeamentos de cores e compará-los**

    Pretendemos apresentar mais testes com mapas de cores para ter uma maior base de comparação entre os resultados obtidos. Esses mapeamentos serão utilizados através da biblioteca Matplotlib.

## Referências

[1] How To Read An Airport Security X-Ray Image. Disponível em: < http://snallabolaget.com/how-to-read-an-airport-security-x-ray-image/ >. Acesso em: 12 jun. 2018.
