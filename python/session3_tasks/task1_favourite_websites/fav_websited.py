import favlinks

if favlinks.choosenlink in favlinks.urls:
    favlinks.firefox(favlinks.choosenlink)
elif favlinks.choosenlink not in favlinks.urls:
    print("choosen website unavilabe")
