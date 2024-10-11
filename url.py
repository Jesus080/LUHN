import ssl
import socket
from urllib.parse import urlparse

def verificar_certificado_ssl(url):
    # Extraer el dominio de la URL
    dominio = urlparse(url).netloc
    
    try:
        # Crear un contexto SSL
        contexto = ssl.create_default_context()
        # Obtener el certificado del sitio web
        with contexto.wrap_socket(socket.socket(), server_hostname=dominio) as conn:
            conn.connect((dominio, 443))
            cert = conn.getpeercert()
        # Si no hay excepción, el certificado es válido
        return True
    except ssl.SSLError:
        return False

def verificar_dominio_oficial(url, dominios_oficiales):
    # Extraer el dominio de la URL
    dominio = urlparse(url).netloc
    # Verificar si el dominio está en la lista de dominios oficiales
    if dominio in dominios_oficiales:
        return True
    else:
        return False

# Lista de dominios oficiales (puedes agregar más)
dominios_oficiales = ["www.dhl.com", "www.mercadolibre.com.mx"]

# URL a verificar
url = "https://sooyou.net/mex/"

# Verificar si el certificado SSL es válido
if verificar_certificado_ssl(url):
    print(f"El certificado SSL de {url} es válido.")
else:
    print(f"El certificado SSL de {url} no es válido.")

# Verificar si el dominio es oficial
if verificar_dominio_oficial(url, dominios_oficiales):
    print(f"{url} es un sitio oficial.")
else:
    print(f"{url} no es un sitio oficial.")