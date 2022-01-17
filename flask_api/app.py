# import libraries
from flask import Flask, render_template, request
import urllib.request, json
import requests
from const import url_list, api_key, sesion_id, url_create_list, url_mp, url_gmid

app = Flask(__name__)

#Create an enviroment in this proyect
#Activate the enviroment env\Scripts\activate
#Excecute the command set FLASK_APP=app
#Excecute the command flask run
#Running on http://127.0.0.1:5000/

#Welcome
@app.route("/")
def welcome():
    return render_template('index.html')

#Sending a request to the https://www.themoviedb.org/ API. 
#Create a URL using the TMDB API key. 
#Return data to the template movie.html
@app.route("/popular")
def get_movies():
    url=url_mp+api_key
    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    return render_template ('movie.html', movies=jsondata["results"])


#Send a request to the API with search parameters by id_movie
@app.route("/search_by_id/<int:movie_id>")
def get_only_movie(movie_id):
    response = requests.get(url=url_gmid+str(movie_id),params = {"api_key":api_key})
    data=response.json()
    return {"movie information": data}

#Post peticion to create a list in TMDB API
#Data to create list in sending by ULR
@app.route("/create/<string:name_list>/<string:desc>/<string:lang>", methods=['POST'])
def create_list(name_list,desc,lang):
    url=url_create_list+'?api_key='+api_key+'&session_id='+sesion_id
    data={'name':name_list, 'description':desc,'language':lang}
    response = requests.post(url,data)
    json_response= response.json()
    return json_response

#Send a request to the API with search parameters by id_list
@app.route("/view/<int:id>")
def view_list(id):
    response = requests.get(url=url_list+str(id),params={'api_key':api_key})
    json_response= response.json()
    
    return json_response

#Delete peticion to the TMDB API to delete a list
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    response=requests.delete(url=url_list+str(id), params={'api_key':api_key,'session_id':sesion_id})
    
    return 'Lista eliminada'
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

