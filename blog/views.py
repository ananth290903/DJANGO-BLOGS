from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts=[
        {
        "slug":"hike-in-the-mountains",
       "images":"mountain.jpeg",
       "author":"Maxmillian",
       "date":date(2024,7,7),
       "title":"Mountain Hiking",
       "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },

        {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
    #thesee are the dummy posts and info related to them
]


def get_date(post):
    return post.get('date')
    #return post['date']



def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{"posts":latest_posts})
    #"posts" is the variable that stores the latest_posts"
    #posts can be directly accessed from the templates inside blog project

def posts(request):
    return render(request,"blog/all-posts.html")

def post_detail(request,slug):
    return render(request,"blog/post-detail.html")




'''
def starting_page(request):
    return render(request,"blog/index.html")

'''



# posts as lists can be stored in posts=[]
#Every post can be a dictionary with a couple of keys
'''
     Eg : slug key as an identifier.
     This identifier can be used for search b 



     posts=[
     {
       "slug":"hike-in-the-mountains",
       "images":"mountain.jpeg",
       "date":date(2024,07,07),

     
     
     }
     
     
     ]
'''