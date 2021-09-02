# Interfacer une Pile/ LIFO
(une pile sera aussi nommer LIFO)

## Définition de la Pile/ LIFO
La Pile est une structure en programmation qui permet le stokage de données et qui fonctionne selon le principe LIFO (Last In Fisrt Out). Le dernier element passé à la pile sera la premier à sortir.

## Activité
Avec les éléments fournis dans la description créez une Pile fonctionnel, qui respecte les spécification données.

### Spécification
Vous devez créer une classe nommer "Pile" suivant les specifications suivantes:
- La pile doit utiliser une "list" python et pouvant accepter les données de base.
- il doit y avoir une fonction pour verifier si la pile est vide
- il doit y avoir une fonction pour ajouter un obj.
- il doit y avoir une fonction pour recuperer le dernier elements donné à la liste, puis le supprimer.
- La class doit valider le test de base PyTest. (def test_PileLIFO_base() donné dans le dossier)


```python
class Pile:
    def __init__(self) -> None:
        #create and init a list, this is our data structure
        #self.varName #use "self." in your class

    def is_void(self) -> bool:
        if True:
            return True
        else:
            return False

    def append(self, obj) -> None:
        #just append "obj" to this pile

    def get(self):
        #return the last obj of this list and delete it
```

