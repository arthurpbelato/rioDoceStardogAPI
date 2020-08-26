from flask import Flask
from flask import request
from flask import Response
from flask_restful import Resource
from flask_restful import Api
from dao.setup import *
from fp.setup import *
from const import Constant

mainApp = Flask(__name__)
api = Api(mainApp)


class River(Resource):
    def get(self):
        cf = ConnectionFactory()
        json = cf.listRiver()
        json = UriTreatment.formatJson(json)
        
        if(json['results']['bindings'] == []):
            return ('', 204)
        return json
    
class Property(Resource):
    def get(self):
        cf = ConnectionFactory()
        json = cf.listProperty()
        json = UriTreatment.formatJson(json)
        
        if(json['results']['bindings'] == []):
            return ('', 204)
        return json


class Party(Resource):
    def get(self):
        cf = ConnectionFactory()
        json = cf.listParty()
        json = UriTreatment.formatJson(json)
        
        if(json['results']['bindings'] == []):
            return ('', 204)
        return json


class FilteredMeasurement(Resource):
    def get(self):
        propertyList = []
        initialPoint = ''
        finalPoint = ''
        cf = ConnectionFactory()
        capableFilters = cf.listProperty()
        capableFilters = UriTreatment.formatJson(capableFilters)
        capablePropertyFiltersList = FilterAnalyser.getFilterList(capableFilters)
        propertyList = str(request.args.get('property', default = '')).split('$')
        
        '''
        Check if there is more than one point selected
        '''
        initialPoint = request.args.get('selectedPoint', default = '')
        
        if(initialPoint != ''):
            finalPoint = initialPoint
        else:
            initialPoint = request.args.get('initialPoint', default = '')
            finalPoint =  request.args.get('finalPoint', default = '')
        

        '''
        Check if there is more than one date selected
        '''
        initialDate = request.args.get('selectedDate', default = '')
        
        if(initialDate != ''):
            finalDate = initialDate
        else:
            initialDate = request.args.get('initialDate', default = '')
            finalDate = request.args.get('finalDate', default = '')
            
        filterString = FilterAnalyser.createFilterString(propertyList,
            request.args.get('measurementPartiesSelect', default = ''),
            initialDate,
            finalDate,
            initialPoint,
            finalPoint)
        json = cf.getFilteredData(filterString)
        
        if(json['results']['bindings'] == []):
            return ('', 204)
        return json

class Measurement(Resource):
    def get(self):
        cf = ConnectionFactory()
        print ('Parametros = ')
        argsDict =  request.args
        argsDict = dict(argsDict)
        filterString = FilterAnalyser.newFilter(argsDict)
        json = cf.measurement(filterString)    
        return json
    
api.add_resource(Property,'/list/property')
api.add_resource(Party,'/list/party')
api.add_resource(River,'/list/river')
api.add_resource(FilteredMeasurement, '/filter/measurement')
api.add_resource(Measurement, '/measurement')


if __name__ == '__main__':
    mainApp.run(debug=True)
