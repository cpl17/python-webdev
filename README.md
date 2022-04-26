Repo Includes: 

* __Library__: A Flask App that acts as a mock personal library and rating system. Data (books) are store and queried in a SQLite database managed by SQLAlchemy.  The database is a single table with book, author and rating. 

* __Login Manager__ : A Flask App that acts as a registry/verification portal. Password hashes are generate and checked using werkzeug. User activity tracking and verification is managed using flask-login. Finally, user information is stored in a SQLite DB. Pages are styled in CSS. 

* __Top 10 Movies__ :  A Flask App that stores and presents details on one’s favorite movies. The user inputs a movie and, using the IMDB api, images, actors and other information is collected. Additionally, user ratings collected through forms created with wtf-forms and stored in SQLite dbs (along with the details collected with the api query). HTML/code templating is implement through Jinja and Flask-Bootstrap.

