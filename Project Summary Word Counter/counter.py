"""
Program counts the number of words in a project summary


Assumption(s):
    Formatting is correct i.e. no space before comma/full-stop, etc.

    
Excludes:
    Figure labelling
    Words encased in a bracket
    Bibliography and Annexes
    Section headers

    
User is to:
    Make sure the bibliography is named "Bibliography"
    Make sure the annexes are named "Annex X"
"""


filename = "ps" + ".txt"


word_count = 0
SECTION_HEADERS = [
"""\
Real-World Problem or Opportunity Identified in Project & Rationale
Identification of real-world problem or opportunity
Analysis of problem or opportunity
Support choice of problem or opportunity using research findings\
""",
"""\
Aim(s) of Project\
""",
"""\
Target Group of Project & Rationale\
""",
"""\
Proposed Ideas & Rationale
Brief description of proposed ideas
Analysis of how proposed ideas address the project aim(s) and the needs of the target group
Justify proposed ideas using research findings and evaluate proposed ideas for their strengths and limitations\
"""
]
words = []

with open(filename, "r") as f:
    bracket_open = False
    lines = f.readlines()

    #  Removal of Section Headers
    for section_header in SECTION_HEADERS:
        if section_header in "".join(lines):
            word_count -= len(section_header.split())

    #  Word counting
    for line in lines:
        space = True

        #  Count end of line word
        if "word" in locals() and word and word.lower() != "figure":
            if word.lower() in {"bibliography", "annex", "appendix"}:
                break
            word_count += 1
            words.append(word)
            print(repr(word))
        word = ""

        for letter in line:
            #  Exclude words in bracket
            if bracket_open:
                if letter == ")":
                    bracket_open = False
                continue
            
            if letter in {".", ",", ":"}:
                continue

            #  Exclusion of Figure lines and Bibliography
            if word.lower() in {"bibliography", "annex", "figure", "appendix"}:
                break

            if letter == "(":
                bracket_open = True

            elif letter.isspace():
                space = True

            elif space and not letter.isspace() and word:
                if not bracket_open:
                    print(repr(word))
                    word_count += 1
                    words.append(word)

                word = letter
                space = False
            else:
                space = False
                word += letter


print("Word count:", word_count)

