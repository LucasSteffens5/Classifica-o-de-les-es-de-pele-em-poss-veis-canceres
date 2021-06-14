# Classificação de lesões de pele em possiveis cânceres
Utilizando transferência de aprendizado e um classificador SVM foi criado um modelo para classificação de lesões de pele em malignas e benignas.

- Para utilizar os códigos basta criar um diretório para os dados com o seguinte formato:
```
---- BaseDeDados
          |
          ------- train
          |          |
          |           -------- benign
          |          |
          |           -------- malignant
          ------- val
          |         |
          |          -------- benign
          |         |
          |          -------- malignant
          ------- test
                    |
                     -------- benign
                    |
                     -------- malignant
  ```  
  No aquivo ExemploDiretorio.rar há um exemplo da estrutura do diretório.
  
Atualize os endereços do diretório para os do diretorio da sua máquina, nos dois arquivos disponibilizados.




A fonte de dados é a  <a href="https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery">ISIC</a>, que foi baixada via API disponibilizada juntamento com os arquivos de anotações de cada imagem.

As duplicatas e imagens que continha obstruções foram removidas, o desbalancemanto entre as classes malignas e benignas foi resolvido utilizando o algoritmo SMOTE Borderline, onde apenas a base de treinamento foi reamostrada.

A tranferência de aprendizado foi realizada utilizando a rede <a href="https://keras.io/api/applications/xception/">Xception</a>.

A camada totalmente conectada original foi removidas e os vetores de saída serviram de entrada para um classificador SVM Linear.
Foi obtido os seguintes resultados:


# Resultado para a rede Xception.

<br>
<img src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ercasxception.png"/><br>

Onde a base de teste antingiu uma acurácia de 80,15%.



# Exemplos de imagens classificadas corretamente:
<br>
<img  width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010117.jpg"/>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010493.jpg"/><br>
<br>

 # Exemplos de imagens classificadas incorretamente:
<br>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011504.jpg"/>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011268.jpg"/><br>


No arquivo ImagensDeExemploParaClassificacao.rar pode ser encontrado mais imagens que foram classificadas por este algoritmo.

