import Coffre

print("Bienvenue dans le coffre fort")
mdp_default = 'Default'
verrouiller = True
while verrouiller:
    User = input('Quel est votre nom')
    entre = input("Entrez le mot de passe")
    lvl_security = input('Quel est le niveau de sécurité que voulez vous ?')
    if lvl_security == 'Faible':
        Coffre.Coffre_Base()
    elif lvl_security == 'Moyen':
        Coffre.Coffre_Moyen()
