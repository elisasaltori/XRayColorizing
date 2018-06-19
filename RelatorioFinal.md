
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
 
 ### Realce de bordas
 
 ### Normalização ou equalização
 
 ### Colorização
 
 ## Resultados
 
 ### Imagens de bagagens
 
 ### Radiografias
