import os, time, json, sys
import openai
from gpt3 import gpt3
import colors as colors


#### set some vars, later put in a cfg file
#prompt = "This robot rides strong yet alone thru the carbonized fields and synth-diamond rails of Unifed Mongolia to"
FILENAMESEEDCOUNT = int(32)
LOGENDING = ".log"
FILENAMEENDING = ".md"
THISTIMESTAMP = "-" + time.strftime("%H%M%S")
DIRROOT = "./"
DIRDELIM = "/"
LINEBREAKER = "\n"

##### call gpt-3 to g3pt (get it, g3t it?)
def g3pt_idea():
	#ask for input to get started
	prompt = input(colors.color.cyan + "give us a prompt:" + colors.color.white)
	
	filename_base = create_filename(prompt)
	
	#make a dir to keep writing and .log files in
	# TODO - make the dir
	thisdir = DIRROOT + filename_base
	dir_action(thisdir)
	
	#make the file
	filename_story = DIRROOT + thisdir + DIRDELIM + filename_base + THISTIMESTAMP + FILENAMEENDING
	filename_log = DIRROOT + thisdir + DIRDELIM + filename_base + LOGENDING
	header_prompt = "## " + prompt
	file_action(filename_story, header_prompt, "w", newpgh=True)
	
		
	while True:
		print(prompt + LINEBREAKER)
		prompt += " " + input(colors.color.cyan + 'g3pt more: ' + colors.color.white)
		bold_prompt = "**" + prompt + "** "
		file_action(filename_story, bold_prompt, "a")
		# TODO look at the NEW INPUT eleement of gpt3 def
	
		# get response from OPEN AI GPT-3
		response, answer, prompt = gpt3(prompt,temperature=0.9,top_p=1,frequency_penalty=1,presence_penalty=1,start_text='',restart_text='',stop_seq='')
		json_response = json.dumps(response, indent = 4)
		print(colors.color.cyan + 'gpt3 adds: ' + colors.color.magenta + answer + colors.color.white)

		##### write a file, yo
		file_action(filename_story, answer, "a", newpgh=True)
		file_action(filename_log, json_response, "a") # TODO -- next the JSONs, or move to different format



def create_filename(seed_filename):
	# do some lowercase, space, .,,. replace
	# TODO -- get a lib that handles this
	filename_base = seed_filename.casefold().replace(" ","_").replace(",","").replace(",","").replace('"','').replace("'","")

	# take the first FILENAMESEEDCOUNT chars
	filename_base = filename_base[ 0 : FILENAMESEEDCOUNT ]
	
	return filename_base



##### write a file, yo
def file_action(thisfilename, content, mode, newpgh = False):
	# now make a file
	# TODO: wrap in some pre/error checking and return a real result
	# print("content: " + content + LINEBREAKER)
	
	with open(thisfilename, mode) as f:
		f.write(content)
		if newpgh == True:
			f.write(LINEBREAKER + LINEBREAKER + " ---(next)---" + LINEBREAKER)
		f.close()
	
	# give a little feedback
	if mode == "w":
		print(colors.color.cyan + "new file: "  + colors.color.white + thisfilename)

	if mode == "a":
		print(colors.color.cyan + "added to file: "  + colors.color.white + thisfilename)	


##### make a directory
def dir_action(path_to_thisdir):
  
  #make if needed
  if not os.path.exists(path_to_thisdir):
    os.makedirs(path_to_thisdir)
    print("find or make: " + path_to_thisdir)
    status = True
  else:
    status = False
  
  return status




#### kick things off
if __name__ == '__main__':
    g3pt_idea()
    
    
    
    
    
