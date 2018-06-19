
# Colorização de Imagens de Raio-X

**Tema:** Colorização de imagens

## Descrição

Imagens de raio-x são usadas para diversas aplicações. Dois de seus principais usos incluem a realização de exames médicos e a checagem do conteúdo de bagagens em aeroportos. Imagens em raio-x são, por sua própria natureza, imagens em escala de cinza, com um único canal gerado pela incidência dos raios-x nos detectores da aparelhagem.

No entanto, sabe-se que a percepção de tons de cinza por humanos é limitada quando comparada à sua capacidade de distinção entre o uso de cores. Sendo assim, a colorização pode ser utilizada para facilitar a distinção de características de interesse nessas imagens, facilitando o trabalho do profissional envolvido.

Nesse projeto, visamos trabalhar com imagens em escala de cinza provenientes de raios-x, mais especificamente, com imagens médicas (como radiografias) e checagem de segurança de bagagens. Nosso objetivo é a colorização dessas imagens.

Para isso, as imagens raio-x são primeiro tratadas a fim de melhorar sua qualidade e o contraste entre seus elementos significativos. Em seguida, é aplicada uma entre seis formas de colorização, obtendo a imagem final em pseudo cor. 
 
## Autores
  Chan Ken Chen (n.USP: 9436170)
  
  Elisa Saltori Trujillo (n.USP: 8551100)
 
## Imagens utilizadas

As imagens utilizadas no projeto, como indicado anteriormente, são de dois tipos distintos: temos imagens raio-x de bagagens e radiografias médicas. Os dois conjuntos de imagens, com sua origem, estão indicados a seguir.

### Imagens raio-X de bagagens 

