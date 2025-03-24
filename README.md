# Démineur avec IA integrée 🎮🤖

## Description
Ce projet est une implémentation du jeu classique **Démineur** en **Python** en utilisant **PyQt6** pour l'interface graphique. Il intègre également une **IA d'assistance** qui aide le joueur en lui indiquant :

- ✅ **Les cases sûres** à cliquer (**vert clair**)
- ⚠️ **Les cases suspectes** où une mine pourrait être cachée (**jaune**)

L'objectif est d'offrir une expérience de jeu améliorée tout en permettant aux joueurs d'apprendre à mieux détecter les mines ! 🚀

## Fonctionnalités 🛠️
- Interface graphique intuitive avec PyQt6
- Clic **gauche** pour révéler une case
- **Clic droit** pour poser/enlever un drapeau 🚩
- Affichage automatique des mines en cas de défaite 💣
- **Bouton IA** pour suggérer un coup sûr ou signaler une case dangereuse 🤖

## Installation 🔧
1. Clonez le dépôt :
   ```sh
   git clone https://github.com/MohaYass92/Demineur-Intelligent
   cd demineur-pyqt6
   ```
2. Installez les dépendances :
   ```sh
   pip install PyQt6
   ```
3. Lancez le jeu :
   ```sh
   python demineur.py
   ```

## Comment fonctionne l'IA ? 🤯
L'IA analyse l'état actuel de la grille et applique la logique suivante :
1. Si une **case sûre** est détectée (zéro mines autour), elle est **mise en vert** pour être cliquée en toute sécurité.
2. Si aucune case sûre n'est trouvée, l'IA met en **jaune** une case suspecte où une mine est possible.
3. L'IA ne joue pas automatiquement mais **donne des indices** pour guider le joueur !

## Améliorations futures 🚀
- Ajouter une **difficulté progressive**
- Intégrer une IA plus avancée pour **résoudre automatiquement** certaines grilles
- Améliorer l'affichage des scores et statistiques

## Contributions ✨
Toute contribution est la bienvenue ! N'hésitez pas à faire un **fork** et proposer des améliorations via une **pull request**.

🎉 **Bon jeu !** 🎉

