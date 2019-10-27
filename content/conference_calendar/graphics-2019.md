title: Computer Graphics Conference Calendar 2019
slug: graphics-calendar-2019
category: conference calendar
date: 2018-11-13
modified: 2018-11-13
summary: A table containing important dates for Computer Graphics conferences in 2019

<div id = "tabulator"></div>

<span>Rank Information from <a href="http://www.conferenceranks.com/">Conference Ranks</a>

{% set TABULATOR_COLUMNS = [
        {"title":"Name", "field":"name", "sorter":"string"},
        {"title":"Abbrev", "field":"abbrev", "sorter":"string", "width": 120},
        {"title":"Rank", "field":"rank", "sorter":"string", "width": 80},
        {"title":"Topics", "field":"topics", "sorter":"string"},
    ] 
%}

{% set TABULATOR_DATA = [
        {"name": "Graphics Interface", "abbrev": "GI", "rank": "A2/B", "topics": "Graphics, Visualization, HCI"},
        {"name": "Eurographics Symposium on Rendering", "abbrev": "EGSR", "rank": "B1", "topics": "Rendering, Machine Learning for Image Synthesis, Realistic, Non-Photorealistic"},
        {"name": "European Graphics Conference", "abbrev": "EUROGRAPH", "rank": "A", "topics": ""},
        {"name": "Eurographics Annual Conference of the European Association for Computer Graphics", "abbrev": "EUROGRAPHICS", "rank": "A2", "topics": ""},
        {"name": "Eurographics/IEEE Symposium on Visualization", "abbrev": "EuroVis", "rank": "B/B1", "topics": ""},
        {"name": "Eurographics Symposium on Parallel Graphics and Visualization", "abbrev": "EGPGV", "rank": "B", "topics": ""},
        {"name": "ACM Symposium on Interactive 3D Graphics and Games", "abbrev": "I3D", "rank": "A2", "topics": ""},
        {"name": "Interactive 3D Graphics", "abbrev": "I3DG", "rank": "A", "topics": ""},
        {"name": "Computer Graphics International", "abbrev": "CGI", "rank": "B/B1", "topics": ""},
        {"name": "Pacific Conference on Computer Graphics and Applications", "abbrev": "PG", "rank": "A/A2", "topics": ""},
        {"name": "International Conference on Computer Graphics and Interactive Techniques in Australasia and Southeast Asia", "abbrev": "SIGGRAPHASIA", "rank": "B", "topics": ""},
        {"name": "International Conference on Computer Graphics Theory and Applications", "abbrev": "GRAPP", "rank": "A/B4", "topics": ""},
        {"name": "Eurographics Symposium on Computer Animation", "abbrev": "SCA", "rank": "A2/B", "topics": ""},
        {"name": "ACM SIG International Conference on Computer Graphics and Interactive Techniques", "abbrev": "SIGGRAPH", "rank": "A", "topics": ""},
    ]
%}

{% include "include/tabulator.html" %}