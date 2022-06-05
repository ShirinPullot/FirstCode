def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    
    for character in string:
        if character not in valid:
            return True
         
    return False
    

def is_valid(email):
    if email.count("@")!=1:
        return False
    else:
        newemail= email.split("@")
        prefix, domain= newemail
        if has_invalid_characters(domain) or has_invalid_characters(prefix):
                return False

                        
        if len(prefix)==0:
                return False
        if domain.count(".")!=1:
                return False
        domain_name, extension= domain.split(".")
        if len(domain_name)==0:
                return False
        if len(extension)==0:
                return False
        
        return True

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]
for mail in emails:
    
    if is_valid(mail):
        print(mail+ ' is valid')
    else:
        print(mail+ " is invalid")
