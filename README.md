# LIGUE DES CHAMPIONS 2025 - 2026 _ GRAPHE NEO4J

## DESCRIPTION
Ce projet importe les matchs de la Ligue des Champions 2025-2026(tour préliminaire) dans une base de données Neo4j sous forme de graphe.
Les données proviennent du dataset "Champions League Matches 2025-2026" dans le site kaggle.

## Contenu des données
- 150 matchs de la phase préliminaire
- 36 équipes participantes
- Statistiques : possession , tirs , arrêts , résultats

## Structure du graphe

### Noeuds par référence
Team : Les 36 équipes
Match : chaque match joué
Venue : Les stades
Refereee : Les arbitres

### Relations entre noeuds
DOMICILE : les clubs jouant leur match à domicile
EXTERIEUR : les clubs jouant leur match à l'exterieur 
JOUÉ À : Correspondance du match au stade d'acceuil
ARBITRÉ PAR : Désigne le nom de chaque arbitre lors du match
MATCH DE : Correspondance entre la date et les matchs en ce jour

## Fichiers du projet
- ldc.py : fichier contenant les syntaxes de la creation du graphe sur neo4j en python
- champions_league_matches.csv : contient les données dataset récupéré sur le site kaggle
- Neo4j-1e39da71-Created-2026-05-15.txt : c'est un fichier de reference qui permet de visualiser précisement le graphe sur neo4j

## Prerequis
- Python3
- Neo4j Desktop
- Bibliothèques Python : 
  pip install neo4j pandas

## Comment lancer le projet

### 1. Demarrer Neo4j Desktop et ajouter l instance
- lancer Neo4j Desktop et cliquer dans l'onglet "Remote connections" puis sur "add connections" 
### 2. visualiser le graphe 
- inclure le fichier "Neo4j-1e39da71-Created-2026-05-15.txt" et on peut visualiser le resultat dans l onglet "connect" puis "Query"

## Auteur
Ramiandrisoa Sitraka Nathan




