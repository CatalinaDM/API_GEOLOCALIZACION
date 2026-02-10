#Importando la libreria de  Flask 
from flask import Flask, render_template, request
import requests


#Creando una instancia de la clase Flask, que es la aplicación web. El nombre del módulo actual se pasa como argumento para que Flask pueda encontrar los recursos y las rutas correctamente.
app = Flask(__name__)

@app.route('/')
#Se define la función index() que se ejecutará cuando se acceda a la ruta raíz ('/') de la aplicación. Esta función utiliza render_template para renderizar y devolver el archivo 'index.html' como respuesta al navegador del usuario. Esto permite mostrar una página web al usuario cuando accede a la ruta raíz de la aplicación.
def index():
    return render_template('index.html')

#Se define la función buscar() que se ejecutará cuando se acceda a la ruta '/
@app.route('/buscar', methods=['POST', 'GET'])


def buscar():
    if request.method == 'POST':
        lugar = request.form['lugar']
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': lugar,
            'format': 'json',
            'limit': 1
        }
        headers = {
            'User-Agent': 'Flask-Education-App'
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            name = data[0]['display_name']
            return render_template('map.html', lat=lat, lon=lon, nombre = name)

    else:
        return render_template('map.html', error="No se encontró el lugar.")
    
if __name__ == '__main__':
    app.run(debug=True)
