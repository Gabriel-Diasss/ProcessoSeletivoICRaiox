# ProcessoSeletivoICRaiox
Repositório para documentação do desafio computacional do processo seletivo da iniciação científica em IA multimodal na triagem de Raios-X

## Parte 1: Configuração e Execução do PACS (Orthanc) usando Docker

### Requisitos

- Docker instalado ([Guia de Instalação](https://docs.docker.com/get-docker/))

### Comando para rodar o Orthanc

Para rodar o Orthanc localmente usando Docker, execute o seguinte comando no terminal:

```bash
sudo docker run --rm -d --name orthanc -p 8042:8042 -p 4242:4242 jodogne/orthanc-plugins

em seguida digite no navegador "http://localhost:8042"
