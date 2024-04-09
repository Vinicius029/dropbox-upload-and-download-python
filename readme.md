# SCRIPT DE UPLOAD E DOWNLOAD NO DROPBOX VIA PYTHON


## Como usar o script

-  Para usar esse script, você precisa ter sua conta no dropbox. Para criar seu app no dropbox developer [Clicando aqui](https://www.dropbox.com/developers/). Com seu app criado, vai em permissões e habilita as opções de `arquivos.metadata.write`, `arquivos.content.write` e `arquivos.content.read`, salva e vai em configuração e gera o `TOKEN`.
- criar dentro da pasta raiz do script, um arquivo chamado de `token.txt`, nesse arquivo você salva o token que foi criado do dropbox.
- Executa o comando: 
    ```bash
    pip install dropbox
    ```
- Start seu script