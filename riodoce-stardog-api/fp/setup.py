from urllib.parse import unquote

class UriTreatment():
    @staticmethod
    def __formatValue(value):
        v = value.split('#')
        value = v[len(v)-1]
        return str(unquote(value))

    @staticmethod
    def formatJson(json):
        file = json['results']['bindings']
        for i in range(len(file)):
            file[i]['prop']['value'] = UriTreatment.__formatValue(file[i]['prop']['value'])
        return json
    
class FilterAnalyser():
    
    @staticmethod
    def getFilterList(json):
        filters = []
        props = json['results']['bindings']
        for i in range(len(props)):
            filters.append(props[i]['prop']['value'])
        return filters
    
    @staticmethod
    def createFilterString(propList, party, initialDate, finalDate, initialPoint, finalPoint):
        allFilter = ''
        propSelected = []
        print(propList)
        if(propList != ['']):
            print('entrou')
            for i in range(len(propList)):
                allFilter = allFilter + ' FILTER( ?property = prd:' + propList[i] + ')'
            
        if(initialDate != ''):
            pass
        
        if(finalDate != ''):
            pass
        
        if(initialPoint != '' and finalPoint != ''):
            lat1 = FilterAnalyser.getLat(initialPoint)
            lat2 = FilterAnalyser.getLat(finalPoint)
            long1 = FilterAnalyser.getLong(initialPoint)
            long2 = FilterAnalyser.getLong(finalPoint)
            allFilter = allFilter + ' FILTER( ?lat >= "' + lat1 + '" && ?lat <= "'+lat2+'")'
            allFilter = allFilter + ' FILTER( ?long >= "' + long1 + '" && ?long <= "'+long2+'")'
            
        print("allFilter: " + allFilter)
        return allFilter        

    @staticmethod
    def newFilter(myDict):
        allFilter = ''
        operador = '='
        
        for i, j in myDict.items():
            array = i.split('.')
            if(j[:2].upper() == 'BT'):
                operador = '>='
                j = j[2:]
                #print('j=')
                #print(j)
            elif (j[:2].upper() == 'LT'):
                operador = '<='
                j = j[2:]
                #print('j=')
                #print(j)
            if(len(array)>1):    
                allFilter = allFilter + ' FILTER ( ?'+ array[len(array)-1]+' '+operador+' "'+j+'")'
                print(allFilter)
            else:
                allFilter = allFilter + ' FILTER ( ?'+ array[0]+' '+operador+' '+'prd:'+j+')'
            
        return allFilter

  
    @staticmethod
    def getLat(point):
        point = point.split('$')
        return point[0]
        
    @staticmethod    
    def getLong(point):
        point = point.split('$')
        return point[1]