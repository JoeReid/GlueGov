GlueGov
=======

Surfacing disporate goverment spreadsheet data with a clean searchable API.

Created at [National Hack the Goverment 2015 London](http://hacks.rewiredstate.org/events/nhtg-2015-london/)


Summary
-------

There are multiple government departments that publish data via spreadsheets. Although this data is 'open' it is reasonably inaccessible to developers. Each developer has to load/parse/clean/transform the data before use. If the developer/user wants to access all the information for 'Bristol' they need to open 20+ Spreadsheets from radically differnt sources and extract the relevant 'Bristol' data.

### Problem ###

1. ) There is no central way for developers to view or search disparate spreadsheet data from multiple government departments.
2. ) Services exisit to list simplifyed goverment data to users via a web frontend e.g [FindAHood](http://www.findahood.com/locations/bristol,cityof/6275035 "FindAHood Bristol"). But these services are closed and limited.

### Solution ###

1. ) Create an API that surfaces spreadsheets with search/filter functionality in a uniform way.
2. ) With the API, new frontend and user explorable services are possible


Future Development
------------------

### API Features ###

* Add more datasets
    * Currently only a few prototype examples are avalable
* Add automatic redownload and updating of sources datasets
    * The API could return the last datetime the source was updated and provide links back to the orginal source material
* API endpoint to search accoss multiple sources automatically (currenly searching is explicit for each type of table)

### Overall ####

* It would be nice if this API concept was officailly supported and maintained by the goverment.
* A user visible web service could be created to allow everyday people to explore the data and ask there own questions. 


Supported Datasets
------------------
See [server/gluegov/data](https://github.com/JoeReid/GlueGov/tree/master/server/gluegov/data) for current plugins


Project Structure
-----------------

* server
	* downloads spreadsheet data from known dataset list 
	* serve acessible api `json`, `xml`, `html` tables
* client
	* Example `bootstrap` client to demo aquiring filtered information for a town by name.
* graphs
	* Example of graphs drawing from data from the API 


Setup/Running
-------------

* server
    * `git clone https://github.com/JoeReid/GlueGov.git && cd GlueGov/server && make run && python -m webbrowser -t "http://localhost:6543/"` (this should automatically download the source datasets and may take some time)
    * Filter examples
	    * http://localhost:6543/traffic/majorroads?Year=eq:2013
	    * http://localhost:6543/landregistry/pricepaid?format=json&price=lte:100000
* client
    * view the `client/client.html` file (after running `make`)


Team
----

* Joe Reid (jcreid.computing@gmail.com)
* Allan Callaghan (calaldees@gmail.com) (@calaldees)
* Richard Lancaster (lancasterrich@gmail.com) (@RichLancaster)
