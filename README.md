# gpt3-robo-writingpartner
Initial Commit  -- instructions to come

**Intention** 
On the way to understanding how to get code creation out of GPT-3, it seems worth while to play with it in various capacities. 
And this capacity is the idea generation element, tweaking the `temperature`, `top-p`, `response length`, `frequency penalty` and of course the engine.

(much more to come!)


**Requires** 

 1. Python installed
 
    -- This script uses Python 3, and so i didnt test Python 2.7 (which ships with macOS)
    
 2. An OpenAI API key
 
    -- If you don't have one, you can request one at https://beta.openai.com
    
 3. Know how to add and export environment variables to your bash_profile, so you do not put your APIKEY in source control
 
    -- https://www.schrodinger.com/kb/1842
    
    -- quick example of what i added to my bash_profile
    
    `# openai vars`
    
     `export OPENAI_API_KEY="<put your api key here>"`


**ToDos** 

# append to `<name>.log` so one json object with many entries
# in gpt3.py use configured or passed param values
# create interactive or run-time passed args for temp, top-p, freq, etc
