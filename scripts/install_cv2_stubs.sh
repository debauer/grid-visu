#!/bin/bash

if [[ $1 == "pyright" ]]; then
    # pyright wants it in root/typings
    mkdir -p typings
    targetFile="typings/cv2.pyi"
else
    targetFile="$(poetry run python -c "import cv2, os; print(os.path.dirname(cv2.__file__))")/cv2.pyi"
fi

echo "Adding stubs to cv2 at path: $targetFile"

if [[ -e $targetFile ]]; then
    echo "$targetFile exists, remove and override"
    rm -v "$targetFile"
fi

curl -sSL https://raw.githubusercontent.com/microsoft/python-type-stubs/main/cv2/__init__.pyi \
    -o "$targetFile"
