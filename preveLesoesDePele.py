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


################ Carrega base e passa pela CNN
base_modelo = InceptionResNetV2(weights='imagenet')
base_modelo.summary()
modelo = Model(inputs = base_modelo.input,outputs=base_modelo.get_layer('avg_pool').output) 
modelo.summary()


datagen = ImageDataGenerator(rescale=1./255)
batch_size = 32

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


diretorioTeste = 'E:\\OneDrive - Movere Software\\BaseSeparada26032021borderline\\DiretorioImagens\\test\\'
vetoresDeCaracterisca, rotulos = extratrorDeCaracteristicas(diretorioTeste, 140)
from joblib import dump, load


svm = load('pesos.joblib') 
previsoes = svm.predict(vetoresDeCaracterisca)


print(accuracy_score(rotulos, previsoes))
