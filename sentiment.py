#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def load_data():
    # load album data from csv file
    lyrics = pd.read_csv("data/taylor_swift_lyrics_2006-2022_all.csv")
    return lyrics

def album_data(row):  
    # map the name of the album to release year
    if row['album_name'] == 'Taylor Swift':
        return '2006'
    elif row['album_name'] == 'Fearless (Taylor’s Version)':
        return '2008'
    elif row['album_name'] == 'Speak Now (Deluxe)':
        return '2010'
    elif row['album_name'] == 'Red (Deluxe Edition)':
        return '2012'
    elif row['album_name'] == '1989 (Deluxe)':
        return '2014'
    elif row['album_name'] == 'reputation':
        return '2017'
    elif row['album_name'] == 'Lover':
        return '2019'
    elif row['album_name'] == 'evermore (deluxe version)':
        return '2020'
    elif row['album_name'] == 'folklore (deluxe version)':
        return '2021'
    else:
        return 'No Date'
    
def clean_lyrics(lyrics):
    lyrics['clean_lyric'] = lyrics['lyric'].str.lower()
    lyrics['clean_lyric']= lyrics['clean_lyric'].str.replace('[^\w\s]','')

    stopwords = ['the', 'in', 'a', 'an', 'and', 'but', 'or', 'this', 'that', 'to', 'is', 'am', 'was', 'were', 'be', 'being', 'been']
    
    lyrics['clean_lyric'] = lyrics['clean_lyric'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    
    return lyrics

lyrics = load_data()

lyrics['album_year'] = lyrics.apply(lambda row: album_data(row), axis=1)

lyrics = clean_lyrics(lyrics)

