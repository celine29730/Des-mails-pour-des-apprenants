import mysql.connector as mysqlpyth
import os 


#ouverture du fichier apprenantmail
with open("C:/Users/utilisateur/Documents/apprenant/apprenantmail.txt", 'r') as fichier :
    mail = fichier.readlines()
print(mail)

#Python se connecte sur la bdd

    
bdd = mysqlpyth.connect(user='root', 
    password='root', 
    host='localhost', 
    port="8081", 
    database='binomotron')

# récupèration du curseur 
cursor = bdd.cursor()

# requete recuperant les elements de la table etudiant
query1="SELECT id_etudiant, nom, prenom FROM etudiant;"

# exécute la requête grâce au curseur
cursor.execute(query1)
etudiant=cursor.fetchall()


#création d'une liste de nom à partir de la requête
liste_etudiant=[]
for x in etudiant:
    nom_etudiant=x[1].replace("'", "").replace(" ", "-").lower()
    prenom_etudiant = x[2].replace("'", "").replace(" ", "-").lower()
#permet la gestion d'éventuels doublons
    liste_etudiant.append(prenom_etudiant+"."+nom_etudiant)
print(liste_etudiant)    

#requête pour ajouter une colonne mail etudiant à la table etudiant
#query2 = 'ALTER TABLE etudiant ADD COLUMN mail_etudiant VARCHAR(150) NOT NULL'
#cursor.execute(query2)


#comparaison des noms des listes etudiants de la bdd et des noms de la liste de mails
#insertion des mails dans la colonne mail_etudiant de la table etudiant
#print(liste_etudiant)
for i, nom_etud in enumerate(liste_etudiant):
    for elem in mail:
        if nom_etud in elem:
            query = f'UPDATE etudiant SET mail_etudiant="{elem}" WHERE nom="{etudiant[i][1]}";'
            cursor.execute(query)
            break



bdd.commit()
#Fermeture du curseur et de la base de données 
cursor.close()
bdd.close()