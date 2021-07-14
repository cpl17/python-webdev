from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import desc

from data import get_selection_options, get_movie_details


# Configure APP

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)




# Create DB

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





# Tables

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()




# Forms

class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10',validators=[DataRequired()])
    review = StringField('Your Review',validators=[DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField('Movie Title',validators=[DataRequired()])
    submit = SubmitField("Add Movie")



# Routes
    
@app.route("/")
def home():
    all_movies = Movie.query.order_by(desc(Movie.rating))
    for index,movie in enumerate(all_movies):
        movie.ranking = float(index + 1)
    db.session.commit()
    return render_template("index.html",movies=all_movies)

@app.route("/edit",methods=["POST","GET"])
def edit_rating():

    form = EditForm()

    if request.method == "POST":
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.review = form.review.data
        movie_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html',form=form)

@app.route("/delete",methods=["POST","GET"])
def delete_movie():

    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/add",methods=["POST","GET"])
def add_movie():

    form = AddForm()

    if request.method == "POST":

        title = form.title.data
        movies_to_select_from = get_selection_options(title)

        return render_template("select.html", movies=movies_to_select_from)

    return render_template("add.html",form=form)


#TODO: Check if movie in database already

@app.route("/find")
def find_movie_details():

    movie_api_id = request.args.get("id")

    movie_details = get_movie_details(movie_api_id)

    if movie_api_id:


        new_movie = Movie(
            title= movie_details.title,
            img_url=movie_details.image_url,
            year=movie_details.year,
            description = movie_details.description)
 
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('edit_rating',id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)
