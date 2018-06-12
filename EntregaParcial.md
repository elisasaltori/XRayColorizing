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
Três métodos de suavização foram testados:    
- Filtro de média
- Filtro de mediana
- Filtro gaussiano

#### Filtro de média

### Filtros de realce de bordas
### Métodos de equalização
### Mapeamento de cores

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
