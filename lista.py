#!/bin/bash

echo "Ingrese 7 números separados por espacio:"
read -a numeros

# Verificar que sean 7 números
if [ ${#numeros[@]} -ne 7 ]; then
    echo "Debe ingresar exactamente 7 números."
    exit 1
fi

# Ordenar los números
ordenados=($(printf "%s\n" "${numeros[@]}" | sort -n))

echo "Números ordenados de menor a mayor:"
echo "${ordenados[@]}"
