text="My name is Utkarsh";

new_text=text.upper(); #MY NAME IS UTKARSH
new_text=text.lower();#my name is utkarsh;
new_text=text.title();#My Name Is Utkarsh;
new_text=text.strip();#remove the spaces in front and back;
new_text=text.find("U");#11
new_text=text.replace("U","your") #My name is yourtkarsh
new_text="name" in text #True
new_text="YOUR" not in text #True
print(new_text)