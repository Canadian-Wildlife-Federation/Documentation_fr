.. _data-catalogue:

====================
Catalogue de données
====================

Le catalogue de données de la BDOAC contient les renseignements dont vous avez besoin pour comprendre les attributs de chaque type d’élément de la BDOAC (barrages, chutes et passes à poissons), y compris des noms de champs interprétables par l’utilisateur, des ventilations des valeurs de champs autorisées et des définitions. Si vous avez des questions au sujet des renseignements de cette page, vous pouvez communiquer avec nous à cabd@cwf-fcf.org.

Types d’éléments
----------------
..
   .. raw:: html
   
      <div id="datasourcecontent">
      </div>
      
      <script>
      function loadDataSources() {
      
         let url = "https://cabd-web.azurewebsites.net/cabd-api/docs?options=types"
         let xhr = new XMLHttpRequest();
         // Making our connection 
         xhr.open("GET", url, true);
      
         // function execute after request is successful
         xhr.onreadystatechange = function () {
         if (this.readyState == 4 && this.status == 200) {
               let element = document.getElementById("datasourcecontent");
               element.innerHTML = this.responseText;      
               
               //make a data table out of the nhn watershed id field
               //across all feature types
               $("table[id^='datatable_attribute_nhn_watershed_id']").each(function(){
                  $("#" + this.id).DataTable();
               });            
            
               let kids = $('div[class*=\"tocsection\"]');
               for (kid of kids){        
                  for (kid2 of kid.parentElement.children){
                     if (kid2.tagName == "NAV") createToC(element, kid2);
                  }
               }
         }
         }
         // Sending our request
         xhr.send();
      }
      
      function createToC(element, appendTo){
      
         for (let kid of element.children){
            
            if (kid.tagName.toLowerCase() == "section" && (kid.id.startsWith("ft_") || kid.id.startsWith("ftatt_"))){
               
               let ulchild = document.createElement("ul");
               ulchild.className = "visible nav section-nav flex-column";
               
               
               let child = document.createElement("li");
               child.className = "nav-item toc-entry toc-h2";
               
               let achild = document.createElement("a");
               achild.className="reference internal nav-link";
               achild.href = "#" + kid.id;
               achild.innerHTML = kid.children[0].innerHTML;
               
               child.appendChild(achild);
               ulchild.appendChild(child);
         
               appendTo.appendChild(ulchild);
               
               for (let kid2 of kid.children){
                  if (kid2.tagName.toLowerCase() == "section" && (kid.id.startsWith("ft_") || kid.id.startsWith("ftatt_"))){         
                     let ulchild = document.createElement("ul");
                     ulchild.className = "visible nav section-nav flex-column";
                     
                     
                     let child2 = document.createElement("li");
                     child2.className = "nav-item toc-entry toc-h3";
                     
                     let achild = document.createElement("a");
                     achild.className="reference internal nav-link";
                     achild.href = "#" + kid2.id;
                     //achild.innerHTML = kid2.innerHTML
                     achild.innerHTML = kid2.children[0].innerHTML;
                     
                     child2.appendChild(achild);
                     ulchild.appendChild(child2);
               
                     child.appendChild(ulchild);
                  }
               }
            }    
         }
      }
      loadDataSources();
      </script>

-----

.. _dams-layer:

Barrages
~~~~~~~~
Définition:	
    *Un barrage est une structure construite pour détourner ou retenir l’eau d’un ruisseau, d’une rivière ou d’un lac dans un but précis, par exemple, pour produire de l’hydroélectricité, stocker de l’eau ou prévenir les inondations. Ces structures empêchent les poissons de remonter le courant, à moins qu’elles soient dotées d’une passe à poissons. Dans la BDOAC, les barrages sont définis comme suit : petits barrages (d’une hauteur inférieure à 5 m), barrages moyens (d’une hauteur de 5 à 15 m) et grands barrages (d’une hauteur de 15 m ou plus, ou d’une hauteur de 5 à 15 m avec retenue de plus de 3 000 000 m3).* 
    
    *Actuellement, la couche de données relatives aux barrages de la BDOAC comprend également d’autres types de structures, dont les déversoirs, les centrales électriques, les évacuateurs de crues, les canaux et les structures latérales (par exemple, les endiguements et les barrages de col). Certaines de ces structures ne fragmentent pas nécessairement les systèmes d’eau douce dans le plan amont-aval. Il ne faut donc pas utiliser ces structures pour les analyses de réseau de connectivité ou les exercices de hiérarchisation des obstacles. Vous pouvez filtrer ces points de données au moyen du champ* :ref:`utilisé pour l’analyse de réseau <useanalysis>` (``use_analysis = false`` *dans les données*).
