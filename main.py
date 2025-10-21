####################################################################
# Undertale Launcher 2025
# 
# GitHub: https://github.com/chocolife13/UndertaleLauncher
# WhatsApp: https://whatsapp.com/channel/0029Vb9tYfi7IUYTeusCq70D
# 
#                      ---Task---
# 
# TODO:
#  - Steam version
#  - all lang
#   
# 
# DOING: 
#  -Battle button
#
# 
# 
# DONE :
#  
#  
#
#
#
# ----------------------------------------------
############ Importation des librairies nécessaires ##################

from playsound import playsound
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import ttk
import tkinter as tk
import configparser
import webbrowser
import subprocess
import threading
import traceback
import requests
import platform
import zipfile
import shutil
import json
import sys
import os


#------------------------------------------------
os_platform = platform.system()
print("Creation du prossesus root")

root = tk.Tk()

def error(exc_type, exc_value, exc_traceback):
    message = ''.join(traceback.format_exception_only(exc_type, exc_value)).strip()
    yes = messagebox.askyesno("An error has ocurred", f"{message}\n\n Do you want to feedback ?")
    if yes:
        url = "monday left me broken"
        trace = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)).strip()
        data = {"content":f"```{trace}```"}
        try:
            requests.post(url, json=data)
        except:
            print("no conection")
root.report_callback_exception = error
sys.excepthook = error



root.withdraw()
############### Variables d'initialisation ##########################
version = "v1.2"
username = os.getlogin()
var_launcher_path = os.getcwd()
Launcher_save_dir = os.path.join(var_launcher_path, "saves")
Launcher_version_dir = os.path.join(var_launcher_path, "versions")


if os_platform == "Windows":
    var_winletter = os.environ.get("SystemDrive")
    save_appdata_local = fr"{var_winletter}\Users\{username}\AppData\Local\UNDERTALE"

elif os_platform == "Linux":
    var_winletter = fr"/home/{username}/.wine/drive_c/"
    save_appdata_local = fr"{var_winletter}/Users/{username}/AppData/Local/UNDERTALE"

print("checking update..")
try:
    update_request = requests.get("https://api.github.com/repos/chocolife13/UndertaleLauncher/tags")
    wifi = 1
except:
    print("have u tested internet yet ?")
    wifi = 0

if wifi == 1:
    if update_request.status_code == 200:
        print("sever here")   
        new_version = update_request.json()[0]["name"]
        print("newest update is :" + new_version)
        if new_version == version:
            print("updated yet")
        else:

            print("not updated")
            
            wantupdate = messagebox.askyesno("UndertaleLauncher is not up to date",f"Do you want to update ? \n{version} => {new_version}")
            if wantupdate:
                webbrowser.open("https://github.com/chocolife13/UndertaleLauncher/releases/latest")
            version = version + " Not updated"
    else:   
        print("server down")

    
with open("rooms.json", "r") as file:
    list_number_to_rooms = json.load(file)
    file.close()
picture_run_0 = ImageTk.PhotoImage(Image.open("run_button_0.png").resize((60,25)))

picture_save_0 = ImageTk.PhotoImage(Image.open("save_button_0.png").resize((60,25)))

picture_new_0 = ImageTk.PhotoImage(Image.open("new_button_0.png").resize((60,25)))

picture_delete_0 = ImageTk.PhotoImage(Image.open("delete_button_0.png").resize((60,25)))

picture_erase_0 = ImageTk.PhotoImage(Image.open("erase_button_0.png").resize((60,25)))

picture_rename_0 = ImageTk.PhotoImage(Image.open("rename_button_0.png").resize((60,25)))

picture_kill_0 = ImageTk.PhotoImage(Image.open("kill_button_0.png").resize((60,25)))

picture_download_0 = ImageTk.PhotoImage(Image.open("download_button_0.png").resize((75,25)))


######################## Prossesus "root" ############################




# Obtenir la resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#Créer la fenetre de Chargement
win_loading = tk.Toplevel(root)
win_loading.title("load")
win_loading.geometry(f"400x200+{(screen_width // 2) - 200}+{(screen_height // 2) - 100}")
win_loading.overrideredirect(True)
win_loading.configure(bg="black")

#Mis en place de l'image de chargement -Aaron was here 🤠
picture_loading = tk.PhotoImage(file = os.path.join(var_launcher_path, "loading.png")).subsample(4, 4)
image_loading = tk.Label(win_loading, image= picture_loading)
image_loading.pack()


