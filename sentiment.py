#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

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
    #removes capitalisation and punctuation
    lyrics['clean_lyric'] = lyrics['lyric'].str.lower()
    lyrics['clean_lyric']= lyrics['clean_lyric'].str.replace('[^\w\s]','')

    #removes stopwords
    stopwords = ['the', 'in', 'a', 'an', 'and', 'but', 'or', 'this', 'that', 'to', 'is', 'am', 'was', 'were', 'be', 'being', 'been']
    lyrics['clean_lyric'] = lyrics['clean_lyric'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    
    return lyrics

def time_keywords(lyrics):
    #creates expression strings for time-related words
    day = ['day', 'morning', 'light', 'sun', 'dawn', 'noon', 'golden', 'bright']
    night = ['night','midnight', 'dawn', 'dusk', 'evening', 'late', 'dark', 'dim', '1am', '2am', '3am', '4am']
    time = ['today', 'tomorrow', 'yesterday']
    night = '|'.join(night)
    day = '|'.join(day)
    time = '|'.join(time)
    
    lyrics['night'] = lyrics['clean_lyric'].str.contains(night)
    lyrics['day'] = lyrics['clean_lyric'].str.contains(day)
    lyrics['time'] = lyrics['clean_lyric'].str.contains(time)
    
    return lyrics

def yearly_mentions(lyrics):
    #creates new dataframe that groups mentions by year
    yearly_mentions = lyrics.groupby('album_year').sum().reset_index()
    
    #reinstates album name
    year_name = pd.read_csv('data/album_year_name.csv')
    yearly_mentions.sort_values(by='album_year', ascending=True, inplace=True)
    year_name.sort_values(by='album_year', ascending=True, inplace=True)
    yearly_mentions['album_name'] = year_name['album_name']
    
    #plots mentions of night over years
    plt.plot(yearly_mentions['album_year'], yearly_mentions['night'])
    plt.xlabel('Year')
    plt.ylabel('Mentions')
    plt.show()
    
    return yearly_mentions

lyrics = load_data()

lyrics['album_year'] = lyrics.apply(lambda row: album_data(row), axis=1)

lyrics = clean_lyrics(lyrics)
lyrics = time_keywords(lyrics)
yearly_mentions = yearly_mentions(lyrics)