Attributs :
    :ref:`Horaire d’évaluation <assessment-schedule>`, :ref:`Débit moyen (L/s) <avgrate>`, :ref:`Identifiant de l’obstacle <bid>`, :ref:`Commentaires <commentdef>`, :ref:`Quantité d’info <complvl>`, :ref:`Matériaux de construction <conmaterial>`, :ref:`Année de construction <conyear>`, :ref:`État du barrage <damcon>`, :ref:`Fonction du barrage <damfunc>`, :ref:`Nom du barrage (anglais) <damnameen>`, :ref:`Nom du barrage (français) <damnamefr>`, :ref:`Taille du barrage <damsize>`, :ref:`Utilisation du barrage <damuse>`, :ref:`Degré de régularisation <degreg>`, :ref:`Voie de passage en aval <downpass>`, :ref:`Durée utile probable (années) <explife>`, :ref:`Nom de l’installation (anglais) <facilnameen>`, :ref:`Nom de l’installation (français) <facilnamefr>`, :ref:`Détails sur la source des données sur l’élément <ftdatasrc>`, :ref:`Type d’élément <fttype>`, :ref:`Conformité à la réglementation fédérale <fedcompstat>`, :ref:`Exigences de débit fédérales (m3/s) <fedflowreq>`, :ref:`Capacité de production (MWh) <gencap>`, :ref:`Système de pointe hydroélectrique <hydropeak>`, :ref:`Hauteur (m) <damheight>`, :ref:`Régulateur du niveau du lac <lakectrl>`, :ref:`Date de la dernière maintenance <lastmaint>`, :ref:`Dernière modification <lastmod>`, :ref:`Latitude <lat>`, :ref:`Longueur (m) <length>`, :ref:`Longitude <long>`, :ref:`Municipalité <municipality>`, :ref:`Date de la prochaine maintenance <nextmaint>`, :ref:`Identifiant du bassin versant RHN <nhnid>`, :ref:`Nom du bassin versant RHN <nhnname>`, :ref:`Nombre de turbines <turbcount>`, :ref:`Note sur l’exploitation <opnote>`, :ref:`État d’exploitation <opstat>`, :ref:`Propriétaire <owner>`, :ref:`Type de propriété <owntype>`, :ref:`État du passage <passstat>`, :ref:`Note sur l’état du passage <passstatnote>`, :ref:`Nom province/territoire <provterr>`, :ref:`Conformité à la réglementation provinciale <provcompstat>`, :ref:`Exigences de débit provinciales (m3/s) <provflowreq>`, :ref:`Année du retrait <remyear>`, :ref:`Superficie du réservoir (km2) <resarea>`, :ref:`Profondeur du réservoir (m) <resdepth>`, :ref:`Nom du réservoir (anglais) <resnameen>`, :ref:`Nom du réservoir (français) <resnamefr>`, :ref:`Réservoir présent <respres>`, :ref:`Capacité du déversoir <spillcap>`, :ref:`Type de déversoir <spilltype>`, :ref:`Capacité de stockage (mmc) <storagecap>`, :ref:`Type de structure <structype>`, :ref:`Type de turbine <turbtype>`, :ref:`Superficie du bassin récepteur en amont (km2) <upcatcharea>`, :ref:`Longueur linéraire en amont (km) <uplength>`, :ref:`Type de passage en amont <uppasstype>`, :ref:`Utilisation pour conservation  <useconservation>`, :ref:`Utilisation pour pêches <usefish>`, :ref:`Utilisation pour contrôle des inondations <useflood>`, :ref:`Utilisation pour hydroélectricité <usehydro>`, :ref:`Utilisation pour contrôle d’espèces envahissantes <useais>`, :ref:`Utilisation pour irrigation <useirr>`, :ref:`Utilisation pour navigation <usenav>`, :ref:`Autre utilisation <useother>`, :ref:`Utilisation pour contrôle de la pollution <usepoll>`, :ref:`Utilisation pour récréation <userec>`, :ref:`Utilisation pour approvisionnement en eau <usesupply>`, :ref:`Utilisé pour l’analyse de réseau <useanalysis>`, :ref:`Nom du plan d’eau (anglais) <waterbodynameen>`, :ref:`Nom du plan d’eau (français) <waterbodynamefr>`

Chutes
~~~~~~~~~~~~
Définition:
    *Structure naturelle qui peut entraver la capacité des poissons à se déplacer en amont en raison de changements d’altitude et de l’augmentation de la vitesse d’écoulement.*
Attributs :	
    :ref:`Identifiant de l’obstacle <bid>`, :ref:`Commentaires <commentdef>`, :ref:`Quantité d’info <complvl>`, :ref:`Dernière modification <lastmod>`, :ref:`Hauteur de la chute (m) <fallheight>`, :ref:`Nom de la chute (anglais) <fallnameen>`, :ref:`Nom de la chute (français) <fallnamefr>`, :ref:`Détails sur la source des données sur l’élément <ftdatasrc>`, :ref:`Type d’élément <fttype>`, :ref:`Latitude <lat>`, :ref:`Longitude <long>`, :ref:`Municipalité <municipality>`, :ref:`Identifiant du bassin versant RHN <nhnid>`, :ref:`Nom du bassin versant RHN <nhnname>`, :ref:`État du passage <passstat>`, :ref:`Nom province/territoire <provterr>`, :ref:`Utilisé pour l’analyse de réseau <useanalysis>`, :ref:`Nom du plan d’eau (anglais) <waterbodynameen>`, :ref:`Nom du plan d’eau (français) <waterbodynamefr>` 

Passes à poissons
~~~~~~~~~~~~~~~~~~
Définition:
    *Structure construite pour faciliter le passage des poissons en amont et/ou en aval d’un obstacle aquatique (par exemple, un barrage ou une chute).*
