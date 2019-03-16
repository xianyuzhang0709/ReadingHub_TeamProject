import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ReadingHub_TeamProject.settings')

import django

django.setup()
from readinghub.models import Category, Book


def populate():
    # Created a list of dictionaries containing books placed in different category.

    fiction_books = [
        {"title": "The Hunger Games - 1",
         "author": "Suzanne Collins",
         "url": "https://www.amazon.com/gp/product/0439023483/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0439023483&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Could you survive on your own, in the wild, with everyone out to make sure you don't live to see the morning? In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV. Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she is forced to represent her district in the Games. But Katniss has been close to dead before - and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.",
         "likes": 20},
        {"title": "Harry Potter and the Sorcerer's Stone - 1",
         "author": "J.k.Rowling",
         "url": "https://www.amazon.com/gp/product/0439554934/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0439554934&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he's a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.",
         "likes": 20},
        {"title": "The Great Gatsby (Paperback)",
         "author": "Scott Fitzgerald",
         "url": "https://www.amazon.com/s?k=The+Great+Gatsby&i=stripbooks&adid=082VK13VJJCZTQYGWWCZ&campaign=211041&creative=374001&tag=x_gr_w_bb-20&ref=x_gr_w_bb",
         "description": "THE GREAT GATSBY, F. Scott Fitzgerald's third book, stands as the supreme achievement of his career. This exemplary novel of the Jazz Age has been acclaimed by generations of readers. The story is of the fabulously wealthy Jay Gatsby and his new love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted gin was the national drink and sex the national obsession, it is an exquisitely crafted tale of America in the 1920s.",
         "likes": 20},
    ]

    nonFiction_books = [
        {"title": "Sapiens: A brief History of Humankind",
         "author": "Yuval noah Harari",
         "url": "https://www.amazon.com/s?k=Sapiens&i=stripbooks&adid=082VK13VJJCZTQYGWWCZ&campaign=211041&creative=374001&tag=x_gr_w_bb-20&ref=x_gr_w_bb",
         "description": "In Sapiens, Dr Yuval Noah Harari spans the whole of human history, from the very first humans to walk the earth to the radical – and sometimes devastating – breakthroughs of the Cognitive, Agricultural and Scientific Revolutions. Drawing on insights from biology, anthropology, paleontology and economics, he explores how the currents of history have shaped our human societies, the animals and plants around us, and even our personalities. Have we become happier as history has unfolded? Can we ever free our behaviour from the heritage of our ancestors? And what, if anything, can we do to influence the course of the centuries to come?",
         "likes": 20},
        {"title": "We Should All Be Feminists",
         "author": "Chimamanda Ngozi Adichie",
         "url": "https://www.amazon.com/gp/product/B00L0F01NK/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=B00L0F01NK&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "What does “feminism” mean today? That is the question at the heart of We Should All Be Feminists, a personal, eloquently-argued essay—adapted from her much-viewed TEDx talk of the same name—by Chimamanda Ngozi Adichie, the award-winning author of Americanah and Half of a Yellow Sun.",
         "likes": 20},
        {"title": "I Am Malala: The Story of the Girl Who Stood Up for Education and Was Shot by the Taliban",
         "author": "Malala Yousafzai, Christina Lamb",
         "url": "https://www.amazon.com/gp/product/0316322407/ref=x_gr_e_nl_newreleases_sout_bb?ie=UTF8&tag=x_gr_e_nl_newreleases_sout_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0316322407&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "When the Taliban took control of the Swat Valley in Pakistan, one girl spoke out. Malala Yousafzai refused to be silenced and fought for her right to an education.",
         "likes": 20},
    ]

    poetry_books = [
        {"title": "The Complete Poems of Emily Dickson",
         "author": "Emily Dickson",
         "url": "https://www.amazon.com/gp/product/0316184136/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0316184136&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "Only eleven of Emily Dickinson’s poems were published prior to her death in 1886; the startling originality of her work doomed it to obscurity in her lifetime. Early posthumously published collections-some of them featuring liberally “edited” versions of the poems-did not fully and accurately represent Dickinson’s bold experiments in prosody, her tragic vision, and the range of her intellectual and emotional explorations. Not until the 1955 publication of The Complete Poems of Emily Dickinson, a three-volume critical edition compiled by Thomas H. Johnson, were readers able for the first time to assess, understand, and appreciate the whole of Dickinson’s extraordinary poetic genius.",
         "likes": 20},
        {"title": "Twenty Love Poems and a Song of Despair",
         "author": "Pablo Neruda",
         "url": "",
         "description": "When it appeared in 1924, this work launched into the international spotlight a young and unknown poet whose writings would ignite a generation. W. S. Merwin's incomparable translation faces the original Spanish text. Now in a black-spine Classics edition with an introduction by Cristina Garcia, this book stands as an essential collection that continues to inspire lovers and poets around the world. The most popular work by Chile's Nobel Prize-winning poet, and the subject of Pablo Larraín's acclaimed feature film Neruda starring Gael García Bernal.",
         "likes": 20},
    ]

    children_books = [
        {"title": "Ella Enchanted - 1",
         "author": "Gail Carson Levine",
         "url": "https://www.goodreads.com/book/show/24337.Ella_Enchanted",
         "description": "At birth, Ella is inadvertently cursed by an imprudent young fairy named Lucinda, who bestows on her the gift of obedience. Anything anyone tells her to do, Ella must obey. Another girl might have been cowed by this affliction, but not feisty Ella: Instead of making me docile, Lucinda's curse made a rebel of me. Or perhaps I was that way naturally. When her beloved mother dies, leaving her in the care of a mostly absent and avaricious father, and later, a loathsome stepmother and two treacherous stepsisters, Ellas life and well-being seem to be in grave peril. But her intelligence and saucy nature keep her in good stead as she sets out on a quest for freedom and self-discovery as she tries to track down Lucinda to undo the curse, fending off ogres, befriending elves, and falling in love with a prince along the way. Yes, there is a pumpkin coach, a glass slipper, and a happily ever after, but this is the most remarkable, delightful, and profound version of Cinderella you will ever read.",
         "likes": 20},
        {"title": "The Lion, the Witch and the Wardrobe (Chronicles of Narnia) - 1",
         "author": "C.S Lewis",
         "url": "https://www.amazon.com/gp/product/0060764899/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0060764899&SubscriptionId=1MGPYB6YW3HWK55XCGG2",
         "description": "NARNIA...the land beyond the wardrobe, the secret country known only to Peter, Susan, Edmund, and Lucy...the place where the adventure begins. Lucy is the first to find the secret of the wardrobe in the professor's mysterious old house. At first, no one believes her when she tells of her adventures in the land of Narnia. But soon Edmund and then Peter and Susan discover the Magic and meet Aslan, the Great Lion, for themselves. In the blink of an eye, their lives are changed forever",
         "likes": 20},
        {"title": "Book of a Thousand Days",
         "author": "Shannon Hale",
         "url": "When Dashti, a maid, and Lady Saren, her mistress, are shut in a tower for seven years because of Saren's refusal to marry a man she despises, the two prepare for a very long and dark imprisonment.",
         "description": "https://www.amazon.co.uk/gp/product/1599900513/ref=x_gr_w_bb?ie=UTF8&tag=x_gr_w_bb_uk-21&linkCode=as2&camp=1634&creative=6738",
         "likes": 20},
    ]

    cats = {"Fiction": {"books": fiction_books},
            "Non Fiction": {"books": nonFiction_books},
            "Poetry": {"books": poetry_books},
            "Children Books": {"books": children_books}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for b in cat_data["books"]:
            add_book(c, b["title"], b["author"], b["url"], b["description"], b["likes"])

    # Print out all the categories we have added
    for c in Category.objects.all():
        for b in Book.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(b)))


def add_book(cat, title, author, url, description, likes=0):
    b = Book.objects.get_or_create(category=cat, title=title)[0]
    b.author = author
    b.url = url
    b.description = description
    b.likes = likes
    b.save()
    return b


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


# Execution starts here
if __name__ == '__main__':
    print("Starting ReadingHub population script...")
    populate()