#! python3
# Script for getting web adresses from text copied to clipboard.

import re, pyperclip


webRegex= re.compile(r'''(
(http(s)?)           #http/https      
([:/]){3}            #://
([w]{3})?            #www (optional)
([a-zA-Z0-9-]+)      #web main name            
(\.\w{2,3})          #.com .pl .org etc.
([([a-zA-Z0-9./]*)?  #rest of adres (optional)  
)''', re.VERBOSE)

# find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in webRegex.findall(text):
    website = groups[0]
    matches.append(website)

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Matches Found:')
    print('\n' .join(matches))
else:
    print('Nothing Found')