Attributs :
    :ref:`Architecte <architect>`, :ref:`Estimation du taux d’attraction (%) <attraction>`, :ref:`Vitesse moyenne du débit (m/s) <avgvelocity>`, :ref:`Quantité d’info <complvl>`, :ref:`Construit par <constructby>`, :ref:`Contrat avec <contractby>`, :ref:`Identifiant du barrage <damid>`, :ref:`Conception en fonction de la biologie <biodesign>`, :ref:`Élévation (m) <elevation>`, :ref:`Notes d’ingénierie <engnotes>`, :ref:`Emplacement de l’entrée <enterlocal>`, :ref:`Position de l’entrée <enterpos>`, :ref:`Étude d’évaluation <evalstudy>`, :ref:`Détails sur la source des données sur l’élément <ftdatasrc>`, :ref:`Type d’élément <fttype>`, :ref:`Type de passe à poissons <fishwaytype>`, :ref:`Gradient <Gradient>`, :ref:`Avec études d’évaluation <hasevalstudy>`, :ref:`Modifications <ismod>`, :ref:`Latitude <lat>`, :ref:`Longueur (m) <length>`, :ref:`Longitude <long>`, :ref:`Vitesse maximale du débit (m/s) <maxvelo>`, :ref:`Profondeur moyenne du canal (m) <meandepth>`, :ref:`But des modifications <modpurpose>`, :ref:`Année des modifications <modyear>`, :ref:`Équipement de surveillance <monitor>`, :ref:`Municipalité <municipality>`, :ref:`Nature des études d’évaluation <natureevalstudy>`, :ref:`Identifiant du bassin versant RHN <nhnid>`, :ref:`Nom du bassin versant RHN <nhnname>`, :ref:`Exploitation par <opby>`, :ref:`Note sur l’exploitation <opnote>`, :ref:`Période d’exploitation <opperiod>`, :ref:`Plans détenus par <plansheld>`, :ref:`Nom province/territoire <provterr>`, :ref:`But de la passe à poissons  <fishwaypurpose>`, :ref:`Nom rivière/ruisseau (anglais) <rivnameen>`, :ref:`Nom rivière/ruisseau (français) <rivnamefr>`, :ref:`Espèces qui ne l’utilisent pas <knowntouse>`, :ref:`Espèces qui l’utilisent <knowntouse>`, :ref:`Structure Name (English) <strucnameen>`, :ref:`Nom de la structure (français) <strucnamefr>`, :ref:`Identifiant du système <systemid>`, :ref:`Estimation du taux de passage (%) <success>`, :ref:`Nom du plan d’eau (anglais) <waterbodynameen>`, :ref:`Nom du plan d’eau (français) <waterbodynamefr>`, :ref:`Année de construction <yearconst>`


Attributs 
---------

-----

Attributs communs à plusieurs types d’éléments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _bid:

Identifiant de l’obstacle
+++++++++++++++++++++++++
 **Définition:**	*Identifiant unique et statique pour chaque point d’obstacle.* 

 **Nom du champ :** cabd_id

|dcdamsreturn|

.. _commentdef:

Commentaires
++++++++++++
 **Définition:** *Commentaires non structurés sur l’élément.*

 **Nom du champ :** comments

|dcdamsreturn|

.. _complvl:

Quantité d’info
+++++++++++++++
 **Définition:** *Le niveau de renseignements disponible pour l’élément dans la BDOAC.*

 **Nom du champ :** complete_level_code

 **Valeurs autorisées :** 

.. csv-table:: 
    :file: tbl/complvl_fr.csv
    :widths: 15, 20, 25, 25, 25
    :header-rows: 1

|dcdamsreturn|

.. _ftdatasrc:

Détails sur la source des données sur l’élément
+++++++++++++++++++++++++++++++++++++++++++++++
 **Définition:** *Lien permettant de télécharger un fichier CSV contenant des renseignements sur la source de données pour tous les attributs d’un élément.* 

 **Champs inclus dans le téléchargement :**

.. csv-table:: 
    :file: tbl/ftdatasrc_fr.csv
    :widths: 25, 75
    :header-rows: 1

|dcdamsreturn|

.. _fttype:

Type d’élément
++++++++++++++
 **Définition:** *Le type d’élément que le point de données représente.*

 **Valeurs autorisées :**		

.. csv-table:: 
    :file: tbl/fttype_fr.csv
    :widths: 15, 85
    :header-rows: 1

|dcdamsreturn|

.. _lastmod:

Dernière modification
+++++++++++++++++++++
 **Définition:** *La date de publication de la source de données la plus récemment utilisée pour la création, la révision ou la confirmation de l’enregistrement de l’élément.*

 **Nom du champ :** last_modified

|dcdamsreturn|

.. _lat:

Latitude
++++++++
 **Définition:** *La coordonnée géographique x représentant l’emplacement de l’élément.* 

|dcdamsreturn|

.. _length:

Longueur (m)
++++++++++++
 **Définition:** *Barrage – la longueur de la crête d’une rive (ou d’une culée) à l’autre, en mètres. Passe migratoire – la longueur de la passe à poissons, en mètres.*

 **Nom du champ :** length_m

|dcdamsreturn|

.. _long:

Longitude
+++++++++
 **Définition:** *La coordonnée géographique y représentant l’emplacement de l’élément.* 

|dcdamsreturn|

.. _municipality:

Municipalité
++++++++++++
 **Définition:** *La municipalité dans laquelle l’élément est situé.*

 **Nom du champ :** municipality

|dcdamsreturn|

.. _nhnid:

Identifiant du bassin versant RHN
+++++++++++++++++++++++++++++++++
 **Définition:** *Un code faisant référence à l’unité de travail Nom du jeu de données du Réseau hydrographique national (RHN) au sein de laquelle l’élément est situé.* 

 **Nom du champ :** nhn_watershed_id

|dcdamsreturn|

.. _nhnname:

