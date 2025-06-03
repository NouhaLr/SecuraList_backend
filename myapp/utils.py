def categorize_product(title, description):
    text = (title + " " + description).lower()

    if any(word in text for word in ["laptop", "ordinateur", "pc", "macbook", "asus", "hp", "dell"]):
        return "Informatique"
    elif any(word in text for word in ["smartphone", "iphone", "samsung", "android", "téléphone", "portable"]):
        return "Téléphonie"
    elif any(word in text for word in ["télé", "tv", "écran", "projecteur", "home cinéma"]):
        return "Électronique"
    elif any(word in text for word in ["chaise", "table", "canapé", "lit", "armoire", "meuble"]):
        return "Maison"
    elif any(word in text for word in ["vêtement", "t-shirt", "jean", "robe", "pull", "chaussure"]):
        return "Mode"
    elif any(word in text for word in ["livre", "roman", "bd", "manga", "lecture", "ouvrage"]):
        return "Livres"
    elif any(word in text for word in ["jouet", "lego", "barbie", "puzzle", "jeu enfant"]):
        return "Jouets"
    elif any(word in text for word in ["vélo", "trottinette", "skate", "roller", "hoverboard"]):
        return "Mobilité urbaine"
    elif any(word in text for word in ["voiture", "moto", "auto", "peugeot", "yamaha", "renault"]):
        return "Véhicules"
    elif any(word in text for word in ["montre", "bijou", "bracelet", "collier", "accessoire"]):
        return "Accessoires"
    elif any(word in text for word in ["console", "playstation", "ps5", "xbox", "switch", "jeu vidéo"]):
        return "Jeux vidéo"
    elif any(word in text for word in ["cuisine", "four", "frigo", "micro-ondes", "électroménager"]):
        return "Électroménager"
    elif any(word in text for word in ["sac", "valise", "sac à dos", "bagage"]):
        return "Bagagerie"
    elif any(word in text for word in ["instrument", "guitare", "piano", "musique", "violon"]):
        return "Musique"
    elif any(word in text for word in ["outil", "bricolage", "perceuse", "visseuse", "tournevis"]):
        return "Bricolage"
    else:
        return "Autre"
