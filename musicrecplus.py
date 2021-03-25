'''
Author: Kai Qi Chee
Created on November 13, 2019
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - musicrecplus
'''
import sys
from cs115 import map, reduce, filter
NAME=''
ARTISTS=[]
DATABASE={}


def main():
    global NAME
    global ARTISTS
    global DATABASE
    try:
        f=open('musicrecplus.txt','r')
        for line in f:
            user,artist=line.split(':')
            artist=artist.split(',')
            artists = []
            for x in artist:
                artists.append(x.strip())
            DATABASE[user] = artists
        if NAME in DATABASE:
            ARTISTS=DATABASE[NAME]
            menu()
        else:
            enter(False) 

    except IOError as error:
        f=open('musicrecplus.txt','w')
        f.close()
        enter(False)

def menu():
    '''Prints the menu and takes in user input to call a
    specific functions'''
    global NAME
    global ARTISTS
    global DATABASE
    choice=input("Enter a letter to choose an option:" "\n"
                "e - Enter preferences" "\n"
                "r - Get recommendations" "\n"
                "p - Show most popular artists" "\n"
                "h - How popular is the most popular" "\n"
                "m - Which user has the most likes" "\n"
                "q - Save and quit" "\n")
    if choice=="e": 
        enter(False)
    elif choice=="r": 
        getRecommendations(NAME, ARTISTS, DATABASE)
    elif choice=="p":  
        popular()     
    elif choice=="h":  
        howPopular()  
    elif choice=="m": 
        most_likes()
    elif choice=="q": 
        saveUserPreferences()
    else:
        print("Please enter valid input")
        menu()


def enter(entering): 
    '''asks the user for artists preferences'''
    global NAME
    global ARTISTS
    global DATABASE
    if entering==False:
        ARTISTS.clear()
    artist=input("Enter an artist that you like (Enter to finish): " "\n")
    if artist != '':
        ARTISTS.append(artist)
        enter(True)
    else:
        ARTISTS.sort()
        DATABASE[NAME]=ARTISTS
        menu()
            
def most_likes():
    '''Finds the user with the most preferences'''
    global NAME
    global ARTISTS
    global DATABASE
    result=[]
    most=0
    for x in DATABASE:
        a=len(DATABASE[x]) 
        if x[-1] != '$':
            if a>most:
                result.clear()
                most=a
                result.append(x)
            elif a==most:
                result.append(x)
    if result==[]:
        print("No users...look in doc")
    else:
        result.sort()
        for i in result:
            print(i)
    menu()

def get_artists():
    '''this puts all the artists that are liked in a singles list, and
    returns a dictionary with each artist once with the number of times
    they are mentioned'''
    global NAME
    global ARTISTS
    global DATABASE
    result={}
    all_artists=[]
    for x in DATABASE:
        if x[-1] != '$':
            for artists in DATABASE[x]:
                all_artists.append(artists) 
    if all_artists==[]:
        print("Sorry, no artists found")
        menu()
    else:
        for i in all_artists:
            if i in result: 
                result[i]+=1
            else:
                result[i]=1
        return result
    
def popList():
    '''This returns the most popular artist(s) and how many times
    they are mentioned'''
    global NAME
    global ARTISTS
    global DATABASE
    artists=[]
    dictionary=get_artists()
    most=0
    for key in dictionary:
        if dictionary[key] > most:
            artists.clear()
            most=dictionary[key]
            artists.append([key, dictionary[key]])
        elif dictionary[key]==most:
            artists.append([key,dictionary[key]])
    artists.sort()
    return artists

def popular():
    '''Returns the most popular artist(s)'''
    lst=popList()
    for x in lst:
        print(x[0])
    menu()

def howPopular():
    '''Returns the number of times the most popular
    artist(s) appears'''
    lst=popList()
    print(lst[0][1])
    menu()
    
def getRecommendations(currUser, prefs, userMap):
    ''' Returns a list of recommended artists for
    currUser based on the users in userMap and the
    user's preferences in prefs'''
    bestUser = findBestUser()
    recommendations = []
    recs=[]
    if bestUser != []:
        for x in bestUser:
            recommendations.append(drop(prefs, userMap[x]))
        if recommendations!=[]:
            for i in recommendations:
                for j in i:
                    print (j)
    else:
        print("No recommendations available at this time")
    menu()

    
def findBestUser():
    '''Returns the user(s) whose artist preferences are most
    similar to the current user without being exactly the same'''
    global NAME
    global ARTISTS
    global DATABASE
    names=DATABASE
    names=filter(lambda x: x[-1] != '$', names)
    if len(DATABASE)==1:
        print ("No Recommendations available at this time")
        menu()
    else:
        greatest_count=0
        greatest_user = []
        for username in names:
            if DATABASE[username] != DATABASE[NAME]:
                count= numMatches(DATABASE[username],DATABASE[NAME])
                if count>greatest_count:
                    greatest_user.clear()
                    greatest_count=count
                    greatest_user.append(username)
                elif count==greatest_count:
                    greatest_count=count
                    greatest_user.append(username)
        return (greatest_user)
    
def drop(list1, list2):
    '''Return a new list that contains only the elements in
        list2 that were NOT in list1'''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    while j<len(list2):
        list3.append(list2[j])
        j+=1
    return list3

def numMatches( list1, list2 ):
    '''Returns the number of elements that match between list1
    and list2'''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def saveUserPreferences():
    ''' Writes all of the user preferences to the file'''
    global DATABASE
    save=[]
    file = open("musicrecplus.txt", "w")
    for user in DATABASE:
        toSave = str(user)+":"+",".join(DATABASE[user])+"\n"
        save.append(toSave)
    save.sort()
    for i in save:
        file.write(i)
    file.close()
    sys.exit()
    
if __name__=='__main__':
    NAME=input("Enter your name (put a $ symbol after your "
        "name if you wish your preferences to "
        "remain private):" "\n").strip()
    main()


