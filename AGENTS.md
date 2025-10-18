This repo represents a pythonic learning quest. 

The target audience is: 
- my son Joshua, 15 years old, no formal computer science background
- he wants to learn python
- I (John, his dad) think it'd be great to learn the language combined with a structued adventure story that goes along with it - where the only way to progress through the adventure is to solve the python programming examples along the way.  each programming example will teach Joshua an important part of the language

The target languages are:
- python (for Joshua)
- C# (for John)

The goal is to learn all the topics in the outline.md files.  

# Storyline
The story follows a hero character through a quest.  The subject of the quest is different per person/language, the outline of which is in storyline.md.

# Exercise Template
Each learning quest follows this structure - this is the template you will use for the exercises:

1. **Purpose** – a short explanation of what the learner will achieve conceptually.
2. **Recipe List** – a bullet or table list of the language syntax/concepts and/or constructs being taught, each with an example of syntax or use, along with references to more learning material.  Should be in table format.  The examples should use typical args.
3. **Adventure Story / Problem** – a good explanation and narrative framing the exercise as part of a gamified adventure; then describe a concrete programming problem that uses the concepts from the recipe list.  The story solutions should target very short console apps with rather obvious solutions.
4. Include an example input/output showing the expected behavior.
5. Keep the tone encouraging, imaginative, and concise — like an adventure tutorial.

# Exercises and Outputs
Each person gets their own directory containing the storyline, exercise and solutions. 

The files within that are: 
  - storyline.md - a theme and story to follow
  - outline.md - a comprehensive list of topics that should be learned (sections + bullet points)
  - exercises/<exercise-number>-<slug>.md - the exercises to solve (as markdown)
  - solutions/<exercise-number>-<slug> - the code answers to those exercises - with the appropriate language extension

# Generating Exercises
Use the outline.md and generate funny quests using the exercise template - the goal is to create bite sized quests, that focus on **only one new idea at a time** (occasionally two tightly related ones if necessary). Think in micro-quests: variables *or* strings, not entire chapters.  Default to several short exercises instead of a single large one so the learner gets more practice reps.  You will need to create multiple exercises to finish each bullet point in the outline.  Expect the whole outline to require 50+ adventures.  Smaller and well focused quests are more valuable than longer ones.  

Whenever asked to regenerate quests, refresh all exercise/solution pairs across every learner directory (Joshua/python and John/C#)

When drafting an exercise:
- Keep the required code solution to something that reasonably fits in ~15 lines of Python/C# (excluding blank lines).
- Call out exactly which single concept is new; everything else should rely on earlier knowledge.
- If a bullet point in the outline lists multiple sub-ideas, split them into separate exercises rather than combining them.
- err on the side of creating **additional** exercises whenever a learner might benefit from another focused repetition of the same concept with a fresh story twist.

# Quest Guideline
- No quest should repeat any other quest.
- Quests should rely on prior quest knowledge - earlier quests should not assume lots of knowledge. 
