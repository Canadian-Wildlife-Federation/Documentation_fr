.. _cabd-overview:

===============
Aperçu du BDOAC
===============

La base de données
------------------

-----

La Base de données sur les obstacles aquatiques du Canada (BDOAC) est un dépôt central et organisé de données ouvertes et standardisées sur les obstacles et la connectivité au Canada. La BDOAC 1.0 offre actuellement des données pour trois types d’éléments :

#.	Barrages (et structures connexes) V1.2
#.	Chutes V1.0
#.	Passes à poissons V1.0


Consultez notre :ref:`catalogue de données <data-catalogue>` pour voir les définitions complètes et les attributs associés à chacun de ces types d’éléments.

.. important::
   L’une des :ref:`utilisations définies <use-cases>` de la BDOAC est la création d’un inventaire de l’emplacement et de l’état des infrastructures au Canada. Cela signifie qu’en plus de la structure principale du barrage, la :ref:`couche de données relatives aux barrages <dams-layer>` de la BDOAC comprend des structures auxiliaires et latérales associées aux installations de barrage (par exemple, barrages de col, endiguements latéraux et parois de canal) qui ne fragmentent pas nécessairement les systèmes d’eau douce dans le plan amont-aval. Il ne faut donc pas utiliser ces structures pour les analyses de réseau de connectivité ou les exercices de hiérarchisation des obstacles (à moins que vous vous intéressiez précisément aux effets latéraux ou autres de ces structures auxiliaires). Pour aider les utilisateurs à filtrer ces structures, nous utilisons le champ :ref:`Used for Network Analysis (utilisé pour l’analyse de réseau) <useanalysis>` pour indiquer quels points de données ne doivent pas être utilisés pour l’analyse de réseau (``use_analysis = false`` dans les données).

   En outre, comme la couche des barrages a été compilée à partir de jeux de données existants, certains points de données dans le jeu de données des barrages représentent des structures autres que des barrages (par exemple, des centrales électriques, des prises d'eau, des écluses). À l'avenir, nous avons l'intention de retirer ces structures de la couche des barrages et de les placer dans leurs propres types d'entités, mais en attendant, assurez-vous de vérifier les valeurs des attributs de type de structure des entités dans votre jeu de données avant d'effectuer toute analyse.

Pourquoi développer une base de données nationale sur les obstacles à la connectivité des eaux douces? Nous savons que les obstacles aquatiques sont répandus au Canada, qu’il est nécessaire de les éliminer pour restaurer la connectivité entre les écosystèmes d’eau douce et l’accès aux habitats vitaux pour les espèces aquatiques, et que les projets de restauration demandent de grands investissements. Cependant, d’importantes questions restent encore sans réponse : « Combien d’obstacles retrouve-t-on au Canada? Quelle est la superficie des habitats qui est inaccessible aux poissons et aux autres espèces? Comment pouvons-nous déterminer la priorité des obstacles à restaurer et optimiser les avantages que cela conférera aux espèces? » Nous avons besoin d’une source de renseignements complète pour répondre à ces questions, et c’est là que la BDOAC entre en jeu.

La BDOAC permettra à la FCF et à d’autres organisations partout au pays d’évaluer et de signaler l’état de la connectivité des habitats, ainsi que d’informer la gestion et la prise de décision réglementaire. Elle contribuera également à la planification de la restauration des obstacles et à la définition des priorités des projets visant à améliorer la connectivité et les passages à poissons pour les espèces essentielles. De plus, elle influencera les initiatives de recherche et de surveillance qui cherchent à mieux comprendre les effets qu’ont les obstacles sur les écosystèmes d’eau douce et sur les espèces qui y vivent. La BDOAC offrira par la même occasion un forum national d’échange de ressources, de meilleures pratiques et de réussites pour soutenir l’éducation et la sensibilisation du public.

Les couches de données de la BDOAC 1.0 sont-elles parfaites? **Non!** Nos jeux de données sont incomplets, certaines structures ne sont pas répertoriées et nous devons ajouter des attributs manquants à la plupart des points existants (vous verrez beaucoup de valeurs « Unknown » dans les couches). Dans le cadre de la BDOAC 1.0, nous avons compilé :ref:`des données géographiques de sources existantes <data-sources>` et nous les avons dédupliquées, géolocalisées et normalisées selon la structure de données utilisée pour la BDOAC, en plus de cartographier leurs attributs (c.-à-d. introduire des attributs de diverses sources et en assurer le suivi pour un élément individuel). À ce jour, nous avons compilé plus de 100 sources des données sur des barrages, des chutes et des passes à poissons. Ainsi, bien qu’elles ne soient pas parfaites, les couches de données de la BDOAC constituent la source de renseignements la plus complète sur les barrages, les chutes et les passes à poissons du Canada.

Nous nous efforçons de combler les lacunes en matière de données en passant en revue des sources des données non spatiales (par exemple, des rapports, des études scientifiques et des sites Web) susceptibles de fournir des renseignements supplémentaires pour les structures. Combler ces lacunes en matière de données représente une tâche énorme, et c’est la raison pour laquelle nous espérons obtenir l’aide de la population canadienne. Nous travaillons actuellement à la création de nouveaux outils qui permettront aux utilisateurs de soumettre des renseignements à partir de l’outil Web de la BDOAC. En attendant, vous pouvez consulter la page :ref:`Submit Data Updates (soumettre des mises à jour de données) <submit-updates>` ou communiquer avec nous pour découvrir comment vous pouvez nous aider à combler ces lacunes. Nous allons régulièrement mettre en ligne les données actualisées des nouveaux renseignements. Surveillez :ref:`les annonces à venir sur les prochaines mises à jour <whats-new>`!

Consultez `notre billet de blogue <https://blog.cwf-fcf.org/index.php/fr/loutil-interactif-web-sur-les-obstacles-aquatiques-est-desormais-en-ligne-et-presente-des-donnees-sur-lensemble-du-canada/>`_ pour en savoir plus sur le lancement de la BDOAC 1.0, et consultez `le site Web de la Fédération canadienne de la faune <https://cwf-fcf.org/fr/explorer/permettre-le-passage-du-poisson/obstacles-aquatiques-bd.html>`_ pour obtenir de plus amples renseignements sur les projets, y compris des FAQ.

.. attention::

   *Les données de la BDOAC sont mises à la disposition de tous grâce à la licence* `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/deed.fr>`_ *. Cette licence vous permet de transmettre et d’adapter les données, du moment que vous mentionnez la source et que vous distribuez les données dérivées en utilisant la même licence CC BY-SA 4.0.*

L’outil Web
-----------

-----

Nous sommes emballés par `l’outil Web BDOAC <https://aquaticbarriers.ca/>`_ qui permet d’explorer les données et d’y accéder facilement au moyen de votre navigateur Web. L’outil et le site de documentation sont offerts en français et en anglais.

L’interface cartographique Web permet :

- d’explorer les données sur les obstacles et les passes à poissons, et de voir leurs attributs en cliquant sur les points;
- de passer d’un mode de visualisation de carte de base standard à une imagerie satellite;
- de filtrer les couches en fonction de l’emplacement (par exemple, la province ou le bassin versant) ou des attributs (par exemple, l’utilisation des barrages);
- de télécharger les données dans divers formats (Shapefile, GeoPackage, KML et CSV);
- de voir les sources des données utilisées (jusqu’à maintenant) pour créer la BDOAC.

Consultez la section :ref:`Outil Web de la BDOAC <web-tool>` pour apprendre comment naviguer dans l’outil Web et l’utiliser.

Quelle sera la suite des choses? 
--------------------------------

-----

Nous avons des projets ambitieux pour la BDOAC et nous continuerons de travailler pour combler les lacunes en matière de données sur les barrages, les chutes et les passes à poissons à l’échelle du Canada, mais l’un de nos principaux objectifs pour l’année à venir sera de commencer à compiler les données sur les franchissements de cours d’eau et de les intégrer à la BDOAC.

La BDOAC 1.0 représente un pas essentiel vers l’atteinte des données qui sont nécessaires au soutien de la conservation de la connectivité et aux projets de restauration des passages à poissons, mais les barrages ne sont que l’un des types de structures artificielles qui fragmentent les écosystèmes d’eau douce au Canada. Bien que les barrages constituent souvent des obstacles majeurs à la connectivité, l’augmentation des structures de plus petite taille, telles que les franchissements de cours d’eau dont on compte plus d’un million au pays (p. ex., les traversées routières et ferroviaires ou les passages de sentiers), pose d’importants problèmes à la connectivité des eaux douces en raison des effets cumulatifs de leur quantité. Dans le cadre de la prochaine phase de la BDOAC, la FCF cherche à intégrer les franchissements de cours d’eau à la base de données. Elle compte y parvenir en créant une structure de données standardisées et en compilant les données de sources existantes. La FCF continuera de collaborer avec des partenaires, des parties prenantes et des parties intéressées dans le but de veiller à ce que les données relatives aux franchissements de cours d’eau soient utiles et accessibles aux professionnels du pays.