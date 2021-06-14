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


#Exemplos de imagens classificadas corretamente:
<br>
<img  width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010117.jpg"/>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010493.jpg"/><br>
<br>

 #Exemplos de imagens classificadas incorretamente:
<br>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011504.jpg"/>
<img width="300" height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011268.jpg"/><br>


No arquivo ImagensDeExemploParaClassificacao.rar pode ser encontrado mais imagens que foram classificadas por este algoritmo.