###########################    Verification   ####################################
def verification():
    print("verification...")
    
    if os.path.isdir(Launcher_version_dir):
        print("Dosssier version found")
    else:
        print("dossier version not found")
        os.makedirs(Launcher_version_dir)
        verification()

    if os.path.isdir(Launcher_save_dir):
        print("Dosssier save found")
    else:
        print("dossier save not found")
        os.makedirs(Launcher_save_dir)
        verification()
        
    if os.path.isdir(save_appdata_local):
        print("local UNDERTALE found")
    else:
        print("Local not found never played undertale yet?")
        os.makedirs(save_appdata_local)
        verification()

if os.path.isfile(os.path.join(save_appdata_local, "file0")):
    last_time_save = os.path.getmtime(os.path.join(save_appdata_local, "file0"))
else:
    last_time_save = "none"


verification()
print("end of verification")


########################### Main windows ########################################
win_menu = "Fenetre principale"
print("fenetre menu")
def start_win_menu():
    global win_menu
    global root
    global list_winmenu_versions_installed
    global combobox_winmenu_versionslist
    global button_win_newversion_continue
    global main_update
    global combobox_winmenu_saveslist
    global combobox_winmenu_versionslist
    
    win_loading.destroy()
   
    
    win_menu = tk.Toplevel(root)
    win_menu.protocol("WM_DELETE_WINDOW", quit_app)
    #win_menu.iconbitmap("icon.ico")
    win_menu.title("Undertale Launcher")
    win_menu.geometry(f"800x500+{(screen_width // 2) - 400}+{(screen_height // 2) - 250}")
    win_menu.resizable(False, False)
    win_menu.configure(background="#000000") 

    #title
    label_winmenu_title = tk.Label(  
        win_menu, 
        text="Undertale Launcher", 
        font=("System",50), 
        background="#000000",
        foreground="#FFFFFF"
    )     
    label_winmenu_title.pack()

    #Frame Versions
    frame_winmenu_version = tk.Frame(win_menu) 
    frame_winmenu_version.place(
        relx=0.25,
        rely=0.5,
        relwidth=0.4,
        relheight=0.65,
        anchor="center"
        )
    frame_winmenu_version.configure(background="#FFFFFF")



    frame_winmenu_version2 = tk.Frame(frame_winmenu_version)
    frame_winmenu_version2.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.96,
        relheight=0.96,
        anchor="center"
        )
    frame_winmenu_version2.configure(background="#000000")


    


    #widjet version
    label_winmenu_title_save = tk.Label(
        frame_winmenu_version,
        text="Versions",
        fg="white",
        bg="black",
        font=("System", 18)
        )
    label_winmenu_title_save.pack(pady=10)


    combobox_winmenu_versionslist = ttk.Combobox(frame_winmenu_version)
    combobox_winmenu_versionslist.pack(pady=10)
    combobox_winmenu_versionslist.set("Version")

    
    
    


    button_winmenu_suprrversion = tk.Button(
        frame_winmenu_version,
        bg="black",
        image= picture_delete_0,
        command= delete_version,
        )

    

    button_winmenu_suprrversion.place(
        relx=0.15,
        rely=0.9,
        anchor="center"
        )
    


    button_winmenu_renameversion = tk.Button(frame_winmenu_version, bg="black",image = picture_rename_0, command=win_rename_version)
    button_winmenu_renameversion.place(relx=0.38, rely=0.9, anchor="center")
    
    button_winmenu_newversion = tk.Button(frame_winmenu_version, bg="black", image= picture_new_0, command=new_version)
    button_winmenu_newversion.place(relx=0.62, rely=0.9, anchor="center")
    
    




    #frame save
    frame_winmenu_save = tk.Frame(win_menu)  
    frame_winmenu_save.place(
        relx=0.75,
        rely=0.5,
        relwidth=0.4,
        relheight=0.65,
        anchor="center"
        )
    frame_winmenu_save.configure(background="#FFFFFF")
    

    frame_winmenu_save2 = tk.Frame(frame_winmenu_save)  
    frame_winmenu_save2.place(
        relx=0.5,
        rely=0.5,
        relwidth=0.96,
        relheight=0.96,
        anchor="center"
        )

    frame_winmenu_save2.configure(background="#000000")

    #widjets save
    

    label_winmenu_title_save = tk.Label(
        frame_winmenu_save,
        text="Saves",
        fg="white",
        bg="black",
        font=("System", 18)
        )
    label_winmenu_title_save.pack(pady=10)

    
    
    combobox_winmenu_saveslist = ttk.Combobox(frame_winmenu_save)
    combobox_winmenu_saveslist.pack(pady=10)

    if not os.path.isfile(os.path.join(save_appdata_local, "Undertale_Launcher.ini")):
        combobox_winmenu_saveslist.set("Save")
    else:
        config_save = configparser.ConfigParser()
        config_save.read(os.path.join(save_appdata_local, "Undertale_Launcher.ini"))
        combobox_winmenu_saveslist.set(config_save.get("Info", "name"))
        
        
        
    
    
    button_winmenu_suprrsave = tk.Button(
        frame_winmenu_save,
        bg="black",
        image= picture_erase_0,
        command= delete_save,
        )

    

    button_winmenu_suprrsave.place(
        relx=0.15,
        rely=0.9,
        anchor="center"
        )
    


    button_winmenu_renamesave = tk.Button(frame_winmenu_save, bg="black",image = picture_rename_0, command=win_rename_save)
    button_winmenu_renamesave.place(relx=0.38, rely=0.9, anchor="center")
    
    button_winmenu_newversion = tk.Button(frame_winmenu_save, bg="black",image= picture_new_0, command=new_save)
    button_winmenu_newversion.place(relx=0.62, rely=0.9, anchor="center")
    
    button_winmenu_save = tk.Button(frame_winmenu_save, image=picture_save_0, bg="black", command=save)
    button_winmenu_save.place(relx=0.85, rely=0.9, anchor="center")


    label_winmenu_save_save = tk.Label(frame_winmenu_save, text="", bg="black",fg="#ffffff", font=("System", 15))
    label_winmenu_save_save.pack()
    label_winmenu_route = tk.Label(frame_winmenu_save, text="", bg="black",fg="#ffffff", font=("System", 15))
    label_winmenu_route.pack()

    label_winmenu_save_name = tk.Label(frame_winmenu_save, text="", bg="black",fg="#ffffff", font=("System", 15))
    label_winmenu_save_name.pack()
    
    label_winmenu_save_lv = tk.Label(frame_winmenu_save, text="", bg="black",fg="#ffffff", font=("System", 15))
    label_winmenu_save_lv.pack()
    
    
    
    
    
    button_winmenu_start = tk.Button(win_menu, image=picture_run_0, command=run_undertale, bg="black")
    button_winmenu_start.place(relx=0.5, rely=0.9, anchor="center")
    
    label_version = tk.Label(win_menu, text=version, bg="black", fg="white", font=("System", 15))
    label_version.place(relx= 0.95, rely=0.95, anchor="e")





