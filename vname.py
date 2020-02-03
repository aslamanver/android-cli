#!/bin/bash

import json
import os
import glob


def main():

    try:

        with open('output.json', 'r') as f:
            json_dict = json.load(f)

        for data in json_dict:
            fname = data['apkData']['versionName']

        cname = input("APP Name: ")

        name = (cname + '-' if cname != '' else '') + 'v' + fname + '.apk'

        cfile = glob.glob('*.apk')[0]

        os.rename(cfile, name)

        print(cfile + " -> " + name)

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
