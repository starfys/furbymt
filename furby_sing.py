import os
import glob
import id3reader
import random

def ScanMusic(songTitle = '', performer = '', album = '', directory = './music'):

    # Use OS to access input directory
    os.chdir(directory)

    # Read all files from designated music directory
    mp3Files = []
    for localFile in glob.glob("*.mp3"):
        mp3Data = id3reader.Reader(localFile)
        mp3Files.append({ 'file' : localFile, 'title' : str(mp3Data.getValue('title')), 'artist' : str(mp3Data.getValue('performer')), 'album' : str(mp3Data.getValue('album'))})

    if(len(mp3Files) == 0):
        return []

    # If no parameters were specified, choose a random song
    if(songTitle == '' and performer == '' and album == ''):
        index = random.randint(0, len(mp3Files)-1)
        return [mp3Files[index]]

    # Filter all songs that don't match designated title
    if(songTitle != ''):
        for entry in mp3Files:
            if(entry['title'].lower() != songTitle.lower()):
                mp3Files.remove(entry)

    # Filter all songs that don't match designated artist
    if(performer != ''):
        for entry in mp3Files:
            if(entry['artist'].lower() != performer.lower()):
                mp3Files.remove(entry)

    # Filter all songs that don't match designated album
    if(album != ''):
        for entry in mp3Files:
            if(entry['album'].lower() != album.lower()):
                mp3Files.remove(entry)

    # Remove all repeated files
    for entry in mp3Files:
        for entry2 in mp3Files:
            if(entry2 != entry and entry['title'] == entry2['title'] and entry['artist'] == entry2['artist'] and entry['album'] == entry2['album']):
                mp3Files.remove(entry2)

    return mp3Files