################################### Update ######################################
    
    def main_update():
        global change
        global combobox_winmenu_versionslist
        global list_winmenu_versions_installed
        global combobox_winmenu_versionslist
        global last_time_save
        list_winmenu_versions_installed = [f.name for f in Path(os.path.join(var_launcher_path, "versions")).iterdir() if f.is_dir()]
        
        combobox_winmenu_versionslist["values"] = list_winmenu_versions_installed
        combobox_winmenu_versionslist["font"] = "System"
        
        
        if os_platform == "Windows":
            if "UNDERTALE.exe" in os.popen("tasklist").read():
                button_winmenu_start["image"] = picture_kill_0
                button_winmenu_start["command"] = lambda: os.system("taskkill /f /im UNDERTALE.exe")
            else:
                button_winmenu_start["image"] = picture_run_0
                button_winmenu_start["command"] = run_undertale
        
        elif os_platform == "Linux":
            if "UNDERTALE.exe" in os.popen("pstree").read():
                button_winmenu_start["image"] = picture_kill_0
                button_winmenu_start["command"] = lambda: os.system("pkill UNDERTALE.exe")
            else:
                button_winmenu_start["image"] = picture_run_0
                button_winmenu_start["command"] = run_undertale
            
        
        if os.path.isfile(os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get() , "undertale.ini")):
            
            config = configparser.ConfigParser()
            config.read(os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get() , "undertale.ini"))
            
            
            if float(config.get("General", "Love").strip('"')) == 1:
                label_winmenu_route["text"] = "Pacifist"
                label_winmenu_route["fg"] = "green"
            else:
                label_winmenu_route["text"] = "Genocide or neutral"
                label_winmenu_route["fg"] = "orange"
            label_winmenu_save_name["fg"] = "white"
            label_winmenu_save_name["text"] = "Name:" + config.get("General", "Name").strip('"')
            
            label_winmenu_save_lv["text"] = "Lv:" + (config.get("General", "Love").strip('"'))[:4]
            room = config.get("General", "Room").strip('"')
            room = room[:-7]

            label_winmenu_save_save["text"] = list_number_to_rooms.get(room, "Location not found")
        else:      
            label_winmenu_save_name["fg"] = "red"
            label_winmenu_save_name["text"] = "Save Empty" 
             
            label_winmenu_save_save["text"] = ""
            label_winmenu_save_lv["text"] = ""
            label_winmenu_route["text"] = "" 
        
        if os.path.isfile(os.path.join(save_appdata_local, "file0")):      
            if os.path.getmtime(os.path.join(save_appdata_local, "file0")) != last_time_save:
                last_time_save = os.path.getmtime(os.path.join(save_appdata_local, "file0"))
                saving = tk.Toplevel(root)
                saving.title("save")
                saving.geometry(f"600x150+{screen_width - 600}+{(screen_height * 0.8):.0f}")
                saving.overrideredirect(True)
                saving.attributes("-topmost", True)
                border = tk.Frame(saving)
                border.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, width=-25, height=-25, anchor="center")
                border.configure(bg="black")
                saving_label = tk.Label(saving, text="* Saving...", font=("System", 20), bg="black", fg="white")
                saving_label.place(x = 15, y=35, anchor="w")
                save()
                sound_play(os.path.join(var_launcher_path, "save.wav"))
                
                saving.after(2500,saving.destroy)
                
        list_winmenu_saves_installed = [f.name for f in Path(os.path.join(var_launcher_path, "saves")).iterdir() if f.is_dir()]
        
        combobox_winmenu_saveslist["values"] = list_winmenu_saves_installed      
        combobox_winmenu_saveslist["font"] = "System"
       
        
        win_menu.after(700, main_update)
        

    thread_update = threading.Thread(target=main_update, daemon=True)



    thread_update.start()