(disponível em:  http://dmery.ing.puc.cl/index.php/material/gdxray/)

As imagens raio-x de bagagens foram obtidas da GRIMA X-ray Database. Elas consistem em imagens no formato PNG em escala de cinza com resolução variável. Elas apresentam imagens raio-x de bolsas ou malas com objetos em seu interior, com destaque para objetos perigosos, como armas, pregos ou lâminas.  
Segundo a base de dados, essas imagens foram obtidas com a utilização de um detector digital de raio-X (Canon, modelo CXDI-50G), um tubo emissor de raio-x (Poskom, modelo PXM-20BT) e um protetor de chumbo de segurança para isolamento do ambiente de inspeção. 

 **Exemplos:**
 
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0044_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Baggages/B0023_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0011_0001.png" height="300">
 </p>
 
[1] Mery, D.; Riffo, V.; Zscherpel, U.; Mondragón, G.; Lillo, I.; Zuccar, I.; Lobel, H.; Carrasco, M. (2015): GDXray: The database of X-ray images for nondestructive testing. Journal of Nondestructive Evaluation, 34.4:1-12. [ PDF ]

### Radiografias 

(disponível em:  https://www.kaggle.com/nih-chest-xrays/data)

As radiografias foram obtidas do National Institutes of Health Chest X-Ray Dataset e consistem em radiografias da região do tórax. Elas possuem um tamanho padrão de 1024x1024 pixels e estão no formato PNG. As imagens utilizadas no projeto serão retiradas do conjunto amostra disponibilizado do dataset, consistindo em um total 5606 imagens. 

 **Exemplos:**

  <p float="left" align="middle">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000132_002.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00003896_005.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00003989_024.png" height="300">
  </p>
  
[2] Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases. IEEE CVPR 2017, ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf

## Etapas de solução do problema

 Cada imagem, para ser colorizada, passa pelas seguintes etapas:
 - Suavização
 - Realce de bordas
 - Normalização ou equalização
 - Colorização
 
 Cada um desses passos possui, ao menos, dois métodos distintos que podem ser aplicados sobre a imagem. Cada uma dessas etapas será descrita nas seções a seguir.
 
 ### Suavização
 
A suavização da imagem é a primeira etapa no tratamento da imagem de entrada. Seu objetivo é a remoção de ruído, tornando a imagem de saída mais nítida. 

Para esse passo, três métodos foram implementados e testados:
- Filtro de média
- Filtro de mediana
- Filtro gaussiano

#### Filtro de média

Esse filtro consiste simplesmente na média dos valores na vizinhança de um pixel. Ele foi aplicado por ser um método simples e comum de suavização.

No entanto, notamos logo de início os problemas típicos desse filtro: a perda de bordas, com "borramento" da imagem. Logo abaixo, podemos ver um exemplo da aplicação do filtro (aplicado com uma vizinha de tamanho 3x3). À esquerda, temos a imagem original; à direita, a imagem com o filtro aplicado.

 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Smoothing_Filters/average.png" height="300">
 </p>

Esse filtro, logo, não possui um comportamento adequado para a aplicação. A perda de detalhes é excessiva e poderia causar dificuldade na análise da imagem.

#### Filtro de mediana

Para esse filtro, o valor de um pixel é definido pela mediana dos valores encontrados em uma janela de vizinhança determinada em torno do pixel.

Ele apresenta um comportamento mais adequado que o filtro de média, ocasionando menor "borramento" da imagem. Logo abaixo, podemos ver dois exemplos de aplicação do filtro (aplicado com uma vizinha de tamanho 3x3). Em ambos os casos, temos, a esquerda, temos a imagem original; à direita, a imagem com o filtro aplicado.

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

 ### Realce de bordas
A segunda etapa pela qual a imagem passa é o realce de bordas. Essa etapa é opcional, podendo não ser aplicada na obtenção da imagem final. Os filtros de realce de bordas são utilizados para recuperar detalhes que possam ter sido perdidos com a suavização e destacar elementos importantes na imagem.

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
O filtro implementado é o laplaciano. Diferentemente do filtro Sobel, que se trata de um filtro de derivada de primeira ordem, o filtro laplaciano aproxima uma derivada de segunda ordem e, portanto, é mais sensível a ruído. Esse método foi aplicado para comparar sua atuação com o operador anterior.
Foi utilizada uma aproximação 3x3 do filtro para a implementação.
Abaixo, estão os resultados da aplicação do filtro. Temos à esquerda a imagem original, e à direita, o resultado da aplicação do filtro. Ambos os conjuntos de imagens são apresentados já equalizados a fim de facilitar a visualização dos efeitos do operador.

- **Imagem de bagagem:**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/gun_histogram.png" height="300">
 <img src="hhttps://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Sharpening_Filters/new_laplacian.png" height="300">
 </p>
 
 Como pode ser visto, não conseguimos obter um bom resultado com o filtro laplaciano. A imagem de saída possui um excesso de ruído, o que não é observado com a aplicação do operador sobel.

 ### Normalização ou equalização
Como terceira etapa, a imagem passa necessariamente por um método de aumento de contraste. Essa etapa é importante para facilitar a distinção dos elementos da figura.

Há duas opções nessa etapa:
 - Apenas a normalização da imagem
 - Normalização seguida de equalização por histograma
 
 Segundo as características de uma imagem, uma ou a outra abordagem pode ser mais apropriada.

#### Normalização da imagem

Nesse método, temos um simples "alargamento" do contraste, mapeando os valores da imagem de forma que sua menor intensidade seja 0 e sua maior seja 255. A normalização não há nenhum efeito, portanto, se o intervalo original das imagem já for de 0 a 255.

Abaixo, temos um exemplo de aplicação da normalização:

- **Imagem original (esquerda) vs normalização da imagem (direita):**
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Test_Images/Histogram/compare_chest_hist/00000013_026.png_1121_grey.png" height="300">
 </p>

#### Equalização por histograma

A equalização por histograma aumenta o contraste global da imagem, melhor distribuindo suas intensidades. 

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
 
 ### Colorização
 
 Como última etapa do processo, temos a colorização da imagem. Nesse passo, obtemos uma imagem de 3 camadas, correspendentes cada uma a um dos canais RGB.

Nessa etapa, procuramos aplicar uma 
 
 #### Metódo 1: Colorização de bagagem com thresholds fixos
 #### Metódo 2: Colorização de bagagem com thresholds variáveis
 #### Metódo 3: Colorização de bagagem com funções seno
 #### Metódo 4: Colormap Hot 
 #### Método 5: Colormap Inferno
 #### Método 6: Colormap Spectral
 
 ## Resultados
 
 ### Imagens de bagagens
 
 ### Radiografias
