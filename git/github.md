
*GitHub* est un outil de développement web qui permet aux utilisateurs de suivre le travail des autres, de collaborer sur des projets et de télécharger des fichiers.  Il permet également aux développeurs de créer des "repositories" (dépôts) pour stocker et partager leur code.  GitHub est gratuit pour les utilisateurs individuels, mais il existe également des plans payants pour les entreprises.  

 - `"git push"` permet de transférer des fichiers du dépôt local vers le dépôt en ligne. 
 - `"git commit"` permet de sauvegarder les fichiers du dépôt local. 
 - `"git clone"` permet de copier un dépôt en ligne vers le dépôt local. 
 - `"git add"` permet d'ajouter des fichiers au dépôt local. 
 - `"git pull"` permet de récupérer les fichiers du dépôt en ligne vers le dépôt local.

La branche est une fonctionnalité de Git qui permet aux utilisateurs de développer leur code de manière isolée des autres. 
Les utilisateurs peuvent créer une nouvelle branche à partir de leur code principal (la « branche master »), 
puis travailler sur cette nouvelle branche sans affecter le code principal. 
Les utilisateurs peuvent ensuite fusionner leur code de la branche avec la branche master une fois qu'ils ont terminé leur travail.

voilà c'est tout pour le moment


## Les commandes
### Git merge:
Git merge est une commande Git qui permet de fusionner deux branches Git. Cela signifie que vous pouvez prendre le code d'une autre branche et l'ajouter à votre branche actuelle. Cela peut être utile lorsque vous voulez fusionner le travail de plusieurs personnes sur différentes branches.

Exemple:
```
git merge
```
### Git add:
Git add est une commande Git qui permet d'ajouter des fichiers à un dépôt Git. Cela signifie que vous pouvez prendre des fichiers de votre ordinateur et les ajouter au code source d'un projet. Git add peut être utilisé pour ajouter des fichiers à un commit ou pour ajouter des fichiers à une branche.

Exemple:
```
git add .
git add nomdufichier
```

### Git push:
Git push est une commande Git qui permet de publier des commits sur un dépôt Git. Cela signifie que vous pouvez prendre le code de votre ordinateur et le mettre en ligne sur un serveur Git. Git push peut être utilisé pour publier des commits sur une branche ou pour publier des commits sur un dépôt.

Exemple:
```
git push -u
```
### Git pull:
Git pull est une commande Git qui permet de récupérer des commits d'un dépôt Git. Cela signifie que vous pouvez prendre le code d'un serveur Git et le mettre sur votre ordinateur. Git pull peut être utilisé pour récupérer des commits d'une branche ou pour récupérer des commits d'un dépôt.

Exemple:
```
git pull
```
### Git commit:
Git commit est une commande Git qui permet de sauvegarder des modifications dans un dépôt Git. Cela signifie que vous pouvez prendre le code d'un projet et le sauvegarder dans un dépôt Git. Git commit peut être utilisé pour sauvegarder des modifications dans une branche ou pour sauvegarder des modifications dans un dépôt.

Exemple:
```
git commit -m "nom du commit"
git commit -am "nom du commit" (cela va faire la effectuer la commande git add . juste avant)
```
