# Importa a classe YOLO da biblioteca ultralytics
from ultralytics import YOLO

# Função principal do script
def main():

    # Carrega o modelo YOLO pré-treinado
    model = YOLO("yolov8n.pt") 
    # "yolov8n.pt" é o arquivo do modelo pré-treinado da versão 8 do YOLO, na variante (n), que é uma versão leve e rápida do modelo.

    # Treina o modelo utilizando os dados especificados no arquivo "train.yaml" por 30 épocas
    model.train(data="train.yaml", epochs=30)  
    # "data="train.yaml"" especifica o caminho do arquivo YAML que contém as informações sobre os dados de treinamento (caminhos para as imagens, classes, etc).
    # "epochs=30" indica que o modelo será treinado por 30 épocas, ou seja, o conjunto de dados de treinamento será passado 30 vezes pelo modelo durante o treinamento.

    # Avalia o modelo treinado utilizando os dados de validação
    metrics = model.val() 
    # "model.val()" realiza a validação do modelo treinado, retornando métricas que indicam o desempenho do modelo, como precisão, recall, entre outros.

    model.export(format="onnx")


# Verifica se o script está sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    main()
    # Chama a função principal para iniciar o treinamento e a validação do modelo.