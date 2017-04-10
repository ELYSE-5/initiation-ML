# Initiation au challenge de Machine Learning

## Matériel nécessaire

Nous travaillerons sur Python pour ce TP. Pour le bon déroulement du TP, je vous invite à télécharger la dernière version d'[Anaconda](https://www.continuum.io/Downloads). Pour ce TP nous travaillerons sur la version 3 de Python. Je vous invite donc à télécharger Anaconda pour python 3.

### Installation 

#### Sur Windows

Exécuter le .exe et suivre les instructions.

#### Sur Linux et macOS

Exécuter le .sh :

```
bash Anaconda3-(version)-Linux-x86_64.sh 
```

Le .bashrc devrait être automatiquement modifié pour pointer vers Anaconda.

### Packages

Nous aurons besoin de différents modules python. Ouvrez un terminal de commande et exécutez la commande ci-dessous pour installer et/ou mettre à jour les packages nécessaires:

``` 
conda install numpy pandas matplotlib scipy jupyter notebook scikit-learn git
```

### Librairies optionnelles

Pour aller plus loins certaines librairies sont intéressantes et peuvent servir pour la parallélisation.

```
conda install dask distributed 
```

## Créer un compte GitHub

Nous travaillerons ici sur GitHub, qui est un service d'hébergement web des dépots Git. Le site possède la plus grande communauté de développeurs et héberge un très grand nombre de logiciels libres. Je vous invite donc à vous créer un compte [ici](https://github.com/join?source=header-home). 

## Forker le dépot GitHub

Le terme `fork` consiste à copier le dépot d'un utilisateur vers son propre compte. Cela permet d'effectuer des modifications aux codes de l'utilisateur sans modifier le dépot d'origine de l'auteur principal. Pour cela, il suffit d'aller sur le dépot d'un utilisateur et de cliquer sur le bouton `fork` en haut a gauche. Le dépot de ce cour ce trouve [ici](https://github.com/NazBen/initiation-ML.git).

## Récupérer le dossier en local

Maintenant que les différents outils sont installés sur votre ordinateur et que vous avez `forkez` le dépot sur votre compte, vous pouvez faire une copie du dépot, de GitHub vers votre ordinateur en local. Pour cela il suffit d'ouvrir un terminal, se placer dans un dossier et de lancer la commande :

```
git clone https://github.com/'Votre pseudo GitHub'/initiation-ML.git
```

Un dossier `initiation-ML` s'est créer sur votre répertoire courant.

## Associer votre dépot au dépot local au serveur

Il vous faut maintenant associé votre dépot local vers le serveur pour que les modifications soient syncronisées dessus.

```
git remote add origin master https://github.com/'Votre pseudo GitHub'/initiation-ML.git
```

## Premier push

Maintenant que vous avez copiez le dossier, je vous invite à faire une légère moidification du dépot. Ajoutez un fichier, corrigez une faute dans le readme.md, ou autre. Une fois la modification effecuté, ouvrez votre terminal dans le dossier du dépot et exécutez :

```
git status
```

Cela vous affiche en couleur les modifications qui ont été effectuées et dans quels fichiers. Si les modifications vous conviennent vous pouvez les ajouter à votre `commit`, qui sera la validation de votre modification. Pour ajoutez ces modifications à votre commit, executez la commande 

```
git add .
```

Ceci ajoute l'ensemble des fichiers dans votre commit. Si vous ne souhaitez ajouter qu'un des fichiers, vous pouvez remplacer le `.` par l'emplacement de votre fichier.

Vous pouvez maintenant effectuer votre commit. Sachez qu'un commit est toujours associé à un message. Pour une meilleur compréhension des modifications, surtout lorsque plusieurs personnes travaillent sur le même projet, il est important d'être clair et synthétique dans le message. Si les modifications sont très courtes et que le message est lui aussi court, vous pouvez exécuter la commande :

```
git commit -m "Votre message"
```

Si le message est plus long et nécessite une plus grande rédaction, vous pouvez simplement éxecuter

```
git commit
```

Puis une instance VIM se lancera pour ecrire votre texte. Une fois terminé, vous pouvez enregistrer en faisant `echap` et `:wq`. Si vous êtes allergique à VIM, vous pouvez utiliser un autre editeur (gedit par exemple) via :

```
git config core.editor "Votre editeur"
```

Vous pouvez désormais syncroniser votre dépot local vers le serveur. Pour cela il vous faut faire un `push`. Pour votre premier push, vous devez ajouter l'option `--set-upstream` pour specifier que vos prochains push seront associé à la `branch` utilisée. Une `branch` est peut être vu comme une version de votre dépot. La branch master est la branche par défaut, c'est à dire celle en cours de développement. Nous reviendrons dessus plus tard. Pour finaliser votre push, effectuez donc la commande :

```
git push --set-upstream origin master
```

Vous devrez ensuite suivre les indications en ajoutant votre identifiant GitHub et votre mot de passe. Par la suite, le push se feront uniquement avec la commande :

```
git push
```