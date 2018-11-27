import json
import requests


def change_publisher(uuid_dataset, uuid_new_publisher, header_comment, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Change publisher for a given dataset and add comments about it
    '''
    response = requests.get(api+uuid_dataset)
    headers = {'Content-Type': 'application/json'}
    if response.ok:
        response = response.json()
        my_comment = {'content': (header_comment + 'Changed publisher from ' +
                                  response["publishingOrganizationKey"] + ' to ' +
                                  uuid_new_publisher + ' after request from publishers')}
        # Add comment
        add_comments = requests.post(api + uuid_dataset + "/comment",
                                     data=json.dumps(my_comment),
                                     auth=(login, password),
                                     headers=headers)
        if add_comments.ok:
            print("comment added")
            response["publishingOrganizationKey"] = uuid_new_publisher
            update_dataset = requests.put(api + uuid_dataset,
                                          data=json.dumps(response),
                                          auth=(login, password),
                                          headers=headers)
            if update_dataset.ok:
                print("dataset updated")
            else:
                print("dataset NOT updated")
        else:
            print("Comment could NOT be added")


def add_endpoint(uuid_dataset, new_URL, endpoint_type, header_comment, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Add new endpoint for a given dataset and add comments about it
    '''
    response = requests.get(api+uuid_dataset+"/endpoint")
    headers = {'Content-Type': 'application/json'}
    if response.ok:
        my_comment = {
            'content': (header_comment + 'Replaced endpoint after request from hosting installation')
        }
        # Add comment
        add_comments = requests.post(api + uuid_dataset + "/comment",
                                     data=json.dumps(my_comment),
                                     auth=(login, password),
                                     headers=headers)
        if add_comments.ok:
            print("comment added")
            my_endpoint = {
                "url": new_URL,
                "type": endpoint_type
            }
            update_dataset = requests.post(api + uuid_dataset + "/endpoint",
                                           data=json.dumps(my_endpoint),
                                           auth=(login, password),
                                           headers=headers)
            for endpoints in response.json():
                delete_endpoint = requests.delete(api + uuid_dataset + "/endpoint/"+str(endpoints["key"]),
                                                  auth=(login, password),
                                                  headers=headers)
            if update_dataset.ok and delete_endpoint.ok:
                print("dataset updated")
            else:
                print("dataset NOT updated")
        else:
            print("Comment could NOT be added")


def delete_dataset(uuid_dataset, header_comment, requesting_organization, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Delete a dataset and add a comment
    '''
    my_comment = {
        'content': (header_comment + 'Deleted after request from ' + requesting_organization)
    }
    headers = {'Content-Type': 'application/json'}
    # Add comment
    add_comments = requests.post(api + uuid_dataset + "/comment",
                                 data=json.dumps(my_comment),
                                 auth=(login, password),
                                 headers=headers)
    if add_comments.ok:
        print("comment added")
        deletedDS = requests.delete(api + uuid_dataset,
                                    auth=(login, password),
                                    headers=headers)
        if deletedDS.ok:
            print("dataset deleted")
        else:
            print("dataset NOT deleted")
    else:
        print("Comment could NOT be added")

        
def add_machineTag(uuid_dataset, namespace, name, value, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Add new machineTag for a given dataset
    '''
    headers = {'Content-Type': 'application/json'}
    machineTag = {
        "namespace": namespace,
        "name": name,
        "value": value
    }
    update_dataset = requests.post(api + uuid_dataset + "/machineTag",
                                   data=json.dumps(machineTag),
                                   auth=(login, password),
                                   headers=headers)

    if update_dataset.ok:
        print("machineTag added")
    else:
        print("machineTag NOT added")



def delete_machineTag_from_namespace(uuid_dataset, namespace, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Delete machineTag for a given dataset from a given namespace
    '''
    response = requests.get(api+uuid_dataset+"/machineTag")
    headers = {'Content-Type': 'application/json'}
    if response.ok:
        response = response.json()
        for tag in response:
            if tag["namespace"] == namespace:
                update_dataset = requests.delete(api + uuid_dataset + "/machineTag/"+str(tag["key"]),
                                                 auth=(login, password),
                                                 headers=headers)

                if update_dataset.ok:
                    print("machineTag deleted")
                else:
                    print("machineTag NOT deleted")
    else:
        print("Dataset NOT found")


def delete_comment(uuid_dataset, comment_content, login, password, api="http://api.gbif-uat.org/v1/dataset/"):
    '''
    Delete a specific comment for a given dataset
    '''
    response = requests.get(api+uuid_dataset+"/comment")
    headers = {'Content-Type': 'application/json'}
    if response.ok:
        response = response.json()
        for tag in response:
            if tag["content"] == comment_content:
                update_dataset = requests.delete(api + uuid_dataset + "/comment/"+str(tag["key"]),
                                                 auth=(login, password),
                                                 headers=headers)

                if update_dataset.ok:
                    print("comment deleted")
                else:
                    print("comment NOT deleted")
    else:
        print("Dataset NOT found")
