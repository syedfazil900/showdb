from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .apiCalls import *
views = Blueprint('views', __name__, url_prefix='/')






@views.route('/')
def trending_shows():
    shows = apiCallTrending("tv")
    return render_template('index.html',id="Trending Shows", props=shows, type="tv")
@views.route('/popular-shows/')
def popular_shows():
    shows = apiCallPopular("tv")
    return render_template('index.html',id="Popular Shows",props=shows, type="tv")

@views.route('/trending-movies/')
def trending_movies():
    movies = apiCallTrending("movie")
    return render_template('index.html',id="Trending Movies",props=movies ,type="movie") 

@views.route("/popular-movies/")
def popular_movies():
    movies = apiCallPopular("movie")
    return render_template ("index.html",id="Popular Movies", props=movies ,type="movie")

@views.route('/search/', methods=['GET'])
def search():
    query= request.args.get('query')
    results = apiCallSearch("tv",query)
    results += apiCallSearch("movie",query)
    return render_template('index.html',id="Search Results",props=results)
    
@views.route('/movie/<string:id>')
def movie(id):
    result = apiCall("movie",id)
    casts = apiCallCast("movie",id)
    return render_template('details.html', id=id,name="movie", result=result ,casts=casts)

@views.route('/show/<string:id>')
def show(id):
    result = apiCall("tv",id)
    casts = apiCallCast("tv",id)
    return render_template('details.html', id=id,name="show", result=result ,casts=casts)


@views.route('/people/<string:name>')
def person(name):
    person = apiCallPerson(name)
    details = apiCallPersonDetails(name)
    return render_template('people.html', name=name,persons=person,details=details)