# Initiation aux challenges de Machine Learning

## Matériel nécessaire

Ce TP se déroule sur Python. Pour le bon déroulement du TP, je vous invite à télécharger la dernière version d'[Anaconda](https://www.continuum.io/Downloads). Python 3 est choisi par défaut. Je vous invite donc à télécharger la version 3 d'Anaconda.

### Installation 

L'installation diffère selon le système d'exploitation. Assurez vous de télécharger la version correspondant à votre processeur : 32 ou 64 bit. Je suppose par la suite que vous avez une version 64 bit de votre système d'exploitation.

Téléchargez le fichier d'installation d'Anaconda sur votre PC et suivez les instructions suivantes selon votre système d'exploitation.

#### Sur Windows

Exécutez le .exe et suivez les instructions de l'interface graphique.

#### Sur Linux et macOS

Ouvrez un terminal, allez vers l'emplacement du fichier d'installation et exécuter le .sh avec la commande :

```
bash Anaconda3-(version)-Linux-x86_64.sh 
```

La balise `(version)` représente la version d'Anaconda téléchargé. Suivez les instructions sur le terminal. A la fin de l'installation votre .bashrc devrait être automatiquement modifié pour pointer vers Anaconda.

### Packages

Pour ce TP, nous aurons besoin de différents modules python. La plupart sont déjà installés avec Anaconda. Pour installer et/ou mettre à jour les packages nécessaires, ouvrez un terminal de commande et exécutez la commande ci-dessous :

``` 
conda install numpy pandas matplotlib scipy jupyter notebook scikit-learn git
```

### Librairies optionnelles

Pour aller plus loin je vous invite à installer la librairie dask et dask-distributed qui pourront servir pour la parallélisation des calculs. Lancez la commande :

```
conda install dask distributed 
```

## Récupérer le dépôt Git

Git est un logiciel de gestion de version, utilisé pour l'integration continue de logiciels. Git est aussi très utilisé par les statisticiens pour collaborer sur leurs scripts, notebooks, notes, articles, etc... Nous utiliserons donc Git pour effectuer ensemble ce TP et apprendre à faire des modifications simultanées et structurées afin de mieux collaborer en équipe.

### Créer un compte GitHub

Nous travaillerons ici sur GitHub, qui est un service d'hébergement web des dépôts Git. Le site possède la plus grande communauté de développeurs et héberge un très grand nombre de logiciels libres. Je vous invite donc à d'abord créer un compte [ici](https://github.com/join?source=header-home). 

### Forker le dépôt GitHub

Le terme `fork` consiste à copier le dépôt d'un utilisateur vers son propre compte. Cela permet d'effectuer des modifications aux codes de l'utilisateur sans modifier le dépôt d'origine de l'auteur principal (lorsque l'on a pas les droits d'écriture). Pour cela, il suffit d'aller sur le dépôt d'un utilisateur et de cliquer sur le bouton `fork` en haut a droite. Le dépôt de ce TP se trouve [ici](https://github.com/NazBen/initiation-ML.git). Après ceci, le dépôt sera copié sur votre compte. Vous travaillerez donc sur cette copie du dépôt dans un premier temps.

### Récupérer le dossier en local

Maintenant que les différents outils sont installés sur votre ordinateur et que vous avez `forké` le dépôt sur votre compte, vous pouvez faire une copie du dépôt, de GitHub vers votre ordinateur en local. Pour cela il suffit d'ouvrir un terminal, se placer dans un dossier et d’exécuter la commande :

```
git clone https://github.com/'Votre pseudo GitHub'/initiation-ML.git
```

Un dossier `initiation-ML` s'est créer sur votre répertoire courant.

### Associer votre dépôt au dépôt local au serveur

Il vous faut maintenant associer votre dépôt local vers le serveur pour que les modifications soient synchronisées. Pour cela, lancez la commande :

```
git remote add origin master https://github.com/'Votre pseudo GitHub'/initiation-ML.git
```

### Premier push

Maintenant que vous avez copié le dossier, je vous invite à faire une légère modification du dépôt. Ajoutez un fichier, corrigez une faute d'orthographe dans le readme.md, ou n'importe quelle autre modification. Une fois la modification effectuée, ouvrez un terminal dans le dossier du dépôt et exécutez :

```
git status
```

Cela vous affiche en couleur les modifications qui ont été effectuées. Si les modifications vous conviennent vous pouvez les ajouter à votre `commit`, qui est la validation de votre modification. Pour ajoutez ces modifications à votre commit, exécutez la commande :

```
git add .
```

Le `.` ajoute l'ensemble des fichiers dans votre commit. Si vous ne souhaitez ajouter qu'un des fichiers, vous pouvez remplacer le `.` par l'emplacement d'un des fichiers modifié.

Vous pouvez maintenant effectuer votre commit. Sachez qu'un commit est toujours associé à un message. Pour une meilleure compréhension des modifications, surtout lorsque plusieurs personnes travaillent sur le même projet, il est important d'être clair et synthétique dans le message. Si les modifications sont très courtes et que le message est lui aussi court, vous pouvez exécuter la commande :

```
git commit -m "Votre message"
```

Si le message est plus long et nécessite une plus grande rédaction, vous pouvez simplement exécuter la commande :

```
git commit
```

Une instance VIM se lance alors vous permettant d'écrire votre texte. Une fois terminé, vous pouvez enregistrer en faisant appuyant sur `echap` et `:wq`. Si vous êtes allergique à VIM, vous pouvez utiliser un autre éditeur (gedit par exemple) via :

```
git config core.editor "Le nom de votre éditeur"
```

Vous pouvez désormais synchroniser votre dépôt local vers le serveur. Pour cela il vous faut faire un `push`. Pour votre premier push, vous devez ajouter l'option `--set-upstream` afin de spécifier que les prochains push seront associé à la `branch` utilisée. Une `branch` peut être vu comme une version de votre dépôt. La branch par défaut est la branch `master`, c'est à dire celle en cours de développement. Nous reviendrons dessus plus tard. Pour finaliser votre push, effectuez la commande :

```
git push --set-upstream origin master
```

Vous devrez ensuite suivre les indications en ajoutant votre identifiant GitHub et votre mot de passe. Par la suite, les pushs se feront uniquement avec la commande :

```
git push
```