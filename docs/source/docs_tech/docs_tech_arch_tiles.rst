======================
CHyF Services API REST
======================

Aperçu
------

-----

Projection
~~~~~~~~~~

Toutes les coordonnées sont affichés en format latitude/longitude (EPSG:4617).

Nombre maximum d’éléments
~~~~~~~~~~~~~~~~~~~~~~~~~

Pour tous les points de fin de l’API des éléments ci-dessous, l’application renvoie un maximum de 5 000 éléments. Vous pouvez modifier ce réglage si vous le voulez.

.. admonition:: Remarque
    Les données disponibles par l’entremise des points de fin CHyF ne comprennent pour l’instant que les données disponibles pour les huit régions incluses dans notre projet pilote – vous pouvez le voir sur la couche Hydro Networks de l’outil Web de la BDOAC. L’équipe de la BDOAC travaille d’arrache-pied à la préparation de nouvelles données sur les réseaux hydrographiques qui seront ajoutées ultérieurement.
    
Spécification d’API
~~~~~~~~~~~~~~~~~~~

La plus récente spécification Open API V3 est disponible sur le serveur :

https://chyf-web.azurewebsites.net/chyf-web/v3/api-docs.yaml (YAML)

https://chyf-web.azurewebsites.net/chyf-web/v3/api-docs (JSON)

Points de fin d’élément
-----------------------

-----

Format
~~~~~~

Le serveur API de base pour les points de fin CHyF est le suivant : https://chyf-web.azurewebsites.net/chyf-web/

Le seul format pris en charge pour les points de fin d’élément est GeoJSON.

Les attributs d’élément GeoJSON diffèrent selon le type d’élément, mais comprennent un sous-ensemble des attributs suivants :

* ``id`` - identifiant du système

* ``ef_type`` - code représentant le type de trajet d’écoulement  

* ``ef_type_name`` - description en anglais de l’attribut ef_type. 

* ``ec_type`` - code représentant le type de bassin récepteur  

* ``ec_type_name`` - description en anglais de l’attribut ec_type.

* ``rank`` - rang (primaire ou secondaire) associé au trajet d’écoulement

* ``length`` - longueur du trajet d’écoulement

* ``aoi_id`` - identifiant de zone d’intérêt CHyF

* ``aoi_name`` - nom de zone d’intérêt CHyF

* ``ecatchment_id`` - bassin récepteur contenant le trajet d’écoulement

* ``rivernameid1`` - identifiant de nom CHyF primaire

* ``rivername1_en`` - nom anglais de l’élément

* ``rivername1_fr`` - nom français de l’élément

* ``rivernameid2`` - identifiant de nom CHyF secondaire

* ``rivername2_en`` - nom anglais de l’élément

* ``rivername2_fr`` - nom français de l’élément

* ``lakenameid1`` - identifiant de nom de lac CHyF primaire

* ``lakename1_en`` - nom anglais de l’élément

* ``lakename1_fr`` - nom français de l’élément

* ``lakenameid2`` - identifiant de nom CHyF secondaire

* ``lakename2_en`` - nom anglais de l’élément

* ``lakename2_fr`` - nom français de l’élément

Trouver un élément unique
~~~~~~~~~~~~~~~~~~~~~~~~~

|chyfuuid|

Renvoie l’élément unique représenté par la valeur uuid. Cet élément peut être un trajet d’écoulement, un bassin récepteur ou un rivage. Veuillez noter que le renvoi de nexus n’est pas pris en charge pour le moment.

Recherche par nom ou type d’élément (un ou plusieurs éléments)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|singlemultisearch|

Renvoie tous les éléments qui correspondent aux paramètres de recherche.

* ``name`` – OBLIGATOIRE – le nom d’élément recherché. Toutes les recherches sont insensibles à la casse.

* ``max-results`` – FACULTATIF – le nombre maximal d’éléments à renvoyer. La valeur par défaut est de 5 000.

* ``result-type`` – FACULTATIF (mais recommandé) – définit la façon dont les résultats sont renvoyés. Valeurs valides : BBOX, ALL, GROUPBYTYPE et GROUPBYNAME. La valeur par défaut est BBOX. Nous vous recommandons de tester la même requête avec différents paramètres result-type afin de déterminer celui qui répond le mieux à vos besoins.

  * ``BBOX`` – pour chaque nom correspondant, un élément unique est renvoyé avec la géométrie représentant le cadre d’objet de tous les éléments correspondants.

  * ``ALL`` – pour chaque nom correspondant, chaque ligne de base de données correspondante est renvoyée sous la forme d’un élément avec la géométrie d’origine (chaîne de lignes/polygone).

  * ``GROUPBYTYPE`` - pour chaque nom correspondant, les lignes de base de données correspondantes sont fusionnées par type de géométrie. Un maximum de deux éléments sera renvoyé par nom : un pour les chaînes de lignes et un pour les polygones.

  * ``GROUPBYNAME`` - pour chaque nom correspondant, les lignes de base de données correspondantes sont fusionnées en un élément unique. Un élément sera renvoyé par nom, et cet élément contiendra une collection géométrique de chaînes de lignes et de polygones.

