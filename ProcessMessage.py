import json

def is_message_clean(message):
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


process_it_sus = "This is a spam message that shouldnt get through the is message suspicious function preventing spam"
process_it_clean = "This is a message that should be able to pass the suspicious function since the words loving beloved and peace are in it"

print(is_message_suspicious(process_it_sus))
print(is_message_suspicious(process_it_clean))