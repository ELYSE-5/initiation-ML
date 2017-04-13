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
conda install numpy matplotlib scipy jupyter notebook scikit-learn git
```

### Librairies optionnelles

Pour aller plus loin je vous invite à installer la librairie dask et dask-distributed qui pourront servir pour la parallélisation des calculs. Lancez la commande :

```
conda install dask distributed 
```

## Récupérer le dossier du TP

Maintenant que les différents outils sont installés, nous pouvons faire une copie du dépot sur le serveur, vers votre ordinateur en local. Pour cela il suffit d'ouvrir un terminal, se placer dans un dossier et de lancer la commande :

```
git clone https://github.com/NazBen/initiation-ML.git
```
