# Métodos Numéricos para Engenharia

## Dependências 

- Python 3.10+
- GCC

## Testes

### Python

    pip install -r requirements.txt
    pytest

Pra executar um determinado exercício:

    python -m mne.exercises.chap1
### C

    cd tests

Se é a primeira vez executando os testes:

    ./build.sh 1 && ./test

Nas builds subsequentes não é necessário passar argumentos para
`./build.sh`:

    ./build.sh && ./test

Para mais informações, leia: [tests/build.sh](tests/build.sh).
