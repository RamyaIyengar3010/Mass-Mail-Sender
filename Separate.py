#!/usr/bin/env python3
# -*- coding: utf-8 -*-
filler = '[Filler-text]'
def Separate(filename):
    '''Input -> filename with formatted name-email list. Name(first, middle, last)
	should have space btw them, there should be /t between name and email id.
    Output -> dict with name:emailid kay-value pairs
    '''
    fObj = open(filename, 'r')
    nameDict = {}
    for line in fObj:
    	l = line.split('\t')
    	try:
    		nameDict[l[-1]] = l.pop()
    	except IndexError:
    		pass
    		for key in nameDict:
    			l = nameDict[key]
    			l = l[:-1]
    			nameDict[key] = l

    			return nameDict

def formatMail(mailString, repString):
	'''Formats the body of the email, adds the name in place of filler text.
	Caution - filler text should not be repeated in the content of the mail, or it will get replaced as well
	'''
	mailString = mailString.replace(filler, repString)
	return mailString

#def sendMail(nameDict):

def main():
	mailString = '''
	Dear [Filler-text],

	Lorem ipsum dolor sit amet consectetur adipiscing elit suspendisse, neque facilisi eu ligula scelerisque purus metus convallis sagittis, nullam venenatis integer senectus auctor cursus pellentesque. Placerat scelerisque gravida augue iaculis mattis sem non, praesent laoreet nulla lacus odio sapien. In senectus nisi conubia auctor tortor consequat cras tristique, himenaeos massa rhoncus quam et duis vehicula aliquet, iaculis pharetra neque primis natoque facilisis praesent. At eu curabitur eleifend venenatis nostra nullam vulputate, ut fermentum tristique volutpat suscipit etiam vitae, taciti nec tempus egestas morbi penatibus.
	 Accumsan pharetra nibh congue non hac ac eu convallis, consequat leo fames laoreet nascetur facilisi erat,
	 mollis elementum semper facilisis malesuada ligula egestas. Inceptos penatibus lectus ridiculus eget ligula nisi placerat ullamcorper ad dui facilisi luctus feugiat,
	 dapibus vivamus non felis libero quis iaculis etiam dictum morbi varius eleifend.

	 Cheers!
	'''

		

if __name__ == '__main__':
	main()