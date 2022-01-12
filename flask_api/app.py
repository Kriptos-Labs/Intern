# import libraries
from flask import Flask, render_template
import urllib.request, json
import requests

app = Flask(__name__)

#Sending a request to the https://www.themoviedb.org/ API. 
#Create a URL using the TMDB API key. 
#Return data to the template movie.html
@app.route("/")
def get_movies():
    url= "https://api.themoviedb.org/3/movie/popular?api_key=4e83fa69feb76abc963a019c8fec4375"

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    return render_template ('movie.html', movies=jsondata["results"])

#Sending a request to the TMDB API. 
#Create a URL using the TMDB API key. 
@app.route("/movies")
def get_movies_description():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=4e83fa69feb76abc963a019c8fec4375"

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)
    print(jsondata)
    movie_json = []
    
    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
            "original_language": movie["original_language"]
        }
        movie_json.append(movie)
    #print(movie_json)
    return {"movie title": movie_json}

#Send a request to the API with search parameters by id 
@app.route("/search_by_id/<string:movie_id>")
def get_only_movie(movie_id):
    url= "https://api.themoviedb.org/3/movie/"
    params = {"api_key":"4e83fa69feb76abc963a019c8fec4375"}
    
    response = requests.get(url=url+movie_id,params=params)
    data=response.json()
    return {"movie information": data}

#Send a request to the API Spotify with parameter of authorization 
#Generete new token for search  
@app.route("/spotify")
def get_search():
    response = requests.get('https://api.spotify.com/v1/browse/categories',
        headers={'Accept': 'application/json','Authorization':'Bearer BQAIhqR82pLD2PflzkJWRrKy3oWj02-vDOa5XBnMrMrMOaryZxObQDIf5G_1D-tHQ2DR3xeXq9j0bUgzVi7CCnlUout3ExZJ71BSogDuByXzcoxLHY90UkK5gPCg3E42qoxExEiaVhRnRK_SFkpQ1GiY-J7fa5THlqZQTJmVmzyv'}
    )
    json_response= response.json()
    return json_response


if __name__ == '__main__':
    app.run(debug=True)
    
#Running on http://127.0.0.1:5000/