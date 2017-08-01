# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
#True,False是python关键字，不用“”
print formatter %(True,True,True,False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
    "i had this thing.",
	"that you type up right.",
	"but it did't sing.",
	"so i said goodnight."
	)