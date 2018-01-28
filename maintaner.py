import json

#loads data from a json file
def loadJsonData():
    try:
        with open('data.json') as json_data:
            return json.load(json_data)
    except IOError:
        print('No Json File in the root directory, create a blank data.json file')
    except ValueError:
        print('No data in the file, add one using addNewData(name,referred_by) method')

##saves data back to the json file.
def saveJsonData(json_data):
    try:
        with open('data.json', 'w') as outfile:
            json.dump(json_data, outfile)
    except IOError:
        print('No Json File in the root directory, create a blank data.json file') 

##recursively increase the count of referrer by one for the parent
def increaseReferralCountByOne(name):
    ##load json data
    data = loadJsonData()
    my_item = next((item for item in data if item['name'] == name), None)
    if my_item is None:
        return True
    ##increase the count of the referrer
    data[data.index(my_item)]['referred_count'] = data[data.index(my_item)]['referred_count'] +1

    ##find the parent
    parent = data[data.index(my_item)]['referred_by']

    ##save the data
    saveJsonData(data)

    ## if parent is null then stop
    if parent is None:
        return True
    else:
        ##else recursively call the method to increase the parent count
        increaseReferralCountByOne(parent)

##add a new record
def addNewData(name,referred_by):
    data = loadJsonData()
    if data is None:
        data = []
    if referred_by:
        my_item = next((item for item in data if item['name'] == referred_by), None)
        ## check if the referred by name exist
        if my_item is None:
            return "referred_by name does not exist"
        else:
            data.append({'name':name,'referred_by':referred_by,'referred_count':0})
            ##save the data
            saveJsonData(data)
            increaseReferralCountByOne(referred_by)
            return "successfully saved"
    else:
        data.append({'name':name,'referred_by':None,'referred_count':0})
        ##save the data
        saveJsonData(data)
        return "successfully saved"

##show all data
def showAllData():
    try:
        with open('data.json') as json_data:
            print(json.load(json_data))
    except IOError:
        print('No Json File in the root directory, create a blank data.json file')
    except ValueError:
        print('No data in the file, add one using addNewData(name,referred_by) method')
    
        
        
    
    
    
