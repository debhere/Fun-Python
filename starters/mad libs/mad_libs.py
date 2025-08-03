def get_input(input_type: str) -> str:
    return input(f"Enter a {input_type}: ")


noun1 = get_input("noun")
adj = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""

Once upon a time, there was a {adj} {noun1} who used {verb1} all day long. But {noun1} never 
agrees so. One fine day, {noun2} caught {noun1} red handed in the act.

{noun2}: What are you doing?
{noun1}: Just {verb1}ing, what's the big deal?
{noun2}: Well, it's not normal to {verb1} in the middle of the day.
{noun1}: Yeah! maybe you're right. I should take some break.
{noun2}: Let's go for a {verb2} later today?
{noun1}: Ahm! I'm not too sure about today, can we plan something for tomorrow instead?

That 'tomorrow' never came and {noun1} and {noun2} couldn't have their {verb2}ing session till date.
The end.
"""

print(story)
