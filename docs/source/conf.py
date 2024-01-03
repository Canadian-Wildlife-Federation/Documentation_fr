# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Canadian Aquatic Barriers Database'
copyright = '2022, Canadian Wildlife Federation'
#author = 'alexl'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_book_theme
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add custom css file relative to html_static_path
html_css_files = [
    'css/custom_cwf_book.css',
    'https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css',
]

# Java Files
html_js_files = [
    'https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js',
    'main.js',
]
# Add a custom favicon and html logo to sidebar
html_favicon = '_static/branding/favicon.ico'
html_logo = '_static/cwf_logo_fr.png'

html_theme_options = {
    'logo_only': True,
    "repository_url": "https://github.com/Canadian-Wildlife-Federation",
    "use_issues_button": True,
    "repository_branch": "",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "extra_footer": False,
    "extra_navbar": "<p></p>",
    "home_page_in_toc": False,
    "toc_title": "Document Contents",
    "navigation_depth": 3,
    "search_bar_text": "Recherche...",
}

# Role created to be able to use up arrow symbol as a the target for hyperlinks (i.e., return to top)
rst_epilog = """
.. role:: raw-html(raw)
   :format: html

.. |ds_searchtbl_return| replace:: :raw-html:`<a href="#data-sources-search-table"><i class="fas fa-arrow-up">
   </i></a>`
.. |dcdamsreturn| replace:: :raw-html:`<a href="#dams"><i class="fas fa-arrow-up">
   </i></a>`
.. |dcfishreturn| replace:: :raw-html:`<a href="#fishways"><i class="fas fa-arrow-up">
   </i></a>`
.. |dcfallreturn| replace:: :raw-html:`<a href="#waterfalls"><i class="fas fa-arrow-up">
   </i></a>`
.. |arrdown| replace:: :raw-html:`<i class="fas fa-arrow-down">
   </i>`
.. |fttype| replace:: :raw-html:`<p><span class="cbm">/features/types/<span class="cbmcc">&lt;type&gt</span></span></p>`
.. |ftid| replace:: :raw-html:`<p><span class="cbm">/features/<span class="cbmcc">&lt;feature-id&gt</span></span></p>`
.. |ftbbox| replace:: :raw-html:`<p><span class="cbm">/features?bbox=<span class="cbmcc">&lt;min_long&gt</span>,<span class="cbmcc">&lt;min_lat&gt</span>,<span class="cbmcc">&lt;max_long&gt</span>,<span class="cbmcc">&lt;max_lat&gt</span>&types=<span class="cbmcc">&lt;type&gt</span>,<span class="cbmcc">&lt;type&gt</span></span></p>`
.. |ftpoint| replace:: :raw-html:`<p><span class="cbm">/features?point=<span class="cbmcc">&lt;longitude&gt</span>,<span class="cbmcc">&lt;latitude&gt</span>&max-results=<span class="cbmcc">&lt;n&gt</span>&types=<span class="cbmcc">&lt;type&gt</span>,<span class="cbmcc">&lt;type&gt</span></span></p>`
.. |ftfilter| replace:: :raw-html:`<p><span class="cbm">/features?filter=<span class="cbmcc">&lt;filter&gt</span>&filter=<span class="cbmcc">&lt;filter&gt</span></span></p>`
.. |ftnamefilter| replace:: :raw-html:`<p><span class="cbm">/features?namefilter=<span class="cbmcc">&lt;namefilter&gt</span></span></p>`
.. |bboxcoords| replace:: :raw-html:`<p><span class="cbm"><span class="cbmcc">&lt;min_long&gt</span>,<span class="cbmcc">&lt;min_lat&gt</span>,<span class="cbmcc">&lt;max_long&gt</span>,<span class="cbmcc">&lt;max_lat&gt</span></span></p>`
.. |latlong| replace:: :raw-html:`<p><span class="cbm"><span class="cbmcc">&lt;longitude&gt</span>,<span class="cbmcc">&lt;latitude&gt</span></span></p>`
.. |ftstype| replace:: :raw-html:`<p><span class="cbm">/features/<span class="cbmcc">&lt;type&gt</span></span></p>`
.. |ftsbbox| replace:: :raw-html:`<p><span class="cbm">/features/<span class="cbmcc">&lt;type&gt</span>?bbox=<span class="cbmcc">&lt;min_lat&gt</span>,<span class="cbmcc">&lt;min_long&gt</span>,<span class="cbmcc">&lt;max_lat&gt</span>,<span class="cbmcc">&lt;max_long&gt</span></span></p>`
.. |ftspoint| replace:: :raw-html:`<p><span class="cbm">/features/<span class="cbmcc">&lt;type&gt</span>?point=<span class="cbmcc">&lt;min_long&gt</span>,<span class="cbmcc">&lt;min_lat&gt</span>&max-results=<span class="cbmcc">&lt;n&gt</span></span></p>`
.. |ftsfilter| replace:: :raw-html:`<p><span class="cbm">/features/<span class="cbmcc">&lt;type&gt</span>?filter=<span class="cbmcc">&lt;filter&gt</span>&filter=<span class="cbmcc">&lt;filter&gt</span></span></p>`
.. |tilestype| replace:: :raw-html:`<p><span class="cbm">/tiles/<span class="cbmcc">&lt;type&gt</span>/z/x/y.mvt</span></p>`
.. |filterreq| replace:: :raw-html:`<p><span class="cbm">filter=<span class="cbmcc">&lt;attribute&gt</span>:<span class="cbmcc">&lt;operator&gt</span>:<span class="cbmcc">&lt;values&gt</span></span>, ou:</p>`
.. |namefilterreq| replace:: :raw-html:`<p><span class="cbm">namefilter=<span class="cbmcc">&lt;operator&gt</span>:<span class="cbmcc">&lt;values&gt</span></span></p>`
.. |filterattr| replace:: :raw-html:`<p><span class="cbmcc">&lt;attribute&gt</span></p>`
.. |filterop| replace:: :raw-html:`<p><span class="cbmcc">&lt;operator&gt</span></p>`
.. |filtervals| replace:: :raw-html:`<p><span class="cbmcc">&lt;values&gt</span></p>`
.. |namefilterop| replace:: :raw-html:`<p><span class="cbmcc">&lt;operator&gt</span></p>`
.. |namefiltervals| replace:: :raw-html:`<p><span class="cbmcc">&lt;values&gt</span></p>`
.. |fttype2| replace:: :raw-html:`<p>La clé d’attribut décrite dans le schéma du type d’élément (<span class="cbm">features/types/<span class="cbmcc">&lt;type&gt</span></span>).</p>`
.. |ftdsid| replace:: :raw-html:`<p><span class="cbm">/features/datasources/<span class="cbmcc">&lt;feature-id&gt</span></span></p>`
.. |ftdsidflds| replace:: :raw-html:`<p><span class="cbm">/features/datasources/<span class="cbmcc">&lt;feature-id&gt</span>?fields=all</span></p>`
.. |ftdsidjson| replace:: :raw-html:`<p><span class="cbm">/features/datasources/<span class="cbmcc">&lt;feature-id&gt</span>?format=json</span></p>`
.. |requestex1|  replace:: :raw-html:`<p>Si vous souhaitez demander les métadonnées associées aux barrages, <span class="cbm">/features/types/<span class="cbmcc">&lt;type&gt</span></span> doit être remplacé par <span class="cbm">/features/types/dams</span>.</p>`
.. |enfr| replace:: :raw-html:`<p>The view <span class="cbm">cabd.all_features_view_<span class="cbmcc">&lt;en/fr&gt</span></span> supports all feature api endpoints.</p>`
.. |formatnote|  replace:: :raw-html:`<p>The best way to download data for multiple feature types using the API is to use the <span class="cbm">/features/<span class="cbmcc">&lt;type&gt</span></span> endpoint.</p>`
.. |typenote| replace:: :raw-html:`<p>While the <span class="cbm">/features/</span> endpoint will return features from multiple feature types, the list of attributes returned are very limited compared to the list of attributes returned when the <span class="cbm"><span class="cbmcc">&lt;type&gt</span></span> is specified.</p>`
.. |chyfuuid| replace:: :raw-html:`<p><span class="cbm">/chyf-web/features/<span class="cbmcc">&lt;uuid&gt</span></span></p>`
.. |singlemultisearch| replace:: :raw-html:`<p><span class="cbm">/chyf-web/features?name= <span class="cbmcc">&lt;string&gt</span> &max-results= <span class="cbmcc">&lt;int&gt</span> &result-type= <span class="cbmcc">[BBOX,ALL,GROUPBYTYPE,GROUPBYNAME]</span> &feature-type= <span class="cbmcc">[WATERBODY,FLOWPATH,CATCHMENT]</span> &match-type= <span class="cbmcc">[EXACT,CONTAINS]</span></span></p>`
"""
def setup(app):
    app.add_css_file('custom.css')