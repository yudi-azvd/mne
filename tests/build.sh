set -e

includes="-I../lib -I../src"

# https://serverfault.com/questions/7503/how-to-determine-if-a-bash-variable-is-empty
# NOTE: É necessário fazer a compilação de main.test.o apenas 1 vez.
# Se tiver algo no primeiro argumento, essa compilação ocorre.
if [[ $1 ]]
then
    g++ $includes -o main.test.o -c main.test.cpp
fi

g++ \
    -g \
    -lm \
    $includes \
    \
    ../src/roots.cpp \
    ../src/functions.cpp \
    \
    bisection.test.cpp \
    regula_falsi.test.cpp \
    \
    main.test.o \
    -o test