* ``match-type`` - FACULTATIF – le type de correspondance à effectuer. Les valeurs valides sont les suivantes : EXACT et CONTAINS. La valeur par défaut est CONTAINS.

* ``feature-type`` - FACULTTIF – le type d’élément à rechercher. Les valeurs valides comprennent les suivantes : WATERBODY, FLOWPATH et CATCHMENT. Vous pouvez effectuer plusieurs entrées pour rechercher plusieurs types d’éléments. Si vous n’entrez rien, tous les types d’éléments seront recherchés.

Exemples
++++++++

Renvoie des renseignements sur un élément unique dont l’identifiant est f2e7c275-5425-4d19-9db5-d6916b940799 : 
``https://chyf-web.azurewebsites.net/chyf-web/features/f2e7c275-5425-4d19-9db5-d6916b940799``

Renvoie toutes les lignes de base de données pour tout type d’élément correspondant au nom South Berland : 
``https://chyf-web.azurewebsites.net/chyf-web/features?name=South+Berland&result-type=ALL``

Renvoie un maximum de cinq lignes de base de données pour tout type d’élément correspondant au nom Berland (insensible à la casse) : 
``https://chyf-web.azurewebsites.net/chyf-web/features?name=Berland&result-type=ALL&max-results=5``

Renvoie un maximum de cinq lignes de base de données pour les trajets d’écoulement correspondant au nom Berland (insensible à la casse) : 
``https://chyf-web.azurewebsites.net/chyf-web/features?name=Berland&result-type=ALL&max-results=5&feature-type=FLOWPATH``


Exportations de réseau
----------------------

-----

Vous pouvez extraire les jeux de données de réseau CHyF au moyen de l’API graphique. Cette exportation comprend tous les trajets d’écoulement, les nexus et les bassins récepteurs pour la zone demandée avec les renseignements de réseau appropriés inclus dans les éléments.

Format
~~~~~~

Geopackage est le seul format pris en charge pour les exportations de réseau.

API
~~~

Les exportations de réseau sont limitées à 500 000 trajets d’écoulement. Vous pouvez spécifier la zone d’intérêt en fournissant un cadre d’objet ou une ou plusieurs zones d’intérêt.

* ``aoi`` - FACULTATIF – une liste délimitée commune des noms abrégés de zone d’intérêt
* ``bbox`` - FACULTATIF – l’étendue des éléments à inclure dans l’exportation : 'minlong,minlat,maxlong,maxlat'

Il faut fournir au moins une valeur aoi ou bbox.

Exemple
~~~~~~~

Renvoie une exportation de graphique pour la zone d’intérêt 02OJ000 : 
``https://chyf-web.azurewebsites.net/chyf-web/graph?aoi=02OJ000``
  


Service de tuiles vectorielles
------------------------------

-----

Format
~~~~~~

Le seul format pris en charge pour les services de tuiles vectorielles est MVT (mapbox vector tile).

Points de fin
~~~~~~~~~~~~~

``/chyf-web/tiles/water/{z}/{x}/{y}.{format}``

Point de fin pour les éléments d’eau. Cela inclut les cours d’eau simples et les plans d’eau polygonaux. Les éléments de sortie comprennent les attributs suivants :

.. csv-table:: 
    :file: tbl/flow_attributes_fr.csv
    :widths: 30, 70
    :header-rows: 1

``/chyf-web/tiles/ecatchment/{z}/{x}/{y}.{format}``

Contient des bassins récepteurs. Actuellement, aucun bassin récepteur n’est chargé dans la base de données CHyF, et ces tuiles vectorielles seront donc vides. Les éléments de sortie comprennent les attributs suivants :

.. csv-table:: 
    :file: tbl/catch_attributes_fr.csv
    :widths: 30, 70
    :header-rows: 1

``/chyf-web/tiles/nhnworkunit/{z}/{x}/{y}.{format}``

Point de fin pour les unités de travail polygonales RHN. Les éléments de sortie comprennent les attributs suivants :

.. csv-table:: 
    :file: tbl/wu_attributes_fr.csv
    :widths: 30, 70
    :header-rows: 1
