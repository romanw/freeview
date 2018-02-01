#!/usr/bin/env python

import json

with open("freeview.json") as json_file:
    json_data = json.load(json_file)
    muxes = json_data["muxes"]
    genres = json_data["genres"]
    channels = json_data["channels"]
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print('<playlist version="1" xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/">')
    print('<title>DVB Playlist</title>')
    print('<trackList>')

    #item = next((item for item in muxes if item["id"] == 2), None)
    #if item:
    #    print(item["name"])

    for channel in channels:
        if 'ignore' in channel:
            continue

        print('<track>')
        print('\t<title>' + str(channel["lcn"]) + " " + channel["title"] + '</title>')
        mux = next((mux for mux in muxes if mux["id"] == channel["mux"]), None)
        print('\t<location>dvb-t://frequency=' + mux["freq"] + ':inversion=2:bandwidth=8</location>')
        print('\t<extension application="http://www.videolan.org/vlc/playlist/0">')
        print('\t\t<vlc:id>' + str(channel["lcn"]) + '</vlc:id>')
        if channel["prog"]:
            print('\t\t<vlc:option>program=' + str(channel["prog"]) + '</vlc:option>')
        print('\t</extension>')
        print('</track>')

    print('</trackList>')
    print('</playlist>')
