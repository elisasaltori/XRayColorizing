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
 
 Como pode ser visto, não conseguimos obter um bom resultado com o filtro laplaciano. A imagem de saída é muito similar a de entrada e possui uma maior quantidade de ruído. O funcionamento do filtro será verificado para a próxima etapa.

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

Portanto, embora o método do histograma tenha bons resultados para a maioria das imagens, devemos ter cuidado ao aplicá-la sobre todas. Pretendemos, na próxima etapa, buscar um método de equalização adaptativa com histogramas para tentar corrigir os mals casos da equalização por histograma comum.


### Mapeamento de cores

O mapeamento para cores visa também aumentar a distinção entre os elementos da imagem, uma vez que pode-se distinguir mais tons de cores do que tons de cinza.


## Próximos passos
- **Aprimorar mapeamento de cores para bagagens**

    Como visto na discussão de resultados, o mapeamento implementado não funciona da forma esperada em todas as ocasiões. Será buscada uma nova estratégia de mapeamento de forma a se aproximar do resultado esperado, uma que não dependa apenas de thresholds sobre a intensidade da imagem.
    Pretende-se, inicialmente, testar a técnica baseada em cossenos descrita em [1].

- **Implementação do Equalização por Histograma Adaptativo**

    Para os casos em que a equalização por histograma comum não funciona bem, como em imagens com grandes fundos brancos, pretendemos aplicar um método de histograma adaptativo. Nós esperamos que isso aumente o contraste dos elementos da imagem final.

- **Testar novos mapeamentos de cores**

    Pretendemos apresentar mais testes com mapas de cores para ter uma maior base de comparação entre os resultados obtidos. Esses mapeamentos serão utilizados através da biblioteca Matplotlib.

## Referências

[1]  KASE, Kannan. Effective Use of Color in X-ray Image Enhancement for
Luggage Inspection. 2002. 30f. Dissertação de Mestrado - University of Tennessee, Knoxville, 2002.
