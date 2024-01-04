.. Canadian Aquatic Barriers Database documentation master file, created by
   sphinx-quickstart on Fri Nov 19 15:33:08 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**La Base de données sur les obstacles aquatiques du Canada (BDOAC)**
=====================================================================

Site de documentation
---------------------

.. admonition:: Remarque

   Le projet BDOAC est en cours de développement, ce qui signifie que le contenu de la base de données et de ce site peut changer fréquemment. Consultez notre page :ref:`Quoi de neuf ? <whats-new>` pour connaître les dernières mises à jour !

-----

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Bienvenue sur le site de documentation de la Base de données sur les obstacles aquatiques du Canada (BDOAC) !
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Toute l'information sur les barrières aquatiques et la connectivité en eau douce au Canada en un seul endroit - facilement et ouvertement accessible !*

La BDOAC est un référentiel normalisé, curé, central et ouvert pour les données sur les barrières et la connectivité au Canada. Il s'agit d'un outil destiné à soutenir les travaux dans divers domaines et secteurs liés à la connectivité des eaux douces et aux barrières aquatiques. La base de données est accessible via notre outil web à `aquaticbarriers.ca <https://aquaticbarriers.ca/fr>`_.

Il s'agit d'un guichet unique pour en savoir plus sur le BDOAC, sur la manière d'accéder aux données et de les utiliser, et pour nous aider à combler les lacunes et à améliorer la base de données. Le site est divisé en deux sections :

#. Ressources utilisateurs BDOAC
#. Documentations techniques du BDOAC

Consultez la section **Ressources utilisateurs BDOAC** si vous souhaitez l'explorer :

- Les dernières :ref:`annonces et publications de données <whats-new>`
- Un :ref:`aperçu du projet BDOAC <cabd-overview>` et les utilisations des données
- :ref:`Tutoriels <tutorials>` sur l'utilisation de l'outil web et l'accès aux données
- Les :ref:`sources des données <data-sources>` utilisées pour développer le BDOAC
- Les :ref:`définitions <data-catalogue>` des couches de données et des attributs associés
- Comment nous aider :ref:`à combler les lacunes des données <submit-updates>` en soumettant des mises à jour d'utilisateurs
- Le :ref:`processus d'engagement <stakeholder-engagement>` qui a soutenu le développement de la BDOAC et des outils associés

Si vous souhaitez vous plonger dans les aspects plus techniques de la base de données, consultez la section **Documentations techniques du BDOAC** :

- Un aperçu de :ref:`l'architecture de l'application <cabd-models>`
- Comment accéder aux données et aux sources des données de la BDOAC via :ref:`les services API REST <cabd-rest-services>`
- Apprendre comment les données de la BDOAC ont été :ref:`compilées et traitées <reviewmethods>`

Le BDOAC est un projet collaboratif développé et maintenu par la Fédération canadienne de la faune. Vous pouvez visiter notre `site web <https://cwf-fcf.org/fr/explorer/permettre-le-passage-du-poisson/>`_ pour en savoir plus sur notre travail en faveur de la connectivité des eaux douces et du passage des poissons.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Remerciements pour le financement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*La base de données canadienne sur les barrières aquatiques est un projet pluriannuel soutenu en partie par des contributions financières de Pêches et Océans Canada.*

*La base de données sur les barrières aquatiques canadiennes est également financée en partie par RBC Fondation dans le cadre du programme Techno nature RBC.*


.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: DOCUMENTATION ANGLAIS

   https://cabd-docs.netlify.app/

.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: RESSOURCES UTILISATEUR BDOAC

   docs_user/whats_new
   docs_user/cabd_overview
   docs_user/docs_user_web_map
   docs_user/docs_user_data_sources
   docs_user/docs_user_data_catalogue
   docs_user/docs_user_submitted_updates
   docs_user/docs_user_engagement
   docs_user/acknowledgements



.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Documents techniques du BDOAC

   docs_tech/docs_tech_arch_models
   docs_tech/docs_tech_arch_api
   docs_tech/docs_tech_arch_tiles
   docs_tech/docs_tech_feature_review

.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: CHyF Documents

   docs_chyf/docs_chyf_logical_model
   docs_chyf/docs_chyf_data_model
   docs_chyf/docs_chyf_tools
   docs_chyf/docs_chyf_process