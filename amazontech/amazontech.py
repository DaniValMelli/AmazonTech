import json, os, urllib
from flair.data import Sentence
from flair.models import SequenceTagger

class Amazontech():
"""
Clase para implementar las funciones de análisis de texto y procesamiento de imagenes con el fin de proteger la amazonio de la deforestación a partir de la detección de patrones en los datos capturados.
"""
        
        
    @staticmethod
    def ner_from_str(text, output_path): 
    """
    Método que se encarga de extraer de un texto las entidades que afectan de forma directa o indirecta a la región del Amazonas
    Input: Texto a examinar, Ruta del archivo que se guardará con la información estructurada
    Output: Descarga un archivo en formato json en la ruta proporcionada
    """
        
        # load tagger
        tagger = SequenceTagger.load("flair/ner-spanish-large")
        # make example sentence
        sentence = Sentence(text)
        # predict NER tags
        tagger.predict(sentence)
        
        ner=sentence.get_spans('ner')
        entities = [x.text for x in ner]
        tags = [x.tag for x in ner]
        
        json_ner = {
            "text": text,
            "org": [],
            "loc" : [],
            "per" : [],
            "dates" : [],
            "misc": [],
            "impact": ""
        }   
        
        for i,entity in enumerate(entities):
            if tags[i] == "ORG" or tags[i] == "org":
                if entity not in json_ner["org"]:
                    json_ner["org"].append(entity)
            elif tags[i] == "LOC" or tags[i] == "loc":
                if entity not in json_ner["loc"]:
                    json_ner["loc"].append(entity)
            elif tags[i] == "PER" or tags[i] == "per":
                if entity not in json_ner["per"]:
                    json_ner["per"].append(entity)
            elif tags[i] == "DATE" or tags[i] == "DATES" or tags[i] == "dates" or tags[i] == "date":
                if entity not in json_ner["dates"]:
                    json_ner["dates"].append(entity)
            else:
                if entity not in json_ner["misc"]:
                    json_ner["misc"].append(entity)
            
        
        json_object = json.dumps(json_ner, indent=4)
        
        number = 1
        name = "ner (" + str(number) + ").json"
        path = output_path+"/"+name
        while os.path.exists(path):                
            number+=1
            name = "ner (" + str(number) + ").json"
            path = output_path+"/"+name
        with open(path, "w") as outfile:
            outfile.write(json_object)
        
    @staticmethod
    def ner_from_file(text_path, output_path):
    """
    Método que se encarga de extraer de un archivo de texto las entidades que afectan de forma directa o indirecta a la región del Amazonas
    Input: Ruta del fichero de texto a examinar, Ruta del archivo que se guardará con la información estructurada
    Output: Descarga un archivo en formato json en la ruta proporcionada
    """
        
        with open(text_path) as f:
            text = f.read()
        ner_from_str(text, output_path)
    
    @staticmethod
    def ner_from_url(url, output_path):
    """
    Método que se encarga de extraer de una pagina web las entidades que afectan de forma directa o indirecta a la región del Amazonas
    Input: Ruta del fichero de texto a examinar, Ruta del archivo que se guardará con la información estructurada
    Output: Descarga un archivo en formato json en la ruta proporcionada
    """
        f = urllib.urlopen(url)
        text = f.read()
        ner_from_str(text, output_path)