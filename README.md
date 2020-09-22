# Jetours
Aplicativo de prueba.

## Entorno en el que fue desarrollado;

* [x]  Sistema operativo Ubuntu 20.04 LTS
* [x]  Python 3.8.2

## Stack Tecnológico


### Para backend se utilizaron las siguientes librerías
* [x] flask
* [x] flask-cors

###  Las librerías se instalan de la siguiente forma:

pip install -r requirements.txt

## La aplicación funciona de la siguiente manera de forma -----  local:

### 1ro 
- Abrir una terminal y ubicarse en la carpeta raíz de la aplicación "jetours". 
  Ejecutar el comando: python3 -m api.v1.main 


### 2do
- En el navegador digitar la url: http://localhost:5000/status esto le indicará si la API está respondiendo adecuadamente.

## La aplicación funciona de la siguiente manera de forma -----  online:
- En el navegador digitar la url: http://35.239.166.35:5000/api/v1/status/ esto le indicará si la API está respondiendo adecuadamente.

## Endpoints

### Para ordenar números
En el navegador puede digitar de las siguientes formas y ambas son válidas

* http://localhost:5000/api/v1/sorted_numbers/?numbers=10,27,3,8,1

* http://localhost:5000/api/v1/sorted_numbers/?numbers=[10,27,3,8,1]


*** Con curl:
* curl -X GET http://0.0.0.0:5000/api/v1/sorted_numbers/\?numbers\=10,27,3,8,1
* curl -X GET http://localhost:5000/api/v1/sorted_numbers/?numbers=%5B1,2,3%5D


### Obtener el número de letras mayúsculas de un archivo

En este caso se utilizará curl: 
(debe reemplazar "filename.txt" por el nombre del archivo que desea subir, asegurese que está en el directorio del archivo a subir o que la ruta del archivo esté bien)


* curl -i -X GET http://35.239.166.35:5000/api/v1/name_file/ -F "file=@index.html"
* curl -i -X GET http://localhost:5000/api/v1/name_file/ -F "file=@filename.txt"