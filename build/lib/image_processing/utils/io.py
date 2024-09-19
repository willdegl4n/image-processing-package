# Esse código permite a leitura e salvamento de imagens usando 
# a biblioteca skimage. A função read_image pode ler uma imagem 
# em escala de cinza se o parâmetro is_gray for definido como 
# True, e a função save_image salva a imagem no caminho especificado.

from skimage.io import imread, imsave

def read_image(path, is_gray=False):
    image = imread(path, as_gray=is_gray)
    return image

def save_image(image, path):
    imsave(path, image)