########################################################################### 


def quit_app():
    global root
    print("Fermeture en cours..")

    root.destroy()                                                                                                                                                  
    root.quit()
    
  
def sound_play(path):

    def play(p):
        playsound(p)

    threading.Thread(target=play, daemon=True, args=(path,)).start()
    


def delete_version():
    global win_menu
    if not os.path.exists(os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get())):
         sound_play("sqek.wav")
         messagebox.showinfo("U stupid","This version don't exist")
         pass
    else:
        print(f"la version {combobox_winmenu_versionslist.get()} va etre suprr")
        print(os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get()))
        choose = messagebox.askyesno("Are you sure ?", "Do you want to realy end now ?")
        if choose:
            shutil.rmtree(os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get()))

def delete_save():
    global win_menu
    if not os.path.exists(os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get())):
         sound_play("sqek.wav")
         messagebox.showinfo("U stupid","This save don't exist")
         pass
    else:
        print(f"la save {combobox_winmenu_saveslist.get()} va etre suprr")
        print(os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get()))
        choose = messagebox.askyesno("Are you sure ?", "Do you want to really reset this timeline ? :)")
        if choose:
            shutil.rmtree(os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get()))
    

def rename_save():
    print("renaming..")
    rename_path_old = os.path.join(var_launcher_path, "saves", combobox_winmenu_saveslist.get())
    rename_path_new = os.path.join(var_launcher_path, "saves", Entry_winrename_namesave.get())
    print("rename" + rename_path_old + "to" + rename_path_new)
    
    os.rename(rename_path_old, rename_path_new)

    
    config = configparser.ConfigParser()
    config.read(os.path.join(var_launcher_path, "saves", Entry_winrename_namesave.get(), "Undertale_Launcher.ini"))
    config["Info"]["name"] = Entry_winrename_namesave.get()
    
    with open(os.path.join(var_launcher_path, "saves", Entry_winrename_namesave.get(), "Undertale_Launcher.ini"), "w", encoding="utf-8") as configfile:
        config.write(configfile)
    win_rename_save.destroy()

