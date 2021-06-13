import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import Xception, InceptionResNetV2
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Model

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from sklearn.metrics import accuracy_score
from joblib import dump, load


def plotaCurvaROC(rotulos, predicoes):

    test_fpr, test_tpr, te_thresholds = roc_curve(rotulos, predicoes)
    
    
    
    print(str(auc(test_fpr, test_tpr)))
    plt.plot(test_fpr, test_tpr, label=" Classificador = "+str(auc(test_fpr, test_tpr)), color='orange')
    plt.plot([0,1],[0,1],'b--')
    plt.legend()
    plt.xlabel("Taxa de Verdadeiro Positivo")
    plt.ylabel("Taxa de Falso Positivo")
    plt.show()


def plotaCurvaDeAprendizado(estimador, title, X, y, eixos=None, ylim=None, particoes=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
  
    if eixos is None:
        _, eixos = plt.subplots(1, 3, figsize=(20, 5))

    eixos[0].set_title(title)
    if ylim is not None:
        eixos[0].set_ylim(*ylim)
    eixos[0].set_xlabel("Treinamento")
    eixos[0].set_ylabel("Acurácia")

    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimador, X, y, cv=particoes, n_jobs=n_jobs,
                       train_sizes=train_sizes,
                       return_times=True)
    mediaAcuraciaTreinamento = np.mean(train_scores, axis=1)
    desvioPadraoAcuraciaTreinamento = np.std(train_scores, axis=1)
    mediaAcuraciaTeste = np.mean(test_scores, axis=1)
    desvioPadraoAcuraciaTeste = np.std(test_scores, axis=1)
    mediaEpocas = np.mean(fit_times, axis=1)
    desvioPadraoEpocas = np.std(fit_times, axis=1)

    # plota a curva de aprendizado
    eixos[0].grid()
    eixos[0].fill_between(train_sizes, mediaAcuraciaTreinamento - desvioPadraoAcuraciaTreinamento,
                         mediaAcuraciaTreinamento + desvioPadraoAcuraciaTreinamento, alpha=0.1,
                         color="r")
    eixos[0].fill_between(train_sizes, mediaAcuraciaTeste - desvioPadraoAcuraciaTeste,
                         mediaAcuraciaTeste + desvioPadraoAcuraciaTeste, alpha=0.1,
                         color="g")
    eixos[0].plot(train_sizes, mediaAcuraciaTreinamento, 'o-', color="r",
                 label="Acurácia do treinamento")
    eixos[0].plot(train_sizes, mediaAcuraciaTeste, 'o-', color="g",
                 label="Acurácia da Validação Cruzada")
    eixos[0].legend(loc="best")

       #Plota acurácia vs volume de dados avaliados
    eixos[1].grid()
    eixos[1].plot(train_sizes, mediaEpocas, 'o-')
    eixos[1].fill_between(train_sizes, mediaEpocas - desvioPadraoEpocas,
                         mediaEpocas + desvioPadraoEpocas, alpha=0.1)
    eixos[1].set_xlabel("Treinamento")
    eixos[1].set_ylabel("Interação")
    eixos[1].set_title("Escalabiliddade do Modelo")

     # Plota acurácia vs época/interacao
    eixos[2].grid()
    eixos[2].plot(mediaEpocas, mediaAcuraciaTeste, 'o-')
    eixos[2].fill_between(mediaEpocas, mediaAcuraciaTeste - desvioPadraoAcuraciaTeste,
                         mediaAcuraciaTeste + desvioPadraoAcuraciaTeste, alpha=0.1)
    eixos[2].set_xlabel("Interação")
    eixos[2].set_ylabel("Acurácia")
    eixos[2].set_title("Performace do Modelo")

    return plt

def extratrorDeCaracteristicas(directory, contadorDasAmostras):
    vetoresDeCaracterisca = np.zeros(shape=(contadorDasAmostras, 1536))  # O valor deve ser igual o da saida da rede selecionada (InceptionResNetV2 -> 1536) (Xception -> 2048)
    rotulos = np.zeros(shape=(contadorDasAmostras))
    # Preprocess data
    generator = datagen.flow_from_directory(directory,
                                            target_size=(299,299),
                                            batch_size = batch_size,
                                            class_mode='binary')
    # Pass data through convolutional base
    i = 0
    for inputs_batch, rotulos_batch in generator:
        vetoresDeCaracteriscaDoBatch = modelo.predict(inputs_batch)
        vetoresDeCaracterisca[i * batch_size: (i + 1) * batch_size] = vetoresDeCaracteriscaDoBatch
        rotulos[i * batch_size: (i + 1) * batch_size] = rotulos_batch
        i += 1
        if i * batch_size >= contadorDasAmostras:
            break
    return vetoresDeCaracterisca, rotulos

fig, eixos = plt.subplots(3, 2, figsize=(10, 15))

# Carrega CNN utilizada para transferência de aprendizado, removendo a camada totalmente conectada
base_modelo = InceptionResNetV2(weights='imagenet') # Para utilizar a Xception basta alterar o nome do modelo
base_modelo.summary()
modelo = Model(inputs = base_modelo.input,outputs=base_modelo.get_layer('avg_pool').output) 
modelo.summary()

#Inicia carregamento das imagens
datagen = ImageDataGenerator(rescale=1./255) 
batch_size = 32 # Define o batch size
diretorioBaseTreinamento = 'SeuCaminhoAqui'
diretorioBaseValidacao = 'SeuCaminhoAqui'
diretorioBaseTeste = 'SeuCaminhoAqui'

#Gera os vetores de caracteriscas para entrada da SVM
vetoresCaracteristicaTreinamento, rotulosTreinamento =extratrorDeCaracteristicas(diretorioBaseTreinamento, 98)  # Deve ser passado a quantidade de imagem de cada diretório
vetoresCaracteristicaValidacao, rotulosValidacao = extratrorDeCaracteristicas(diretorioBaseValidacao, 112)
vetoresCaracteristicaTeste, rotulosTeste = extratrorDeCaracteristicas(diretorioBaseTeste, 140)



#Concatena os dados de treinamento e validação para realizar a validação cruzada
vetoresCaracteristicaSVM = np.concatenate((vetoresCaracteristicaTreinamento, vetoresCaracteristicaValidacao))
rotulosSVM = np.concatenate((rotulosTreinamento, rotulosValidacao))

#Realiza o particionamento para validação cruzada
particoes = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

estimador = LinearSVC(penalty='l2', max_iter=8000) # Inicializa o objeto do SVM

#plota a curva de aprendizado
plotaCurvaDeAprendizado(estimador,  "Curva de Aprendizado",vetoresCaracteristicaSVM, rotulosSVM, eixos=eixos[:, 0], ylim=(0.7, 1.01),
                    particoes=particoes, n_jobs=-1)
plt.show()

#Realiza o treinamento com os mesmo parametros que geraram a curva de aprendizado e salva os pesos.
clf = LinearSVC(penalty='l2', max_iter=8000).fit(vetoresCaracteristicaSVM,rotulosSVM ) # A loss Hinge é a padrão para a penalidade l2, o numero maximo de interações foi adptado conforme os testes

dump(clf, 'pesos.joblib') 

previsaoBaseTreino = clf.predict(vetoresCaracteristicaSVM) # Realiza a predição da base de treino
previsaoBaseTeste = clf.predict(vetoresCaracteristicaTeste) # Realiza a predição da base de teste


print(accuracy_score(rotulosTeste, previsaoBaseTeste))
plotaCurvaROC(rotulosSVM, previsaoBaseTreino)
plotaCurvaROC(rotulosTeste, previsaoBaseTeste)



