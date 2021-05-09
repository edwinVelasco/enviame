### Prueba BackEnd
#### Ejercicios de prueba para la vacante de backend en enviame
***
### Índice
1. [Punto 1 y 2](#punto12)
2. [Punto 3](#punto3)
3. [Punto 4](#punto4)
4. [Punto 5](#punto5)
5. [Punto 6](#punto6)
6. [Punto 7](#punto7)
***

#### Punto 1 y 2:

 - ingresar a la carpeta para la ejecución del docker-compose
```shell script
    $ cd Punto_1_2/crud
    $ docker-compose up -d
    # esperar a la descarga de las imagenes y el despliegue de las instancias de docker
```
 - El punto 1 se abordo con una instancia de nginx, node y postgresql para desplegar sitios web con nodejs y postgresql, se puede observar la configuración en el archivo [docker-compose.yml](https://github.com/edwinVelasco/enviame/blob/main/Punto_1_2/crud/docker-compose.yml)
 - El punto 2, es abordado con un servicio REST con mongoDB, NodeJS (Express) y nginx.
 - Para probar los servicios se debe importar el siguiente archivo en [postman](https://www.postman.com/)
 [CRUD Company.postman_collection.json](https://github.com/edwinVelasco/enviame/blob/main/Punto_1_2/CRUD%20Company.postman_collection.json)
 - Se creó el modelo de empresa con {name, nit, description}
 - El primer servicio que se debe ejecutar es el que resuelve el requerimiento de utilización de una libreria faker
 ```json
 {
    url: http://localhost/api/company/faker
    method: POST
    body:
    {
        "n": "120"
    }
 }
 ```
 - el servicio recibe la variable "n" para ingresar en mongo la cantidad similar de registros.
 - La utilización de los demas servicios se describe en el archivo de postman

***

#### Punto 3:
 - El punto 3 se desarrollo con Python 3.8
 - Para la ejecución del mismo se debe tener instalado cualquier versión de python 3.x
 [Punto_3/script.py](https://github.com/edwinVelasco/enviame/blob/main/Punto_3/script.py)
 ```shell script
    $ cd Punto_3
    $ python script.py
```

***
#### Punto 4:
