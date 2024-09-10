# ProcessoSeletivoICRaiox
Repositório para documentação do desafio computacional do processo seletivo da iniciação científica em IA multimodal na triagem de Raios-X

## Parte 1: Configuração e Execução do PACS (Orthanc) usando Docker

### Requisitos

- Docker instalado ([Guia de Instalação](https://docs.docker.com/get-docker/))

### Comando para rodar o Orthanc

Para rodar o Orthanc localmente usando Docker, execute o seguinte comando no terminal:

```bash
sudo docker run --rm -d --name orthanc -p 8042:8042 -p 4242:4242 jodogne/orthanc-plugins
```
em seguida digite no navegador "http://localhost:8042"

## Parte 2: Envio de Arquivo DICOM
 Utilizei o seguinte código python envia.py para realizar o envio dos dados dicom para o Orthanc. A primeira vista tive dificuldades em acessar os arquivos porque tentei utilizar google colab mas estava tendo problemas pelos dados estarem salvos localmente na minha máquina, então abri o notebook jupyter localmente no meu computador.
 O código tinha encontrado erros no começo ao tentar fazer os uploads sem ter o usuário e senha cadastrados. Após colocar os dois no código consegui fazer o upload sem problemas.
 Outro problema que tive, foi que tentei usar comandos de terminal no python para localizar os arquivos, e isso gerou "erros de nomeclatura" que a priori atribuí ao nome dos arquivos, por isso renomeei uma imagem, acreditando que fosse resolver o problema.
 

 
