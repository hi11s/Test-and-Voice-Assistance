import pyttsx3
import wikipedia


def is_music_related(summary):
    keywords = ['album', 'song', 'musician', 'band', 'singer', 'music', 'genre']
    return any(keyword in summary.lower() for keyword in keywords)


voice = pyttsx3.init()
In = input("Searching for music-related content on Wikipedia: ")

try:
    # Adding a context word to guide the search
    search_query = In + " music"
    result = wikipedia.summary(search_query, sentences=3)

    if is_music_related(result):
        print(result)
        voice.say(result)
    else:
        print("The search result doesn't seem to be related to music.")
        voice.say("The search result doesn't seem to be related to music.")
except wikipedia.exceptions.DisambiguationError as e:
    print("The search term is too broad, please be more specific.")
    voice.say("The search term is too broad, please be more specific.")
except wikipedia.exceptions.PageError:
    print("No Wikipedia page found for the search term.")
    voice.say("No Wikipedia page found for the search term.")
except Exception as e:
    print(f"An error occurred: {e}")
    voice.say("An error occurred.")
finally:
    voice.runAndWait()
