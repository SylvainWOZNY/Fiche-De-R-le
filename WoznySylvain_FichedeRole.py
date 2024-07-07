
#############(Importation des Library)
import os
from re import template
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from win32api import GetSystemMetrics
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.image import Image,AsyncImage
from kivy.uix.bubble import Bubble

#Window.fullscreen = True
colors = {"Txt":(.99,.97,.8),"Back":(.97,.93,.8),"Check":(0,1,0),"Handi":(0,0,0),"v1":(0.5,1,0.5),"v2":(.85,1,.48,0.5),"cc":(0,0.32,0.22,1)}
c_read = open("info/inf.txt",'r')
c = c_read.readlines()
c_l=[]
for w in c:
    c_l.append(w)
print(c_l)
if c_l[7]=='1':
    colors = {"Txt":(0,0,0),"Back":(1,1,1),"Check":(0,0,0),"Handi":(0,0,0),"v1":(1,1,1),"v2":(0,0,0),"cc":(1,1,1,1)}
c_read.close()
Window.clearcolor=colors["cc"]
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
Window.size = (height*0.95*2*1.1*(21/29.7),0.95*height)   
Window.resizable = False


        
#======================================================================================================================================================================================
#===========================================================CLASS======================================================================================================================
#======================================================================================================================================================================================


class LoginWindow(Screen):
    def build(self):                    #Fenêtre de Login
        self.name='Login'
        self.Box1 = BoxLayout(spacing=50,padding=50,orientation = 'vertical')

        self.Box1.add_widget(Label(halign='center',size_hint=(1,0.4),font_size = 50,bold=True,color=(.85,1,.48,0.5),text="CONNECTION \nEntrez votre pseudo :"))
        self.Box1.pseudo = TextInput(font_size=80,multiline=False,size_hint=(0.8,0.2),pos_hint={'x':0.1},hint_text="Pseudo...",background_color=(0.99, 0.97, 0.9))
        self.Box1.add_widget(self.Box1.pseudo)
        self.Parametre_Btn()
        self.add_widget(self.Box1)

    def Parametre_Btn(self):            #Bouton de validation
        self.Bouton1=Button(halign='center',background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5),size_hint=(0.2,0.4),pos_hint={'x':0.4})
        self.Bouton1.text='Valider'
        self.Bouton1.bind(on_press=self.Login_Btn_fonction)
        self.Box1.add_widget(self.Bouton1)
        sm.add_widget(self)
    
    def Login_Btn_fonction(self,instance):
        #Vérification 
        pseudo = self.Box1.pseudo.text        
        autorized = True
        correct_symbol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
         'S','T','U','V','W','X','Y','Z',"_","0","1","2","3","4","5","6","7","8",
         "9","é","è","à","ù","ç","ö","ô","û","ü","î","ï","â","ä","ê","ë","ÿ"]           #Liste de symboles autorisés
        for elt in pseudo:
            if elt not in correct_symbol :
                autorized = False
        
        #Modification du pseudo dans le fichier inf
        if (autorized == True) and (pseudo != "") and (len(pseudo) <= 30):
            inf= open("info/inf.txt",'r')
            info = inf.readlines()
            info[1]="True\n"
            info[3]=pseudo+"\n"
            txt=""
            inf.close()
        
            for elt in info:
                txt = txt+elt

            inf= open("info/inf.txt",'w')
            inf.write(txt)
            inf.close()
            #Aller au menu principal
            sm.current='Main'
        else : 
            vide=""
            ttt=0
            for elt in correct_symbol:
                if ttt >= 20:
                    vide= vide+"\n"
                    ttt=0
                vide = vide + elt
                ttt+=1
            popup = Popup(title="ERROR",separator_color=(1,0,0),title_color=(1,0,0),title_size=54,title_align='center',content=Label(halign='center',bold=True,color=(1,0,0),text="Pseudo Interdit\nTaille max de pseudo : 30\nSymboles corrects : \n"+vide,font_size=40),size_hint=(None, None), size=((height*0.95*2*1.1*(21/29.7))/2,(0.95*height)/2))
            popup.open()
        
#======================================================================================================================================================================================
#===========================================================CLASS======================================================================================================================
#======================================================================================================================================================================================


class MainWindow(Screen):

    def build(self):
        self.name='Main'                                                  
        self.Box1 = BoxLayout(orientation = 'horizontal',padding=10)
        


        self.Box1.Gauche_Layout=GridLayout(cols=1,size_hint=(0.85,1))
        self.Box1.Gauche_Layout.add_widget(Label(text="Fichiers déjà existants : ",size_hint=(1,0.1),font_size=50,bold=True,color=(.85,1,.48,0.5)))
        self.Box1.Gauche_Layout.Fichier_Layout=GridLayout(spacing = 20,padding=20,cols=2)
        self.Mes_Boutons_fichier()
        self.Box1.Gauche_Layout.add_widget(self.Box1.Gauche_Layout.Fichier_Layout)
        self.Box1.add_widget(self.Box1.Gauche_Layout)

        self.Box1.Droite_Layout=BoxLayout(spacing = 50,padding=20,orientation = 'vertical',size_hint=(0.2, 1))

        self.Parametre_Btn()            
        self.Box1.add_widget(self.Box1.Droite_Layout)
        self.add_widget(self.Box1)
        sm.add_widget(self)

    def Parametre_Btn(self):
        #Bouton1 : Parametre
        self.Bouton1=Button(background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5))
        self.Bouton1.text='Paramètre'
        self.Bouton1.size_hint=(1,0.25)
        self.Bouton1.pos_hint={'top':1}
        self.Bouton1.bind(on_press=self.ParametreBtn_fonction)
        self.Box1.Droite_Layout.add_widget(self.Bouton1)
        
        #Bouton2 : Close
        self.Bouton2=Button(background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5))
        self.Bouton2.text='Close'
        self.Bouton2.size_hint=(1,0.25)
        self.Bouton2.pos_hint={'top':1}
        self.Bouton2.bind(on_press=self.CloseBtn_fonction)
        self.Box1.Droite_Layout.add_widget(self.Bouton2)

        #Bouton3 : +Fiche
        self.Bouton3=Button(background_color=(0.5,1,0),font_size=500,bold=True,color=(.85,1,.48,0.5))
        self.Bouton3.text='+'
        self.Bouton3.size_hint=(1,0.25)
        self.Bouton3.pos_hint={'top':1}
        self.Bouton3.bind(on_press=self.PlusBtn_fonction)
        self.Box1.Droite_Layout.add_widget(self.Bouton3)


    def Mes_Boutons_fichier(self):
        self.Liste_Boutons_fichier=[]
        i=0
        fichiers = os.listdir("fiche")          #Recherche de tout les fichiers dans "fiche"
        for elt in fichiers:                    #Création d'un bouton par fichier
            self.Liste_Boutons_fichier.append(Button(text=str(elt),background_color=(0.5,1,0.5),font_size=50,bold=True,color=(.85,1,.48,0.5)))
            self.Liste_Boutons_fichier[i].bind(on_press=self.p)
            self.Box1.Gauche_Layout.Fichier_Layout.add_widget(self.Liste_Boutons_fichier[i])
            i+=1

    def p(self,instance):
        r = instance.text

                      
