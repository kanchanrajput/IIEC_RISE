import pyttsx3
import os

pyttsx3.speak("welcome to my tools ")

while True :
    
    print("  CHAT WITH ME WITH YOUR REQUIREMENTS  : ", end ="")

    p = input().lower()
    
    
    if (("not " in p ) or ("don't" in p ) or ("dont" in p) ):
        pass
    
    #for browser
    elif  (("run" in p ) or ("execute" in p) or ("launch" in p) or ("open" in p ) )and ( ("chrome" in p) or ("browser" in p) or ("google" in p)): 
        os.system("chrome")
    
     # for notepad
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))  and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
    
     # for window media player
    elif (("run" in p) or ("execute" in p) or ("open" in p )or ("launch" in p)) and ( ("player" in p) or ("mediaplayer" in p) ):
        os.system("wmplayer")
    
    # for jupyter notebook
    elif (("run" in p)or ("launch" in p)or ("execute" in p) or ("open" in p )) and (("jupyter" in p) or ("notbook" in p)):
        os.system("jupyter-notebook")
    
    #for virtual machine
    elif (("run" in p)or ("launch" in p) or ("open" in p)or ("execute" in p)) and ("virtual machine" in p):

        pyttsx3.speak("WHICH MACHINE DO YOU WANNA OPEN  : ")
        machine_name  = input(" WHICH MACHINE DO YOU WANNA OPEN  : ")
        os.system("VBoxManage startvm "+ machine_name)
    
    #for command prompt
    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("command prompt" in p):
        os.system("start cmd.exe")
    
    #for calclator
    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("calculator" in p) or ("calci" in p)) :
        os.system("calc")
    
    #for control panel
    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("control panel" in p):
        os.system("control")
    
    #for internet exploler
    elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("ie" in p )or ("internet exp") in p )):
        os.system("iexplore")
    
    #for mspaint
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("mspaint" in p ) or ("mspaint" in p )):
        os.system("mspaint")
    
    #for printer
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p)) and (("printer" in p )):
        os.system("control printers")
    
    #for device management
    elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p))  and (("device manage" in p ))) :
        os.system("devmgmt.msc")
    
    #for disk management
    elif (("run" in p) or ("start" in p) or ("open"  in p )or ("execute" in p) or ("launch" in p)) and (("disk manage" in p ) or ("disk mngmnt" in p )):
        os.system("diskmgmt.msc")
    
    #remote desktop connection
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("remote desk" in p )):
        os.system("mstsc")
    
    #remote  twitter
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("twitter" in p )):
        os.system("start twitter:")
    
    #remote  facebook
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("facebook" in p )):
        os.system("start fb:")
    
    #setting
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("settings" in p )):
        os.system("start ms-settings:")
    
    #calender
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("calender" in p )):
        os.system("start outlookcal:")
    
    ##camera
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("camera" in p ) or ("webcam" in p)):
        os.system("start microsoft.windows.camera:")
        
    #Alarms & Clock
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("alarm" in p ) or ("clock" in p)):
        os.system("start ms-clock:")
        
    #available networks
    elif ("show" in p) and (("available networks" in p )):
        os.system("start ms-availablenetworks:")
    
    #cortona
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("cortana" in p )):
        os.system("start ms-cortana:")
        
    #mail
    elif (("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("mail" in p )):
        os.system("start outlookmail:")
        
    #maps
    elif (("show" in p) or ("start" in p) or ("open" in p )  or ("launch" in p)) and (("maps" in p )):
        os.system("start bingmaps:")    
    
    #ms store
    elif (("run" in p) or ("start" in p) or ("open" in p )  or ("launch" in p)) and (("microsoft windows store" in p)):
        os.system("start ms-windows-store:")
    
    #onenote
    elif (("run" in p) or ("start" in p) or ("open" in p )  or ("launch" in p)) and (("onenote" in p)):
        os.system("start onenote:")
        
        
    #exit
    elif ("exit" in p) or ("quit" in p):
        break
        
    else:
        print("do not support")
