from flask import Blueprint
from flask import request
from flask import render_template
import urllib.request
import os
from app.models import Movie, db, Review

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def hello_world():
    return render_template('review.html')

@main.route('/', methods=['POST'])
def handle_fomdata():
        moviename = request.form['name']
        movielength = Movie.query.filter_by(Name = moviename).count()
        if movielength==0 :
            moviedesc = request.form['desc']
            movieposter = request.form['poster']
            try:
                f = open('app/static/poster/' + moviename + '.jpg','wb')
                with urllib.request.urlopen(movieposter) as url:
                    s = url.read()
                f.write(s)
                f.close()
                dbmovieposter = '/poster/' + moviename + '.jpg'
            except:
                dbmovieposter = ""            
            nmovie = Movie(moviename, moviedesc, dbmovieposter)
            db.session.add(nmovie)
        else:
            nmovie = Movie.query.filter_by(Name = moviename).first()
        reviewscore = request.form['score']
        reviewdesc = request.form['review']
        reviewuser = request.form['user']
        deviceid = request.headers.get('User-Agent')
        nreview = Review(moviename, reviewdesc, reviewuser, deviceid, reviewscore)
        db.session.add(nreview)
        db.session.commit()
            
        return render_template('review.html')
