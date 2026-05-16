from neo4j import GraphDatabase
import pandas as pd

url = "bolt://127.0.0.1:7687"
utilisateur = "neo4j"
mdp = "nathanaru"

driver = GraphDatabase.driver(url, auth=(utilisateur, mdp))

liste = pd.read_csv("champions_league_matches.csv")

#creation liste des equipes
equipes = set(liste['home_team'].dropna().tolist() + liste['away_team'].dropna().tolist())

#creation liste des stades
stades = liste['venue'].dropna().tolist()

#creation liste des arbitres
arbitres = liste['referee'].dropna().tolist()

#creation liste des dates
dates = liste['date'].dropna().tolist()

#creation liste des scores
scores = liste['score'].dropna().tolist()

#creation liste des domiciles
domiciles = liste['home_team'].dropna().tolist()

#creation liste des exterieurs
exterieurs = liste['away_team'].dropna().tolist()

#creation liste des possessions domiciles
possession_domicile = liste['home_possession'].dropna().tolist()

#creation liste des possessions exterieurs
possession_exterieur = liste['away_possession'].dropna().tolist()

#creation liste des tirs cadrés domiciles
domicile_cadre = liste['home_shots_on_target'].dropna().tolist()

#creation liste des tirs cadrés exterieurs
exterieur_cadre = liste['away_shots_on_target'].dropna().tolist()

#creation liste des sauvetages domiciles
domicile_sauvetage = liste['home_saves'].dropna().tolist()

#creation liste des sauvetages exterieurs
exterieur_sauvetage = liste['away_saves'].dropna().tolist()

#creation liste des gagnants
gagnants = liste['winner'].dropna().tolist()

iteration = 0
date_avant = ""
with driver.session() as session:

    session.run("MATCH (n) DETACH DELETE n")
#creation des noeuds
    #nom des clubs
    for equipe in (equipes):
        session.run("MERGE (t:Team {name: $name})", name=equipe)
    #nom des stades
    for stade in (stades):
        session.run("MERGE (t:Venue {name: $name})", name=stade)
    #dates des matchs
    for date , domicile , exterieur , gagnant , score in zip (dates , domiciles , exterieurs , gagnants , scores):
        if ( date_avant != date ):
            session.run("MERGE (t:Date {name: $name})", name=date)
            date_avant = date
        if (date_avant == date ):
            nom = f"{domicile} VS {exterieur}"
            if ( gagnant == "Draw" ):
                gagnant = "egalité"
            session.run("MERGE (t:Match {name: $name , score: $score , gagnant: $gagnant} )", name=nom , score=score , gagnant=gagnant)
    #nom des arbitres
    for arbitre in (arbitres):
        session.run("MERGE (t:Referee {name: $name})", name=arbitre)
 
 #creation des relations
    for domicile , exterieur , stade , date , arbitre , pos_dom , pos_ext , dom_cadre , ext_cadre , dom_sau , ext_sau in zip (domiciles,exterieurs,stades,dates,arbitres,possession_domicile,possession_exterieur,domicile_cadre,exterieur_cadre,domicile_sauvetage,exterieur_sauvetage):
        nom = f"{domicile} VS {exterieur}"
        # pour les clubs jouant à domiciles
        session.run("MATCH (t:Team {name: $name}) , (n:Match {name: $nom}) MERGE (t) -[:DOMICILE {possession: $pos_dom , tir_cadre: $dom_cadre , sauvetage: $dom_sau}]-> (n) ", name=domicile , nom=nom , pos_dom=pos_dom , dom_cadre=dom_cadre , dom_sau=dom_sau)
        # pour les clubs jouant à l exterieur 
        session.run("MATCH (t:Team {name: $name}) , (n:Match {name: $nom}) MERGE (t) -[:EXTERIEUR{possession: $pos_ext , tir_cadre: $ext_cadre , sauvetage: $ext_sau}]-> (n) ", name=exterieur , nom=nom , pos_ext=pos_ext , ext_cadre=ext_cadre , ext_sau=ext_sau)
        # pour les stades acceuillant les matches
        session.run("MATCH (n:Match {name: $nom}) , (t:Venue {name: $name}) MERGE (n) -[:JOUÉ_À]-> (t) ", nom=nom , name=stade)
        # pour les arbitres
        session.run("MATCH (t:Referee {name: $name}) , (n:Match {name: $nom}) MERGE (t) -[:ARBITRÉ_PAR]-> (n) ", name=arbitre , nom=nom )
        # pour les matches dans une journée
        session.run("MATCH (t:Match {name: $name}) , (n:Date {name: $nom}) MERGE (t) -[:MATCH_DE]-> (n) ", name=nom , nom=date )
    
driver.close()

