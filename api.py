import os
from flask import Flask, abort, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)


password=os.getenv('code')
host=os.getenv('host')

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@{}:5432/bibliotheque".format(password,host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# creation de la table 
class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.Integer,nullable=False)
    titre=db.Column(db.String(100),nullable=False)
    date_publication=db.Column(db.Date,nullable=True)
    auteur=db.Column(db.String(100),nullable=False)
    editeur=db.Column(db.String(100),nullable=True)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
    
    #quelques fonctions
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format_livre(self):
        cat=Categorie.query.get(self.categorie_id)
        return {
        'id':self.id,
        'isbn':self.isbn,
        'titre':self.titre,
        'date_publication':self.date_publication,
        'auteur':self.auteur,
        'editeur':self.editeur,
        'categorie':cat.libelle_categorie
    }
    
# creation de la table categorie
class Categorie(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(50),nullable=False)
    livres= db.relationship('Livre',backref='categorie',lazy=True)
 
    #quelques fonctions
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format_cat(self):
        return {
            'id':self.id,
            'libelle':self.libelle_categorie
        }
        
     
   
db.create_all()
@app.route('/')
def test():
    return "test success"

#creer une categorie
@app.route('/categorie',methods=['POST'])
def add_categorie():
    body=request.get_json()
    new_cat=body.get('libelle')
    if new_cat is None:
        return "Impossible de faire cet ajout veillez réesayer en saisissant le libelle"
    else:
        categorie=Categorie(libelle_categorie=new_cat)
        categorie.insert()
        return jsonify({
            'success':True,
            'Total_categorie':Categorie.query.count(),
            'categorie':[cat.format_cat() for cat in Categorie.query.all()]
        })
        
#liste des categories
@app.route('/categories',methods=['GET'])
def list_categorie():
    categories=Categorie.query.all()
    return jsonify({
            'success':True,
            'Total_categorie':Categorie.query.count(),
            'categorie':[cat.format_cat() for cat in Categorie.query.all()]
        })
# rechercher une categorie
@app.route('/categorie/<int:id>')
def get_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return jsonify({
            'success':True,
            'selected_id':id,
            'categorie': categorie.format_cat()
        })

# modifier une categorie
@app.route('/categorie/<int:id>',methods=['PATCH'])
def set_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        body=request.get_json()
        categorie.libelle_categorie=body.get('libelle')
        categorie.update()
        return jsonify({
            'successs':True,
            'update_id':id,
            'categorie': categorie.format_cat()
        })
# effacer une categorie
@app.route('/categorie/<int:id>',methods=['DELETE'])
def delete_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify({
            'success':True,
            'categorie':categorie.format_cat(),
            'total_categorie': Categorie.query.count()
        })


# ajouter un livre
@app.route('/livre',methods=['POST'])
def add_livre():
    body=request.get_json()
    new_isbn=body.get('isbn')
    new_titre=body.get('titre')
    new_date=body.get('date','')
    new_auteur=body.get('auteur')
    new_editeur=body.get('editeur','')
    new_cat=body.get('categorie')
    
    if new_isbn is None:
        return "le isbn est obligatoire"
    elif new_titre is None:
        return "le titre du livre est obligatoire"
    elif new_auteur is None:
        return "le nom de l'auteur est obligatoire"
    elif new_cat is None:
        return "le numero de la categorie est obligatoire"
    elif new_date is None and new_editeur is None:
        livre=Livre(isbn=new_isbn,titre=new_titre,date_publication=new_date,auteur=new_auteur,editeur=new_editeur,categorie_id=new_cat)
        livre.insert()
        return jsonify({
            'success':True,
            'total_livres': Livre.query.count(),
            'Livres': [liv.format_livre() for liv in Livre.query.all()]
        })
    elif new_date is None or new_editeur is None:
        if new_date is None:
            
            livre=Livre(isbn=new_isbn,titre=new_titre,date_publication=new_date,auteur=new_auteur,editeur=new_editeur,categorie_id=new_cat)
            livre.insert()
            return jsonify({
                'success':True,
                'total_livres': Livre.query.count(),
                'Livres': [liv.format_livre() for liv in Livre.query.all()]
        })
        else:   
            livre=Livre(isbn=new_isbn,titre=new_titre,date_publication=new_date,auteur=new_auteur,editeur=new_editeur,categorie_id=new_cat)
            livre.insert()
            return jsonify({
                'success':True,
                'total_livres': Livre.query.count(),
                'Livres': [liv.format_livre() for liv in Livre.query.all()]
        })
    else:
        livre=Livre(isbn=new_isbn,titre=new_titre,date_publication=new_date,auteur=new_auteur,editeur=new_editeur,categorie_id=new_cat)
        livre.insert()
        return jsonify({
                'success':True,
                'total_livres': Livre.query.count(),
                'Livres': [liv.format_livre() for liv in Livre.query.all()]
        })
# affichier les livres
@app.route('/livres',methods=['GET'])
def list_livres():
    livres=Livre.query.all()
    return jsonify({
        'success':True,
        'total_livres':Livre.query.count(),
        'Livres': [liv.format_livre() for liv in Livre.query.all()]
    })      
# recherche un livre
@app.route('/livre/<int:id>')
def get_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify({
            'success':True,
            'selected_id':id,
            'livre':livre.format_livre()
        })            
           
# modifier un livre
@app.route('/livre/<int:id>',methods=['PATCH'])
def set_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        body=request.get_json()
        livre.isbn=body.get('isbn')
        livre.titre=body.get('titre')
        livre.date_publication=body.get('date')
        livre.auteur=body.get('auteur')
        livre.editeur=body.get('editeur')
        livre.categorie_id=body.get('categorie')
        livre.update()
        return jsonify({
            'successs':True,
            'update_id':id,
            'livre':livre.format_livre()
        })
# suprimer un livre
@app.route('/livre/<int:id>',methods=['DELETE'])
def delete_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            'success':True,
            'livre':livre.format_livre(),
            'total_livre': Livre.query.count()
        })

#les livres d'un categorie
@app.route('/categorie/<int:id>/livres')
def cat_livres(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        livres=Livre.query.filter_by(categorie_id=id)
        if livres.count()==0 :
            return "La categorie {} ne contient aucun livres. Merci!!!".format(categorie.libelle_categorie)
        else:
            return jsonify({
                'success':True,
                'categorie':categorie.libelle_categorie,
                'livres':[liv.titre for liv in livres],
                'total_livre': livres.count()
            })
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404