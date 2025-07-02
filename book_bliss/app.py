from flask import Flask, render_template, request
from urllib.parse import unquote
import random

app = Flask(__name__)

# Your existing book_data and get_book_summary functions...

# Static Book Data
book_data = {
    "motivational": [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "rating": "4.8",
            "desc": "Tiny changes, remarkable results.",
            "img": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg"
        },
        {
            "title": "Can't Hurt Me",
            "author": "David Goggins",
            "rating": "4.7",
            "desc": "Master your mind and defy the odds.",
            "img": "https://m.media-amazon.com/images/I/81o1oy0y9-L.jpg"
        },
        {
            "title": "Make Your Bed",
            "author": "William H. McRaven",
            "rating": "4.6",
            "desc": "Small things that can change your life.",
            "img": "https://m.media-amazon.com/images/I/81r+LN7DhsL.jpg"
        },
        {
            "title": "The 5 AM Club",
            "author": "Robin Sharma",
            "rating": "4.4",
            "desc": "Own your mornings, elevate your life.",
            "img": "https://m.media-amazon.com/images/I/71zytzrg6lL.jpg"
        }
    ],
    "calm": [
        {
            "title": "Ikigai",
            "author": "Héctor García",
            "rating": "4.3",
            "desc": "The Japanese secret to a long and happy life.",
            "img": "https://m.media-amazon.com/images/I/81QpkIctqPL.jpg"
        },
        {
            "title": "The Power of Now",
            "author": "Eckhart Tolle",
            "rating": "4.5",
            "desc": "Spiritual guide to live in the present.",
            "img": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"
        },
        {
            "title": "Stillness is the Key",
            "author": "Ryan Holiday",
            "rating": "4.4",
            "desc": "Unlocking the power of quietude and clarity.",
            "img": "https://m.media-amazon.com/images/I/71nT3b5U8xL.jpg"
        }
    ],
    "curious": [
        {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "rating": "4.6",
            "desc": "A brief history of humankind.",
            "img": "https://m.media-amazon.com/images/I/713jIoMO3UL.jpg"
        },
        {
            "title": "The Psychology of Money",
            "author": "Morgan Housel",
            "rating": "4.5",
            "desc": "Timeless lessons on wealth and happiness.",
            "img": "https://m.media-amazon.com/images/I/71g2ednj0JL.jpg"
        },
        {
            "title": "Homo Deus",
            "author": "Yuval Noah Harari",
            "rating": "4.4",
            "desc": "A glimpse into the future of humanity.",
            "img": "https://m.media-amazon.com/images/I/81RdvW9ZR-L.jpg"
        }
    ],
    "inspirational": [
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "rating": "4.7",
            "desc": "Follow your dreams and listen to your heart.",
            "img": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"
        },
        {
            "title": "Think Like a Monk",
            "author": "Jay Shetty",
            "rating": "4.6",
            "desc": "Train your mind for peace and purpose.",
            "img": "https://m.media-amazon.com/images/I/81s6DUyQCZL.jpg"
        },
        {
            "title": "Man’s Search for Meaning",
            "author": "Viktor E. Frankl",
            "rating": "4.8",
            "desc": "Finding hope and purpose in life's darkest hours.",
            "img": "https://m.media-amazon.com/images/I/71e0PUh3XwL.jpg"
        }
    ]
}


def get_book_summary(title, duration):
    summaries = {
        'Atomic Habits': {
            "quote": "You do not rise to the level of your goals. You fall to the level of your systems.",
            "desc": "A practical guide to building good habits and breaking bad ones."
        },
        "Can't Hurt Me": {
            "quote": "You are in danger of living a life so comfortable and soft, that you will die without ever realizing your true potential.",
            "desc": "Goggins shows how mental toughness transforms lives."
        },
        "Make Your Bed": {
            "quote": "If you want to change the world, start off by making your bed.",
            "desc": "Admiral McRaven outlines 10 life lessons learned from Navy SEAL training."
        },
        'Sapiens': {
            "quote": "Culture tends to argue that it forbids only that which is unnatural.",
            "desc": "Covers the cognitive, agricultural, and scientific revolutions."
        },
        'The Psychology of Money': {
            "quote": "Success with money has little to do with how smart you are and a lot to do with how you behave.",
            "desc": "Explains that financial success is more about behavior than knowledge."
        },
        'Ikigai': {
            "quote": "Only staying active will make you want to live a hundred years.",
            "desc": "Introduces the concept of finding joy through purpose and balance."
        },
        'The Power of Now': {
            "quote": "Realize deeply that the present moment is all you ever have.",
            "desc": "Teaches how living in the present can lead to deep inner peace."
        },
        'The Alchemist': {
            "quote": "When you want something, all the universe conspires in helping you to achieve it.",
            "desc": "Santiago’s mystical journey in search of a treasure — and himself."
        },
        'Think Like a Monk': {
            "quote": "Detach yourself to reconnect with yourself.",
            "desc": "Shares lessons on overcoming negativity and finding purpose."
        },
        'Stillness is the Key': {
            "quote": "Stillness is the key to self-mastery.",
            "desc": "Taps into the ancient idea that stillness is essential to self-mastery."
        },
        'The 5 AM Club': {
            "quote": "Own your morning. Elevate your life.",
            "desc": "Early rising secrets to boost productivity, performance, and well-being."
        },
        'Homo Deus': {
            "quote": "The most interesting place in the universe is inside our own minds.",
            "desc": "Explores possible directions for the future of humanity."
        },
        'Man’s Search for Meaning': {
            "quote": "When we are no longer able to change a situation, we are challenged to change ourselves.",
            "desc": "A Holocaust survivor’s powerful story of spiritual survival and purpose."
        }
    }

    data = summaries.get(title, {
        "quote": "Quote not available.",
        "desc": "Summary not available."
    })

    quote = data["quote"]
    desc = data["desc"]

    return quote, desc


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mood = request.form['mood']
        books = book_data.get(mood, [])
        random.shuffle(books)
        return render_template('results.html', results=books[:3])
    return render_template('index.html')

@app.route('/summary', methods=['GET'])
def summary():
    title = request.args.get('title')
    duration = request.args.get('duration', '5')

    summary_text = get_book_summary(title, duration)

    # Get book details for rendering
    book = next(
        (b for mood_books in book_data.values() for b in mood_books if b['title'] == title),
        None
    )

    if not book:
        return "Book not found", 404

    book['summary'] = summary_text

    return render_template('summary.html', book=book, duration=duration)