def rename_version():
    print("renaming..")
    print(f"rename {os.path.join(var_launcher_path, 'saves', combobox_winmenu_saveslist.get())} to {os.path.join(var_launcher_path, 'saves' , Entry_winrename_nameversion.get())}")
    os.rename(os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get()), os.path.join(var_launcher_path, "versions", Entry_winrename_nameversion.get()))
    win_rename_version.destroy()

def win_rename_version():
    global Entry_winrename_nameversion, win_rename_version
    print("start version rename win ")
    win_rename_version = tk.Toplevel(root)
    win_rename_version.title(f"Rename version {combobox_winmenu_versionslist.get()}")
    win_rename_version.geometry(f"400x250+{(screen_width // 2) - 200}+{(screen_height // 2) - 125}")
    win_rename_version.resizable(False, False)

    frame_winrename = tk.Frame(win_rename_version, bg="black")
    frame_winrename.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, height=-10, width=-10, anchor="center")

    Label_winrename_title = tk.Label(win_rename_version, text="Rename",  bg="black", fg="white", font=("System",20))
    Label_winrename_title.pack(pady=10)
    Entry_winrename_nameversion = tk.Entry(win_rename_version)
    Entry_winrename_nameversion.pack()

    button_winrename = tk.Button(win_rename_version, text="Rename", image=picture_rename_0, bg="black", font=("System"), command= rename_version) 
    button_winrename.pack(pady=10,side="bottom")

def win_rename_save():
    global Entry_winrename_namesave, win_rename_save
    print("start save rename win ")
    win_rename_save = tk.Toplevel(root)
    win_rename_save.title(f"Rename save {combobox_winmenu_saveslist.get()}")
    win_rename_save.geometry(f"400x250+{(screen_width // 2) - 200}+{(screen_height // 2) - 125}")
    win_rename_save.resizable(False, False)

    frame_winrename = tk.Frame(win_rename_save, bg="black")
    frame_winrename.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, height=-10, width=-10, anchor="center")

    Label_winrename_title = tk.Label(win_rename_save, text="Rename", bg="black", fg="white", font=("System",20))
    Label_winrename_title.pack(pady=10)
    Entry_winrename_namesave = tk.Entry(win_rename_save)
    Entry_winrename_namesave.pack()

    button_winrename = tk.Button(win_rename_save, text="Rename",image=picture_rename_0, bg="black", font=("System"), command= rename_save) 
    button_winrename.pack(pady=10,side="bottom")








    
win_newversion = "lol"

def new_version():
    global win_newversion
    global button_win_newversion_continue
    global entry_win_newversion_nameversion
    global combobox_win_newversion_versionchoice
    global root
    
    
    
    win_newversion = tk.Toplevel(root)
    win_newversion.title("New version")
    win_newversion.geometry(f"400x250+{(screen_width // 2) - 200}+{(screen_height // 2) - 125}")
    win_newversion.resizable(False, False)


    frame_win_newversion = tk.Frame(win_newversion)
    frame_win_newversion.place(rely=0.5, relx=0.5, relwidth=0.96, relheight=0.96, anchor="center")
    frame_win_newversion.configure(background="#000000")
    


    label_win_newversion_title = ttk.Label(frame_win_newversion, text="New version", font=("System", 20), background="black", foreground="white")
    label_win_newversion_title.pack()
    
    label_win_newversion_nameversion = ttk.Label(frame_win_newversion, text="Name of new version", font=("System", 10), background="black", foreground="white")
    label_win_newversion_nameversion.pack()
    
    
    entry_win_newversion_nameversion = ttk.Entry(frame_win_newversion, font=("System"))
    entry_win_newversion_nameversion.pack()
    entry_win_newversion_nameversion.insert(0, "Name of new version")
    
    label_win_newversion_versionchoice = ttk.Label(frame_win_newversion, text="Version", font=("System", 10), background="black", foreground="white")
    label_win_newversion_versionchoice.pack()

    combobox_win_newversion_versionchoice = ttk.Combobox(frame_win_newversion, values=["v1.08","v1.06","v1.001","v1.00","201406TEST18","DEMO20130608","DEMO20130523"], font=("System"))
    combobox_win_newversion_versionchoice.pack()
    combobox_win_newversion_versionchoice.set("v1.08")

    
    button_win_newversion_continue = tk.Button(frame_win_newversion, text="Install", image=picture_download_0, background="black", foreground="black", font=("System",5), command= lambda: threading.Thread(target = start_win_download).start())
    button_win_newversion_continue.pack(side="bottom", pady=10)
    
    sound_play(os.path.join(var_launcher_path, "new.wav"))


















