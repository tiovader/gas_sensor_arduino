Após dar upload do `firmata.StandardFirmata` no arduíno, siga os passos:


* Configure o projeto em `settings.py`, insira os valores onde estão conectado os pinos referente a cada componente, além de outras configurações para conectar ao arduíno;
* Rode os testes unitários e garanta que todos foram sucedidos, assim ao rodar o script principal garante que não terá problemas (eu espero);
    ```bash
    python ./test.py
    ```
* Agora é só rodar o script principal, e verificar se o programa está funcionando!
    ```bash
    python ./main.py
    ```