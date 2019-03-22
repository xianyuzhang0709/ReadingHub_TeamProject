import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ReadingHub_TeamProject.settings')

import django

django.setup()
from readinghub.models import Category, Book, Event, UserProfile, User
from datetime import datetime
from django.contrib.auth.models import User
import media



def populate():
    # Created a list of dictionaries containing books placed in different category.

    fiction_books = [
        {"title": "The Hunger Games",
         "author": "Suzanne Collins",
         "url": "http://www.amazon.com/gp/product/0439023483/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0439023483&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Could you survive on your own, in the wild, with everyone out to make sure you don't live to see the morning? In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV. Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she is forced to represent her district in the Games. But Katniss has been close to dead before - and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.",
         "likes": 12,
         "image": "book01.jpg"},
        {"title": "Harry Potter and the Sorcerer's Stone",
         "author": "J.k.Rowling",
         "url": "http://www.amazon.com/gp/product/0439554934/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0439554934&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he's a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.",
         "likes": 39,
         "image": "book02.jpg"},
        {"title": "The Great Gatsby",
         "author": "Scott Fitzgerald",
         "url": "http://www.amazon.com/s?k=The+Great+Gatsby&i=stripbooks&adid=082VK13VJJCZTQYGWWCZ&campaign=211041&creative=374001&tag=x_gr_w_bb-20&ref=x_gr_w_bb",
         "description": "THE GREAT GATSBY, F. Scott Fitzgerald's third book, stands as the supreme achievement of his career. This exemplary novel of the Jazz Age has been acclaimed by generations of readers. The story is of the fabulously wealthy Jay Gatsby and his new love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted gin was the national drink and sex the national obsession, it is an exquisitely crafted tale of America in the 1920s.",
         "likes": 32,
         "image": "book03.jpg"},
    ]

    nonFiction_books = [
        {"title": "Sapiens: A brief History of Humankind",
         "author": "Yuval noah Harari",
         "url": "http://www.amazon.com/s?k=Sapiens&i=stripbooks&adid=082VK13VJJCZTQYGWWCZ&campaign=211041&creative=374001&tag=x_gr_w_bb-20&ref=x_gr_w_bb",
         "description": "In Sapiens, Dr Yuval Noah Harari spans the whole of human history, from the very first humans to walk the earth to the radical – and sometimes devastating – breakthroughs of the Cognitive, Agricultural and Scientific Revolutions. Drawing on insights from biology, anthropology, paleontology and economics, he explores how the currents of history have shaped our human societies, the animals and plants around us, and even our personalities. Have we become happier as history has unfolded? Can we ever free our behaviour from the heritage of our ancestors? And what, if anything, can we do to influence the course of the centuries to come?",
         "likes": 47,
         "image": "book04.jpg"},
        {"title": "We Should All Be Feminists",
         "author": "Chimamanda Ngozi Adichie",
         "url": "http://www.amazon.com/gp/product/B00L0F01NK/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=B00L0F01NK&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "What does “feminism” mean today? That is the question at the heart of We Should All Be Feminists, a personal, eloquently-argued essay—adapted from her much-viewed TEDx talk of the same name—by Chimamanda Ngozi Adichie, the award-winning author of Americanah and Half of a Yellow Sun.",
         "likes": 11,
         "image": "book05.jpg"},
        {"title": "I Am Malala",
         "author": "Malala Yousafzai, Christina Lamb",
         "url": "http://www.amazon.com/gp/product/0316322407/ref=x_gr_e_nl_newreleases_sout_bb?ie=UTF8&tag=x_gr_e_nl_newreleases_sout_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0316322407&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "When the Taliban took control of the Swat Valley in Pakistan, one girl spoke out. Malala Yousafzai refused to be silenced and fought for her right to an education.",
         "likes": 13,
         "image": "book06.jpg"},
    ]

    poetry_books = [
        {"title": "The Complete Poems of Emily Dickson",
         "author": "Emily Dickson",
         "url": "http://www.amazon.com/gp/product/0316184136/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0316184136&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Only eleven of Emily Dickinson’s poems were published prior to her death in 1886; the startling originality of her work doomed it to obscurity in her lifetime. Early posthumously published collections-some of them featuring liberally “edited” versions of the poems-did not fully and accurately represent Dickinson’s bold experiments in prosody, her tragic vision, and the range of her intellectual and emotional explorations. Not until the 1955 publication of The Complete Poems of Emily Dickinson, a three-volume critical edition compiled by Thomas H. Johnson, were readers able for the first time to assess, understand, and appreciate the whole of Dickinson’s extraordinary poetic genius.",
         "likes": 21,
         "image": "book07.jpg"},
        {"title": "Twenty Love Poems and a Song of Despair",
         "author": "Pablo Neruda",
         "url": "http://www.amazon.com/Twenty-Poems-Despair-Spanish-English/dp/0143039962/ref=sr_1_1?keywords=Twenty+Love+Poems+and+a+Song+of+Despair&qid=1553134564&s=gateway&sr=8-1",
         "description": "When it appeared in 1924, this work launched into the international spotlight a young and unknown poet whose writings would ignite a generation. W. S. Merwin's incomparable translation faces the original Spanish text. Now in a black-spine Classics edition with an introduction by Cristina Garcia, this book stands as an essential collection that continues to inspire lovers and poets around the world. The most popular work by Chile's Nobel Prize-winning poet, and the subject of Pablo Larraín's acclaimed feature film Neruda starring Gael García Bernal.",
         "likes": 15,
         "image": "book08.jpg"},
    ]

    children_books = [
        {"title": "Ella Enchanted",
         "author": "Gail Carson Levine",
         "url": "http://www.goodreads.com/book/show/24337.Ella_Enchanted",
         "description": "At birth, Ella is inadvertently cursed by an imprudent young fairy named Lucinda, who bestows on her the gift of obedience. Anything anyone tells her to do, Ella must obey. Another girl might have been cowed by this affliction, but not feisty Ella: Instead of making me docile, Lucinda's curse made a rebel of me. Or perhaps I was that way naturally. When her beloved mother dies, leaving her in the care of a mostly absent and avaricious father, and later, a loathsome stepmother and two treacherous stepsisters, Ellas life and well-being seem to be in grave peril. But her intelligence and saucy nature keep her in good stead as she sets out on a quest for freedom and self-discovery as she tries to track down Lucinda to undo the curse, fending off ogres, befriending elves, and falling in love with a prince along the way. Yes, there is a pumpkin coach, a glass slipper, and a happily ever after, but this is the most remarkable, delightful, and profound version of Cinderella you will ever read.",
         "likes": 55,
         "image": "book09.jpg"},
        {"title": "The Lion, the Witch and the Wardrobe",
         "author": "C.S Lewis",
         "url": "http://www.amazon.com/gp/product/0060764899/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0060764899&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "NARNIA...the land beyond the wardrobe, the secret country known only to Peter, Susan, Edmund, and Lucy...the place where the adventure begins. Lucy is the first to find the secret of the wardrobe in the professor's mysterious old house. At first, no one believes her when she tells of her adventures in the land of Narnia. But soon Edmund and then Peter and Susan discover the Magic and meet Aslan, the Great Lion, for themselves. In the blink of an eye, their lives are changed forever",
         "likes": 72,
         "image": "book10.jpg"},
        {"title": "Book of a Thousand Days",
         "author": "Shannon Hale",
         "url": "http://www.amazon.co.uk/gp/product/1599900513/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb_uk-21&linkCode=as2&camp=1634&creative=6738",
         "description": "When Dashti, a maid, and Lady Saren, her mistress, are shut in a tower for seven years because of Saren's refusal to marry a man she despises, the two prepare for a very long and dark imprisonment.",
         "likes": 22,
         "image": "book11.jpg"},
    ]

    cats = {"Fiction": {"books": fiction_books, "image": "c1.jpeg"},
            "Non Fiction": {"books": nonFiction_books, "image": "c2.jpeg"},
            "Poetry": {"books": poetry_books, "image": "c3.jpeg"},
            "Children Books": {"books": children_books, "image": "c4.jpeg"}}


    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["image"])
        for b in cat_data["books"]:
            add_book(c, b["title"], b["author"], b["url"], b["description"], b["likes"], b["image"])

    # Print out all the categories we have added
    for c in Category.objects.all():
        for b in Book.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(b)))


    events = [
                {'title': "Let's enjoy the life! Coming!",
                  'venue': "603 Great Western Rd, Glasgow G12 8HX",
                  "date": "2019/01/15",
                  "time": "18:30",
                  'book': "Book of a Thousand Days",
                  'participators': "44",
                  'description': "A person's temperament can see a lot of things, everyone in life, selfishness, kindness, intelligence, self-confidence in their body... can be reflected in many aspects. The book brings people the wisdom of not having the predecessors, there are many, one by one needs their own experience.",
                  'image': "e1.jpg"
                  },
                
                {'title': "Dreams in the book, come, guys!",
                  'venue': "Millfield, Livingston EH54 7AR",
                  "date": "2019/02/06",
                  "time": "9:30",
                  'book': "The Complete Poems of Emily Dickson",
                  'participators': "157",
                  'description': "The poet is a poem that has been smashed into lines by his own life. In today's era when this poem is obscured, he adheres to his inner ideals and feelings. The distant people think that the poet can't lie, he always shows himself the most realistically.",
                  'image': "e2.jpg"
                  },
                
                {'title': "Come to join us! we need you !",
                  'venue': "the killingworth centre, Killingworth, Newcastle upon Tyne NE12 6HA",
                  "date": "2019/03/07",
                  "time": "19:30",
                  'book': "The Lion, the Witch and the Wardrobe",
                  'participators': "66",
                  'description': "You always have to believe that children are more energetic than us and have more wisdom than us. This kind of thinking is the encouragement to the child, but it is also an identity, it will enhance the child's spiritual belonging.",
                  'image': "e3.png"
                  },
              ]


    for e in events:
        add_event(e)
        print("Adding event...")

    users = [{
                'username': 'XianyuZhang',
                'email': 'xianyuzhang@qq.com',
                'password': 'zxyzxyzxy12',
                'picture': 'u1.jpeg',
                'description': "I'm outgoing, come to make friend with me!",
              },
             {
                'username': 'HaotianWu',
                'email': 'HaotianWu@qq.com',
                'password': 'zxyzxyzxy3242',
                'picture': 'u2.jpeg',
                'description': "I'm a handsome boy, come, let us talk about life!",
              },
             {
                'username': 'ChengXu',
                'email': 'XuCheng@qq.com',
                'password': 'zxyzxyzxy32423',
                'picture': 'u4.jpeg',
                'description': "we come from different places, but we should be friends with each other!",
              },

             {
                'username': 'AsuquoEffiongGlory',
                'email': 'AsuquoEffiongGlory@outlook.com',
                'password': 'zxyzxyzxy32423',
                'picture': 'u3.jpeg',
                'description': "I love books and hope I can talk with you guys here!",
             },
     ]

    for u in users:
        add_user_profile(u)
        print("Adding User...")

def add_book(cat, title, author, url, description, likes, image):
    b = Book.objects.get_or_create(category=cat, title=title)[0]
    b.author = author
    b.url = url
    b.description = description
    b.likes = likes
    b.image = image
    b.save()
    return b


def add_cat(name, image):
    c = Category.objects.get_or_create(name=name, image=image)[0]
    c.save()
    return c

def add_event(event):
    event_date = datetime.strptime(event['date'] + " " + event['time'], '%Y/%m/%d %H:%M')
    e = Event.objects.get_or_create(title=event["title"], venue=["venue"], date=event_date,
                                    time=event['time'], participators=event['participators'],
                                    description=event['description'], image=event['image'])[0]
    e.save()
    return e

def add_user_profile(user):
    u = User.objects.create_user(username=user["username"], email=user["email"], password=user["password"])
    u.save()
    user_profile = UserProfile.objects.get_or_create(user=u, description=user["description"], picture=user["picture"])[0]
    user_profile.save()
    return user_profile



# Execution starts here
if __name__ == '__main__':
    print("Starting ReadingHub population script...")
    populate()