Nom du bassin versant RHN
+++++++++++++++++++++++++
 **Définition:** *Le nom du sous-sous-bassin versant au sein duquel l’élément est situé. Le nom aura une valeur d’attribut nhn_watershed_id correspondante.*

 **Nom du champ :** sub_sub_drainage_area

|dcdamsreturn|

.. _opnote:

Note sur l’exploitation
+++++++++++++++++++++++
 **Définition:** *Commentaires non structurés sur des considérations importantes relatives à l’exploitation du barrage ou de la passe à poissons.* 

 **Nom du champ :** operating_notes

|dcdamsreturn|

.. _passstat:

État du passage
+++++++++++++++
 **Définition:** *La mesure dans laquelle l’élément agit comme un obstacle pour les poissons en amont.* 

 **Nom du champ :** passability_status_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/passstat_fr.csv
    :widths: 15, 15, 30, 20, 20
    :header-rows: 1

|dcdamsreturn|

.. _passstatnote:

Note sur l’état du passage
++++++++++++++++++++++++++
 **Définition:** *Notes non structurées qui offrent du contexte sur l’état du passage attribué (par exemple, restrictions concernant les espèces).*

 **Nom du champ :** passability_status_note

|dcdamsreturn|

.. _provterr:

Nom province/territoire
+++++++++++++++++++++++
 **Définition:** *La province ou le territoire où l’élément est situé.*

 **Nom du champ :** province_territory_code

|dcdamsreturn|

.. _waterbodynameen:

Nom du plan d’eau (anglais)
+++++++++++++++++++++++++++
 **Définition:** *Le nom du plan d’eau dans lequel l’élément est enregistré (en anglais).* 

 **Nom du champ :** waterbody_name_en

|dcdamsreturn|

.. _waterbodynamefr:

Nom du plan d’eau (français)
++++++++++++++++++++++++++++
 **Définition:** *Le nom du plan d’eau dans lequel l’élément est enregistré (en français).* 

 **Nom du champ :** waterbody_name_fr

|dcdamsreturn|

.. _useanalysis:

Utilisé pour l’analyse de réseau
++++++++++++++++++++++++++++++++
**Définition:** *Indique si un obstacle doit être relié au réseau de cours d’eau et utilisé pour l’analyse de la connectivité du réseau.*

**Nom du champ :** use_analysis

**Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/useanalysis_fr.csv
    :widths: 15, 25, 30, 30
    :header-rows: 1

|dcdamsreturn|

Attributs uniques aux barrages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _assessment-schedule:

Horaire d’évaluation
++++++++++++++++++++
 **Définition:** *La fréquence à laquelle le barrage est évalué ou entretenu par un propriétaire ou un organisme de réglementation.*

 **Nom du champ :** assess_schedule

|dcdamsreturn|

.. _avgrate:

Débit moyen (L/s)
+++++++++++++++++
 **Définition:** *Le débit moyen à l’emplacement du barrage, en litres par seconde.*

 **Nom du champ :** avg_rate_of_discharge_ls

|dcdamsreturn|

.. _conmaterial:

Matériaux de construction
+++++++++++++++++++++++++
**Définition:** *Le matériaux de construction principal de la structure.*

**Nom du champ :** construction_material_code

.. csv-table:: 
    :file: tbl/materialtype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _conyear:

Année de construction
+++++++++++++++++++++
 **Définition:** *L’année au cours de laquelle on a terminé la construction du barrage (il s’agit parfois d’une estimation).*

 **Nom du champ :** construction_year

|dcdamsreturn|

.. _damcon:

État du barrage
+++++++++++++++
 **Définition:** *L’état physique du barrage.*

 **Nom du champ :** condition_code

 **Valeurs autorisées :**

.. csv-table:: 
    :file: tbl/damcon_fr.csv
    :widths: 15, 15, 70
    :header-rows: 1

|dcdamsreturn|

.. _damfunc:

Fonction du barrage
+++++++++++++++++++
 **Définition:** *La fonction prévue de la structure.* 

 **Nom du champ :** function_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/damfunc_fr.csv
    :widths: 15, 25, 70
    :header-rows: 1

|dcdamsreturn|

.. _damnameen:

Nom du barrage (anglais)
++++++++++++++++++++++++
 **Définition:** *Nom du barrage (en anglais).*

 **Nom du champ :** dam_name_en

|dcdamsreturn|

.. _damnamefr:

Nom du barrage (français)
+++++++++++++++++++++++++
 **Définition:** *Nom du barrage (en français).*

 **Nom du champ :** dam_name_fr

|dcdamsreturn|

.. _damsize:

Taille du barrage
+++++++++++++++++
 **Définition:** *La catégorie de taille du barrage en fonction de sa hauteur, en mètres.* 

 **Nom du champ :** size_class_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/damsize_fr.csv
    :widths: 15, 15, 70
    :header-rows: 1

|dcdamsreturn|

.. _damuse:

Utilisation du barrage
++++++++++++++++++++++
 **Définition:** *L’utilisation principale du barrage.*

 **Nom du champ :** use_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/damuse_fr.csv
    :widths: 15, 25, 60
    :header-rows: 1

|dcdamsreturn|

.. _degreg:

Degré de régularisation
+++++++++++++++++++++++
 **Définition:** *Degré de régularisation en pourcentage; équivaut au temps de séjour de l’eau dans le réservoir.*

 **Nom du champ :** degree_of_regulation_pc

|dcdamsreturn|

.. _downpass:

