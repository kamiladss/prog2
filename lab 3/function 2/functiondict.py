movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1
def checkfpf(name, movies):
    for movie in movies:
        if movie["name"] == name and movie["imdb"] > 5.5:  
            return True
    return False

#print(checkfpf("Exam", movies))

#2----------------------------------------------------------------------
def allcheckfpf(movies):
    abovefpf=[]
    for movie in movies:
         if movie["imdb"] > 5.5:
            abovefpf.append(movie)# for only names we cn add ["name"]
    return abovefpf
        
#print(allcheckfpf(movies))

#3---------------------------------------------------------------------
def category(category, movies):
    allmoviesincat=[]
    for movie in movies:
         if movie["category"] == category:
            allmoviesincat.append(movie)
    return allmoviesincat

#print(category("Thriller", movies))
    
#4---------------------------------------------------------------------
def avIMDB(movies):
    counterscore = 0
    mals =0
    for movie in movies:
          counterscore += movie["imdb"] 
          mals+=1        
    return (float(counterscore/mals))

#print(avIMDB(movies))

#5---------------------------------------------------------------------
def avcategory(category, movies):
    counterscore = 0
    mals =0     
    for movie in movies:
         if movie["category"] == category:
            counterscore += movie["imdb"] 
            mals+=1 
    return (float(counterscore/mals))

print(avcategory("Thriller", movies))