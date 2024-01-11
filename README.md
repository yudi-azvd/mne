<br />
<div align="center">
  <a href="docs/bifurcacao.png">
    <img src="docs/bifurcacao.png" alt="Logo" width="200" height="200">
  </a>
</div>

# Métodos Numéricos para Engenharia

Uns códigos aí que foram feitos durante a disciplina.

## Dependências 

- Python 3.10+
- g++

## Testes

### Python

    pip install -r requirements.txt
    pytest

Pra executar um determinado exercício:

    python -m mne.exercises.chap1

### C
Não tem muita coisa feita em C porque acabei trocando continuando com Python por 
ser mais produtivo e flexível. Mas se você quiser testar, faça:

    cd tests

Se é a primeira vez executando os testes:

    ./build.sh 1 && ./test

Nas builds subsequentes não é necessário passar argumentos para `./build.sh`:

    ./build.sh && ./test

Para mais informações, leia: [tests/build.sh](tests/build.sh).