Voie de passage en aval
+++++++++++++++++++++++
 **Définition:** *Le type de voie de passage à poissons en aval associé au barrage.*

 **Nom du champ :** down_passage_route_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/downpass_fr.csv
    :widths: 15, 15, 70
    :header-rows: 1

|dcdamsreturn|

.. _explife:

Durée utile probable (années)
+++++++++++++++++++++++++++++
 **Définition:** *L’année où la structure atteindra sa fin de vie prévue.* 

 **Nom du champ :** expected_end_of_life

|dcdamsreturn|

.. _facilnameen:

Nom de l’installation (anglais)
+++++++++++++++++++++++++++++++
 **Définition:** *Le nom de l’installation plus importante dont le barrage fait partie (par exemple, une centrale hydroélectrique ou une exploitation minière), en anglais.*

 **Nom du champ :** facility_name_en

|dcdamsreturn|

.. _facilnamefr:

Nom de l’installation (français)
++++++++++++++++++++++++++++++++
 **Définition:** *Le nom de l’installation plus importante dont le barrage fait partie (par exemple, une centrale hydroélectrique ou une exploitation minière), en français.*

 **Nom du champ :** facility_name_fr

|dcdamsreturn|

.. _fedcompstat:

Conformité à la réglementation fédérale
+++++++++++++++++++++++++++++++++++++++
 **Définition:** *Les autorisations réglementaires que l’organisme fédéral chargé de délivrer les permis a approuvées pour le barrage.*

 **Nom du champ :** federal_compliance_status

|dcdamsreturn|

.. _fedflowreq:

Exigences de débit fédérales (m3/s)
+++++++++++++++++++++++++++++++++++
 **Définition:** *Le débit minimal recommandé pour le barrage, en mètres cubes par seconde (m3/s). Sur la base d’évaluations réalisées par Pêches et Océans Canada pour la protection des poissons et de leur habitat.*

 **Nom du champ :** federal_flow_req

|dcdamsreturn|

.. _gencap:

Capacité de production (MWh)
++++++++++++++++++++++++++++
 **Définition:** *La quantité d’électricité que l’installation hydroélectrique peut produire, en mégawattheures.*

 **Nom du champ :** generating_capacity_mwh

|dcdamsreturn|

.. _hydropeak:

Système de pointe hydroélectrique
+++++++++++++++++++++++++++++++++
 **Définition:** *Indique si le barrage utilise un système de pointe hydroélectrique.*

 **Nom du champ :** hydro_peaking_system

|dcdamsreturn|

.. _damheight:

Hauteur (m)
+++++++++++
 **Définition:** *La hauteur déclarée du barrage, en mètres. Selon la source de données, il peut s’agir de la hauteur de la paroi du barrage, de la hauteur de la crête ou de la hauteur de la chute.* 

 **Nom du champ :** height_m

|dcdamsreturn|

.. _lakectrl:

Régulateur du niveau du lac
+++++++++++++++++++++++++++
 **Définition:** *Indique si un réservoir a été construit à l’emplacement d’un lac naturel existant, le barrage agissant comme une structure de régulateur du niveau du lac.*

 **Nom du champ :** lake_control_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/lakectrl_fr.csv
    :widths: 15, 15, 70
    :header-rows: 1

|dcdamsreturn|

.. _lastmaint:

Date de la dernière maintenance
+++++++++++++++++++++++++++++++
 **Définition:** *La date des derniers travaux d’entretien ou de rénovation.*

 **Nom du champ :** maintenance_last

|dcdamsreturn|

.. _nextmaint:

Date de la prochaine maintenance
++++++++++++++++++++++++++++++++
 **Définition:** *La date des prochains travaux d’entretien ou de rénovation prévus.*

 **Nom du champ :** maintenance_next

|dcdamsreturn|

.. _turbcount:

Nombre de turbines
++++++++++++++++++
 **Définition:** *Le nombre de turbines du barrage.*

 **Nom du champ :** turbine_number

|dcdamsreturn|

.. _opstat:

État d’exploitation
+++++++++++++++++++
 **Définition:** *L’état d’exploitation du barrage.*

 **Nom du champ :** operating_status_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/opstat_fr.csv
    :widths: 15, 25, 60
    :header-rows: 1

|dcdamsreturn|

.. _owner:

Propriétaire
++++++++++++
 **Définition:** *La personne, l’entreprise, l’organisation, l’unité gouvernementale, le service public, la société ou toute autre entité qui détient un permis d’utilisation des eaux pour l’exploitation d’un barrage ou qui détient le titre de propriété légal du site du barrage.* 

 **Nom du champ :** owner

|dcdamsreturn|

.. _owntype:

Type de propriété
+++++++++++++++++
 **Définition:** *La catégorie de propriété associée au barrage.*

 **Nom du champ :** ownership_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/owntype_fr.csv
    :widths: 15, 25, 60
    :header-rows: 1

|dcdamsreturn|

.. _provcompstat:

Conformité à la réglementation provinciale
++++++++++++++++++++++++++++++++++++++++++
 **Définition:** *Les autorisations réglementaires que l’organisme provincial chargé de délivrer les permis a approuvées pour le barrage.* 

 **Nom du champ :** provincial_compliance_status

|dcdamsreturn|

.. _provflowreq:

Exigences de débit provinciales (m3/s)
++++++++++++++++++++++++++++++++++++++
 **Définition:** *Les exigences légales en matière d’écoulement pour le barrage, en mètres cubes par seconde (m3/s), réglementées par l’organisme provincial chargé de délivrer les permis.*

 **Nom du champ :** provincial_flow_req

