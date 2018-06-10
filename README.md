# Colorização de Imagens de Raio-X

**Tema:** Colorização de imagens

## Descrição

 Tratamento e colorização de imagens raio-x em escala de cinza a fim de melhorar sua visualização. As imagens utilizadas serão tanto de origem médica (radiografias) quanto scans de bagagens para segurança.
 
## Autores
  Chan Ken Chen (n.USP: 9436170)
  
  Elisa Saltori Trujillo (n.USP: 8551100)
 
## Imagens utilizadas

### Imagens raio-X de bagagens 

(disponível em:  http://dmery.ing.puc.cl/index.php/material/gdxray/)

 **Exemplos:**
 
 <p float="left" align="middle">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Baggages/B0009_0001.png" height="300">
 <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Baggages/B0023_0001.png" height="300">
 </p>
 
[1] Mery, D.; Riffo, V.; Zscherpel, U.; Mondragón, G.; Lillo, I.; Zuccar, I.; Lobel, H.; Carrasco, M. (2015): GDXray: The database of X-ray images for nondestructive testing. Journal of Nondestructive Evaluation, 34.4:1-12. [ PDF ]

### Radiografias 

(disponível em:  https://www.kaggle.com/nih-chest-xrays/data)

 **Exemplos:**

  <p float="left" align="middle">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000013_026.png" height="300">
  <img src="https://github.com/elisasaltori/XRayColorizing/raw/elisa/Sample_Images/Chest_Xrays/00000132_002.png" height="300">
  </p>
[2] Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases. IEEE CVPR 2017, ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf

## Métodos
 As imagens de raio-X passarão por uma combinação de filtros e métodos para remoção de ruído e aumento da nitidez. Pretende-se testar múltiplos métodos de forma a determinar quais apresentam os melhores resultados para cada tipo de imagem (radiografia ou raio-x de bagagem).

Depois de tratadas, essas imagens serão então colorizadas. Várias opções de mapeamento de cores serão exploradas a fim de avaliar os melhores resultados, assim como feita na etapa anterior.

### Filtros de suavização
Esses filtros serão utilizados para a remoção de ruído das imagens de entrada. 

Inicialmente, pretende-se utilizar os seguintes métodos:
- Filtro de média
- Filtro de mediana
- Filtro gaussiano

### Filtros de realce de bordas
Esses filtros serão utilizados a fim de tornas as bordas mais nitidas, facilitando a distinção entre objetos distintos. Eles também têm como função reverter qualquer suavização excessiva sobre bordas que tenha sido causada pelos filtros de suavização.

Inicialmente, pretende-se utilizar os seguintes métodos:
- Filtro laplaciano
- Operador Sobel

### Equalização da imagem
Esses métodos serão utilizados para aumentar o contraste final da imagem.

Inicialmente, pretende-se utilizar os seguintes métodos:
- Normalização comum da imagem
- Equalização por histograma

### Mapeamento para cores
No momento, três mapeamentos de cores distintos estão em uso:
- Mapa para colorização de bagagens
- Hot colormap
- Inferno colormap
