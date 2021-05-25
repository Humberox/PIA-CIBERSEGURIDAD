import argparse
import configparser
import os

from MetaData import DataMeta

from MailTest import testmail

from Cifrado import CifradoCesar

from Scraping import Scraping

from SitiosWeb import VirusTotal

if __name__ == '__main__':

    description = """                        PROGRAMACION PARA CIBERSEGURIDAD

                           ---OPCIONES PARA ELEGIR---
    C --> CIFRADO DE MENSAJES             Necesita mensaje y clave de cifrado
    E --> ENVIO CORREOS ELECTRONICOS      Necesita un archivo de configuracion
    S --> VALIDACION DE SITIOS WEB        Necesita una API de VirusTotal y una url
    M --> METADATA                        Necesita una carpeta de imagenes
    W --> WEB SCRAPING                    Necesita una url """


    parser = argparse.ArgumentParser(description=description,
                        formatter_class = argparse.
                        RawDescriptionHelpFormatter)

    parser.add_argument('-op', dest = 'op', metavar = 'Opcion',
                help = 'Elige alguna opcion: C, E, O, W, M', default = 'H')
    parser.add_argument('-path', dest = 'path', metavar = 'Ruta',
                help = 'Indica la ruta de la carpeta', default = 'IMG')
    parser.add_argument("-config", type=argparse.FileType('r'),
                help = 'Archivo de Configuracion')
    parser.add_argument("-msg", dest = "msg", metavar = 'Mensaje',
                help = 'Mensaje a Cifrar')
    parser.add_argument("-clave", dest = "clave", metavar = 'Clave',
                help = 'Clave con la que se cifra')
    parser.add_argument("-url", dest = "url", metavar = 'Enlace',
                help = 'Direccion web de un sitio ', default = 'default')
    parser.add_argument("-api", dest = "api", metavar = 'Clave API',
                help = 'Necesitas una API de VirusTotal')


    i = 0
    params = parser.parse_args()
    if params.config:
        i += 1
        config = configparser.ConfigParser()
        config.read_file(params.config)
        params.a1 = str(config['CORREO']['EMISOR'])
        params.a2 = str(config['CORREO']['CONTRA'])
        params.a3 = str(config['CORREO']['RECEPTOR'])
        params.a4 = str(config['CORREO']['ASUNTO'])
        params.a5 = str(config['CORREO']['DESCRIP'])
        params.a6 = str(config['CORREO']['FILE'])

    op = params.op
    path = params.path
    msg = params.msg
    clave = params.clave
    url = params.url
    api = params.api

    if op == 'H':
        print (' --- Eliga opcion -h para el menu --- ')
    elif op == 'C':
        if type(msg) == str and type(clave) == str:
            print('\n Elegiste cifrado de mensajes')
            CifradoCesar(msg, clave)
        else:
            print(" Falta el mensaje o la clave (  -msg, -clave  )")

    elif op == 'E':
        print('\n Elegiste envio de correos')
        if i == 1:
            testmail(params.a1, params.a2, params.a3, params.a4, params.a5, params.a6)
            print("---- Correo enviado con exito ----")
        else:
            print("\n Falta el archivo de configuracion (  -config  )")

    elif op == 'S':
        if type(api) == str and url != 'default':
            print('\n Elegiste analisis de SitiosWeb')
            VirusTotal(api, url)

        else:
            print("\n Falta algun parametro (  -api, -url  )")

    elif op == 'W':
        print('\n Elegiste web scraping')

        if url != "nosabemos":

            scraping = Scraping()
            scraping.Carpeta()
            scraping.scrapingImages(url)
            scraping.scrapingPDF(url)
            scraping.scrapingLinks(url)


        else:
            print(" Te falta la direccion web (  -url  )")

    elif op == 'M':

        print('\n Elegiste metadata')
        if os.path.exists(path) == True:
            DataMeta(path)
            print("---- Hecho! ----")
        else:
            print("\n Falta la ruta de carpeta (  -path  )")

    else:
        print("Error, esa opcion no existe!")
