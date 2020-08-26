import stardog
from request.setup import Prefixes

class ConnectionFactory():
    '''
    A class used to represent and manage a Stardog database connection
    
    Attributes
    ----------
    
    connectionPool : dict
        A dict with three items used to connect to stardog.
            endpoint : str
                the host where stardog is running. Default = 'http://localhost:5820'
            username : str
                the username used to log in to the base. Default = 'admin'
            password : str
                the password dused to log in to the base. Default = 'admin'
    '''
    connectionPool = {
        'endpoint' : 'http://192.168.56.104:5820',
        'username' : 'admin',
        'password' : 'admin'
    }

    connectionPoolUfes = {
        'endpoint' : 'http://200.137.66.31:5820',
        'username' : 'nemo',
        'password' : 'nemonemo'
    }
    
    databaseName = 'riodoce'
    
    connection = stardog.Connection(databaseName,**connectionPool)
    if(connection):
        print(str(connection))
    else:
        print('null')
    def __init__(self):
        pass
    
    
    def __listAllProps(self, prd):
        return self.connection.select('PREFIX prd: <'+ Prefixes.PREFIX +'>'+
                          ' SELECT distinct ?prop WHERE{?prop rdf:type prd:'+ prd +'}')
    
    def listProperty(self):
        return self.__listAllProps('Measurable_Property')
        
        
    def listParty(self):
        return self.__listAllProps('Agent_Party')

        
    def listRiver(self):
        return self.__listAllProps('River')    
        
    def getFilteredData(self, allFilters):
        finalQuery = ''
        filterPropertiesSelected = ''
        print('all filters '+allFilters)
        finalQuery = ('PREFIX prd: <'+ Prefixes.PREFIX +'>'
        + 'SELECT ?author ?property ?value ?unity ?sample'
        + '?sampleDate ?lat ?long ?monitoringFacility ?locale'
        + ' WHERE {'
        + ' ?measurement rdf:type prd:Measurement.'
        + ' ?measurement prd:measure_unit ?unity.'
        + ' ?measurement prd:measures ?property.'
        + ' ?measurement prd:val ?value.'
        + ' ?measurement prd:uses ?sample.'
        + ' ?measurement prd:isDoneBy ?author.'
        + filterPropertiesSelected
        + ' ?sample rdf:type prd:Sampling.'
        + ' ?sample prd:date ?sampleDate.'
        + ' ?monitoringFacility rdf:type prd:Monitoring_Facility.'
        + ' ?monitoringFacility prd:performs ?sample.'
        + ' ?monitoringFacility prd:locates ?locale.'
        + ' ?locale rdf:type prd:Geographic_Point.'
        + ' ?locale prd:latitude ?lat.'
        + ' ?locale prd:longitude ?long'
        + allFilters
        + '.}LIMIT 10')
        return self.connection.select(finalQuery)
    
    def measurement(self, allFilters):
        finalQuery = ''
        filterPropertiesSelected = ''
        print('all filters '+allFilters)
        finalQuery = ('PREFIX prd: <'+ Prefixes.PREFIX +'>'
        + 'SELECT ?author ?property ?value ?unity ?sample'
        + '?sampleDate ?lat ?long ?monitoringFacility ?locale'
        + ' WHERE {'
        + ' ?measurement rdf:type prd:Measurement.'
        + ' ?measurement prd:measure_unit ?unity.'
        + ' ?measurement prd:measures ?property.'
        + ' ?measurement prd:val ?value.'
        + ' ?measurement prd:uses ?sample.'
        + ' ?measurement prd:isDoneBy ?author.'
        + filterPropertiesSelected
        + ' ?sample rdf:type prd:Sampling.'
        + ' ?sample prd:date ?sampleDate.'
        + ' ?monitoringFacility rdf:type prd:Monitoring_Facility.'
        + ' ?monitoringFacility prd:performs ?sample.'
        + ' ?monitoringFacility prd:locates ?locale.'
        + ' ?locale rdf:type prd:Geographic_Point.'
        + ' ?locale prd:latitude ?lat.'
        + ' ?locale prd:longitude ?long'
        + allFilters
        + '.}LIMIT 10')
        return self.connection.select(finalQuery)