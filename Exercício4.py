# quarto exemplo de uma biblioteca - SQLAlchemy:

# pip install sqlalchemy - PARA INSTALAR A BILBIOTECA

#pip install --pre SQLAlchemy

# conda install -c anaconda sqlalchemy

alldata = session.query(Filme).all()


# SELECT * FROM Filme

f1 = Filme("Star Trek", 2009)
session.add(f1)

#INSERT INTO Filme (nome, ano) VALUES ("Star Trek", 2009)