|dcdamsreturn|

.. _remyear:

Année du retrait
++++++++++++++++
 **Définition:** *L’année au cours de laquelle le barrage a été mis hors service, retiré, remplacé, intégré ou détruit.*

 **Nom du champ :** removed_year

|dcdamsreturn|

.. _resarea:

Superficie du réservoir (km2)
+++++++++++++++++++++++++++++
 **Définition:** *La superficie du réservoir, en kilomètres carrés.* 

 **Nom du champ :** reservoir_area_skm

|dcdamsreturn|

.. _resdepth:

Profondeur du réservoir (m)
+++++++++++++++++++++++++++
 **Définition:** *La profondeur moyenne du réservoir, en mètres.*

 **Nom du champ :** reservoir_depth_m

|dcdamsreturn|

.. _resnameen:

Nom du réservoir (anglais)
++++++++++++++++++++++++++
 **Définition:** *Nom du réservoir ou du lac contrôlé (en anglais).* 

 **Nom du champ :** reservoir_name_en

|dcdamsreturn|

.. _resnamefr:

Nom du réservoir (français)
+++++++++++++++++++++++++++
 **Définition:** *Nom du réservoir ou du lac contrôlé (en français).* 

 **Nom du champ :** reservoir_name_fr

|dcdamsreturn|

.. _respres:

Réservoir présent
+++++++++++++++++
 **Définition:** *Indique si un réservoir est présent en raison de la construction du barrage.* 

 **Nom du champ :** reservoir_present

|dcdamsreturn|

.. _spillcap:

Capacité du déversoir
+++++++++++++++++++++
 **Définition:** *La capacité nominale de l’évacuateur de crues, en m3/s.* 

 **Nom du champ :** spillway_capacity

|dcdamsreturn|

.. _spilltype:

Type de déversoir
+++++++++++++++++
 **Définition:** *Le type de déversoir du barrage.* 

 **Nom du champ :** spillway_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/spilltype_fr.csv
    :widths: 15, 15, 70
    :header-rows: 1

|dcdamsreturn|

.. _storagecap:

Capacité de stockage (mmc)
++++++++++++++++++++++++++
 **Définition:** *La capacité de stockage du réservoir, en millions de mètres cubes.*

 **Nom du champ :** storage_capacity_mcm

|dcdamsreturn|

.. _structype:

Type de structure
+++++++++++++++++
 **Définition:** *Le type de structure.* 

 **Nom du champ :** structure_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/structype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _turbtype:

Type de turbine
+++++++++++++++
 **Définition:** *Le type de turbine du barrage.* 

 **Nom du champ :** turbine_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/turbtype_fr.csv
    :widths: 10, 25, 65
    :header-rows: 1

|dcdamsreturn|

.. _upcatcharea:

Superficie du bassin récepteur en amont (km2)
+++++++++++++++++++++++++++++++++++++++++++++
 **Définition:** *La superficie du bassin récepteur en amont se déversant dans le cours d’eau ou le réservoir, en kilomètres carrés.*

 **Nom du champ :** catchment_area_skm

|dcdamsreturn|

.. _uplength:

Longueur linéraire en amont (km)
++++++++++++++++++++++++++++++++
 **Définition:** *Le nombre de kilomètres linéaires non obstrués en amont du barrage qui deviendraient disponibles pour les espèces aquatiques si le barrage était éliminé.*

 **Nom du champ :** upstream_linear_km

|dcdamsreturn|

.. _uppasstype:

Type de passage en amont
++++++++++++++++++++++++
 **Définition:** *Le type de mesure de passage à poissons en amont associé au barrage.*

 **Nom du champ :** up_passage_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/uppasstype_fr.csv
    :widths: 15, 25, 60
    :header-rows: 1

|dcdamsreturn|

.. _useconservation:

Utilisation pour conservation 
+++++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins de conservation des espèces sauvages, et dans quelle mesure la conservation des espèces sauvages est une utilisation prévue.*

 **Nom du champ :** use_conservation_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _usefish:

Utilisation pour pêches
+++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins de pêcherie, et dans quelle mesure les pêcheries sont une utilisation prévue.*

 **Nom du champ :** use_fish_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _useflood:

Utilisation pour contrôle des inondations
+++++++++++++++++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins de prévention des inondations, et dans quelle mesure la prévention des inondations est une utilisation prévue.*

 **Nom du champ :** use_floodcontrol_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _usehydro:

Utilisation pour hydroélectricité
+++++++++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé pour la production d’hydroélectricité, et dans quelle mesure la production d’hydroélectricité est une utilisation prévue.*

 **Nom du champ :** use_eletricity_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _useais:

Utilisation pour contrôle d’espèces envahissantes
+++++++++++++++++++++++++++++++++++++++++++++++++
 **Définition:** 	*Indique qu’on utilise le barrage pour lutter contre les espèces envahissantes, et dans quelle mesure la lutte contre les espèces envahissantes est une utilisation prévue.*

 **Nom du champ :** use_invasivespecies_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _useirr:

Utilisation pour irrigation
+++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins d’irrigation, et dans quelle mesure l’irrigation est une utilisation prévue.* 

 **Nom du champ :** use_irrigation_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _usenav:

Utilisation pour navigation
+++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé pour la navigation, et dans quelle mesure la navigation est une utilisation prévue.*

 **Nom du champ :** use_navigation_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _useother:

Autre utilisation
+++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à d’autres fins, et dans quelle mesure il s’agit d’une utilisation prévue.*

 **Nom du champ :** use_other_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _usepoll:

Utilisation pour contrôle de la pollution
+++++++++++++++++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins de lutte contre la pollution, et dans quelle mesure la lutte contre la pollution est une utilisation prévue.*

 **Nom du champ :** use_pollution_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _userec:

Utilisation pour récréation
+++++++++++++++++++++++++++
 **Définition:** *Indique que le barrage est utilisé à des fins récréatives, et dans quelle mesure il s’agit d’une utilisation prévue.*

 **Nom du champ :** use_recreation_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

.. _usesupply:

Utilisation pour approvisionnement en eau
+++++++++++++++++++++++++++++++++++++++++
 **Définition:** *Indique qu’on utilise le barrage pour l’approvisionnement en eau, et dans quelle mesure il s’agit d’une utilisation prévue.*

 **Nom du champ :** use_supply_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/usetype_fr.csv
    :widths: 15, 20, 65
    :header-rows: 1

|dcdamsreturn|

Attributs propres aux chutes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _fallheight:

Hauteur de la chute (m)
+++++++++++++++++++++++
 **Définition:** *La hauteur de la chute, en mètres.* 

 **Nom du champ :** fall_height_m

|dcfallreturn|

.. _fallnameen:

Nom de la chute (anglais)
+++++++++++++++++++++++++
 **Définition:** *Nom de la chute (en anglais).*

 **Nom du champ :** fall_name_en

|dcfallreturn|

.. _fallnamefr:

Nom de la chute (français)
++++++++++++++++++++++++++
 **Définition:** *Nom de la chute (en français).*

 **Nom du champ :** fall_name_fr

|dcfallreturn|

Attributs uniques aux passes à poissons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _architect:

Architecte
++++++++++
 **Définition:** *Entreprise ou organisation ayant conçu la passe à poissons.* 

 **Nom du champ :** architect

|dcfishreturn|

.. _attraction:

Estimation du taux d’attraction (%)
+++++++++++++++++++++++++++++++++++
 **Définition:** *Proportion d’individus attirés par la passe à poissons, en pourcentage.* 

 **Nom du champ :** estimate_of_attraction_pct

|dcfishreturn|

.. _avgvelocity:

Vitesse moyenne du débit (m/s)
++++++++++++++++++++++++++++++
 **Définition:** *Vitesse moyenne de l’écoulement d’eau dans la passe à poissons, en m/s.* 

 **Nom du champ :** mean_fishway_velocity_ms

|dcfishreturn|

.. _constructby:

Construit par
+++++++++++++
 **Définition:** *Nom de l’entreprise ayant construit la passe à poissons.* 

 **Nom du champ :** constructed_by

|dcfishreturn|

.. _contractby:

Contrat avec
++++++++++++
 **Définition:** *Nom de l’agence avec laquelle on a conclu un contrat relativement à la passe à poissons.* 

 **Nom du champ :** contracted_by

|dcfishreturn|

.. _damid:

Identifiant du barrage
++++++++++++++++++++++
 **Définition:** *L’identifiant unique d’obstacle () du barrage auquel la passe à poissons est associée.* 

 **Nom du champ :** dam_id

|dcfishreturn|

.. _biodesign:

Conception en fonction de la biologie
+++++++++++++++++++++++++++++++++++++
 **Définition:** *Indique si la passe à poissons a été conçue en fonction de la biologie des espèces.* 

 **Nom du champ :** designed_on_biology

|dcfishreturn|

.. _elevation:

Élévation (m)
+++++++++++++
 **Définition:** *Variation de hauteur entre la sortie et l’entrée de la passe à poissons, en mètres.* 

 **Nom du champ :** elevation_m

|dcfishreturn|

.. _engnotes:

Notes d’ingénierie
++++++++++++++++++
 **Définition:** *Notes concernant la conception et la construction de la passe à poissons.* 

 **Nom du champ :** engineering_notes

|dcfishreturn|

.. _enterlocal:

Emplacement de l’entrée
+++++++++++++++++++++++
 **Définition:** *Indique si l’entrée de la passe à poissons est située au milieu du ruisseau ou sur la berge.* 

 **Nom du champ :** entrance_location_code

 **Valeurs autorisées :** Midstream(1), Bank(2)

|dcfishreturn|

.. _enterpos:

Position de l’entrée
++++++++++++++++++++
 **Définition:** *Indique la position de l’entrée de la passe à poissons dans la colonne d’eau.*

 **Nom du champ :** entrance_position_code 

 **Valeurs autorisées :** Bottom(1), Surface(2), Bottom and Surface(3), Mid-column(4)

|dcfishreturn|

.. _evalstudy:

Étude d’évaluation
++++++++++++++++++
 **Définition:** *La référence de la littérature (évaluée par les pairs et « grise ») que l’on a utilisée pour recueillir des renseignements supplémentaires sur la passe à poissons.* 

 **Nom du champ :** fishway_reference_id

|dcfishreturn|

.. _fishwaytype:

Type de passe à poissons
++++++++++++++++++++++++
 **Définition:** *Le type de passe à poissons (les valeurs correspondent à celles sous « Type de passage en amont »).* 

 **Nom du champ :** fishpass_type_code

 **Valeurs autorisées :**	

.. csv-table:: 
    :file: tbl/uppasstype_fr.csv
    :widths: 15, 25, 60
    :header-rows: 1