def new_save():
    global win_newversion
    global save_appdata_local
    global button_win_newversion_continue
    global entry_win_newversion_nameversion
    global combobox_win_newversion_versionchoice
    global root
    
    
    
    win_newversion = tk.Toplevel(root)
    win_newversion.title("New save")
    win_newversion.geometry(f"400x250+{(screen_width // 2) - 200}+{(screen_height // 2) - 125}")
    win_newversion.resizable(False, False)
    
    
    frame_win_newversion = tk.Frame(win_newversion)
    frame_win_newversion.place(rely=0.5, relx=0.5, relwidth=0.96, relheight=0.96, anchor="center")
    frame_win_newversion.configure(background="#000000")

    label_win_newversion_title = tk.Label(win_newversion, text="New save", bg="black", fg="white",font=("System", 20))
    label_win_newversion_title.pack()
    
    label_win_newversion_nameversion = tk.Label(win_newversion, text="name for the new save", bg="black", fg="white")
    label_win_newversion_nameversion.pack()
    
    
    entry_win_newversion_nameversion = tk.Entry(win_newversion)
    entry_win_newversion_nameversion.pack()
    entry_win_newversion_nameversion.insert(0, "name")
    def toggle():

        if label_win_newversion_versionchoic.get() == False:
            label_win_newversion_versionchoic = 0
        else:
             label_win_newversion_versionchoic = 1
    var_toggle = tk.BooleanVar()
    
    
  
    
    label_win_newversion_versionchoic = ttk.Checkbutton(win_newversion,variable=var_toggle ,text="importer actual save", command=lambda: toggle)
    label_win_newversion_versionchoic.pack()
    

    def newing_save():
        global save_appdata_local
        
        config_save = configparser.ConfigParser()
        
        
  
        

       
        
        config_save["Info"] = {
            "name": entry_win_newversion_nameversion.get()
        }
        
        if var_toggle.get(): 
            
            shutil.copytree(save_appdata_local, os.path.join(Launcher_save_dir, entry_win_newversion_nameversion.get()), dirs_exist_ok=False)
        else:
            os.makedirs(os.path.join(Launcher_save_dir, entry_win_newversion_nameversion.get()))   
        
        with open(os.path.join(Launcher_save_dir, entry_win_newversion_nameversion.get(), "Undertale_Launcher.ini"), "w") as f:
            config_save.write(f)
        
        main_update()
        win_newversion.destroy()
    
    button_win_newversion_continue = ttk.Button(win_newversion, text="Ok", command= newing_save)
    button_win_newversion_continue.pack(side="bottom")
    
    sound_play(os.path.join(var_launcher_path, "new.wav"))








def start_win_download():
    global entry
    global entry_win_newversion_nameversion
    global combobox_win_newversion_versionchoice
    global win_menu
    

    nom_de_version = entry_win_newversion_nameversion.get()
    version_selected = combobox_win_newversion_versionchoice.get()
    
    win_newversion.destroy()
    
    
    win_download = tk.Toplevel()
    win_download.geometry(f"500x100+{(screen_width // 2) - 250}+{(screen_height // 2) - 50}")
    win_download.resizable(False, False)
    win_download.title("Chargement 0%")
    
    frame_win_download = tk.Frame(win_download)
    frame_win_download.place(rely=0.5, relx=0.5, relwidth=0.96, relheight=0.96, anchor="center")
    frame_win_download.configure(background="#000000")
   
    loading = ttk.Progressbar(win_download, orient="horizontal", length=300, mode="determinate")
    
    loading.pack(side="bottom", pady=20)

    win_download.protocol("WM_DELETE_WINDOW", quit_app)



    url_download = f"https://github.com/chocolife13/----------------------------------/releases/download/{version_selected}/file.zip"
    undertale_chunk_downloaded = 0
    request_undertale_download = requests.get(url_download, stream=True)


    

    if request_undertale_download.status_code == 200:
        print("Server disponible et fichier trouvé")

        undertale_max_length_file = request_undertale_download.headers.get("content-length")
    
        print(f"le fichier fais: {undertale_max_length_file} octes")

        with open(os.path.join(var_launcher_path, "temp.zip"), "wb") as file:
            for chunk in request_undertale_download.iter_content(chunk_size=81920):
                if chunk:
                    file.write(chunk)
                    undertale_chunk_downloaded += len(chunk)
                    loading['value'] = int(f"{int(undertale_chunk_downloaded) / int(undertale_max_length_file) * 100:.0f}")
                    win_download.title(f"Chargement {int(undertale_chunk_downloaded) / int(undertale_max_length_file) * 100:.1f}%")

            file.close()
            print("fichier télécharger")
            
            zip_path = os.path.join(var_launcher_path, "temp.zip")

            ziping_path = os.path.join(var_launcher_path, "versions")
            with zipfile.ZipFile(zip_path, "r") as zip_file:
                zip_file.extractall(ziping_path)
            
            
            print("Fini")
            win_download.destroy()
            
            os.rename(os.path.join(var_launcher_path, "versions", version_selected), os.path.join(var_launcher_path, "versions", nom_de_version ))
            
            
            main_update()
            
            
            
    else: 
        print("serveur down")
        win_download.destroy()



