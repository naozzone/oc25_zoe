//var message = 'bienvenue';

// console.log(message);

// function ma_fonction() {
//      console.log('ma fonction');
//}

// ma_fonction();

//
//

//
//
//

//function ajouter_perso(){
    //var nom_perso = 'Jean';

    //var nouveau_li = document.createElement('li');
   // var nouveau_text = document.createTextNode(text_personnage);
    //console.log('perso');
//}

var jean = {
    nom: 'jean' ,
    classe: 'guerrier',
    niveau: 2,
    passer_niveau: function (){
        this.niveau++;
    }
    
}

console.log(jean);
console.log(jean.niveau);
jean.passer_niveau(); 
console.log(jean.niveau);

function creer_personnage(nom, classe, niveau){
    var nouveau_personnage={
    nom: nom,
    classe: classe,
    niveau: niveau,
    passer_niveau: function (){
        this.niveau++;
    },
    creer_li: function() {
        var li_personnage = document.createElement('li');
        var texte_personnage = document.createTextNode(
            this.nom + '(' + this.classe + ', niveau' + this.niveau + ')'
        );
        li_personnage.appendChild(texte_personnage); //relier les deux éléments
        li_personnage.setAttribute('class', this.classe)
        return li_personnage
    }
}
 return nouveau_personnage;
};

var nicole = creer_personnage('nicole','voleur',3);

console.log(nicole)

var troupe = [
    creer_personnage('jean','guerrier',2),
    creer_personnage('nicole','voleur',3),
    creer_personnage('matteo','magician',1)
]

console.log(troupe);
console.log(troupe[0])

for (var i=0; i < troupe.length; i++) {
    console.log(troupe[i].nom);
}

for (var i = 0; i < troupe.length; i++) {
    var perso = troupe[i];
    // var li_personnage = document.createElement('li');
    // var texte_personnage = document.createTextNode(perso.nom); //créer un élément texte
    // li_personnage.appendChild(texte_personnage); //relier les deux éléments 
    li_personnage = perso.creer_li();


    var liste_perso = document.getElementById("liste_de_perso");
    liste_perso.appendChild(li_personnage);
}

