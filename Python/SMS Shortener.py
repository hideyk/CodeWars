def shortener(message):
    to_trim = len(message) - 160
    message_list = message.split()
    capitalized_list = [i[0].upper() + i[1:] for i in message_list[-to_trim:]]
    final_message = " ".join(message_list[:-to_trim]) + "".join(capitalized_list)
    return final_message


sms = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it."
trimmed_sms = shortener(sms)
print(trimmed_sms)