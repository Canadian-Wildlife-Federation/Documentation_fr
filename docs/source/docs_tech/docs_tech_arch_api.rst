.. raw:: html

    <style> .green {color: #2a997d} </style>

.. role:: green    


.. _cabd-rest-services:

CABD Services API REST
######################

.. _api-overview:

Aperçu
******

-----

.. _api-projection:

Projection
==========

Toutes les coordonnées sont affichées en format latitude/longitude (EPSG:4617).

.. _api-max-features:

Nombre maximum d’éléments
=========================

Pour tous les points de fin de l’API des éléments« Feature API » ci-dessous, l’application renvoie un maximum de 55 000 éléments. Vous pouvez modifier ce réglage si vous le voulez.

.. _api-specification:

Spécification d’API
===================

La plus récente spécification Open API V3 est disponible sur le serveur :

https://cabd-web.azurewebsites.net/cabd-api/v3/api-docs.yaml (YAML)

https://cabd-web.azurewebsites.net/cabd-api/v3/api-docs (JSON)

.. _api-endpoints:

Points de fin de l’API
**********************

-----

Le serveur API de base pour les points de fin de la BDOAC est le suivant : ``https://cabd-web.azurewebsites.net/cabd-api``.

.. admonition:: Remarque
    
    Les demandes d’API décrites dans les sections suivantes peuvent contenir un ou plusieurs paramètres entourés de chevrons (< et >) et accentués par la couleur verte. Si une demande d’API est faite au moyen d’un ou de plusieurs des paramètres énumérés, le paramètre choisi doit être remplacé par une valeur prédéfinie appropriée. 
    
    **Exemple:**

    |requestex1|


.. _feature-type-endpoints:

Points de fin des métadonnées des types d’éléments
==================================================

Le format de sortie de tous les points de fin des types d’entités est ``JSON``.

Les types d’éléments existants sont les suivants : ``barriers``, ``dams``, ``waterfalls``, ``fishways``, ``medium``, et ``big``. Consultez la section :ref:`Modèle d’élément mis en œuvre <implemented-feature-model>` pour voir la définition de chaque type d’élément.

``/features/types/``

    Renvoie la liste des types d’éléments. Chaque objet de type d’élément comprend une URL qui répertorie les métadonnées pour le type d’élément et une URL qui répertorie tous les éléments pour la période.  
    
    .. admonition:: Remarque
        
        Certains types peuvent être des supertypes contenant des données provenant d’autres types (par exemple, barriers est un supertype qui contient des barrages et des chutes).

|fttype|

    Renvoie une description du type d’élément. Cette description comprend tous les attributs, les noms et les autres métadonnées associés au type d’élément. En outre, les métadonnées contiennent des renseignements sur l’affichage pour les attributs, y compris les attributs à inclure dans l’affichage « simple » et ceux à inclure dans l’affichage « all ».

    .. admonition:: Exemple
        
        ``https://cabd-web.azurewebsites.net/cabd-api/features/types/dams`` renvoie une entrée ``JSON`` avec la description du type d’élément ``dams``.

.. _feature-endpoints:

Points de fin d’élément
=======================

|ftid|

    Renvoie un élément unique sur la base de son identifiant, qui est fourni sous la forme ``<feature-id>``. Cela comprendra tous les attributs propres au type d’élément. Par conséquent, le schéma de cette ressource varie en fonction du type d’élément.

``/features``

|ftbbox|

|ftpoint|

|ftfilter|

|ftnamefilter|

    Renvoie tous les éléments qui correspondent aux paramètres de la requête. Plusieurs options de requête peuvent être fournies dans une même requête, mais une seule des options ``bbox`` et ``point`` doit être spécifiée. Les options de requête comprennent les suivantes :
        
    - ``bbox`` - n’inclut que les éléments qui correspondent au cadre d’objet fourni. Les coordonnées du cadre d’objet doivent être indiquées en format latitude/longitude : |bboxcoords|
    - ``point`` - renvoie les éléments les plus proches d’un point donné. Le point doit être indiqué en format latitude/longitude : |latlong|
    - ``max-results`` - le nombre maximal d’éléments pouvant être renvoyé.
    - ``types`` - les types d’éléments visés par la requête.
    - ``filter`` - une chaîne filtrant les éléments en fonction d’attributs. Peut être fournie plus d’une fois. Les filtres multiples sont combinés au moyen d’opérateurs logiques AND. Vous trouverez ci-dessous des renseignements détaillés sur le format de filtre.
    - ``namefilter`` - une chaîne filtrant les éléments en fonction de tous les noms d’attribut (en anglais et en français). On peut fournir plusieurs filtres namefilters. Les filtres multiples sont combinés au moyen d’opérateurs logiques OR. Vous trouverez ci-dessous des renseignements détaillés sur les filtres namefilter.

|ftstype|

|ftsbbox|

|ftspoint|

|ftsfilter|

    Renvoie une liste des éléments d’un type donné (par exemple, dams ou waterfalls). Les options de requête sont les mêmes que pour le point de fin ``/features`` (voir ci-dessus).

``/tiles/z/x/y.mvt``

    Renvoie une tuile vectorielle de tous les éléments barrier.

|tilestype|

    Renvoie une tuile vectorielle de tous les éléments d’un type donné.

Exemples de point de fin d’élément
----------------------------------

Pour renvoyer tous les barrages du bassin versant du RHN 02OE000 : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=nhn_watershed_id:eq:02OE000``

Pour renvoyer toutes les passes à poissons au sein du cadre d’objet [(-95.16,41.66), (-74.34,56.86)] : 
``https://cabd-web.azurewebsites.net/cabd-api/features/fishways?bbox=-95.16,41.66,-74.34,56.86``

Pour renvoyer toutes les chutes au Québec : 
``https://cabd-web.azurewebsites.net/cabd-api/features/waterfalls?filter=province_territory_code:eq:qc``

Pour renvoyer toutes les passes à poissons associées à un barrage : 
``https://cabd-web.azurewebsites.net/cabd-api/features/fishways?filter=dam_id:notnull:``

Pour renvoyer tous les barrages dont le code d’utilisation est 2 (Hydroelectricity) : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=use_code:eq:2``

Pour renvoyer tous les barrages dont le code d’utilisation est 2 (Hydroelectricity) et auxquels une passe à poissons à bassins et à déversoirs est associée (up_passage_type_code = 3) :
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=use_code:eq:2&filter=up_passage_type_code:eq:3``

.. _feature-endpoints-filter:

Filtre
------

Fournit une option de base pour filtrer les éléments en fonction de leurs attributs.

- Si le nom de l’attribut de filtre fourni n’est pas valide pour le type d’élément, un message d’erreur s’affichera (code d’état HTTP ``400 – Bad Request``).
- Se combine au filtre ``bbox`` décrit ci-dessus (lié au filtre bbox au moyen d’un opérateur logique AND).
- On peut combiner plusieurs filtres au moyen d’opérateurs logiques ``AND``, qui sont représentés par le symbole ``&`` dans les demandes d’API.
- Les filtres à chaîne sont insensibles à la casse (pour les opérateurs ``eq``, ``neq``, ``in`` et ``like``).

Format de demande de filtre :

|filterreq|

.. csv-table:: 
    :file: tbl/filter-format_fr.csv
    :widths: 30, 70
    :header-rows: 1

.. admonition:: Exemple
    
    ``/features/dams?bbox=0,0,1,1&filter=passability_status_code:in:1,2&filter=nhn_watershed_id:eq:08GABX1``

Cette requête renverra tous les barrages avec un code d’état du passage 1 (Barrier) ou 2 (Partial Barrier) dans l’unité de travail RHN 08GABX1 au sein du cadre d’objet [(0 0), (1 1)].

.. note::

    .. container:: toggle

        .. container:: header

            Cliquez sur la flèche ci-dessous pour développer une **liste interrogeable d’attributs filtrables** avec des valeurs codées et autorisées, le cas échéant.

            Veuillez noter que les filtres pour tous les attributs avec des valeurs codées doivent indiquer le code au lieu du nom associé (par exemple, un filtre en fonction de l’attribut operating_status_code doit indiquer la valeur « 1 » pour les barrages Abandoned/Orphaned : ``&filter=operating_status_code:eq:1``).

        .. table:: 
            :class: datatable
            :widths: 15, 20, 30, 35

            ========================== ===================================== =============================== ==============================================================================================================================================================================================================================================================
            Types d’éléments           Nom d'attribut                        Nom de l'attribut de filtre     Valeurs autorisées
            ========================== ===================================== =============================== ==============================================================================================================================================================================================================================================================
            Dams, waterfalls           Passability status                    passability_status_code         1-barrier, 2-partial barrier, 3-passable, 4-unknown
            Dams                       Operating status                      operating_status_code           1-abandoned/orphaned, 2-active, 3-decommissioned/removed, 4-retired/closed, 5-unknown, 6-remediated 
            Dams                       Ownership type                        ownership_type_code             1-charity/non-profit, 2-federal, 3-municipal, 4-private, 5-provincial/territorial, 6-other, 7-unknown, 8-indigenous
            Dams                       Dam use                               use_code                        1-irrigation, 2-hydroelectricity, 3-water supply, 4-flood control, 5-recreation, 6-navigation, 7-fisheries, 8-pollution control, 9-invasive species control, 10-other, 11-unknown
            Dams                       Dam size                              size_class_code                 1-small, 2-medium, 3-large, 4-unknown  
            Dams, waterfalls, fishways Province/territory name               province_territory_code         ab-alberta, bc-british columbia, mb-manittoba, nb-new brunswick, nl-newfoundland and labrador, ns-nova scotia, nt-northwest territories, nu-nunavut, on-ontario, pe-prince edward island, qc-quebec, sk-saskatchewan, us-united states, yt-yukon         
            Dams                       Dam height (m)                        height_m                        n/a
            Dams                       Construction year                     construction_year               n/a
            Dams                       Upstream passage type                 up_passage_type_code            1-denil, 2-nature-like fishway, 3-pool and weir, 4-pool and weir with hole, 5-trap and truck, 6-vertical slot, 7-other, 8-no structure, 9-unknown
            Dams                       Dam function                          function_code                   1-storage, diversion, 3-detention, 4-debris, 6-saddle, 7-hydro - closed-cycle pumped storage, 8-hydro - conventional storage, 9-hydro - open-cycle pumped storage, 10-hydro - run-of-river, 11-hydro - tidal, 12-other, 13-unknown
            Dams                       Use irrigation                        use_irrigation_code             1-main, 2-major, 3-secondary 
            Dams                       Use hydroelectricity                  use_electricity_code            1-main, 2-major, 3-secondary 
            Dams                       Use water supply                      use_supply_code                 1-main, 2-major, 3-secondary 
            Dams                       Use flood control                     use_floodcontrol_code           1-main, 2-major, 3-secondary 
            Dams                       Use recreation                        use_recreation_code             1-main, 2-major, 3-secondary 
            Dams                       Use navigation                        use_navigation_code             1-main, 2-major, 3-secondary 
            Dams                       Use fisheries                         use_fish_code                   1-main, 2-major, 3-secondary 
            Dams                       Use pollution control                 use_pollution_code              1-main, 2-major, 3-secondary 
            Dams                       Use invasive species                  use_invasivespecies_code        1-main, 2-major, 3-secondary 
            Dams                       Use other                             use_other_code                  1-main, 2-major, 3-secondary 
            Dams                       Construction type                     construction_type_code          1-arch, 2-buttress, 3-earth, 4-gravity, 5-multiple arch, 6-rock, 7-steel, 8-timber, 9-unknown, 10-other, 11-concrete, 12-masonry
            Dams                       Spillway type                         spillway_type_code              1-combined, 2-free, 3-gated, 4-other, 5-none, 6-unknown 
            Dams                       Turbine type                          turbine_type_code               1-cross-flow, 2-francis, 3-kaplan, 4-pelton, 5-unknown, 6-other 
            Dams                       Downstream passage route              down_passage_route_code         1-bypass, 2-river channel, 3-spillway, 4-turbine  
            Dams, waterfalls, fishways Completeness level                    complete_level_code             1-unverified, 2-minimal, 3-moderate, 4-complete  
            Dams                       Lake control                          lake_control_code               1-yes, 2-enlarged, 3-maybe 
            Dams                       Dam condition                         condition_code                  1-good, 2-fair, 3-poor, 4-unreliable  
            Waterfalls                 Waterfall height                      fall_height_m                   n/a
            Fishways                   Fishway type                          fishpass_type_code              1-denil, 2-nature-like fishway, 3-pool and weir, 4-pool and weir with hole, 5-trap and truck, 6-vertical slot, 7-other, 8-no structure, 9-unknown
            Fishways                   Year constructed                      year_constructed                n/a
            Dams, waterfalls, fishways Municipality                          municipality                    n/a
            Dams                       Dam name (English)                    dam_name_en                     n/a
            Dams                       Dam name (French)                     dam_name_fr                     n/a
            Dams, waterfalls, fishways Waterbody name (English)              waterbody_name_en               n/a
            Dams, waterfalls, fishways Waterbody name (French)               waterbody_name_fr               n/a
            Dams, waterfalls, fishways Barrier/system Identifier             cabd_id                         n/a
            Dams                       Reservoir name (English)              reservoir_name_en               n/a
            Dams                       Reservoir name (French)               reservoir_name_fr               n/a
            Dams, waterfalls, fishways NHN Watershed ID                      nhn_watershed_id                n/a
            Dams, waterfalls, fishways Used for Network Analysis             use_analysis                    true, false
            Waterfalls                 Waterfall name (English)              fall_name_en                    n/a
            Waterfalls                 Waterfall name (French)               fall_name_fr                    n/a
            Dams                       Generating capacity (MWh)             generating_capacity_mwh         n/a
            Dams                       Federal compliance status             federal_compliance_status       n/a
            Dams                       Provincial compliance status          provincial_compliance_status    n/a
            Dams, fishways             Operating notes                       operating_notes                 n/a 
            Dams                       Removed year                          removed_year                    n/a
            Dams                       Assessment schedule                   assess_schedule                 n/a 
            Dams                       Expected life (years)                 expected_life                   n/a 
            Dams                       Next maintenance date                 maintenance_next                n/a
            Dams                       Last maintenance date                 maintenance_last                n/a 
            Dams                       Dam length (m)                        length_m                        n/a 
            Dams                       Spillway Capacity (m3/s)              spillway_capacity               n/a 
            Dams                       Reservoir present                     reservoir_present               true, false
            Dams                       Reservoir area(km2)                   reservoir_area_skm              n/a
            Dams                       Reservoir depth (m)                   reservoir_depth_m               n/a 
            Dams                       Storage Capacity (mcm)                storage_capacity_mcm            n/a 
            Dams                       Average rate of discharge (L/s)       avg_rate_of_discharge_ls        n/a 
            Dams                       Degree of regulation (%)              degree_of_regulation_pc         n/a 
            Dams                       Provincial flow requirements (m3/s)   provincial_flow_req             n/a 
            Dams                       Federal flow requirements (m3/s)      federal_flow_req                n/a 
            Dams                       Catchment Area (km2)                  catchment_area_skm              n/a 
            Dams                       Hydro peaking system                  hydro_peaking_system            n/a 
            Dams                       Number of turbines                    turbine_number                  n/a
            Dams, waterfalls, fishways Last modified                         last_modified                   n/a 
            Dams, waterfalls, fishways Comments                              comments                        n/a 
            Dams                       Upstream linear length (km)           upstream_linear_km              n/a 
            Dams                       Facility name (English)               facility_name_en                n/a 
            Dams                       Facility name (French)                facility_name_fr                n/a 
            Fishways                   Monitoring equipment                  monitoring_equipment            n/a 
            Fishways                   Architect                             architect                       n/a 
            Fishways                   Contracted by                         contracted_by                   n/a 
            Fishways                   Constructed by                        constructed_by                  n/a 
            Fishways                   Plans held by                         plans_held_by                   n/a 
            Fishways                   Purpose                               purpose                         n/a 
            Fishways                   Dam Identifier                        dam_id                          n/a 
            Fishways                   Designed based on biology             designed_on_biology             n/a 
            Fishways                   Fishway length (m)                    length_m                        n/a 
            Fishways                   Elevation (m)                         elevation_m                     n/a 
            Fishways                   Gradient (%)                          gradient                        n/a 
            Fishways                   Depth (m)                             depth (m)                       n/a 
            Fishways                   Entrance location                     entrance_location_code          1-midstream, 2-bank
            Fishways                   Entrance position                     entrance_position_code          1-bottom, 2-surface, 3-bottom and surface, 4-mid-column
            Fishways                   Is modified                           modified                        n/a 
            Fishways                   Modification year                     modification_year               n/a 
            Fishways                   Modification purpose                  modification_purpose            n/a 
            Fishways                   Structure name (English)              structure_name_en               n/a 
            Fishways                   Structure name (French)               structure_name_fr               n/a 
            Fishways                   Operated by                           operated_by                     n/a 
            Fishways                   Operation period                      operation_period                n/a 
            Fishways                   Has evaluating studies                has_evaluating_studies          true, false
            Fishways                   Nature of evaluating studies          nature_of_evaluation_studies    n/a 
            Fishways                   Engineering notes                     engineering_notes               n/a 
            Fishways                   Maximum Velocity of Water Flow (m/s)  max_fishway_velocity_ms         n/a
            Fishways                   Average Velocity of Water Flow (m/s)  mean_fishway_velocity_ms        n/a 
            Fishways                   Attraction Estimate (%)               estimate_of_attraction_pct      n/a 
            Fishways                   Transit Success Estimate (%)          estimate_of_passage_success_pct n/a
            Fishways                   Evaluating study/reference identifier fishway_reference_id            n/a
            Fishways                   River name (English)                  river_name_en                   n/a
            Fishways                   River name (French)                   river_name_fr                   n/a
            ========================== ===================================== =============================== ==============================================================================================================================================================================================================================================================
    
.. _feature-endpoints-namefilter:


Filtre par nom
--------------

Fournit une option de filtrage des éléments en fonction de tous les attributs de nom associés aux types d’éléments. Les attributs de nom sont différents pour chaque type d’élément et sont spécifiés par les métadonnées de base de données. En général, les attributs de nom ne comprennent que les noms anglais et français d’un élément, mais ils peuvent aussi comprendre d’autres champs.

Le filtre par nom se combine au filtre ``bbox`` décrit ci-dessus (lié au filtre bbox au moyen d’un opérateur logique AND). Plusieurs filtres par nom peuvent être fournis et ils seront combinés au moyen d’opérateurs logiques ``OR``, représentés par le symbole ``&`` dans les demandes d’API. Toutes les comparaisons sont insensibles à la casse (holden = Holden = HOLDEN).

Format de demande de filtre par nom :

|namefilterreq|

.. csv-table:: 
    :file: tbl/namefilter-format_fr.csv
    :widths: 30, 70
    :header-rows: 1

.. admonition:: Exemple
    
    ``/features/dams?bbox=0,0,1,1&filtername=like:holden``

Cela renverra tous les barrages au sein du cadre d’objet [(0 0), (1 1)] et un nom anglais ou français comme « holden ».

Exemples
^^^^^^^^

Renvoyer tous les barrages avec un nom anglais ou français comme « holden » (insensible à la casse) : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?&namefilter=like:holden``

Renvoyer tous les barrages avec un nom anglais ou français comme « churchill falls » (insensible à la casse) : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?&namefilter=like:churchill+falls``

Renvoyer tous les barrages avec un nom anglais ou français comme « churchill falls » ou « revelstoke » (insensible à la casse) : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?&namefilter=like:churchill+falls&namefilter=like:revelstoke``

Renvoyer toutes les passes à poissons avec un nom de structure comme « grand falls » (insensible à la casse) : 
``https://cabd-web.azurewebsites.net/cabd-api/features/fishways?&namefilter=like:grand+falls``

.. _feature-endpoints-format:

Format
------

Le format de sortie par défaut est GeoJSON, mais vous pouvez obtenir d’autres formats en fournissant le paramètre de requête de format. Vous pouvez combiner le paramètre de format aux filtres par attribut et aux filtres par nom décrits ci-dessus.

Exemples
^^^^^^^^
    
Renvoyer tous les barrages du bassin versant du RHN 08GABX1 en format geopackage : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=nhn_watershed_id:eq:08GABX1&format=geopackage``

Renvoyer tous les barrages avec un code use_code 2 (Hydroelectricity) en format geopackage : 
``https://cabd-web.azurewebsites.net/cabd-api/features/dams?filter=use_code:eq:2&format=geopackage``

Formats pris en charge
^^^^^^^^^^^^^^^^^^^^^^

Les formats suivants sont pris en charge pour les points de fin d’élément qui renvoient une collection d’éléments.

- ``geopackage``/ ``gpkg`` - produit un fichier geopackage
- ``shp`` – produit un fichier shapefile
- ``kml`` – produit un fichier kml
- ``json``/ ``geojson`` - produit un fichier GeoJSON (option par défaut)
- ``csv`` – produit un fichier csv

Les points de fin d’entité uniques ne renvoient que des fichiers GeoJSON.

Toutes les exportations (sauf celles en format csv) comprennent des métadonnées qui incluent le type d’élément, le numéro de version, l’horodatage de téléchargement et les renseignements sur la licence. Pour les fichiers JSON, ces renseignements sont inclus dans les métadonnées de la collection d’éléments; pour les fichiers SHP, un fichier de métadonnées csv supplémentaire est inclus dans le ZIP; pour les fichiers kml, ces renseignements sont inclus sous extendedData; pour geopackage, ces renseignements sont inclus en tant que couche supplémentaire de métadonnées non spatiales.

.. admonition:: Remarque

   TLa meilleure façon de télécharger des données pour plusieurs types d’éléments à l’aide de l’API est d’utiliser ``/features/<type>``.
   
   Bien que le point de fin /features/ renvoie des éléments de plusieurs types, la liste des attributs renvoyés est très limitée par rapport à la liste des attributs renvoyés lorsqu’une valeur ``<type>`` est indiquée.

.. _feature-endpoints-locale:

Paramètres de lieu
------------------

Les résultats sont disponibles en anglais et en français. La langue dans laquelle les résultats sont renvoyés est déterminée par l’en-tête ``Accept-Language``. La langue par défaut est l’anglais.


.. _feature-endpoints-max-features:

Nombre maximal d’éléments
-------------------------

Un maximum de 55 000 éléments sera renvoyé. Si une demande Feature API aboutit à plus de 55 000 éléments, le système affiche un message d’erreur avec un code d’état HTTP 403 (Forbidden) et une indication comme quoi l’utilisateur doit ajouter un filtre pour limiter les résultats de la requête.

La valeur de ``55 000`` est un paramètre d’application que l’on peut modifier au besoin (voir le fichier ``application.properties``).

.. _feature-endpoints-feature-totals:

Nombres totaux de résultats Feature API
---------------------------------------

La réponse Feature API comprend un en-tête Content-Range qui résume le nombre total d’éléments correspondant aux filtres par rapport au nombre total d’éléments renvoyés. Vous pouvez l’utiliser avec le paramètre max-results pour accéder au nombre d’éléments correspondant à un filtre sans avoir à charger tous les éléments.

Exemple
^^^^^^^

``https://cabd-web.azurewebsites.net/cabd-api/features/waterfalls?filter=fall_name_en:like:fall&max-results=5``
    
L’appel API renverra cinq éléments (max-results=5). Cependant, l’en-tête de la réponse comprendra aussi un en-tête Content-Range qui se présente comme suit : ``Content-Range: features 0-5/65``. La valeur 0-5 indique que seuls les cinq premiers éléments sont inclus dans les résultats. La valeur 65 indique qu’un total de 65 éléments correspondent aux filtres choisis.

Par conséquent, si vous souhaitez obtenir uniquement le nombre total d’éléments, et ne souhaitez obtenir aucun élément, vous pouvez utiliser un paramètre max-results=0 :

``https://cabd-web.azurewebsites.net/cabd-api/features/waterfalls?max-results=0``

Cela renverra une collection d’éléments vide, mais les en-têtes de la réponse incluront Content-Range: ``Content-Range: features 0-0/729``, ce qui indique qu’il y a 729 chutes dans la base de données.

    

.. _feature-datasource-endpoint:

Point de fin de source des données des éléments
===============================================

-----

|ftdsid|

|ftdsidflds|

    Renvoie les renseignements de la source de données pour chaque attribut associé à un identifiant d’élément. Par défaut, cette option renvoie un ensemble réduit d’attributs : ``feature id``, ``attribute field``, ``data source name``, et ``data source feature id``. Pour inclure le jeu d’attributs complet (``feature id``, ``attribute field``, ``attribute name``, ``data source name``, ``data source date``, ``data source version``, ``data source feature id``, ajoutez le paramètre ``fields=all`` à la requête.

.. _feature-datasource-endpoint-format:

Format
------

Le format de sortie par défaut de ce point de fin est CSV.

Le format JSON est aussi pris en charge; pour l’utiliser, ajoutez le paramètre de requête ``format=json`` : |ftdsidjson|

.. _submit-feature-update-end-point:

Points de fin de mise à jour d’élément
======================================

-----

Ce point de fin permet aux utilisateurs de soumettre des demandes de mise à jour d’élément. Ces demandes sont enregistrées dans la base de données et examinées par les administrateurs de la BDOAC avant que les mises à jour soient appliquées à l’élément.


* URL: /features/<feature-id>
* METHOD: PUT
* CONTENT-TYPE: application-json
* BODY: chaîne JSON contenant des renseignements sur la mise à jour d’élément

 * {"name": prénom et nom, "email": "prénom.nom@host.com", "organization": "<facultatif>", "description": "description de la mise à jour d’élément", "datasource", "facultatif, renseignements sur la source de la mise à jour de données}
 * Les valeurs name, email et description sont obligatoires. Les valeurs organization et datasource sont facultatives.


.. _submit-contact-end-point:

Point de fin de personne-ressource
==================================

-----

Ce point de fin permet aux utilisateurs de créer une nouvelle personne-ressource ou de mettre à jour une personne-ressource. Les personnes-ressources sont identifiées par leur adresse courriel. S’il y a déjà une personne-ressource dans la base de données, elle sera mise à jour en fonction des renseignements fournis.


* URL: /contacts
* METHOD: PUT
* CONTENT-TYPE: application-json
* BODY: chaîne JSON contenant les renseignements sur la mise à jour d’élément

 * {"name": "prénom et nom", "email": "prénom.nom@host.com", "organization": "<facultatif>"}
 * Les valeurs name et email sont obligatoires. La valeur organization est facultative.


.. _feature-vector-tile-service:

Service de tuiles vectorielles
==============================

-----

Ce service crée des tuiles vectorielles pour les types d’obstacles.

Format
------

Le seul format pris en charge pour les services de tuiles vectorielles est MVT ().

Point de fin
------------

``https://cabd-web.azurewebsites.net/cabd-api/tiles/{type}/{z}/{x}/{y}.{format}``

La valeur ``type`` doit être un type d’élément valide.

Les attributs inclus dans la tuile vectorielle sont ceux dont la valeur include_vector_tile dans le tableau feature_type_metadata est vraie.