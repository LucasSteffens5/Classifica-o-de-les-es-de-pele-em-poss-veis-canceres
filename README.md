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
<img height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010117.jpg"/><br>
<img height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0010493.jpg"/><br>
 
 #Exemplos de imagens classificadas incorretamente:
 
<img height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011504.jpg"/><br>
<img height="300" src="https://github.com/LucasSteffens5/Classificacao-de-lesoes-de-pele-em-possiveis-canceres/blob/main/ISIC_0011268.jpg"/><br>
