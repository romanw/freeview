#!/usr/bin/env python

import json

with open("freeview.json") as json_file:
    json_data = json.load(json_file)
    dtg = json_data["dtg"]
    muxes = json_data["muxes"]
    genres = json_data["genres"]
    channels = json_data["channels"]

    #item = next((item for item in muxes if item["id"] == 2), None)
    #if item:
    #    print(item["name"])

    for channel in channels:
        if 'ignore' in channel:
            continue

        if not 'vid' in channel:
            continue

        if not 'aid' in channel:
            continue

        props = dtg[0]["properties"]
        #print(props)
        mux = next((mux for mux in muxes if mux["id"] == channel["mux"]), None)
        if channel["mux"] == 3 or channel["mux"] == 7 or channel["mux"] == 8:
            props = dtg[1]["properties"]

        #print('\t<title>' + str(channel["lcn"]) + " " + channel["title"] + '</title>')
        #print('\t<location>dvb-t://frequency=' + mux["freq"] + ':inversion=2:bandwidth=8</location>')
        #print('\t\t<vlc:id>' + str(channel["lcn"]) + '</vlc:id>')
        #if channel["prog"]:
        #    print('\t\t<vlc:option>program=' + str(channel["prog"]) + '</vlc:option>')

        print(channel["title"] + ":" +
            mux["freq"] + ":" +
            props + ":" +
            str(channel["vid"]) + ":" +
            str(channel["aid"]) + ":" +
            str(channel["prog"]))