##################################======================================================================================================================================================================================
##################################===========================================================CLASS======================================================================================================================
##################################======================================================================================================================================================================================

                
        class OpenWindow(Screen):

            def build(self):        
                self.name='Open'                                            #Nom de la fenêtre
                colors = {"Txt":(.99,.97,.8),"Back":(.97,.93,.8),"Check":(0,1,0),"Handi":(0,0,0),"v1":(0.5,1,0.5),"v2":(.85,1,.48,0.5)}
                c_read = open("info/inf.txt",'r')
                c = c_read.readlines()
                c_l=[]
                for w in c:
                    c_l.append(w)
                print(c_l)
                if c_l[7]=='1':
                    colors = {"Txt":(0,0,0),"Back":(1,1,1),"Check":(0,0,0),"Handi":(0,0,0),"v1":(1,1,1),"v2":(0,0,0)}
                c_read.close()
                width = GetSystemMetrics(0)
                height = GetSystemMetrics(1)
                self.box = BoxLayout(orientation = 'horizontal')
                self.box.side = BoxLayout(orientation = 'vertical',size_hint=(0.1,1))

                self.box.side.add_widget(Label(halign='center',text="Le fichier \nouvert est :\n"+r,bold=True,color=colors["v2"],font_size=25))

                self.box.side.Info_btn=Button(text="Info+",background_color=colors["v1"],font_size=50,bold=True,color=colors["v2"],on_press=self.info_f)
                self.box.side.add_widget(self.box.side.Info_btn)

                self.box.side.Menu_btn=Button(text="Retour",background_color=colors["v1"],font_size=50,bold=True,color=colors["v2"],on_press=self.menu_f)
                self.box.side.add_widget(self.box.side.Menu_btn)

                self.box.side.Save_Btn=Button(text="Sauvegarder",font_size=30,background_color=colors["v1"],bold=True,color=colors["v2"],on_press=self.save)
                self.box.side.add_widget(self.box.side.Save_Btn)

                self.box.add_widget(self.box.side)
                self.box.box_dp = BoxLayout(orientation = 'horizontal',size_hint=(0.9,1))
                self.box.box_dp.p1 = BoxLayout(orientation = 'vertical',size_hint=(0.55,1))
                self.box.box_dp.p2 = BoxLayout(orientation = 'vertical',size_hint=(.50, 1))                
                
                self.constru()

                self.box.box_dp.add_widget(self.box.box_dp.p1)
                self.box.box_dp.add_widget(self.box.box_dp.p2)
                self.box.add_widget(self.box.box_dp)
                self.add_widget(self.box)

                sm.add_widget(self)

            def menu_f(self,instance):
                sm.current='Main'

            def info_f(self,instance):         
                info_txt="""Voici quelques informations importantes à prendre en compte :\n
    •   Les symboles accentués ne sont pas suportés (ils produiront
        des symboles ésothériques).
    •   Les guillemets et retours à la lignes seront quant à eux retirés.
    •   Si vous retournez au menu principal, les modifications effectuées 
        dans la fiche actuelle seront conservées jusqu'au redémarage. 
    •   Vous ne pouvez ouvrir qu'une seul fenêtre de fiche, pour en ouvrir
        une autre l'application nécessitera un redémarage
    •   Si vous fermez l'application sans avoir appuyé sur le bouton 
        sauvegardé, les modifications ne seront pas enregistrées.
    •   Il est possible de donner une de vos fiches présente dans le dossier 
        'fiche' à un autre utilisateur. Elle sera ouvrable et modifiable à 
        condition qu'il possède le template adéquat (dossier 'template') et 
        les images (dossier 'img').\n
Amusez-vous bien :D"""       
                height = GetSystemMetrics(1)
                popup = Popup(title="Informations",separator_color=(0,1,0),title_color=(.85,1,.48,0.5),title_size=54,title_align='center',content=Label(bold=True,color=(.97,.93,.80),text=info_txt,font_size=18),size_hint=(None, None), size=((height*0.95*2*1.1*(21/29.7))/2,(0.95*height)/2))
                popup.open()

            def save(self,instance):
                fiche_read = open("fiche/"+r,'r')
                fiche = fiche_read.readlines()
                fiche_read.close()
                fiche_lines = []
                for wow in fiche:
                    wow = list(wow)
                    wow.pop(-1)
                    cc =""
                    for aaa in wow :
                        cc = cc+aaa
                    fiche_lines.append(cc)
            
                template_read = open("template/"+fiche_lines[0]+".txt",'r')
                template = template_read.readlines()
                template_read.close()
                template_lines = []
                for waw in template:
                    waw = list(waw)
                    waw.pop(-1)
                    cc=""
                    for aaa in waw :
                        cc = cc+aaa
                    template_lines.append(cc)
                fts=""
                
                z=0
                nb_txt=0
                for i in range(len(fiche_lines)) :
                    elt = template_lines[i]
                    fic=fiche_lines[i]
                    if elt == "Page_1" :
                        current_page=1
                        fts= fts+fic+"\n"

                    elif elt == "Page_2" :
                        current_page=2
                        fts= fts+fic+"\n"
                        
                    elif ("mod_" in elt) or (elt==""):
                        fts= fts+fic+"\n"
                    else :
                        modul = eval(elt)                     
                        fic=eval(fic)
                        typ = modul[0]
                        
                        if typ =="Inf": #--------------------------------------------------------------------------------------------------------------------------------------------
                            lst_left=modul[2]
                            bbb = int(len(lst_left)/2)
                            lst_left=lst_left[0:bbb]
                            yyy=0

                            for ya in lst_left: 
                                if type(self.box.box_dp.p1.Inf.left.txtinlst_left[yyy+1].text)==str:
                                    fic[ya] = self.box.box_dp.p1.Inf.left.txtinlst_left[yyy+1].text
                                else:
                                    fic[ya] =""
                                yyy+=2
                            lst_droite=modul[2]
                            lst_droite.reverse()
                            lst_droite=lst_droite[0:bbb]
                            yyy=0

                            for ya in lst_droite:
                                if type(self.box.box_dp.p1.Inf.droite.txtinlst_droite[yyy+1].text)==str:                                                                           
                                    fic[ya]=self.box.box_dp.p1.Inf.droite.txtinlst_droite[yyy+1].text
                                else:
                                    fic[ya]=""                             
                                yyy+=2
                            if self.box.box_dp.p1.Inf.img.temp.text != "Changer l'image":
                                fic["IMG"]=self.box.box_dp.p1.Inf.img.temp.text
                            fts= fts + str(fic)+"\n"

                        elif typ =="Complexe_matrice": #--------------------------------------------------------------------------------------------------------------------------------------------
                            matrices = modul[3]                            
                            for matr in range(len(matrices)):                            
                                for compr in range(len(matrices[matr])):
                                    comptage=0
                                    
                                    for k in range(5):
                                        if self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].checklist[k].active:
                                            comptage += 1                                    
                                    fic[matrices[matr][compr]]=comptage                                        
                            fts= fts + str(fic)+"\n"
                        
                        elif typ =="Spe": #--------------------------------------------------------------------------------------------------------------------------------------------
                            for aaa in range(len(modul[3])):
                                comptage = 0
                                for k in range(modul[4]):
                                    if self.box.box_dp.p1.spe.bloc.bloclist[aaa].gridy.lcheck[k].active:
                                        comptage += 1
                                fic[modul[3][aaa]] = comptage
                            fts= fts + str(fic)+"\n"

                        elif typ=="Item": #--------------------------------------------------------------------------------------------------------------------------------------------

                            for n in range(modul[3]):
                                                             
                                fic[n]["nom"] = self.box.box_dp.p1.Item.lsti[n].boxname.name.text                                
                                
                                fic[n]["desc"]=self.box.box_dp.p1.Item.lsti[n].descr.text     

                                comptage=0
                                if self.box.box_dp.p1.Item.lsti[n].stat.left.c1.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.left.c2.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.left.c3.active:
                                    comptage+=1
                                fic[n]["handi"]=comptage

                                comptage=0
                                fic[n]["stat_1"][0]=self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.name.text
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3.active:
                                    comptage+=1
                                fic[n]["stat_1"][1]=comptage
                                
                                comptage=0
                                fic[n]["stat_2"][0]=self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.name.text
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2.active:
                                    comptage+=1
                                if self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3.active:
                                    comptage+=1   
                                fic[n]["stat_2"][1]=comptage
                            
                            fts=fts+str(fic)+"\n"
                            z+=1
                        
                        elif typ=="Texte": #--------------------------------------------------------------------------------------------------------------------------------------------
                            lst_txt=[]
                            if nb_txt==0:
                                lst_txt= list(self.box.box_dp.p2.box1.descr.text)
                            elif nb_txt==1:
                                lst_txt= list(self.box.box_dp.p2.box2.descr.text)                            
                            stock_text=""
                            for u in lst_txt:
                                if u !="\n" and u !='"':
                                    stock_text = stock_text+u
                            fts = fts+'"'+stock_text+'"\n'
                            nb_txt+=1
                            z+=1

                        elif typ=="Listing": #--------------------------------------------------------------------------------------------------------------------------------------------
                            for k in range(modul[3]):     
                                fic[k]=self.box.box_dp.p2.listing.lsto[k].descr.text                            
                            fts=fts+str(fic)+"\n"
                            z+=1

                        elif typ =="Apt": #--------------------------------------------------------------------------------------------------------------------------------------------
                            for a in range(len(fic)):
                                fic[a]["nom"]=self.box.box_dp.p1.apt.bloc.lblock[a].name.text
                                fic[a]["desc"]=self.box.box_dp.p1.apt.bloc.lblock[a].desc.text
                                comptage = 0
                                for aa in range(3):
                                    if self.box.box_dp.p1.apt.bloc.lblock[a].box.lcheck[aa].active:
                                        comptage +=1
                                fic[a]["pwr"]=comptage
                                print(fic)
                            fts=fts+str(fic)+"\n"

                        elif typ=="Complexe_graphic": #--------------------------------------------------------------------------------------------------------------------------------------------
                            graf = modul[3]
                            for k in range(len(graf)):
                                g=graf[k]
                                if len(g)==1:
                                    fic[g[0]]=self.box.box_dp.p2.comgr.lslid[k].slid.value
                                if len(g)==3:
                                    fic[g[2]]=self.box.box_dp.p2.comgr.lslid[k].slid.value
                                if len(g)==4:
                                    fic[g[3]]=self.box.box_dp.p2.comgr.lslid[k].slid.value
                                    
                            fts = fts+str(fic)+"\n"
                            z+=1
                    
                fiche_w = open("fiche/"+r,'w')
                fiche_w.write(fts+"")
                fiche_w.close()

                
            
            #--------------------------------------------------------------------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------------------------------------------------------------------

            def constru(self):
                colors = {"Txt":(.99,.97,.8),"Back":(.97,.93,.8),"Check":(0,1,0),"Handi":(0,0,0)}
                c_read = open("info/inf.txt",'r')
                c = c_read.readlines()
                c_l=[]
                for w in c:
                    c_l.append(w)
                print(c_l)
                if c_l[7]=='1':
                    colors = {"Txt":(0,0,0),"Back":(1,1,1),"Check":(0,0,0),"Handi":(0,0,0)}
                c_read.close()

                fiche_read = open("fiche/"+r,'r')
                fiche = fiche_read.readlines()
                fiche_read.close()
                fiche_lines = []
                for wow in fiche:
                    wow = list(wow)
                    wow.pop(-1)
                    cc =""
                    for aaa in wow :
                        cc = cc+aaa
                    fiche_lines.append(cc)
            
                template_read = open("template/"+fiche_lines[0]+".txt",'r')
                template = template_read.readlines()
                template_read.close()
                template_lines = []
                for waw in template:
                    waw = list(waw)
                    waw.pop(-1)
                    cc=""
                    for aaa in waw :
                        cc = cc+aaa
                    template_lines.append(cc)
                z=0
                i = 0
                nb_txt=0
                for i in range(len(template_lines)) :
                    elt = template_lines[i]
                    

                    if elt == "Page_1" :
                        pass
                    elif elt == "Page_2" :
                        pass

                    elif elt == "Blank":
                        return None
                        
                    elif ("mod_" in elt) or (elt=="") or (elt=="mod_7") :
                        pass
                    else :
                        modul = eval(elt)
                        fic=fiche_lines[i]
                        fic=eval(fic)
                        typ = modul[0]
                                                
                        if typ =="Inf": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100

                            self.box.box_dp.p1.Inf = BoxLayout(orientation ='horizontal',size_hint=(1,h))
                            self.box.box_dp.p1.Inf.left =GridLayout(cols=2,size_hint=(0.4,1))

                            self.box.box_dp.p1.Inf.droite = GridLayout(cols =2,size_hint=(0.4,1))
                            self.box.box_dp.p1.Inf.left.txtinlst_left=[]
                            self.box.box_dp.p1.Inf.droite.txtinlst_droite=[]
                            lst_left=modul[2]
                            bbb = int(len(lst_left)/2)
                            lst_left=lst_left[0:bbb]
                            yyy=0

                            for ya in lst_left:                            
                                self.box.box_dp.p1.Inf.left.txtinlst_left.append(Label(bold=True,color=colors["Txt"],text=ya))                                        
                                self.box.box_dp.p1.Inf.left.txtinlst_left.append(TextInput(background_color=colors["Back"],font_size=11,text=fic[ya]))
                                self.box.box_dp.p1.Inf.left.add_widget(self.box.box_dp.p1.Inf.left.txtinlst_left[yyy])
                                self.box.box_dp.p1.Inf.left.add_widget(self.box.box_dp.p1.Inf.left.txtinlst_left[yyy+1])
                                yyy+=2
                            lst_droite=modul[2]
                            lst_droite.reverse()
                            lst_droite=lst_droite[0:bbb]
                            yyy=0
                            
                            for ya in lst_droite:                                                                           
                                self.box.box_dp.p1.Inf.droite.txtinlst_droite.append(Label(bold=True,color=colors["Txt"],text=ya)) 
                                self.box.box_dp.p1.Inf.droite.txtinlst_droite.append(TextInput(background_color=colors["Back"],font_size=11,text=fic[ya]))
                                self.box.box_dp.p1.Inf.droite.add_widget(self.box.box_dp.p1.Inf.droite.txtinlst_droite[yyy+1])
                                self.box.box_dp.p1.Inf.droite.add_widget(self.box.box_dp.p1.Inf.droite.txtinlst_droite[yyy])
                                yyy+=2
                            yyy=0
                            self.box.box_dp.p1.Inf.add_widget(self.box.box_dp.p1.Inf.left)

                            
                            self.box.box_dp.p1.Inf.img = BoxLayout(orientation ='vertical',size_hint=(0.4,1))

                            names_img = os.listdir("img")
                            self.box.box_dp.p1.Inf.img.temp=Spinner(halign='center',background_color=colors["Back"],font_size=10,bold=True,color=colors["Txt"],size_hint=(0.8,0.2),pos_hint={'x':0.1})
                            self.box.box_dp.p1.Inf.img.temp.text="Changer l'image"
                            self.box.box_dp.p1.Inf.img.temp.values=names_img
                            self.box.box_dp.p1.Inf.img.add_widget(self.box.box_dp.p1.Inf.img.temp)

                            self.box.box_dp.p1.Inf.img.pdp=AsyncImage(source='img/'+fic["IMG"])

                            self.box.box_dp.p1.Inf.img.add_widget(self.box.box_dp.p1.Inf.img.pdp)
                            self.box.box_dp.p1.Inf.add_widget(self.box.box_dp.p1.Inf.img)

                            self.box.box_dp.p1.Inf.add_widget(self.box.box_dp.p1.Inf.droite)
                            z+=1

                            self.box.box_dp.p1.add_widget( self.box.box_dp.p1.Inf)

                        elif typ =="Complexe_matrice": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p1.ComMa = BoxLayout(orientation='vertical',size_hint=(1,h))
                            self.box.box_dp.p1.ComMa.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.05)))
                            self.box.box_dp.p1.ComMa.matri = GridLayout(cols=3)
                            matrices = modul[3]
                            self.box.box_dp.p1.ComMa.matri.matrlist=[]
                            for matr in range(len(matrices)):                            
                                self.box.box_dp.p1.ComMa.matri.matrlist.append(GridLayout(cols=1))
                                self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist = []
                                for compr in range(len(matrices[matr])):
                                    
                                    self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist.append(BoxLayout(orientation='horizontal'))
                                    self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].name = (Label(bold=True,color=colors["Txt"],text=matrices[matr][compr]))
                                    self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].add_widget(self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].name)
                                    comptage=fic[matrices[matr][compr]]
                                    self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].checklist=[]
                                    for k in range(5):
                                        if comptage>0:
                                            self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].checklist.append(CheckBox(color=colors["Check"],active=1,size_hint_x=0.1))
                                            comptage += -1
                                        else:
                                            self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].checklist.append(CheckBox(color=colors["Check"],active=0,size_hint_x=0.1))
                                    
                                    for k in range(5):
                                         self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].add_widget(self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr].checklist[k])
                                    
                                    self.box.box_dp.p1.ComMa.matri.matrlist[matr].add_widget(self.box.box_dp.p1.ComMa.matri.matrlist[matr].comprlist[compr])
                                self.box.box_dp.p1.ComMa.matri.add_widget(self.box.box_dp.p1.ComMa.matri.matrlist[matr])
                            self.box.box_dp.p1.ComMa.add_widget(self.box.box_dp.p1.ComMa.matri)
                            self.box.box_dp.p1.add_widget(self.box.box_dp.p1.ComMa)
                        
                        
                        elif typ =="Spe": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p1.spe = BoxLayout(orientation='vertical',size_hint=(1,h))
                            self.box.box_dp.p1.spe.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.05)))
                            self.box.box_dp.p1.spe.bloc = GridLayout(cols=len(modul[3]))
                            self.box.box_dp.p1.spe.bloc.bloclist=[]
                            for a in range(len(modul[3])):
                                self.box.box_dp.p1.spe.bloc.bloclist.append(BoxLayout(orientation="vertical"))
                                self.box.box_dp.p1.spe.bloc.bloclist[a].name = Label(bold=True,color=colors["Txt"],text=modul[3][a])
                                self.box.box_dp.p1.spe.bloc.bloclist[a].add_widget(self.box.box_dp.p1.spe.bloc.bloclist[a].name)
                                self.box.box_dp.p1.spe.bloc.bloclist[a].gridy = GridLayout(cols=modul[4])
                                self.box.box_dp.p1.spe.bloc.bloclist[a].gridy.lcheck=[]
                                bbb=fic[modul[3][a]]
                                for aa in range(modul[4]):
                                    if bbb>0:
                                        bbb+= -1
                                        ppp=1
                                    else:
                                        ppp=0
                                    self.box.box_dp.p1.spe.bloc.bloclist[a].gridy.lcheck.append(CheckBox(color=colors["Check"],active=ppp,size_hint_x=0.1))
                                    self.box.box_dp.p1.spe.bloc.bloclist[a].gridy.add_widget(self.box.box_dp.p1.spe.bloc.bloclist[a].gridy.lcheck[aa])
                                self.box.box_dp.p1.spe.bloc.bloclist[a].add_widget(self.box.box_dp.p1.spe.bloc.bloclist[a].gridy)
                                self.box.box_dp.p1.spe.bloc.add_widget(self.box.box_dp.p1.spe.bloc.bloclist[a])
                            self.box.box_dp.p1.spe.add_widget(self.box.box_dp.p1.spe.bloc)
                            self.box.box_dp.p1.add_widget(self.box.box_dp.p1.spe)


                        elif typ=="Item": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p1.Item = GridLayout(cols=2,size_hint=(1,h))
                            self.box.box_dp.p1.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.025)))
                            self.box.box_dp.p1.Item.lsti=[]

                            for n in range(modul[3]):
                                self.box.box_dp.p1.Item.lsti.append(BoxLayout(orientation='vertical'))
                                dic=fic[n]

                                self.box.box_dp.p1.Item.lsti[n].boxname = BoxLayout(size_hint=(1,0.20))
                                self.box.box_dp.p1.Item.lsti[n].boxname.name = TextInput(background_color=colors["Back"],hint_text="Nom de l'objet...",text=dic["nom"],font_size=12,multiline=False)
                                self.box.box_dp.p1.Item.lsti[n].boxname.add_widget(self.box.box_dp.p1.Item.lsti[n].boxname.name)
                                self.box.box_dp.p1.Item.lsti[n].add_widget(self.box.box_dp.p1.Item.lsti[n].boxname)

                                self.box.box_dp.p1.Item.lsti[n].descr = TextInput(background_color=colors["Back"],hint_text="Description de l'objet...",text=dic["desc"],size_hint=(1,0.45),font_size=10)
                                self.box.box_dp.p1.Item.lsti[n].add_widget(self.box.box_dp.p1.Item.lsti[n].descr)

                                self.box.box_dp.p1.Item.lsti[n].stat = GridLayout(cols=2,size_hint=(1,0.35))
                                self.box.box_dp.p1.Item.lsti[n].stat.left = GridLayout(cols=4)
                                self.box.box_dp.p1.Item.lsti[n].stat.left.name = Label(bold=True,color=colors["Txt"],text="Handi.")
                                comptage = fic[n]["handi"]
                                if comptage ==3:
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c1 = CheckBox(color=colors["Handi"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c2 = CheckBox(color=colors["Handi"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c3 = CheckBox(color=colors["Handi"],active=True) 
                                elif comptage == 2:
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c1 = CheckBox(color=colors["Handi"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c2 = CheckBox(color=colors["Handi"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c3 = CheckBox(color=colors["Handi"],active=False) 
                                elif comptage ==1:
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c1 = CheckBox(color=colors["Handi"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c2 = CheckBox(color=colors["Handi"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c3 = CheckBox(color=colors["Handi"],active=False) 
                                elif comptage ==0:
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c1 = CheckBox(color=colors["Handi"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c2 = CheckBox(color=colors["Handi"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.left.c3 = CheckBox(color=colors["Handi"],active=False)                                                                   
                                self.box.box_dp.p1.Item.lsti[n].stat.left.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.left.name)
                                self.box.box_dp.p1.Item.lsti[n].stat.left.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.left.c1)
                                self.box.box_dp.p1.Item.lsti[n].stat.left.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.left.c2)
                                self.box.box_dp.p1.Item.lsti[n].stat.left.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.left.c3)                                
                                self.box.box_dp.p1.Item.lsti[n].stat.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.left)
                                
                                self.box.box_dp.p1.Item.lsti[n].stat.droite = BoxLayout(orientation='vertical')
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut = GridLayout(cols=4)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.name = TextInput(background_color=colors["Back"],hint_text="ATTR.",text=dic["stat_1"][0],font_size=10,multiline=False)
                                comptage = fic[n]["stat_1"][1]
                                if comptage ==3:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3 = CheckBox(color=colors["Check"],active=True) 
                                elif comptage == 2:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3 = CheckBox(color=colors["Check"],active=False) 
                                elif comptage ==1:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3 = CheckBox(color=colors["Check"],active=False) 
                                elif comptage ==0:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3 = CheckBox(color=colors["Check"],active=False)                                  
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.name)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c1)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c2)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.haut.c3) 
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.haut)

                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas = GridLayout(cols=4)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.name = TextInput(background_color=colors["Back"],hint_text="ATTR.",text=dic["stat_2"][0],font_size=10,multiline=False)
                                comptage = fic[n]["stat_2"][1]
                                if comptage ==3:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3 = CheckBox(color=colors["Check"],active=True) 
                                elif comptage == 2:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3 = CheckBox(color=colors["Check"],active=False) 
                                elif comptage ==1:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1 = CheckBox(color=colors["Check"],active=True)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3 = CheckBox(color=colors["Check"],active=False) 
                                elif comptage ==0:
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2 = CheckBox(color=colors["Check"],active=False)
                                    self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3 = CheckBox(color=colors["Check"],active=False)                                
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.name)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c1)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c2)
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.bas.c3) 
                                self.box.box_dp.p1.Item.lsti[n].stat.droite.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite.bas)
                                self.box.box_dp.p1.Item.lsti[n].stat.add_widget(self.box.box_dp.p1.Item.lsti[n].stat.droite)

                                self.box.box_dp.p1.Item.lsti[n].add_widget(self.box.box_dp.p1.Item.lsti[n].stat)
                                self.box.box_dp.p1.Item.add_widget(self.box.box_dp.p1.Item.lsti[n])

                            self.box.box_dp.p1.add_widget(self.box.box_dp.p1.Item)
                            z+=1


                        elif typ=="Apt": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p1.apt = BoxLayout(orientation='vertical',size_hint=(1,h))
                            self.box.box_dp.p1.apt.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.05)))
                            self.box.box_dp.p1.apt.bloc = GridLayout(cols=2)
                            self.box.box_dp.p1.apt.bloc.lblock= []
                            for a in range(modul[3]):
                                self.box.box_dp.p1.apt.bloc.lblock.append(BoxLayout(orientation="vertical"))
                                self.box.box_dp.p1.apt.bloc.lblock[a].name = TextInput(background_color=colors["Back"],hint_text="Nom de l'aptitude...",text=fic[a]["nom"],font_size=12,multiline=False,size_hint=(1,.3))
                                self.box.box_dp.p1.apt.bloc.lblock[a].desc = TextInput(background_color=colors["Back"],hint_text="Description de l'aptitude...",text=fic[a]["desc"],size_hint=(1,0.5),font_size=10)
                                self.box.box_dp.p1.apt.bloc.lblock[a].box = BoxLayout(orientation="horizontal",size_hint=(1,.2))
                                self.box.box_dp.p1.apt.bloc.lblock[a].box.lcheck = []
                                self.box.box_dp.p1.apt.bloc.lblock[a].add_widget(self.box.box_dp.p1.apt.bloc.lblock[a].name)
                                self.box.box_dp.p1.apt.bloc.lblock[a].add_widget(self.box.box_dp.p1.apt.bloc.lblock[a].desc)
                                comptage = fic[a]["pwr"]
                                self.box.box_dp.p1.apt.bloc.lblock[a].box.add_widget(Label(bold=True,color=colors["Txt"],text="Puissance : "))
                                for aa in range(3):
                                    t = 0
                                    if comptage >0:
                                        t = 1
                                        comptage += -1
                                    self.box.box_dp.p1.apt.bloc.lblock[a].box.lcheck.append(CheckBox(color=colors["Check"],active=t))
                                    self.box.box_dp.p1.apt.bloc.lblock[a].box.add_widget(self.box.box_dp.p1.apt.bloc.lblock[a].box.lcheck[aa])
                                
                                self.box.box_dp.p1.apt.bloc.lblock[a].add_widget(self.box.box_dp.p1.apt.bloc.lblock[a].box)
                                self.box.box_dp.p1.apt.bloc.add_widget(self.box.box_dp.p1.apt.bloc.lblock[a])
                            self.box.box_dp.p1.apt.add_widget(self.box.box_dp.p1.apt.bloc)
                            self.box.box_dp.p1.add_widget(self.box.box_dp.p1.apt)
                            

                        elif typ=="Texte": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            if nb_txt == 0:
                                self.box.box_dp.p2.box1 = BoxLayout(orientation='vertical',size_hint=(1,h))
                                self.box.box_dp.p2.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.01)))
                                self.box.box_dp.p2.box1.descr = TextInput(background_color=colors["Back"],text=fic)
                                self.box.box_dp.p2.box1.add_widget(self.box.box_dp.p2.box1.descr)
                                self.box.box_dp.p2.add_widget(self.box.box_dp.p2.box1)

                            if nb_txt == 1:
                                self.box.box_dp.p2.box2 = BoxLayout(orientation='vertical',size_hint=(1,h))
                                self.box.box_dp.p2.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.01)))
                                self.box.box_dp.p2.box2.descr = TextInput(background_color=colors["Back"],text=fic)
                                self.box.box_dp.p2.box2.add_widget(self.box.box_dp.p2.box2.descr)
                                self.box.box_dp.p2.add_widget(self.box.box_dp.p2.box2)
                            nb_txt+=1
                            z+=1

                        elif typ=="Listing": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p2.listing = BoxLayout(orientation='vertical',size_hint=(1,h))
                            self.box.box_dp.p2.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.01)))
                            self.box.box_dp.p2.listing.lsto = []                            
                            for k in range(modul[3]):                                
                                self.box.box_dp.p2.listing.lsto.append(BoxLayout(orientation='horizontal'))
                                self.box.box_dp.p2.listing.lsto[k].dot=Label(color=colors["Txt"],text='•',size_hint=(0.01,1))
                                self.box.box_dp.p2.listing.lsto[k].descr = TextInput(background_color=colors["Back"],text=fic[k],size_hint=(0.9,1),font_size=10)
                                self.box.box_dp.p2.listing.lsto[k].add_widget(self.box.box_dp.p2.listing.lsto[k].dot)
                                self.box.box_dp.p2.listing.lsto[k].add_widget(self.box.box_dp.p2.listing.lsto[k].descr)
                                self.box.box_dp.p2.listing.add_widget(self.box.box_dp.p2.listing.lsto[k])
                            self.box.box_dp.p2.add_widget(self.box.box_dp.p2.listing)
                            z+=1

                        elif typ=="Complexe_graphic": #--------------------------------------------------------------------------------------------------------------------------------------------
                            h = list(modul[1])                            
                            h = int(h[0]+h[1])/100
                            self.box.box_dp.p2.comgr = BoxLayout(orientation='horizontal',size_hint=(1,h))
                            self.box.box_dp.p2.add_widget(Label(bold=True,color=colors["Txt"],text="---"+modul[2]+"---",size_hint=(1,0.01)))
                            self.box.box_dp.p2.comgr.lslid = []
                            graf = modul[3]

                            for k in range(len(graf)):
                                g=graf[k]
                                if len(g)==1:
                                    self.box.box_dp.p2.comgr.lslid.append(BoxLayout(orientation='vertical',size_hint=(0.1,1)))
                                    self.box.box_dp.p2.comgr.lslid[k].name = Label(bold=True,color=colors["Txt"],text=g[0],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].name)
                                    self.box.box_dp.p2.comgr.lslid[k].slid = Slider(value=fic[g[0]],cursor_height=20,cursor_width=20,min=-100, max=100,orientation='vertical')
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].slid)
                                    self.box.box_dp.p2.comgr.add_widget(self.box.box_dp.p2.comgr.lslid[k])
                                if len(g)==3:
                                    self.box.box_dp.p2.comgr.lslid.append(BoxLayout(orientation='vertical',size_hint=(0.1,1)))
                                    self.box.box_dp.p2.comgr.lslid[k].name = Label(bold=True,color=colors["Txt"],text=g[0],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].name)
                                    self.box.box_dp.p2.comgr.lslid[k].slid = Slider(value=fic[g[2]],cursor_height=20,cursor_width=20,min=-100, max=100, orientation='vertical')
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].slid)
                                    self.box.box_dp.p2.comgr.lslid[k].name2 = Label(bold=True,color=colors["Txt"],text=g[1],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].name2)
                                    self.box.box_dp.p2.comgr.add_widget(self.box.box_dp.p2.comgr.lslid[k])
                                if len(g)==4:
                                    self.box.box_dp.p2.comgr.lslid.append(BoxLayout(orientation='horizontal',size_hint=(0.1,1)))
                                    self.box.box_dp.p2.comgr.lslid[k].names = BoxLayout(orientation="vertical",size_hint=(0.7,1))

                                    self.box.box_dp.p2.comgr.lslid[k].names.name1 = Label(bold=True,color=colors["Txt"],text=g[0],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].names.add_widget(self.box.box_dp.p2.comgr.lslid[k].names.name1)
                                    self.box.box_dp.p2.comgr.lslid[k].names.name2 = Label(bold=True,color=colors["Txt"],text=g[1],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].names.add_widget(self.box.box_dp.p2.comgr.lslid[k].names.name2)
                                    self.box.box_dp.p2.comgr.lslid[k].names.name3 = Label(bold=True,color=colors["Txt"],text=g[2],size_hint=(1,0.1),font_size=10)
                                    self.box.box_dp.p2.comgr.lslid[k].names.add_widget(self.box.box_dp.p2.comgr.lslid[k].names.name3)
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].names)
                                    
                                    self.box.box_dp.p2.comgr.lslid[k].slid = Slider(value=fic[g[3]],cursor_height=20,cursor_width=20,min=-100, max=100, orientation='vertical')
                                    self.box.box_dp.p2.comgr.lslid[k].add_widget(self.box.box_dp.p2.comgr.lslid[k].slid)

                                    self.box.box_dp.p2.comgr.add_widget(self.box.box_dp.p2.comgr.lslid[k])
                                    
                            self.box.box_dp.p2.add_widget(self.box.box_dp.p2.comgr)
                    i+=1

