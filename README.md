## AMAZONTECH
<img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/logo-fac-azul.png" width="150" height="80" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/logo-uniandes-blanco.png" width="210" height="70" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/perficient-logo.png" width="110" height="70" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/logo-telespazio.png" width="140" height="70" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/esri-logo.png" width="120" height="120" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/adl-digital-logo.png" width="100" height="80" /> <img src="https://github.com/DaniValMelli/AmazonTech/blob/master/images/maxar-logo.png" width="120" height="80" />

La Fuerza Aérea Colombiana y la Universidad de los Andes con el patrocinio de Aval Digital Labs y Maxar, trae una nueva versión del CODEFEST Ad Astra, en este año se elige la región amazónica, la cual es una zona vulnerable, afectada por la deforestación, minería y explotación de hidrocarburos, narcotráfico, entre otras, la Fuerza Aérea vela por la seguridad de esta region para identificar estas vulnerabilidades, usa videos con sensores por medio de FLIR y aeronaves remotamente tripuladas, por lo anterior el reto de este año requiere de grandes ideas que ayuden a la protección del Amazonas. 

Estado: Terminado, con posibilidad de actualización. 

### Objetivo 1.

Identificar por medio de videos las vulnerabilidades de la Amazonia Colombiana, identificando objetos de interés en recuadros,  AMAZONTECH realizó captura de imágenes a partir de los videos proporcionados, y por medio del uso de una librería Open Source llamada YOLO se entrenaron dos modelos, el primero para detectar objetos de interés como vehiculos y casas, y el segundo encargado de extraer los datos de los caracteres mostrados en el video, de esta manera se proporciona apoyo al personal de la Fuerza Aeroespacial, en el proceso de examinar la región.


### Objetivo 2 (Natural Language Processing). 

La librería contiene 3 funciones de procesamiento de noticias escritas, que buscan identificar entidades que afectan directa o indirectamente en la deforestación del Amazonas colombiano, además identifica de entre cuatro categorías distintas (MINERÍA, CONTAMINACIÓN, DEFORESTACIÓN y NINGUNA) la perteneciente a la noticia procesada. El modelo para extracción de entidades se basa en la librería **flair**, el cual está pre-entrenado con los sets de noticias ya etiquetados. Además se utiliza un enfoque 

Las funciones son:
- ner_from_str(text, output_path)
Método que se encarga de extraer de un texto las entidades que afectan de forma directa o indirecta a la región del Amazonas
Input: Texto a examinar, Ruta del archivo que se guardará con la información estructurada
Output: Descarga un archivo en formato json en la ruta proporcionada.
- ner_from_file(text_path, output_path)
Método que se encarga de extraer de un archivo de texto las entidades que afectan de forma directa o indirecta a la región del Amazonas
Input: Ruta del fichero de texto a examinar, Ruta del archivo que se guardará con la información estructurada
Output: Descarga un archivo en formato json en la ruta proporcionada.
- ner_from_url(url, output_path)
Método que se encarga de extraer de una pagina web las entidades que afectan de forma directa o indirecta a la región del Amazonas
Input: Ruta del fichero de texto a examinar, Ruta del archivo que se guardará con la información estructurada
Output: Descarga un archivo en formato json en la ruta proporcionada
 
Los requisitos del entorno de desarrollo para la integración. Se recopila información por medio de textos de noticias en la región de la amazonia Colombiana para identificar entidades que describan afectaciones medio ambientales.

### Importación de librería.

El comando para importar la librería es: 

    - *from amazontech import Amazontech*






