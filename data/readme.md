## Estrutura dos dados

A instância utilizada para a resolução deste modelo de otimização foi fornecida por meio de uma planilha eletrônica, em formato .xlsx.

A fim de manter a confidencialidade dos dados, a planilha original não ser fornecida. Contudo, com o objetivo de dar ao leitor a possibilidade de replicar a aplicação do modelo, forneço, abaixo, um exemplo do input de dados aceito por este modelo de otimização.

## Exemplificação do dataset de entrada

| **Caixa Id** 	| **Item** 	| **Peças** 	|
|:------------:	|:--------:	|:---------:	|
|     9702     	| sku-0001 	|     17    	|
|     0802     	| sku-0001 	|     05    	|
|     0802     	| sku-0002 	|     65    	|
|     0802     	| sku-0003 	|     7     	|
|     0802     	| sku-0004 	|     5     	|

Nota-se que cada caixa pode conter mais de um item(sku), não havendo qualquer tipo de restrição neste sentido. Outro aspecto relevante é que a capacidade das caixas não é objeto de discussão neste modelo de otimização, sendo um parâmetro irrelevante para o processo de modelagem matemática no contexto modelado durante este projeto.