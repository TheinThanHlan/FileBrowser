from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget	
from kivy.uix.gridlayout import GridLayout
import os
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'exit_on_escape', '0')


current_selected=''

class TopBar(GridLayout):
    def openInEditor(self):
        global current_selected
        os.popen(f"alacritty -t '{os.path.basename(current_selected)}' -e nvim '{current_selected}'")	
    
    def moveToTrash(self):
        global current_selected
        if os.path.exists(os.path.dirname(current_selected)+"/.trash")==False:
            os.system(f"mkdir '{os.path.dirname(current_selected)}'/.trash")
            
        os.system(f"mv '{current_selected}' '{os.path.dirname(current_selected)}'/.trash")

    def changeFileName(self,new_name):
        if new_name.strip() !='' and new_name != None:
            os.rename(current_selected,os.path.dirname(current_selected)+'/'+new_name.strip())
            return True
        else:
            return False

    


class NOTI_LABEL(Label):
    def setText(self,text=''):
        self.text=text

    def isFolder(self,path):
            return os.path.isdir(path[0])

class TI(TextInput):
    def setText(self,text=''):
        self.text=text


class MFC(FileChooserListView):
    cwd=os.getcwd()
    def selected(self,filename):
        global current_selected
        try:
            current_selected=filename[0]
        except:
            pass
    
    def reloadMFC(self):
        self._update_files()
    
    


class MyLayout(Widget):
    pass


class MainApp(App):
    title = 'File Browser For Programmers'
    def build(self):
        return MyLayout()	
	
if __name__=='__main__':
	MainApp().run()
