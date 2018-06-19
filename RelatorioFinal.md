Nome
Tema
Descrição
Imagens
Descrição clara de como o problema foi resolvido
Resultados

# Colorização de Imagens de Raio-X

**Tema:** Colorização de imagens

## Descrição

 O projeto consiste na colorização de imagens de raio-x. Para isso, as imagens são primeiro tratadas a fim de melhorar sua qualidade e o contraste entre seus elementos significativos. Em seguida, é aplicada uma entre seis formas de colorização, obtendo a imagem final em pseudo cor. 

As imagens utilizadas são de dois tipos: radiografias médicas e scans de segurança de bagagens.
 
## Autores
  Chan Ken Chen (n.USP: 9436170)
  
  Elisa Saltori Trujillo (n.USP: 8551100)
 
## Imagens utilizadas

As imagens utilizadas no projeto, como indicado anteriormente, são de dois tipos distintos: temos imagens raio-x de bagagens e radiografias médicas. Os dois conjuntos de imagens, com sua origem, estão indicados a seguir.

### Imagens raio-X de bagagens 

(disponível em:  http://dmery.ing.puc.cl/index.php/material/gdxray/)

As imagens de bagagens foram obtidas do projeto GDXray (GRIMA X-Ray Database). Elas consistem em imagens em escala de cinza de malas e bolsas escaneadas, contendo objetos potencialmente perigosos em seu interior.

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

As radiografias foram obtidas do National Institutes of Health Chest X-Ray Dataset e consistem em radiografias da região do tórax. Elas possuem um tamanho padrão de 1024x1024 pixels.


 **Exemplos:**

  <p float="left" align="middle">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000132_002.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00003896_005.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/master/Sample_Images/Chest_Xrays/00003989_024.png" height="300">
  </p>
  
[2] Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases. IEEE CVPR 2017, ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf

##Etapas de solução do problema

 Cada imagem, para ser colorizada, passa pelas seguintes etapas:
 - Suavização
 - Realce de bordas
 - Normalização ou equalização
 - Colorização
