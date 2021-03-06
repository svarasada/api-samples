#!/usr/bin/env python3
# This sample demonstrates how to use the siem endpoint in the
# REST API.

# This sample is interactive.
# THIS SAMPLE WILL MAKE CHANGES TO THE OFFENSE IT IS RUN AGAINST
# The scenario demonstrates the following actions:
#  - How to get a list of closing reasons
#  - How to create a new closing reason

# To view a list of the endpoints with the parameters they accept, you can view
# the REST API interactive help page on your deployment at
# https://<hostname>/api_doc.  You can also retrieve a list of available
# endpoints with the REST API itself at the /api/help/endpoints endpoint.

import json
import os
import sys

import importlib
sys.path.append(os.path.realpath('../modules'))
client_module = importlib.import_module('RestApiClient')
SampleUtilities = importlib.import_module('SampleUtilities')


def main():
    # First we have to create our client
    client = client_module.RestApiClient(version='6.0')

    # This example gives a demonstration of how to create a new closing reason
    # for your offenses.

    # First, check what closing reasons are already available to avoid
    # creating duplicates. Send in the GET request.
    SampleUtilities.pretty_print_request(
        client, 'siem/offense_closing_reasons', 'GET')
    response = client.call_api('siem/offense_closing_reasons', 'GET')
    # and output the response
    SampleUtilities.pretty_print_response(response)

    if (response.code != 200):
        print('Call Failed')
        sys.exit(1)

    # Double check that the user wants to create a new closing reason
    while True:
        confirmation = input('Are you sure you want to create a new ' +
                             'closing reason? (YES/no) ')

        if (confirmation == 'YES'):
            break
        elif (confirmation == 'no'):
            print('Not creating a new closing reason')
            exit(0)
        else:
            print(confirmation + 'is not a valid answer.')

    # Have the user input the text.
    text = input(
        'Please enter the text you want to put in the closing reason.\n')

    # Put through the request to add a closing reason with the text the user
    # entered as the reason
    params = {'reason': text}
    response = client.call_api('siem/offense_closing_reasons', 'POST',
                               params=params, print_request=True)

    SampleUtilities.pretty_print_response(response)

    if (response.code != 201):
        print('Call Failed')
        sys.exit(1)

    print('Closing reason added')

if __name__ == "__main__":
    main()
