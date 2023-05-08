from classes.Student import showStudent,printing
#x = "Python est magique"
#print(x)
#def myfunction(nom):
#   print("Bonjour " +nom)
if __name__ == '__main__':
    print("--------Afficher Bonjour-------")

    showStudent()
    
    print("--------Afficher Printing-------")

    printing()

    """class Personne:
        def __init__(self,name,age):
            self.name=name
            self.age=age

        def __str__(self) -> str:
            pass
            #String laterale
            #Gabarit des Latereaux
            #return f"{self.name}({self.age})"

        def showPerson(self):
            print(self.name,self.age)
    print("--------Affichage de la classe parrent-------")
    p= Personne("Jean",23)
    print(p.name)
    print("--------Affichage de la classe dérivée-------")
    class Student(Personne):
        def __init__(self,name,age, adress):
            self.name=name
            self.age=age
            self.adress=adress
    s = Student("Yves",20,"Ngagara")
    print(s.adress)"""
    #print(s.name, s.age)
    #Les collections
    """
    1.Les lists [] sont ordonnées et changeables
    2.Les tuples () sont ordonnées et inchangeables
    3.Les sets {} ne sont pas ordonnées, inchangeables, non index
    4.Les dictionnaires {}
    """
    #Les listes
    #fruits = ['Mangue', 'Banane','Avocat']

    #Affichage avant insertion d'un nouveau fruit
    #print("----------Affichage avant insertion d'un nouveau fruit--------")
    #print(fruits[0:1])
    """
    for f in fruits:
        print(f)
    
    print("----------Affichage apres insertion d'un nouveau fruit--------")

    fruits.insert(2, 'Pasteque')
    #fruits.append('Pasteque')
    for f in fruits:
        print(f)"""
    """student = {"nom": "Ngabirano",
             "Prenom": "Guy Michel",
             "adresse":"Bujumbura-Ngagara"}"""
    #Les sets 
    """jours={"Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"}
    
    for j in jours:
        print(j)"""
    #Les dictionnaires
    """students={"first_name":"Guy Michel",
             "last_name":"Ngabirano",
             "tel":"67868689",
             "email":"ngabiranog8@gmail.com"}

    print("----------Affichage des cles--------")
    
    for x in students.keys():
        print(x)
    print("----------Affichage des valeurs--------")

    for s in students.values():
        print(s)

    print("----------Affichage des cles/valeurs--------")
    for k,v in students.items():
        print(f"{k}:{v}")"""

    """def myfunction(nom):
        print("Bonjour " +nom)
    myfunction("Guy")"""

   #x,y,z=1,2,3
   #print(x)
   #print(y)
   #print(z)"""
   #print("Hello class")
   #a = 4
   #b = 6
   #c = "Bonjour"
   #d = " Tout le monde" 
   # Les operateurs d'affectation
   #print(10+5)
   #print(10-5)
   #print(10*5)
   #print(10/5)
   #print(10%3)
   #print(5**2)
   # Les operateurs de comparaison
   # inferieur ou égal : <=
   # superieur ou égal : >=
   # inferieur : <
   # superieur : >
   # égal : ==
   # different : !=
   #print(a+b)
   #print(c+d)
   #x = "Bonjour"
   #x = "L\'arbre"
   #print(x)
   #print(len(x))
   #print(x[3])
   #for a in x:
       #print(a)
"""salutation = "Bonjour"
for s in salutation :
    print(s)

a,b = 5,10  

if a == b or a > 7:
    print(a)
elif a < b :
    print(a)
else :
    print(b)"""
"""i = 1
while i < 10:
    i+=1
    if i==5 :
        continue
    print(i)
    #break
    #i += 1"""