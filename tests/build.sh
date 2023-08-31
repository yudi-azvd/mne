set -e

includes="-I../lib -I../src"

# NOTE: Na primeira vez que executar esse script descomente a linha abaixo.
# As próximas execuções podem ser executadas com ela comentada.

# g++ $includes -o main.test.o -c main.test.cpp

g++ \
    -g \
    -lm \
    $includes \
    roots.test.cpp \
    main.test.o \
    -o test
