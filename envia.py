import requests

# Caminho para o arquivo DICOM
dicom_file = "/home/gab/dicom_samples/id_0a1a38c4-c9e03c76-28a14f88-2d30e1d4-6183d46b/Study_79148372.32343444.40535568.71230168.45973202/Series_35159210.86362984.56224315.14980009.77443886/image-75545339-55870039-51885816-92064157-98378507.dcm"

# URL do Orthanc local
url = "http://localhost:8042/instances"

# Headers necessários
headers = {
    "Content-Type": "application/dicom"
}

# Nome de usuário e senha do Orthanc
username = "orthanc"
password = "orthanc"

# Ler e enviar o arquivo DICOM com autenticação
with open(dicom_file, 'rb') as f:
    response = requests.post(url, headers=headers, data=f, auth=(username, password))
    if response.status_code == 200:
        print(f"Arquivo {dicom_file} enviado com sucesso!")
    else:
        print(f"Erro ao enviar o arquivo: {response.status_code}")
