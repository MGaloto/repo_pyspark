


# Pyspark, Python y SQL.

Para ejectuar el código se utilizó una imagen de Docker que contiene las librerías para trabajar con Pyspark y Jupyter Notebook. El archivo docker-compose.yml tiene las instrucciones necesarias para leer la imagen y utilizar el puerto 8888 para la Notebook.

El comando a ejecutar para construir la imagen y correr el contenedor es el siguiente:

```shell
docker-compose up -d
```


Todos los archivos y/o cambios que se generen se van a guardar en la carpeta local `pyspark` configurada en el docker-compose-yml.


### Estructura:

``` shell
.
│   .gitignore
│   docker-compose.yml
│   Dockerfile
│   jupyter_config.json
│
└───pyspark
    │   pyspark_session.ipynb
    │   pyspark_session_sql.ipynb
    │   python_date.ipynb
    │
    ├───csvfiles
    │       Person_CountryRegion.csv
    │       Person_StateProvince.csv
    │       Sales_CountryRegionCurrency.csv
    │       Sales_Currency.csv
    │       Sales_CurrencyRate.csv
    │       Sales_SalesTaxRate.csv
    │       visits.csv
    │
    ├───jsonfiles
    │       MPE1004.json
    │       Sellers.json
    │
    ├───pythondate
            date.py



```

En resumen:

- El archivo `.gitignore` no trackea documentos para el repositorio.
- `jupyter_config.json` nos sirve para configurar la jupyter notebook.
- Con `.docker-compose.yaml` y `Dockerfile` se construye la imagen para ejecutar Pyspark.
- En la carpeta `jsonfiles` y `csvfiles` se encuentran los archivos que se van a leer.
- En la carpeta `pyspark` estan las notebooks a ejecutar.