##################################======================================================================================================================================================================================
##################################======================================================================================================================================================================================
##################################======================================================================================================================================================================================

        Open=OpenWindow()
        Open.build()
        sm.current='Open'

    def ParametreBtn_fonction(self,instance):
        sm.current='Para'                       #Aller à la page Paramètre

    def CloseBtn_fonction(self,instance):
        MainFDRApp.stop(self)                   #Fermer l'appli

    def PlusBtn_fonction(self,instance):
         sm.current='New'                       #Créer un nouveau fichier fiche



#======================================================================================================================================================================================
#===========================================================CLASS======================================================================================================================
#======================================================================================================================================================================================


def pseudo():
    #Va chercher le pseudo actuel dans le fichier inf
    inf1= open("info/inf.txt",'r')
    info2 = inf1.readlines()
    pseudo3 = info2[3]
    pseudo3 = pseudo3.split("\n")
    pseudo3 = pseudo3[0]
    return pseudo3

class ParaWindow(Screen):
    def build(self):                                        #Fenetre des parametres
        self.name='Para'
        self.Box1=BoxLayout(orientation='vertical')
        self.Box1.BoxH=BoxLayout(orientation='horizontal')
        
        self.Box1.BoxH.pseudo = Label(font_size=50,bold=True,color=(.97,.93,.80),text=pseudo())
        self.Box1.BoxH.add_widget(self.Box1.BoxH.pseudo)

        """self.Box1.BoxH.BoxD=BoxLayout(orientation='vertical')
        self.Box1.BoxH.BoxD.add_widget(Label(text="IMG"))
        self.IMG_Button()
        self.Box1.BoxH.add_widget(self.Box1.BoxH.BoxD)"""

        self.Box1.add_widget(self.Box1.BoxH)
        
        self.Box1.BoxB=BoxLayout(spacing = 50,padding=50,orientation='horizontal')
        self.Parametre_Btn()
        self.Deco_Btn()
        self.Box1.add_widget(self.Box1.BoxB)

        self.add_widget(self.Box1)
        sm.add_widget(self)

    def Parametre_Btn(self):
        self.Bouton1=Button(halign='center',background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5))                               #RETOUR AU MENU PRINCIPAL
        self.Bouton1.text='Menu Principal'
        self.Bouton1.bind(on_press=self.MainBtn_fonction)
        self.Box1.BoxB.add_widget(self.Bouton1)
    
    def Deco_Btn(self):                                     #Déconnexion
        self.Bouton1=Button(halign='center',background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5))
        self.Bouton1.text='Déconnexion \n(nécessite un redémarage après\n la saisie du nouveau pseudo)'
        self.Bouton1.bind(on_press=self.Deco_Btn_fonction)
        self.Box1.BoxB.add_widget(self.Bouton1)

    def IMG_Button(self):                                   #Bouton de changement d'image
        self.Bouton2=Button(background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5))
        self.Bouton2.text="Changer d'image"
        self.Bouton2.bind(on_press=self.iMGBTN_fonction)
        self.Box1.BoxH.BoxD.add_widget(self.Bouton2)
        
    def iMGBTN_fonction(self,instance):                     #Chagement d'image (WIP)
        popup = Popup(title="Changement d'image",content=Label(text="WIP",font_size=100),size_hint=(None, None), size=(400, 400))
        popup.open()


    def Deco_Btn_fonction(self,instance):
        #Effacement du pseudo dans le fichier inf
        inf= open("info/inf.txt",'r')
        info = inf.readlines()
        info[1]="False\n"
        info[3]="\n"
        txt=""
        inf.close()
        for elt in info:
            txt = txt+elt
        inf= open("info/inf.txt",'w')
        inf.write(txt)
        inf.close()
        #Retour fenêtre Login
        sm.current='Login'

    def MainBtn_fonction(self,instance):
        sm.current='Main'

