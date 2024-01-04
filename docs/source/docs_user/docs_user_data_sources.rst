.. _data-sources:


===================
Sources des données
===================

.. admonition:: Remarque
    
    Si vous avez accidentellement fermé votre onglet de l’outil Web de la BDOAC, vous pouvez accéder à l’outil Web `ici <https://aquaticbarriers.ca/fr>`_.


La BDOAC existe grâce au travail minutieux de bon nombre de groupes et d’organisations qui ont compilé et tenu à jour des inventaires d’obstacles à l’échelle de l’Amérique du Nord et qui les ont rendus accessibles à tous ou qui ont conclu des ententes d’échange de données avec nous. Un grand merci à ces groupes! La BDOAC s’appuie simplement sur ce travail existant, et nous espérons que notre travail visant à combler les lacunes en matière de données profitera en retour aux détenteurs de données originales. Si vous êtes le responsable de l’une des sources des données figurant sur cette page et que vous souhaitez discuter de la manière dont nous pouvons vous permettre de profiter de certaines de nos mises à jour des données, veuillez communiquer avec nous à cabd@cwf-fcf.org.

Une grande partie du travail effectué par rapport à la BDOAC a servi à dédupliquer et à combiner des attributs dans les cas où plusieurs sources des données avaient un point représentant la même structure. Cela signifie que pour un seul point de la BDOAC, les renseignements sur les attributs peuvent provenir de plusieurs sources différentes, ce qui rend l’attribution des sources des données quelque peu délicate. Nous avons trouvé une solution pour cartographier l’origine de chaque attribut des points de données de la BDOAC; consultez la page :ref:`Feature Data Source Details Download (téléchargement des détails sur la source des données sur l’élément) <data-source-details>` pour en savoir plus.

.. attention::

    *Veuillez noter que les informations suivantes sur les sources des données sont présentées en anglais car elles proviennent directement de la base de données et ne sont pas encore disponibles en français.*
    
    *Les données de la BDOAC sont mises à la disposition de tous grâce à la licence* `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/deed.fr>`_ *Cette licence vous permet de transmettre et d’adapter les données, du moment que vous mentionnez la source et que vous distribuez les données dérivées en utilisant la même licence CC BY-SA 4.0.*

Tableau de recherche des sources des données
--------------------------------------------


.. raw:: html
  
    <div id="datasourcecontent"/>
    
    <script>
    function loadDataSources() {
    
      let url = "https://cabd-web.azurewebsites.net/cabd-api/docs?options=ds"
      let xhr = new XMLHttpRequest();
      // Making our connection 
       xhr.open("GET", url, true);
   
      // function execute after request is successful
      xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let element = document.getElementById("datasourcecontent");
            element.innerHTML = this.responseText;   
            //convert this into a dataTable
            $('#ds_dataTable').DataTable();
            
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
         
         if (kid.tagName.toLowerCase() == "section" && kid.id.startsWith("dsid_")){
            
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
               if (kid2.tagName.toLowerCase() == "section" && kid2.id.startsWith("dsid_")){         
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

  
.. toctree::
    :maxdepth: 3
    :hidden:

    docs_user_data_sources/docs_user_data_sources_csv_download
  
