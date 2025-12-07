# Projet WEB
https://bugnon.github.io/oc-2025/2_web/

# Cahier des charges

° Le site web doit contenir au minimum quatre pages dans quatre fichiers HTML différents, dont une page d’accueil.

-index.html

-oc.html

-lewis.html

-zale.html

-ace.html

-realism.html

°La page d’accueil doit présenter le sujet traiter et offrir au visiteur une table des matières du site web avec un lien vers les pages correspondantes et une brève description du contenu.
````
    <div class="liencategorie">
        <a href="oc.html">Original Character</a>  
        <a href="realism.html">Realism</a>
    </div>
````
°Il doit y avoir une barre de navigation pour naviguer entre les quatre pages.
````
 <div class="liencategorie">
        <a href="oc.html">Original Character</a>  
        <a href="realism.html">Realism</a>
    </div>
````
°Chaque page doit contenir au moins 100 mots. 

°Le sujet traité doit être liés aux STIM et le contenu (texte, images, équations, code, animations, etc.) doit être cohérent, pertinent et maîtrisé par l’élève.

°La page web doit contenir soit des équations, soit du code informatique, soit un formulaire dynamique. 

°Le site web doit être stylé avec une feuille CSS. 
````
        <link href="css/index.css" rel="stylesheet">
````
°Il doit y avoir une animation réalisée avec canvas. (Exemples) 
````
const canvas_image = document.getElementById ("image");
const ctx_image = canvas_image.getContext("2d");

const img_tiger = new Image();


 //img_tiger.onload = function() {
  //   ctx_image.drawImage(img_tiger, 0, 0, 50, 50);
// }
 //img_tiger.src ="/2_web/image/tiger.PNG";


const canavasSizeX = 500;
const canavasSizeY = 500;
const dx = 1;
const dy = 1;
var x = 1;
var y = 1;



function init() {
    img_tiger.src ="/2_web/image/tiger.PNG"
    window.requestAnimationFrame(draw);
}


function draw() {
    ctx_image.clearRect(0,0,500,500);

    if (x > canavasSizeX) {
      ctx_image.translate(-canavasSizeX, -canavasSizeY);
        x = 1;
        y = 1;
    } else {
        ctx_image.translate(-canavasSizeX, -canavasSizeY);
        ctx_image.translate(dx,dy);
        x = x + dx;
        y = y + dy;
    }
    window.requestAnimationFrame(draw);
}

init ()
````
°Le code doit être sur GitHub est être déployé sur le web avec GitHub Pages. 

https://naozzone.github.io/oc25_zoe/2_web/index.html 

°La page doit pouvoir s’adapter aux petits écrans (smartphone).

## Sujet traité

j'ai traité comme sujet pour ce site web mes propres dessins que ce soit digital ou autre techniques. J'ai utilisé mes personnages que j'avais déjà travaillé pour un projet en anglais.

## Maquette
Voici la première maquette du visuel du site web. Les pages ont été assez simplifées.
![Untitled_Artwork](https://github.com/user-attachments/assets/2cb3af6a-6411-4191-bd2c-39196cd84fde)

Le style des pages de bases vont rester très noir/blanc, car les pages avec mes personnages seront "personnalisées" pour chaque personnage.

## comment le code est organisé
voici comment j'ai organisé les fichiers sur visual studio code :

2_web

|

| css -> toutes les pages de css

|

|

| image -> toutes les images qui apparaisent sur le site

|

| 

| js

| 

tout le contenu en html...

Chaque pages d'html a sa propre page de css pour que la personnalisation des pages soient plus simple. 

## Difficultés

- La mise en page de toutes les images

- la réalisation d'une animation canvas ( ratée )

- déployer en site depuis github

- des images de fond qui ne voulaient pas apparaitre en deployant le site sur github