#======================================================================================================================================================================================
#===========================================================CLASS======================================================================================================================
#======================================================================================================================================================================================

class NewWindow(Screen):
    def build(self):
        self.name='New'                                                 
        self.Box1 = BoxLayout(orientation = 'vertical',padding=50,spacing=100)

        #Bouton : Retour
        self.Box1.Bouton1=Button(halign='center',background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5),size_hint=(0.2,0.2),pos_hint={'x':0.4})
        self.Box1.Bouton1.text='Retour'
        self.Box1.Bouton1.bind(on_press=self.MainBtn_fonction)
        self.Box1.add_widget(self.Box1.Bouton1)

        #TextInput : Nom
        self.Box1.name = TextInput(background_color=(0.99, 0.97, 0.9),hint_text="Nom du fichier...",font_size=80,multiline=False,size_hint=(0.8,0.2),pos_hint={'x':0.1})
        self.Box1.add_widget(self.Box1.name)

        #Spinner : Template
        names_temp = os.listdir("template")
        self.Box1.temp=Spinner(halign='center',background_color=(0.5,1,0),font_size=50,bold=True,color=(.85,1,.48,0.5),size_hint=(0.8,0.2),pos_hint={'x':0.1})
        self.Box1.temp.text="Choix du Template"
        self.Box1.temp.values=names_temp
        self.Box1.add_widget(self.Box1.temp)

        #Bouton : Valider
        self.Box1.Bouton2=Button(halign='center',background_color=(0.5,1,0),font_size=35,bold=True,color=(.85,1,.48,0.5),size_hint=(0.4,0.2),pos_hint={'x':0.3})
        self.Box1.Bouton2.text="VALIDER \n (Demande un redémarage\n avant de s'afficher \ndans le menu principal)"
        self.Box1.Bouton2.bind(on_press=self.OkBtn_fonction)
        self.Box1.add_widget(self.Box1.Bouton2)


        self.add_widget(self.Box1)
        sm.add_widget(self)

        
    
    def MainBtn_fonction(self,instance):
        sm.current='Main'                       #Aller à la page principal

    def OkBtn_fonction(self,instance):          
        #Vérification symboles
        name = True
        for elt in self.Box1.name.text :
            if elt not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"_","0","1","2","3","4","5","6","7","8","9"]:
                name =False
        #Vérifications générales
        fichiers = os.listdir("fiche")
        if (self.Box1.temp.text != "Choix du Template") and (self.Box1.name.text+".txt" not in fichiers) and (name ==True) and (self.Box1.name.text !="") and (self.Box1.name.text != "nul"):
            new_page(self.Box1.temp.text,self.Box1.name.text)
            sm.current='Main'

        else:
            popup = Popup(title="ERROR",separator_color=(1,0,0),title_color=(1,0,0),title_size=54,title_align='center',content=Label(halign='center',bold=True,color=(1,0,0),text="Nom de fichier Interdit\n\nOU\n\nTemplate non-choisi",font_size=40),size_hint=(None, None), size=((height*0.95*2*1.1*(21/29.7))/2,(0.95*height)/2))
            popup.open()

