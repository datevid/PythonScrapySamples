# scrapySamples
# spider05.py
En este ejemplo muestra cómo extraemos todas las frases de la página y la guardamos en un archivo. Además nos vamos a la siguiente página para extraer todas sus frases, así sucesivamente hasta la última página. Para el guardado usamos la librería pandas y un archivo donde agregamos todas las frases de cada página.
para ejecutar spider05, debe primero crear el proyecto.
```
pip install Scrapy
```
Luego crear el proyecto
```
scrapy startproject tutorial
```
Dentro de la carpeta spiders crearse el archivo spider05.py con el código respectivo. 

Para la ejecución de un solo archivo se realiza de la siguiente manera:
```
scrapy runspider --nolog spider05.py
```

Para la ejecución de todo el proyecto debe usar el siguiente comando (Muy importate, la propiedad name se debe enviar al momento de la ejecución del código, en este caso es name = 'spider05'):
```
scrapy crawl spider05
```
Ejecución con salida spiderData.json
```
scrapy crawl spider05 -o spiderData.json
```

Ejecución con log en la consola
```
scrapy crawl spider05 -o spiderData.json --nolog
```