|dcfishreturn|

.. _Gradient:

Gradient
++++++++
 **Définition:** *L’angle d’inclinaison de la passe à poissons, en pourcentage.* 

 **Nom du champ :** Gradient

|dcfishreturn|

.. _hasevalstudy:

Avec études d’évaluation
++++++++++++++++++++++++
 **Définition:** *Indique si une étude d’évaluation a été réalisée relativement à la passe à poissons.* 

 **Nom du champ :** has_evaluating_studies

|dcfishreturn|

.. _ismod:

Modifications
+++++++++++++
 **Définition:** *Indique si on a apporté des modifications post-construction à la passe à poissons.* 

 **Nom du champ :** modified

|dcfishreturn|

.. _maxvelo:

Vitesse maximale du débit (m/s)
+++++++++++++++++++++++++++++++
 **Définition:** *Vitesse maximale d’écoulement de l’eau enregistrée dans la passe à poissons, en m/s.* 

 **Nom du champ :** max_fishway_velocity_ms

|dcfishreturn|

.. _meandepth:

Profondeur moyenne du canal (m)
+++++++++++++++++++++++++++++++
 **Définition:** *Profondeur de la passe à poissons, en mètres, pendant l’exploitation.* 

 **Nom du champ :** depth_m

|dcfishreturn|

.. _modpurpose:

But des modifications
+++++++++++++++++++++
 **Définition:** *Objectif des modifications post-construction.*

 **Nom du champ :** modification_purpose

|dcfishreturn|

.. _modyear:

Année des modifications
+++++++++++++++++++++++
 **Définition:** *L’année au cours de laquelle les modifications post-construction ont été achevées.*

 **Nom du champ :** modification_year

|dcfishreturn|

.. _monitor:

Équipement de surveillance
++++++++++++++++++++++++++
 **Définition:** *Équipement de surveillance utilisé pour la passe à poissons.*

 **Nom du champ :** monitoring_equipment

|dcfishreturn|

.. _natureevalstudy:

Nature des études d’évaluation
++++++++++++++++++++++++++++++
 **Définition:** *Le type d’étude d’évaluation effectuée.*

 **Nom du champ :** nature_of_evaluation_studies

|dcfishreturn|

.. _opby:

Exploitation par
++++++++++++++++
 **Définition:** *Agence responsable de l’exploitation de la passe à poissons.*

 **Nom du champ :** operated_by

|dcfishreturn|

.. _opperiod:

Période d’exploitation
++++++++++++++++++++++
 **Définition:** *Les dates auxquelles la passe à poissons est exploitée.*

 **Nom du champ :** operation_period

|dcfishreturn|

.. _plansheld:

Plans détenus par
+++++++++++++++++
 **Définition:** *Nom de l’agence qui possède les plans de la passe à poissons.*

 **Nom du champ :** plans_held_by

|dcfishreturn|

.. _fishwaypurpose:

But de la passe à poissons
++++++++++++++++++++++++++
 **Définition:** *La raison pour laquelle on a conçu et mis en place la passe à poissons.* 

 **Nom du champ :** purpose

|dcfishreturn|

.. _rivnameen:

Nom rivière/ruisseau (anglais)
++++++++++++++++++++++++++++++
 **Définition:** *Nom de la rivière ou du ruisseau dans lequel l’élément est enregistré (en anglais).* 

 **Nom du champ :** river_name_en

|dcfishreturn|

.. _rivnamefr:

Nom rivière/ruisseau (français)
+++++++++++++++++++++++++++++++
 **Définition:** *Nom de la rivière ou du ruisseau dans lequel l’élément est enregistré (en français).* 

 **Nom du champ :** river_name_fr

|dcfishreturn|

.. _knownnotuse:

Espèces qui ne l’utilisent pas
++++++++++++++++++++++++++++++
 **Définition:** *Espèces pour lesquelles on sait que la passe à poissons constitue un obstacle important à la migration.*

 **Nom du champ :** known_to_not_use

|dcfishreturn|

.. _knowntouse:

Espèces qui l’utilisent
+++++++++++++++++++++++
 **Définition:** *Espèces que l’on sait utiliser la passe à poissons.* 

 **Nom du champ :** known_to_use

|dcfishreturn|

.. _strucnameen:

Nom de la structure (anglais)
+++++++++++++++++++++++++++++
 **Définition:** *Le nom de la passe à poissons ou du barrage auquel elle est associée (en anglais).* 

 **Nom du champ :** structure_name_en

|dcfishreturn|

.. _strucnamefr:

Nom de la structure (français)
++++++++++++++++++++++++++++++
 **Définition:** *Le nom de la passe à poissons ou du barrage auquel elle est associée (en français).* 

 **Nom du champ :** structure_name_fr

|dcfishreturn|

.. _systemid:

Identifiant du système
++++++++++++++++++++++
 **Définition:** *Identifiant unique pour chaque point de la passe à poissons.* 

 **Nom du champ :** cabd_id

|dcfishreturn|

.. _success:

Estimation du taux de passage (%)
+++++++++++++++++++++++++++++++++
 **Définition:** *Pourcentage estimé d’individus qui réussissent à franchir la passe à poissons.*

 **Nom du champ :** estimate_of_passage_success_pct

|dcfishreturn|

.. _yearconst:

Année de construction
+++++++++++++++++++++
 **Définition:** *Année au cours de laquelle la passe à poissons a été construite.* 

 **Nom du champ :** year_constructed

|dcfishreturn|