def new_page(temp,name):                        #Créer nouveau fichier
    #Récupération du texte du template pour le mettre dans le nouveau fichier
    temp_read= open("template/"+temp,'r')
    temp_lines = temp_read.readlines()
    fiche_lines = temp_lines[22:]
    temp_read.close()
    fiche_string = ""
    for elt in fiche_lines:
        fiche_string=fiche_string+elt
    fiche_write= open("fiche/"+name+".txt",'w')
    fiche_write.write(fiche_string)
    temp_read.close()

        
#======================================================================================================================================================================================
#======================================================================================================================================================================================
#======================================================================================================================================================================================


sm = ScreenManager()

class MainFDRApp(App):

    def build(self):
        #Construction des fenêtres
        Login=LoginWindow()
        Login.build()
        Main=MainWindow()
        Main.build()
        Para =ParaWindow()
        Para.build()
        New=NewWindow()
        New.build()

        #Vérifie si l'utilisateur est connecté et le dirige vers la bonne fenêtre
        inf= open("info/inf.txt",'r')
        info = inf.readlines()
        if info[1]=='False\n' :
            sm.current='Login'
        else : 
            sm.current='Main'
        inf.close()
        return sm


#Lancement
if __name__ == '__main__':
    MainFDRApp().run()
    Config.set('graphics', 'position', 'custom')