def save():
    Launcher_save_dirs = os.path.join(var_launcher_path, "saves")
    
    print("saving..")
            

    print(f"Dossier LOCAL UNDERTALE: {save_appdata_local}")
    print(f"les Save du Launcher se trouve a {Launcher_save_dirs}")
    
            
            
    config_save = configparser.ConfigParser()
            
            
    print(f"recherche du nom de la save dans le fichier Undertale_Launcher.ini")
    
    
    if os.path.exists(os.path.join(save_appdata_local, "Undertale_Launcher.ini")):
                
        config_save.read(os.path.join(save_appdata_local, "Undertale_Launcher.ini"))
            
        #print(f"Fichier .ini ouvert :{os.path.join(save_appdata_local, "Undertale_Launcher.ini")}")
            
            
            
        nom_save_ini_local = config_save.get("Info", "name")
        print(f"sauvegarde la save de LOCAL UNDERTALE au Laucher")
                
        
        print("Supresion de tous les fichiers LOCAL UNDERTALE")
        
        try:
                os.remove(os.path(save_appdata_local,"Undertale_Launcher.ini"))
                os.remove(os.path(save_appdata_local,"file0"))
                os.remove(os.path(save_appdata_local,"file9"))
                os.remove(os.path(save_appdata_local,"undertale.ini"))
                
        except:
                print("no save found to be deleted")
        
        print("copie")
        shutil.copytree(save_appdata_local, os.path.join(Launcher_save_dirs, nom_save_ini_local), dirs_exist_ok=True)
                
        print(f"sauvegarde dans LOCAL UNDERTALE ({nom_save_ini_local})")
            
    
    
    
    
    
    else:
        print(f"Fichier .ini pas ouvert :{os.path.join(save_appdata_local, 'Undertale_Launcher.ini')}")
            
            
            
            
           






def run_undertale():
    
            
    ########## Gestion des sauvegardes ###################
            
    Launcher_save_dirs = os.path.join(var_launcher_path, "saves")
    
    save_choiced = combobox_winmenu_saveslist.get()
            

    print(f"Dossier LOCAL UNDERTALE: {save_appdata_local}")
    print(f"les Save du Launcher se trouve a {Launcher_save_dirs}")
    print(f"jeux lancer sur la save ({save_choiced})")
            
            
            
    
                
        
    shutil.rmtree(os.path.join(save_appdata_local))
    
    os.makedirs(os.path.join(save_appdata_local))
    print(save_appdata_local)
    print("copie de la save selectioner dans le LOCAL UNDERTALE")
    shutil.copytree((os.path.join(Launcher_save_dirs, save_choiced)), save_appdata_local, dirs_exist_ok=True)
    
            
            
            
            
            

           
    if os_platform == "Windows":
        os.startfile(os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get(), "UNDERTALE.exe"))
    
    elif os_platform == "Linux":
        #os.system(fr"wine {os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get(), "UNDERTALE.exe")}")
        subprocess.Popen(["wine", os.path.join(var_launcher_path, "versions", combobox_winmenu_versionslist.get(), "UNDERTALE.exe")])

            
    
    sound_play(os.path.join(var_launcher_path, "start.wav")) 


  

        



# Attente pour le loading screen
win_loading.after(0, start_win_menu)


root.mainloop()