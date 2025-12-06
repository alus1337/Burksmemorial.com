import json

def is_message_clean(message):
    # profanity check

    message = message.lower()
    try:
        words = open("words.json")
        bad_word_list = json.load(words)['profanity']
        words.close()
    except OSError as e:
        raise Exception("Fatal error: Failed to open words.json")
    except Exception as e:
        raise Exception(f"Fatal error: {e}")
    
    message_words = message.split()
    for word in message_words:
        if word in bad_word_list:
            return False
        
    return True

# anti spam mainly just checks if common funeral words are used
def is_message_suspicious(message):
    message.lower()
    try:
        words = open("words.json")
        common_word_list = json.load(words)["common"]
        words.close()
    except Exception as e:
        raise Exception(f"Fatal error: {e}")
    
    message_words = message.split()
    common_word_count = 0
    for word in message_words:
        if word in common_word_list:
            common_word_count += 1
    
    if common_word_count < 3:
        return True
    
    return False

def is_message_malicious(message):
    # if http, https, www, .com is found as a sequence in the list
    url_properties = ['http', 'https', '.com', 'www']
    if any(url_property in message for url_property in url_properties):
            message_words = message.split()

            for word in message_words:
                if any(url_property in word for url_property in url_properties):
                    if "burksmemorial.com" not in word:
                        return True