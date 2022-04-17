import main


def Coffre_Base():
    verrouiller = main.verrouiller

    if main.entre == main.mdp_default:
        print("Mot de passe accepte")
        verrouiller = False
    elif verrouiller:
        Q = input("Avez vous oublié votre mot de passe ? si oui ecrivez O, sinon N")
        if Q == 'O':
            mdp_oublie = input('Ecrivez votre nouveau mot de passe')
            mdp_oublie2 = input('Comfirmer le mot de passe')
            if mdp_oublie != mdp_oublie2:
                print("Erreur les mot de passe sont different")
                mdp_oublie2 = input('Comfirmer le mot de passe')
            if mdp_oublie == mdp_oublie2:
                print("Le changement du mot de passe a reussi")
                main.verrouiller = False
            else:
                print("Ok")
                main.verrouiller = True


def Coffre_Moyen():
    verrouiller = input('True ou False')
    if verrouiller == 'True':
        verrouiller = True
    else:
        verrouiller = False

    if main.entre == main.mdp_default:
        print("Mot de passe accepte")
        verrouiller = False
    elif verrouiller:
        Q = input("Avez vous oublié votre mot de passe ? si oui ecrivez O, sinon N")
        if Q == 'O':
            mdp_oublie = input('Ecrivez votre nouveau mot de passe')
            mdp_oublie_2 = input('Comfirmer le mot de passe')
            mdp_obli = input('Entrez un second mot de passe')
            mdp_obli_2 = input('Comfirmer le mot de passe')
            mdp_origin = ""
            if mdp_oublie == mdp_oublie_2:
                print("Les deux mots sont corrects")
            else:
                print("Reviens plus tard")
            if mdp_oublie == mdp_obli_2:
                print("Les deux mots sont corrects")
                mdp_oublie += mdp_obli == mdp_origin

                verrouiller = False
            else:
                print("Ok")
